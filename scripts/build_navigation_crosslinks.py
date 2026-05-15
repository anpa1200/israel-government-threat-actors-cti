#!/usr/bin/env python3
"""Build practical cross-reference pages and actor navigation blocks."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_BLOB = "https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main"

ACTOR_DOCS = {
    "G0069": "muddywater",
    "G0049": "oilrig",
    "G0059": "apt35",
    "G1044": "apt42",
    "G1030": "agrius",
    "CYBERAV3NGERS": "cyberav3ngers",
    "IMPERIALKITTEN": "imperial-kitten",
    "PIONEERKITTEN": "pioneer-kitten",
    "DARKBIT": "darkbit",
    "G1001": "lyceum",
    "COTTONSANDSTORM": "cotton-sandstorm",
    "G0087": "apt39",
    "G1028": "arid-viper",
    "UNC3890": "unc3890",
    "CYBERTOUFAN": "cyber-toufan",
    "HANDALA": "handala",
    "LEBANESECEDAR": "lebanese-cedar",
    "WIRTE": "wirte",
    "TA402": "ta402",
    "UNC1860": "unc1860",
    "SCARREDMANTICORE": "scarred-manticore",
}

SCENARIO_ACTORS = {
    "SCN-001": ["HANDALA"],
    "SCN-002": ["G0069"],
    "SCN-003": ["CYBERAV3NGERS", "CYBERTOUFAN"],
    "SCN-004": ["G1044", "G0059"],
}

SURFACES = [
    {
        "id": "identity-mdm",
        "name": "Identity, MDM, And Cloud Administration",
        "capability": "Find privileged identity abuse, destructive device actions, risky MFA changes, and OAuth or session persistence.",
        "actors": ["HANDALA", "G1044", "G0059", "PIONEERKITTEN"],
        "detections": ["DET-001", "DET-004"],
        "hunts": ["HUNT-001", "HUNT-004"],
        "fields": "AuditLogs; CloudAppEvents; Entra ID sign-in logs; Intune audit logs; TargetResources; InitiatedBy; OperationName.",
    },
    {
        "id": "endpoint-rmm",
        "name": "Endpoint RMM, Scripting, And User-Path Execution",
        "capability": "Hunt unauthorized RMM, script execution, signed installer abuse, and phishing-to-execution chains.",
        "actors": ["G0069", "G0049", "G1044", "IMPERIALKITTEN", "TA402", "WIRTE"],
        "detections": ["DET-002", "DET-004"],
        "hunts": ["HUNT-002", "HUNT-004"],
        "fields": "DeviceProcessEvents; DeviceFileEvents; FolderPath; ProcessCommandLine; Parent process; RemoteUrl; approved RMM inventory.",
    },
    {
        "id": "ot-plc",
        "name": "OT, PLC, HMI, And Exposed Engineering Interfaces",
        "capability": "Route exposed industrial interfaces to responsible asset owners and relevant IRGC-aligned actor profiles.",
        "actors": ["CYBERAV3NGERS", "CYBERTOUFAN", "G1001", "UNC1860"],
        "detections": ["DET-003"],
        "hunts": ["HUNT-003"],
        "fields": "Firewall; proxy; OT NDR; VPN; URL; UserAgent; DestinationPort; AssetOwner; approved vendor remote access.",
    },
    {
        "id": "edge-webshell",
        "name": "Internet-Facing Servers, Webshells, And Passive Access",
        "capability": "Pivot from exploited edge services to webshell, IIS module, passive backdoor, and handoff-risk guidance.",
        "actors": ["UNC1860", "SCARREDMANTICORE", "G0049", "LEBANESECEDAR", "PIONEERKITTEN"],
        "detections": [],
        "hunts": [],
        "fields": "Web server logs; IIS configuration; appcmd activity; EDR module loads; file writes under web roots and inetsrv paths.",
    },
    {
        "id": "destructive-operations",
        "name": "Destructive Operations, Backup Deletion, And Wipers",
        "capability": "Connect destructive personas and wiper tradecraft to VSS, backup, and mass file-operation hunts.",
        "actors": ["HANDALA", "G1030", "DARKBIT", "CYBERTOUFAN"],
        "detections": [],
        "hunts": [],
        "fields": "Process creation; service control events; file rename/write telemetry; backup admin logs; cloud backup configuration logs.",
    },
    {
        "id": "email-c2-dns",
        "name": "Email, Cloud-Service, IMAP, And DNS C2",
        "capability": "Connect cloud-service C2, IMAPLoader behavior, DNS tunneling, and mail-driven intrusion chains.",
        "actors": ["IMPERIALKITTEN", "G0049", "G0069", "G1044"],
        "detections": ["DET-004"],
        "hunts": ["HUNT-004"],
        "fields": "DNS logs; proxy logs; IMAP/IMAPS egress; process network connections; mail click logs; cloud storage access logs.",
    },
]


def read_csv(rel_path: str) -> list[dict[str, str]]:
    with (ROOT / rel_path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def repo_link(path: str, label: str | None = None) -> str:
    label = label or path
    return f"[{label}]({REPO_BLOB}/{path})"


def doc_link(doc_id: str, label: str) -> str:
    return f"[{label}](../{doc_id}.md)"


def actor_link(actor_id: str, actors_by_id: dict[str, dict[str, str]]) -> str:
    slug = ACTOR_DOCS[actor_id]
    name = actors_by_id[actor_id]["primary_name"]
    return f"[{name}](../actors/{slug}.md)"


def anchor(value: str) -> str:
    text = value.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def detection_link(row: dict[str, str]) -> str:
    return f"[{row['detection_id']}]({REPO_BLOB}/{row['rule_path']})"


def hunt_link(row: dict[str, str]) -> str:
    return f"[{row['hunt_id']}]({REPO_BLOB}/{row['query_path']})"


def technique_matrix_link(attack_id: str, label: str | None = None, *, relative_to_actor: bool) -> str:
    label = label or attack_id
    prefix = "../navigation/" if relative_to_actor else ""
    return f"[{label}]({prefix}ttp-detection-matrix.md#{anchor(attack_id)})"


def mitre_technique_url(attack_id: str) -> str:
    return f"https://attack.mitre.org/techniques/{attack_id.replace('.', '/')}/"


def build_indexes() -> dict[str, object]:
    actors = read_csv("data/actors.csv")
    ttps = read_csv("data/ttps.csv")
    iocs = read_csv("data/ioc-references.csv")
    malware = read_csv("data/malware-references.csv")
    scenarios = read_csv("examples/registers/threat-scenario-register.csv")
    hunts = read_csv("examples/registers/hunt-backlog.csv")
    detections = read_csv("examples/registers/detection-backlog.csv")
    evidence = read_csv("examples/registers/evidence-register.csv")

    actors_by_id = {row["actor_id"]: row for row in actors}
    detections_by_id = {row["detection_id"]: row for row in detections}
    hunts_by_id = {row["hunt_id"]: row for row in hunts}
    scenario_by_id = {row["scenario_id"]: row for row in scenarios}

    ttps_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    iocs_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    malware_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    evidence_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    detections_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    hunts_by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in ttps:
        ttps_by_actor[row["actor_id"]].append(row)
    for row in iocs:
        iocs_by_actor[row["actor_id"]].append(row)
    for row in malware:
        malware_by_actor[row["actor_id"]].append(row)
    for row in evidence:
        evidence_by_actor[row["actor_id"]].append(row)

    actor_attack_ids = {
        actor_id: {row["attack_id"] for row in rows}
        for actor_id, rows in ttps_by_actor.items()
    }

    for detection in detections:
        scenario_id = detection["scenario_id"]
        attack_id = detection["attack_id"]
        direct_actors = set(SCENARIO_ACTORS.get(scenario_id, []))
        overlap_actors = {
            actor_id
            for actor_id, attack_ids in actor_attack_ids.items()
            if attack_id in attack_ids
        }
        for actor_id in sorted(direct_actors | overlap_actors):
            detections_by_actor[actor_id].append(detection)

    for hunt in hunts:
        scenario_id = hunt["scenario_id"]
        linked_detection_ids = [
            part.strip()
            for part in hunt["linked_detection_ids"].split(";")
            if part.strip()
        ]
        related_actor_ids = set(SCENARIO_ACTORS.get(scenario_id, []))
        for detection_id in linked_detection_ids:
            for actor_id, actor_detections in detections_by_actor.items():
                if any(row["detection_id"] == detection_id for row in actor_detections):
                    related_actor_ids.add(actor_id)
        for actor_id in sorted(related_actor_ids):
            hunts_by_actor[actor_id].append(hunt)

    return {
        "actors": actors,
        "actors_by_id": actors_by_id,
        "ttps_by_actor": ttps_by_actor,
        "iocs_by_actor": iocs_by_actor,
        "malware_by_actor": malware_by_actor,
        "evidence_by_actor": evidence_by_actor,
        "detections_by_actor": detections_by_actor,
        "hunts_by_actor": hunts_by_actor,
        "detections_by_id": detections_by_id,
        "hunts_by_id": hunts_by_id,
        "scenario_by_id": scenario_by_id,
    }


def bullet_links(items: list[str]) -> str:
    if not items:
        return "None currently mapped."
    return "; ".join(items)


def actor_nav_block(actor_id: str, indexes: dict[str, object], *, relative_to_actor: bool) -> str:
    actors_by_id = indexes["actors_by_id"]
    ttps_by_actor = indexes["ttps_by_actor"]
    iocs_by_actor = indexes["iocs_by_actor"]
    malware_by_actor = indexes["malware_by_actor"]
    evidence_by_actor = indexes["evidence_by_actor"]
    detections_by_actor = indexes["detections_by_actor"]
    hunts_by_actor = indexes["hunts_by_actor"]

    actor = actors_by_id[actor_id]
    if relative_to_actor:
        workbench = "../navigation/actor-workbench.md"
        ttp_matrix = "../navigation/ttp-detection-matrix.md"
        surface = "../navigation/surface-capability-matrix.md"
        status = "../detection-engineering/detection-status-dashboard.md"
        hunts_doc = "../threat-hunting/hunt-workflow.md"
    else:
        workbench = "actor-workbench.md"
        ttp_matrix = "ttp-detection-matrix.md"
        surface = "surface-capability-matrix.md"
        status = "../detection-engineering/detection-status-dashboard.md"
        hunts_doc = "../threat-hunting/hunt-workflow.md"

    ttp_rows = ttps_by_actor.get(actor_id, [])
    detection_rows = detections_by_actor.get(actor_id, [])
    hunt_rows = hunts_by_actor.get(actor_id, [])
    ioc_rows = iocs_by_actor.get(actor_id, [])
    malware_rows = malware_by_actor.get(actor_id, [])
    evidence_rows = evidence_by_actor.get(actor_id, [])

    ttp_links = [
        f"{technique_matrix_link(row['attack_id'], row['attack_id'], relative_to_actor=relative_to_actor)} {row['technique']} ({row['mapping_quality']})"
        for row in ttp_rows[:6]
    ]
    detection_links = [
        f"{detection_link(row)} {row['title']} ({row['release_status']}, DRL-{row['drl']})"
        for row in detection_rows
    ]
    hunt_links = [f"{hunt_link(row)} {row['hypothesis']}" for row in hunt_rows]
    ioc_links = [
        f"`{row['source_id']}` {row['ioc_type']}"
        for row in ioc_rows[:5]
    ]
    malware_links = [
        f"`{row['malware_or_tool']}` ({row['type']})"
        for row in malware_rows[:6]
    ]
    evidence_links = [
        f"`{row['evidence_id']}` / `{row['claim_id']}`"
        for row in evidence_rows[:5]
    ]
    source_ids = sorted({row["source_id"] for row in ttp_rows + ioc_rows + malware_rows})
    surfaces = [
        f"[{surface_row['name']}]({surface}#{surface_row['id']})"
        for surface_row in SURFACES
        if actor_id in surface_row["actors"]
    ]

    lines = [
        "<!-- ACTOR-NAVIGATION:START -->",
        "## Repository Navigation",
        "",
        f"- Actor workbench: [{actor['primary_name']}]({workbench}#{anchor(actor['primary_name'])})",
        f"- TTP-to-detection matrix: [all mapped techniques]({ttp_matrix})",
        f"- Surface and capability routes: {bullet_links(surfaces)}",
        f"- Detection status: [dashboard]({status})",
        f"- Hunt workflow: [hunt workflow]({hunts_doc})",
        f"- ATT&CK mappings: {bullet_links(ttp_links)}",
        f"- Mapped detections: {bullet_links(detection_links)}",
        f"- Mapped hunts: {bullet_links(hunt_links)}",
        f"- IOC reference sources: {bullet_links(ioc_links)}",
        f"- Malware and tools: {bullet_links(malware_links)}",
        f"- Evidence records: {bullet_links(evidence_links)}",
        f"- Source IDs in structured data: {', '.join(f'`{source_id}`' for source_id in source_ids) if source_ids else 'None currently mapped.'}",
        "",
        "<!-- ACTOR-NAVIGATION:END -->",
    ]
    return "\n".join(lines)


def inject_actor_blocks(indexes: dict[str, object]) -> None:
    start = "<!-- ACTOR-NAVIGATION:START -->"
    end = "<!-- ACTOR-NAVIGATION:END -->"
    for actor_id, slug in ACTOR_DOCS.items():
        path = ROOT / "docs" / "actors" / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        block = actor_nav_block(actor_id, indexes, relative_to_actor=True)
        pattern = re.compile(
            rf"\n?{re.escape(start)}.*?{re.escape(end)}\n?",
            re.DOTALL,
        )
        if pattern.search(text):
            new_text = pattern.sub("\n" + block + "\n\n", text, count=1)
        else:
            lines = text.splitlines()
            insert_at = 1 if lines and lines[0].startswith("# ") else 0
            new_lines = lines[:insert_at] + ["", block, ""] + lines[insert_at:]
            new_text = "\n".join(new_lines) + "\n"
        new_text = re.sub(
            r"(<!-- ACTOR-NAVIGATION:END -->)\n{3,}",
            r"\1\n\n",
            new_text,
        )
        path.write_text(new_text, encoding="utf-8")


def build_actor_workbench(indexes: dict[str, object]) -> None:
    actors = indexes["actors"]
    actors_by_id = indexes["actors_by_id"]
    ttps_by_actor = indexes["ttps_by_actor"]
    detections_by_actor = indexes["detections_by_actor"]
    hunts_by_actor = indexes["hunts_by_actor"]
    iocs_by_actor = indexes["iocs_by_actor"]
    malware_by_actor = indexes["malware_by_actor"]
    evidence_by_actor = indexes["evidence_by_actor"]

    rows = [
        "---",
        "title: Actor Navigation Workbench",
        "sidebar_label: Actor Workbench",
        "---",
        "",
        "# Actor Navigation Workbench",
        "",
        "Use this page as the click-through hub from an actor to its structured TTPs, IOC reference locations, malware/tool references, mapped hunts, mapped detections, and evidence records.",
        "",
        "The page is generated from repository CSV/register data. It is an analyst navigation aid, not an attribution shortcut.",
        "",
        "## Actor Coverage Matrix",
        "",
        "| Actor | Priority | TTPs | IOC refs | Tools | Hunts | Detections | Evidence |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for actor in actors:
        actor_id = actor["actor_id"]
        if actor_id not in ACTOR_DOCS:
            continue
        rows.append(
            "| "
            + actor_link(actor_id, actors_by_id)
            + f" | {actor['relevance_to_israel_government']} | "
            + f"{len(ttps_by_actor.get(actor_id, []))} | "
            + f"{len(iocs_by_actor.get(actor_id, []))} | "
            + f"{len(malware_by_actor.get(actor_id, []))} | "
            + f"{len(hunts_by_actor.get(actor_id, []))} | "
            + f"{len(detections_by_actor.get(actor_id, []))} | "
            + f"{len(evidence_by_actor.get(actor_id, []))} |"
        )

    rows.extend(["", "## Actor Drilldowns", ""])
    for actor in actors:
        actor_id = actor["actor_id"]
        if actor_id not in ACTOR_DOCS:
            continue
        rows.extend([
            f"### {actor['primary_name']} {{#{anchor(actor['primary_name'])}}}",
            "",
            actor_nav_block(actor_id, indexes, relative_to_actor=False)
                .replace("## Repository Navigation\n\n", "")
                .replace("<!-- ACTOR-NAVIGATION:START -->\n", "")
                .replace("\n<!-- ACTOR-NAVIGATION:END -->", ""),
            "",
        ])

    path = ROOT / "docs" / "navigation" / "actor-workbench.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(rows).rstrip() + "\n", encoding="utf-8")


def build_surface_matrix(indexes: dict[str, object]) -> None:
    actors_by_id = indexes["actors_by_id"]
    detections_by_id = indexes["detections_by_id"]
    hunts_by_id = indexes["hunts_by_id"]

    rows = [
        "---",
        "title: Surface And Capability Matrix",
        "sidebar_label: Surface Matrix",
        "---",
        "",
        "# Surface And Capability Matrix",
        "",
        "Use this page when the starting point is not an actor name. Pick the exposed surface or defender capability, then route to the relevant actors, hunts, detections, and telemetry fields.",
        "",
    ]
    for surface in SURFACES:
        rows.extend([
            f"## {surface['name']} {{#{surface['id']}}}",
            "",
            f"Capability route: {surface['capability']}",
            "",
            f"Relevant actors: {bullet_links([actor_link(actor_id, actors_by_id) for actor_id in surface['actors']])}",
            "",
            f"Mapped detections: {bullet_links([detection_link(detections_by_id[detection_id]) + ' ' + detections_by_id[detection_id]['title'] for detection_id in surface['detections'] if detection_id in detections_by_id])}",
            "",
            f"Mapped hunts: {bullet_links([hunt_link(hunts_by_id[hunt_id]) + ' ' + hunts_by_id[hunt_id]['hypothesis'] for hunt_id in surface['hunts'] if hunt_id in hunts_by_id])}",
            "",
            f"Required telemetry fields: {surface['fields']}",
            "",
        ])

    path = ROOT / "docs" / "navigation" / "surface-capability-matrix.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(rows).rstrip() + "\n", encoding="utf-8")


def build_ttp_detection_matrix(indexes: dict[str, object]) -> None:
    actors_by_id = indexes["actors_by_id"]
    ttps_by_actor = indexes["ttps_by_actor"]
    detections_by_actor = indexes["detections_by_actor"]
    hunts_by_actor = indexes["hunts_by_actor"]
    detections_by_id = indexes["detections_by_id"]

    technique_rows: dict[str, list[tuple[str, dict[str, str]]]] = defaultdict(list)
    for actor_id, rows in ttps_by_actor.items():
        for row in rows:
            technique_rows[row["attack_id"]].append((actor_id, row))

    rows = [
        "---",
        "title: TTP To Detection Matrix",
        "sidebar_label: TTP Matrix",
        "---",
        "",
        "# TTP To Detection Matrix",
        "",
        "Use this page when the starting point is a technique. Each technique links back to relevant actors, mapped repository detections, mapped hunts, and MITRE ATT&CK.",
        "",
        "A missing detection means the technique is tracked for intelligence context but does not yet have a repository rule or hunt mapped to it.",
        "",
        "## Coverage Summary",
        "",
        "| Technique | Actors | Mapped Detections | Mapped Hunts |",
        "| --- | ---: | ---: | ---: |",
    ]

    summary: list[tuple[str, int, int, int]] = []
    for attack_id, actor_rows in sorted(technique_rows.items()):
        related_detections = {
            detection["detection_id"]
            for actor_id, _ in actor_rows
            for detection in detections_by_actor.get(actor_id, [])
            if detection["attack_id"] == attack_id
        }
        related_hunts = {
            hunt["hunt_id"]
            for actor_id, _ in actor_rows
            for hunt in hunts_by_actor.get(actor_id, [])
            if any(
                detection["detection_id"] in hunt["linked_detection_ids"]
                for detection in detections_by_actor.get(actor_id, [])
                if detection["attack_id"] == attack_id
            )
        }
        summary.append((attack_id, len({actor_id for actor_id, _ in actor_rows}), len(related_detections), len(related_hunts)))

    for attack_id, actor_count, detection_count, hunt_count in summary:
        rows.append(
            f"| [{attack_id}](#{anchor(attack_id)}) | {actor_count} | {detection_count} | {hunt_count} |"
        )

    rows.extend(["", "## Technique Drilldowns", ""])
    for attack_id, actor_rows in sorted(technique_rows.items()):
        first = actor_rows[0][1]
        actor_ids = sorted({actor_id for actor_id, _ in actor_rows})
        related_detections = []
        related_hunts = []
        seen_detections: set[str] = set()
        seen_hunts: set[str] = set()
        for actor_id in actor_ids:
            for detection in detections_by_actor.get(actor_id, []):
                if detection["attack_id"] == attack_id and detection["detection_id"] not in seen_detections:
                    seen_detections.add(detection["detection_id"])
                    related_detections.append(detection)
            for hunt in hunts_by_actor.get(actor_id, []):
                linked = [
                    part.strip()
                    for part in hunt["linked_detection_ids"].split(";")
                    if part.strip()
                ]
                if (
                    any(
                        detection_id in seen_detections
                        and detections_by_id[detection_id]["attack_id"] == attack_id
                        for detection_id in linked
                        if detection_id in detections_by_id
                    )
                    and hunt["hunt_id"] not in seen_hunts
                ):
                    seen_hunts.add(hunt["hunt_id"])
                    related_hunts.append(hunt)

        source_ids = sorted({row["source_id"] for _, row in actor_rows})
        mapping_levels = sorted({row["mapping_quality"] for _, row in actor_rows})
        rows.extend(
            [
                f"### {attack_id} - {first['technique']} {{#{anchor(attack_id)}}}",
                "",
                f"MITRE ATT&CK: [{attack_id}]({mitre_technique_url(attack_id)})",
                "",
                f"Tactic(s): {', '.join(sorted({row['tactic'] for _, row in actor_rows}))}",
                "",
                f"Mapped actors: {bullet_links([actor_link(actor_id, actors_by_id) for actor_id in actor_ids])}",
                "",
                f"Mapped detections: {bullet_links([detection_link(row) + ' ' + row['title'] + ' (' + row['release_status'] + ', DRL-' + row['drl'] + ')' for row in related_detections])}",
                "",
                f"Mapped hunts: {bullet_links([hunt_link(row) + ' ' + row['hypothesis'] for row in related_hunts])}",
                "",
                f"Mapping quality levels in repository: {', '.join(mapping_levels)}",
                "",
                f"Source IDs: {', '.join(f'`{source_id}`' for source_id in source_ids)}",
                "",
            ]
        )

    path = ROOT / "docs" / "navigation" / "ttp-detection-matrix.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(rows).rstrip() + "\n", encoding="utf-8")


def update_actor_index(indexes: dict[str, object]) -> None:
    actors = indexes["actors"]
    actors_by_id = indexes["actors_by_id"]
    ttps_by_actor = indexes["ttps_by_actor"]
    detections_by_actor = indexes["detections_by_actor"]
    hunts_by_actor = indexes["hunts_by_actor"]
    iocs_by_actor = indexes["iocs_by_actor"]
    malware_by_actor = indexes["malware_by_actor"]

    rows = [
        "---",
        "title: Actor Index",
        "sidebar_label: Actor Index",
        "---",
        "",
        "# Actor Index",
        "",
        "This index is the entry point for actor-centric navigation. Each actor links to its profile and to the generated cross-reference workbench that joins actor pages to TTPs, IOC references, malware/tool references, hunts, detections, and surfaces.",
        "",
        "- [Actor Navigation Workbench](../navigation/actor-workbench.md)",
        "- [TTP To Detection Matrix](../navigation/ttp-detection-matrix.md)",
        "- [Surface And Capability Matrix](../navigation/surface-capability-matrix.md)",
        "- [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)",
        "",
        "| Actor | Profile | Workbench | Priority | TTPs | IOC refs | Tools | Hunts | Detections |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for actor in actors:
        actor_id = actor["actor_id"]
        if actor_id not in ACTOR_DOCS:
            continue
        slug = ACTOR_DOCS[actor_id]
        name = actor["primary_name"]
        rows.append(
            f"| {name} | [{slug}.md]({slug}.md) | "
            f"[drilldown](../navigation/actor-workbench.md#{anchor(name)}) | "
            f"{actor['relevance_to_israel_government']} | "
            f"{len(ttps_by_actor.get(actor_id, []))} | "
            f"{len(iocs_by_actor.get(actor_id, []))} | "
            f"{len(malware_by_actor.get(actor_id, []))} | "
            f"{len(hunts_by_actor.get(actor_id, []))} | "
            f"{len(detections_by_actor.get(actor_id, []))} |"
        )
    rows.extend([
        "",
        "Profiles are starter assessments. They MUST be updated as new public reporting becomes available. Counts are generated from repository data and should be treated as navigation coverage, not production detection coverage.",
    ])
    (ROOT / "docs" / "actors" / "README.md").write_text(
        "\n".join(rows) + "\n", encoding="utf-8"
    )


def main() -> int:
    indexes = build_indexes()
    inject_actor_blocks(indexes)
    build_actor_workbench(indexes)
    build_surface_matrix(indexes)
    build_ttp_detection_matrix(indexes)
    update_actor_index(indexes)
    print("Wrote actor and surface navigation crosslinks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
