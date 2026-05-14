#!/usr/bin/env python3
"""Validate repository structure and lightweight CTI content hygiene."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CSV_HEADERS = {
    "data/actors.csv": [
        "actor_id",
        "primary_name",
        "aliases",
        "assessed_sponsor",
        "actor_type",
        "relevance_to_israel_government",
        "confidence",
        "primary_motivations",
        "typical_targets",
        "notes",
    ],
    "data/sources.csv": [
        "source_id",
        "title",
        "publisher",
        "publication_date",
        "accessed_date",
        "source_last_updated",
        "record_last_reviewed",
        "archived_date",
        "archive_hash",
        "url",
        "source_type",
        "reliability",
        "notes",
    ],
    "data/ttps.csv": [
        "actor_id",
        "attack_id",
        "tactic",
        "technique",
        "source_id",
        "confidence",
        "notes",
        "mapping_quality",
    ],
    "data/ioc-references.csv": [
        "source_id",
        "actor_id",
        "ioc_type",
        "where_to_get_iocs",
        "handling_notes",
    ],
    "data/malware-references.csv": [
        "malware_or_tool",
        "actor_id",
        "type",
        "description",
        "source_id",
        "handling_notes",
    ],
    "data/research-downloads.csv": [
        "source_id",
        "actor_or_topic",
        "publisher",
        "title",
        "url",
        "status",
        "http_status",
        "content_type",
        "local_archive_path",
        "sha256",
        "bytes",
        "note",
    ],
    "examples/registers/pir-register.csv": [
        "pir_id",
        "decision_owner",
        "decision",
        "question",
        "time_horizon",
        "status",
        "confidence_threshold",
    ],
    "examples/registers/sir-register.csv": [
        "sir_id",
        "pir_id",
        "question",
        "data_source",
        "evidence_type",
        "owner",
        "due_date",
        "status",
    ],
    "examples/registers/evidence-register.csv": [
        "evidence_id",
        "claim_id",
        "actor_id",
        "source_id",
        "claim",
        "source_quote_or_summary",
        "evidence_label",
        "source_reliability",
        "information_credibility",
        "analyst_confidence",
        "confidence_reason",
        "contradiction_or_gap",
        "notes",
    ],
    "examples/registers/persona-claims-register.csv": [
        "claim_id",
        "persona",
        "claim_date",
        "claimed_victim",
        "claimed_sector",
        "claim_channel",
        "evidence_captured",
        "local_telemetry_match",
        "third_party_corroboration",
        "confidence",
        "recommended_comms_action",
        "legal_comms_owner",
        "status",
        "notes",
    ],
    "examples/registers/threat-scenario-register.csv": [
        "scenario_id",
        "pir_id",
        "actor_or_pattern",
        "asset_or_sector",
        "attack_path",
        "likelihood",
        "impact",
        "exposure",
        "detection_gap",
        "time_sensitivity",
        "priority_score",
        "status",
    ],
    "examples/registers/hunt-backlog.csv": [
        "hunt_id",
        "scenario_id",
        "hypothesis",
        "required_telemetry",
        "query_path",
        "expected_observable",
        "status",
        "owner",
    ],
    "examples/registers/detection-backlog.csv": [
        "detection_id",
        "title",
        "scenario_id",
        "attack_id",
        "data_source",
        "drl",
        "rule_path",
        "test_status",
        "soc_action",
        "owner",
        "priority",
    ],
    "examples/registers/detection-health-register.csv": [
        "detection_id",
        "current_drl",
        "last_test_date",
        "false_positive_status",
        "last_tuning_action",
        "owner",
        "next_review_date",
        "health",
    ],
    "examples/registers/metrics.csv": [
        "metric_id",
        "metric_name",
        "scope",
        "value",
        "unit",
        "measurement_date",
        "owner",
        "notes",
    ],
}

SIGMA_REQUIRED_KEYS = [
    "title:",
    "id:",
    "status:",
    "description:",
    "logsource:",
    "detection:",
    "condition:",
    "level:",
]

SIGMA_DISALLOWED_PLACEHOLDERS = [
    "''",
    '""',
    "<configure-",
    "<replace-",
    "<your-",
]

ATTACK_ID_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$")
SIGMA_LEGACY_AGGREGATION_RE = re.compile(
    r"condition:\s*[^\n]*\|\s*(?:count|min|max|avg|sum)\s*\(",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_csv(path: Path, expected_header: list[str]) -> None:
    if not path.exists():
        fail(f"missing CSV file: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            fail(f"empty CSV file: {path.relative_to(ROOT)}")
        if header != expected_header:
            fail(f"bad header in {path.relative_to(ROOT)}: {header}")
        rows = list(reader)
        if not rows:
            fail(f"CSV has no records: {path.relative_to(ROOT)}")
        for index, row in enumerate(rows, start=2):
            if len(row) != len(expected_header):
                fail(f"{path.relative_to(ROOT)} line {index} has {len(row)} fields")


def validate_source_urls(path: Path) -> None:
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            url = row["url"]
            if not url.startswith("https://"):
                fail(f"source URL must use https: {url}")


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate_unique_ids(rows: list[dict[str, str]], field: str, rel_path: str) -> None:
    seen: set[str] = set()
    for row in rows:
        value = row[field]
        if value in seen:
            fail(f"duplicate {field} in {rel_path}: {value}")
        seen.add(value)


def validate_references() -> None:
    actors = read_csv_dicts(ROOT / "data/actors.csv")
    sources = read_csv_dicts(ROOT / "data/sources.csv")
    ttps = read_csv_dicts(ROOT / "data/ttps.csv")
    iocs = read_csv_dicts(ROOT / "data/ioc-references.csv")
    malware = read_csv_dicts(ROOT / "data/malware-references.csv")

    validate_unique_ids(actors, "actor_id", "data/actors.csv")
    validate_unique_ids(sources, "source_id", "data/sources.csv")

    actor_ids = {row["actor_id"] for row in actors}
    source_ids = {row["source_id"] for row in sources}

    for row in ttps:
        actor_id = row["actor_id"]
        source_id = row["source_id"]
        attack_id = row["attack_id"]
        if actor_id not in actor_ids:
            fail(f"data/ttps.csv references unknown actor_id: {actor_id}")
        if source_id not in source_ids:
            fail(f"data/ttps.csv references unknown source_id: {source_id}")
        if not ATTACK_ID_RE.match(attack_id):
            fail(f"data/ttps.csv has invalid ATT&CK technique ID: {attack_id}")

    for rel_path, rows in {
        "data/ioc-references.csv": iocs,
        "data/malware-references.csv": malware,
    }.items():
        for row in rows:
            actor_id = row["actor_id"]
            source_id = row["source_id"]
            if actor_id not in actor_ids:
                fail(f"{rel_path} references unknown actor_id: {actor_id}")
            if source_id not in source_ids:
                fail(f"{rel_path} references unknown source_id: {source_id}")


def validate_sigma(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    missing = [key for key in SIGMA_REQUIRED_KEYS if key not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing Sigma keys: {', '.join(missing)}")
    placeholders = [value for value in SIGMA_DISALLOWED_PLACEHOLDERS if value in text]
    if placeholders:
        fail(
            f"{path.relative_to(ROOT)} contains executable placeholder values: "
            + ", ".join(placeholders)
        )
    if SIGMA_LEGACY_AGGREGATION_RE.search(text):
        fail(
            f"{path.relative_to(ROOT)} uses deprecated Sigma pipe aggregation syntax; "
            "use a companion KQL query or a valid Sigma correlation rule"
        )


def main() -> int:
    for rel_path, header in CSV_HEADERS.items():
        validate_csv(ROOT / rel_path, header)
    validate_source_urls(ROOT / "data/sources.csv")
    validate_references()

    sigma_files = sorted((ROOT / "detections/sigma").glob("*.yml"))
    if not sigma_files:
        fail("no Sigma rules found")
    for sigma_file in sigma_files:
        validate_sigma(sigma_file)

    actor_docs = sorted((ROOT / "docs/actors").glob("*.md"))
    if len(actor_docs) < 5:
        fail("expected at least five actor profile documents")

    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
