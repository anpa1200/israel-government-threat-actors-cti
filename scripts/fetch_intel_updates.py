#!/usr/bin/env python3
"""Fetch no-key public CTI feeds and build an analyst review queue.

This script intentionally does not auto-promote feed items into actor profiles,
source records, detections, or IOC tables. It writes candidate rows that a human
analyst can review, score, and convert into normal repository artifacts.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today()
OUT_PATH = ROOT / "data/intel-update-candidates.csv"
DOC_PATH = ROOT / "docs/intelligence-updates.md"
USER_AGENT = "israel-government-threat-actors-cti/0.1 (+public-defensive-research)"
AMBIGUOUS_MITRE_TERMS = {"karma"}

HEADER = [
    "candidate_id",
    "feed_id",
    "actor_id",
    "matched_terms",
    "item_type",
    "title",
    "published_or_modified",
    "url",
    "relevance_reason",
    "recommended_action",
    "status",
    "review_notes",
]

SURFACE_KEYWORDS = [
    "israel",
    "iran",
    "iranian",
    "irgc",
    "mois",
    "unitronics",
    "rockwell",
    "allen-bradley",
    "plc",
    "hmi",
    "water",
    "wastewater",
    "microsoft exchange",
    "sharepoint",
    "citrix",
    "f5",
    "ivanti",
    "palo alto",
    "fortinet",
    "check point",
    "ransomware",
    "wiper",
    "middle east",
    "telecom",
    "telecommunications",
    "critical infrastructure",
]

RSS_KEYWORDS = [
    "israel",
    "iran",
    "iranian",
    "irgc",
    "mois",
    "unitronics",
    "rockwell",
    "allen-bradley",
    "plc",
    "hmi",
    "microsoft exchange",
    "sharepoint",
    "citrix",
    "f5",
    "ivanti",
    "palo alto",
    "fortinet",
    "check point",
    "ransomware",
    "wiper",
    "middle east",
    "telecom",
    "telecommunications",
]


def read_csv(rel_path: str) -> list[dict[str, str]]:
    with (ROOT / rel_path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fetch_text(url: str, headers: dict[str, str] | None = None) -> str:
    request_headers = {"User-Agent": USER_AGENT}
    if headers:
        request_headers.update(headers)
    request = Request(url, headers=request_headers)
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def stable_suffix(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:10]


def terms_for_actor(row: dict[str, str]) -> list[str]:
    terms = [row["primary_name"], row["actor_id"]]
    terms.extend(part.strip() for part in row["aliases"].split(";") if part.strip())
    return sorted({term for term in terms if term})


def matched_terms(text: str, terms: list[str]) -> list[str]:
    normalized = normalize(text)
    matches = []
    for term in terms:
        if normalize(term) and normalize(term) in normalized:
            matches.append(term)
    return matches


def stix_external_url(obj: dict) -> str:
    for ref in obj.get("external_references", []):
        url = ref.get("url")
        if url:
            return url
    external_id = ""
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            external_id = ref.get("external_id", "")
            break
    if external_id:
        return f"https://attack.mitre.org/groups/{external_id}/"
    return "https://attack.mitre.org/"


def collect_mitre_attack(feed: dict[str, str], actors: list[dict[str, str]]) -> list[dict[str, str]]:
    text = fetch_text(feed["url"])
    bundle = json.loads(text)
    rows = []
    for obj in bundle.get("objects", []):
        if obj.get("type") != "intrusion-set" or obj.get("revoked") is True:
            continue
        haystack = " ".join(
            [
                obj.get("name", ""),
                " ".join(obj.get("aliases", [])),
            ]
        )
        for actor in actors:
            matches = [
                term
                for term in matched_terms(haystack, terms_for_actor(actor))
                if normalize(term) not in AMBIGUOUS_MITRE_TERMS
            ]
            if not matches:
                continue
            rows.append(
                {
                    "candidate_id": f"UPD-MITRE-{actor['actor_id']}-{stable_suffix(stix_external_url(obj))}",
                    "feed_id": feed["feed_id"],
                    "actor_id": actor["actor_id"],
                    "matched_terms": "; ".join(matches),
                    "item_type": "ATT&CK intrusion-set taxonomy update",
                    "title": obj.get("name", actor["primary_name"]),
                    "published_or_modified": obj.get("modified", "")[:10],
                    "url": stix_external_url(obj),
                    "relevance_reason": "Existing actor appears in MITRE ATT&CK Enterprise STIX. Review modified date, aliases, descriptions, and technique references for drift.",
                    "recommended_action": "Compare against data/actors.csv, data/ttps.csv, and actor profile aliases before changing taxonomy.",
                    "status": "Needs analyst review",
                    "review_notes": "",
                }
            )
    return rows


def collect_cisa_kev(feed: dict[str, str]) -> list[dict[str, str]]:
    catalog = json.loads(fetch_text(feed["url"]))
    rows = []
    for vuln in catalog.get("vulnerabilities", []):
        haystack = " ".join(
            [
                vuln.get("vendorProject", ""),
                vuln.get("product", ""),
                vuln.get("vulnerabilityName", ""),
                vuln.get("shortDescription", ""),
                vuln.get("requiredAction", ""),
            ]
        )
        matches = matched_terms(haystack, SURFACE_KEYWORDS)
        if not matches:
            continue
        cve = vuln.get("cveID", "unknown-cve")
        rows.append(
            {
                "candidate_id": f"UPD-KEV-{cve}",
                "feed_id": feed["feed_id"],
                "actor_id": "",
                "matched_terms": "; ".join(matches),
                "item_type": "Known exploited vulnerability",
                "title": f"{cve} - {vuln.get('vulnerabilityName', '')}",
                "published_or_modified": vuln.get("dateAdded", ""),
                "url": feed["url"],
                "relevance_reason": "Product or description overlaps repository edge, OT, identity, remote-access, or regional-threat surfaces.",
                "recommended_action": "Map to Surface And Capability Matrix first; only create actor linkage if a primary source reports actor use.",
                "status": "Needs exposure review",
                "review_notes": vuln.get("knownRansomwareCampaignUse", ""),
            }
        )
    rows.sort(key=lambda row: row["published_or_modified"], reverse=True)
    return rows[:40]


def collect_cisa_advisories(feed: dict[str, str], actors: list[dict[str, str]]) -> list[dict[str, str]]:
    xml_text = fetch_text(feed["url"])
    root = ElementTree.fromstring(xml_text)
    rows = []
    actor_terms = []
    for actor in actors:
        for term in terms_for_actor(actor):
            actor_terms.append((actor["actor_id"], term))
    for item in root.findall("./channel/item"):
        title = item.findtext("title", default="")
        link = item.findtext("link", default=feed["url"])
        pub_date = item.findtext("pubDate", default="")
        description = item.findtext("description", default="")
        haystack = f"{title} {description}"
        actor_matches: dict[str, list[str]] = {}
        for actor_id, term in actor_terms:
            if normalize(term) in normalize(haystack):
                actor_matches.setdefault(actor_id, []).append(term)
        surface_matches = matched_terms(haystack, RSS_KEYWORDS)
        if not actor_matches and not surface_matches:
            continue
        if actor_matches:
            for actor_id, matches in actor_matches.items():
                rows.append(
                    {
                        "candidate_id": f"UPD-CISA-ADV-{actor_id}-{stable_suffix(link)}",
                        "feed_id": feed["feed_id"],
                        "actor_id": actor_id,
                        "matched_terms": "; ".join(sorted(set(matches + surface_matches))),
                        "item_type": "Government advisory",
                        "title": title,
                        "published_or_modified": pub_date,
                        "url": link,
                        "relevance_reason": "CISA advisory text matched an actor or alias already tracked by the repository.",
                        "recommended_action": "If relevant, add or update data/sources.csv and evidence-register.csv with source-reported claims.",
                        "status": "Needs analyst review",
                        "review_notes": "",
                    }
                )
        else:
            rows.append(
                {
                    "candidate_id": f"UPD-CISA-ADV-SURFACE-{stable_suffix(link)}",
                    "feed_id": feed["feed_id"],
                    "actor_id": "",
                    "matched_terms": "; ".join(surface_matches),
                    "item_type": "Government advisory",
                    "title": title,
                    "published_or_modified": pub_date,
                    "url": link,
                    "relevance_reason": "CISA advisory matched repository-relevant surfaces but not a tracked actor name.",
                    "recommended_action": "Review for source-register addition and surface/capability routing; avoid attribution without source evidence.",
                    "status": "Needs analyst review",
                    "review_notes": "",
                }
            )
    return rows[:40]


def collect_otx(feed: dict[str, str], actors: list[dict[str, str]]) -> list[dict[str, str]]:
    api_key = os.environ.get("OTX_API_KEY")
    if not api_key:
        return []
    payload = json.loads(fetch_text(feed["url"], {"X-OTX-API-KEY": api_key}))
    pulses = payload.get("results", payload if isinstance(payload, list) else [])
    rows = []
    actor_terms = [
        (actor["actor_id"], term)
        for actor in actors
        for term in terms_for_actor(actor)
    ]
    for pulse in pulses[:100]:
        name = pulse.get("name", "")
        description = pulse.get("description", "")
        tags = " ".join(pulse.get("tags", []))
        references = pulse.get("references", [])
        haystack = f"{name} {description} {tags} {' '.join(references)}"
        actor_matches: dict[str, list[str]] = {}
        for actor_id, term in actor_terms:
            if normalize(term) in normalize(haystack):
                actor_matches.setdefault(actor_id, []).append(term)
        surface_matches = matched_terms(haystack, RSS_KEYWORDS)
        if not actor_matches and not surface_matches:
            continue
        url = pulse.get("pulse_source", "")
        if not url:
            pulse_id = pulse.get("id", "")
            url = f"https://otx.alienvault.com/pulse/{pulse_id}" if pulse_id else "https://otx.alienvault.com/"
        modified = pulse.get("modified") or pulse.get("created") or ""
        if actor_matches:
            for actor_id, matches in actor_matches.items():
                rows.append(
                    {
                        "candidate_id": f"UPD-OTX-{actor_id}-{stable_suffix(url + name)}",
                        "feed_id": feed["feed_id"],
                        "actor_id": actor_id,
                        "matched_terms": "; ".join(sorted(set(matches + surface_matches))),
                        "item_type": "OTX subscribed pulse",
                        "title": name,
                        "published_or_modified": modified[:10],
                        "url": url,
                        "relevance_reason": "OTX pulse matched a tracked actor or alias.",
                        "recommended_action": "Review references and source quality; promote only source URLs or evidence summaries, not raw pulse dumps.",
                        "status": "Needs analyst review",
                        "review_notes": "",
                    }
                )
        else:
            rows.append(
                {
                    "candidate_id": f"UPD-OTX-SURFACE-{stable_suffix(url + name)}",
                    "feed_id": feed["feed_id"],
                    "actor_id": "",
                    "matched_terms": "; ".join(surface_matches),
                    "item_type": "OTX subscribed pulse",
                    "title": name,
                    "published_or_modified": modified[:10],
                    "url": url,
                    "relevance_reason": "OTX pulse matched repository-relevant surfaces but not a tracked actor name.",
                    "recommended_action": "Review as an enrichment lead; avoid attribution without primary reporting.",
                    "status": "Needs analyst review",
                    "review_notes": "",
                }
            )
    return rows[:40]


def optional_connector_notes(feeds: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    optional_checks = {
        "FEED-OTX-OPTIONAL": "OTX_API_KEY",
        "FEED-MISP-OPTIONAL": "MISP_API_KEY",
        "FEED-OPENCTI-OPTIONAL": "OPENCTI_TOKEN",
    }
    for feed in feeds:
        env_name = optional_checks.get(feed["feed_id"])
        if not env_name:
            continue
        status = "Configured" if os.environ.get(env_name) else "Not configured"
        rows.append(
            {
                "candidate_id": f"UPD-CONNECTOR-{feed['feed_id']}",
                "feed_id": feed["feed_id"],
                "actor_id": "",
                "matched_terms": "",
                "item_type": "Optional connector status",
                "title": feed["name"],
                "published_or_modified": TODAY.isoformat(),
                "url": feed["url"],
                "relevance_reason": f"{feed['provider']} can be used for enrichment when {env_name} is configured.",
                "recommended_action": "Keep API keys in local environment or GitHub Actions secrets. Commit only reviewed summaries, not raw private feed data.",
                "status": status,
                "review_notes": f"Expected secret/env var: {env_name}",
            }
        )
    return rows


def dedupe(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str, str]] = set()
    out = []
    for row in rows:
        key = (row["feed_id"], row["actor_id"], row["url"])
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def write_doc(rows: list[dict[str, str]], errors: list[str]) -> None:
    by_feed: dict[str, int] = {}
    by_status: dict[str, int] = {}
    by_actor: dict[str, list[dict[str, str]]] = {}
    by_surface: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_feed[row["feed_id"]] = by_feed.get(row["feed_id"], 0) + 1
        by_status[row["status"]] = by_status.get(row["status"], 0) + 1
        if row["actor_id"]:
            by_actor.setdefault(row["actor_id"], []).append(row)
        else:
            by_surface.setdefault(row["item_type"], []).append(row)

    lines = [
        "---",
        "title: Intelligence Update Queue",
        "sidebar_label: Intel Updates",
        "---",
        "",
        "# Intelligence Update Queue",
        "",
        "This page summarizes the latest no-key public CTI feed pull. It is a review queue, not an automatic source of truth.",
        "",
        "Feed candidates must be reviewed before they are promoted into `data/sources.csv`, actor profiles, evidence records, TTP mappings, hunts, or detections.",
        "",
        f"Generated: `{TODAY.isoformat()}`",
        "",
        "## Connected Feeds",
        "",
        "- MITRE ATT&CK Enterprise STIX: actor taxonomy and modified-date drift checks.",
        "- CISA Known Exploited Vulnerabilities: exposure-prioritization leads.",
        "- CISA Cybersecurity Advisories RSS: new government advisory leads.",
        "- Optional: OTX subscribed pulses when `OTX_API_KEY` is configured.",
        "- Optional: MISP and OpenCTI connector targets when trusted instance secrets are configured.",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Total candidates | {len(rows)} |",
    ]
    for feed_id, count in sorted(by_feed.items()):
        lines.append(f"| `{feed_id}` candidates | {count} |")
    for status, count in sorted(by_status.items()):
        lines.append(f"| `{status}` | {count} |")
    if errors:
        lines.extend(["", "## Feed Errors", ""])
        for error in errors:
            lines.append(f"- `{error}`")

    lines.extend(
        [
            "",
            "## Candidate Review Rules",
            "",
            "- Treat feed items as collection leads until a human analyst reviews source relevance.",
            "- Do not create actor attribution from KEV or surface matches alone.",
            "- Use CISA KEV matches for exposure review and asset-owner routing first.",
            "- Use MITRE matches to check alias, description, and technique drift.",
            "- Add a normal source/evidence record before changing an actor page or detection mapping.",
            "",
            "## Actor Update Candidates",
            "",
            "| Actor | Candidates | Feeds | Latest candidate date |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for actor_id, actor_rows in sorted(by_actor.items()):
        feeds = ", ".join(
            f"`{feed}`" for feed in sorted({row["feed_id"] for row in actor_rows})
        )
        dated_rows = [row["published_or_modified"] for row in actor_rows if row["published_or_modified"]]
        latest = max(dated_rows) if dated_rows else ""
        lines.append(f"| `{actor_id}` | {len(actor_rows)} | {feeds} | {latest} |")

    lines.extend(
        [
            "",
            "## Surface And Exposure Candidates",
            "",
            "| Candidate Type | Candidates | Feeds | Matched terms |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for item_type, surface_rows in sorted(by_surface.items()):
        feeds = ", ".join(
            f"`{feed}`" for feed in sorted({row["feed_id"] for row in surface_rows})
        )
        matched = sorted(
            {
                term.strip()
                for row in surface_rows
                for term in row["matched_terms"].split(";")
                if term.strip()
            }
        )
        lines.append(
            f"| {item_type} | {len(surface_rows)} | {feeds} | {', '.join(matched) or 'None'} |"
        )

    lines.extend(
        [
            "",
            "## Current Candidates",
            "",
            "| Candidate | Feed | Actor | Type | Title | Date | Status |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        actor = row["actor_id"] or "Surface"
        title = row["title"].replace("|", "\\|")
        lines.append(
            f"| `{row['candidate_id']}` | `{row['feed_id']}` | {actor} | "
            f"{row['item_type']} | [{title}]({row['url']}) | "
            f"{row['published_or_modified']} | {row['status']} |"
        )

    lines.extend(
        [
            "",
            "Machine-readable queue: `data/intel-update-candidates.csv`.",
            "",
            "Feed definitions: `data/intel-feeds.csv`.",
        ]
    )
    DOC_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    feeds = read_csv("data/intel-feeds.csv")
    actors = read_csv("data/actors.csv")
    by_id = {row["feed_id"]: row for row in feeds}

    rows: list[dict[str, str]] = []
    errors: list[str] = []

    collectors = [
        ("FEED-MITRE-ATTACK-ENTERPRISE", lambda feed: collect_mitre_attack(feed, actors)),
        ("FEED-CISA-KEV", collect_cisa_kev),
        ("FEED-CISA-ADVISORIES", lambda feed: collect_cisa_advisories(feed, actors)),
        ("FEED-OTX-OPTIONAL", lambda feed: collect_otx(feed, actors)),
    ]
    for feed_id, collector in collectors:
        try:
            rows.extend(collector(by_id[feed_id]))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, ElementTree.ParseError) as exc:
            errors.append(f"{feed_id}: {type(exc).__name__}: {exc}")

    rows.extend(optional_connector_notes(feeds))
    rows = dedupe(rows)
    rows.sort(key=lambda row: (row["feed_id"], row["actor_id"], row["title"]))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    write_doc(rows, errors)

    print(f"wrote {OUT_PATH.relative_to(ROOT)} with {len(rows)} candidates")
    print(f"wrote {DOC_PATH.relative_to(ROOT)}")
    if errors:
        print("feed_errors=" + " | ".join(errors))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
