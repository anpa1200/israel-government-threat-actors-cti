#!/usr/bin/env python3
"""Create reviewed VirusTotal enrichment candidates from repository hash seeds.

This script intentionally writes a small, reviewable CSV and never stores raw
VirusTotal JSON. Set VT_API_KEY in the environment before running it.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEEDS_PATH = ROOT / "data" / "virustotal-hash-seeds.csv"
OUT_PATH = ROOT / "data" / "virustotal-enrichment-candidates.csv"
API_URL = "https://www.virustotal.com/api/v3/files/{hash_value}"

FIELDNAMES = [
    "candidate_id",
    "seed_id",
    "tool_id",
    "tool_name",
    "actor_id",
    "hash_type",
    "hash",
    "vt_status",
    "vt_meaningful_name",
    "vt_type_description",
    "vt_malicious",
    "vt_suspicious",
    "vt_undetected",
    "vt_harmless",
    "vt_suggested_threat_label",
    "vt_tags",
    "vt_gui_url",
    "queried_at",
    "recommended_action",
    "status",
    "notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def fetch_vt(hash_value: str, api_key: str) -> tuple[int, dict[str, object] | None]:
    req = urllib.request.Request(
        API_URL.format(hash_value=hash_value),
        headers={"x-apikey": api_key},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as exc:
        return exc.code, None


def summarize(seed: dict[str, str], index: int, status_code: int, body: dict[str, object] | None) -> dict[str, str]:
    hash_value = seed["hash"]
    row = {
        "candidate_id": f"VTCAND-{index:03d}",
        "seed_id": seed["seed_id"],
        "tool_id": seed["tool_id"],
        "tool_name": seed["tool_name"],
        "actor_id": seed["actor_id"],
        "hash_type": seed["hash_type"],
        "hash": hash_value,
        "vt_status": "found" if status_code == 200 else "not_found" if status_code == 404 else f"http_{status_code}",
        "vt_meaningful_name": "",
        "vt_type_description": "",
        "vt_malicious": "",
        "vt_suspicious": "",
        "vt_undetected": "",
        "vt_harmless": "",
        "vt_suggested_threat_label": "",
        "vt_tags": "",
        "vt_gui_url": f"https://www.virustotal.com/gui/file/{hash_value}",
        "queried_at": date.today().isoformat(),
        "recommended_action": "Review source context before promotion; do not infer attribution from VT label alone.",
        "status": "needs_review",
        "notes": f"VirusTotal API status {status_code}. Raw VT JSON was not stored.",
    }
    if status_code != 200 or not body:
        return row

    attributes = body.get("data", {}).get("attributes", {})  # type: ignore[union-attr]
    stats = attributes.get("last_analysis_stats", {})  # type: ignore[union-attr]
    threat = attributes.get("popular_threat_classification", {})  # type: ignore[union-attr]
    sha256 = attributes.get("sha256") or hash_value  # type: ignore[union-attr]
    tags = attributes.get("tags", [])  # type: ignore[union-attr]
    row.update(
        {
            "vt_meaningful_name": str(attributes.get("meaningful_name") or ""),
            "vt_type_description": str(attributes.get("type_description") or ""),
            "vt_malicious": str(stats.get("malicious", "")),
            "vt_suspicious": str(stats.get("suspicious", "")),
            "vt_undetected": str(stats.get("undetected", "")),
            "vt_harmless": str(stats.get("harmless", "")),
            "vt_suggested_threat_label": str(threat.get("suggested_threat_label") or ""),
            "vt_tags": ";".join(str(tag) for tag in tags[:8]),
            "vt_gui_url": f"https://www.virustotal.com/gui/file/{sha256}",
            "notes": "Reviewed candidate generated from VT public metadata. Raw VT JSON was not stored.",
        }
    )
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Limit number of seeds queried")
    parser.add_argument("--sleep", type=float, default=16.0, help="Delay between queries for public API rate limits")
    args = parser.parse_args()

    api_key = os.environ.get("VT_API_KEY")
    if not api_key:
        print("VT_API_KEY is not set; no VirusTotal requests were made.", file=sys.stderr)
        return 2

    seeds = read_csv(SEEDS_PATH)
    if args.limit:
        seeds = seeds[: args.limit]

    rows: list[dict[str, str]] = []
    for index, seed in enumerate(seeds, start=1):
        status_code, body = fetch_vt(seed["hash"], api_key)
        rows.append(summarize(seed, index, status_code, body))
        if index < len(seeds):
            time.sleep(args.sleep)

    write_csv(OUT_PATH, rows)
    print(f"Wrote {len(rows)} reviewed VirusTotal candidate rows to {OUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
