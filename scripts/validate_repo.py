#!/usr/bin/env python3
"""Validate repository structure and lightweight CTI content hygiene."""

from __future__ import annotations

import csv
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
        "date",
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
        "source_id",
        "claim",
        "evidence_label",
        "source_reliability",
        "information_credibility",
        "analyst_confidence",
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


def validate_sigma(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    missing = [key for key in SIGMA_REQUIRED_KEYS if key not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing Sigma keys: {', '.join(missing)}")


def main() -> int:
    for rel_path, header in CSV_HEADERS.items():
        validate_csv(ROOT / rel_path, header)
    validate_source_urls(ROOT / "data/sources.csv")

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
