#!/usr/bin/env python3
"""Build the detection status dashboard from committed CSV registers."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/detection-engineering/detection-status-dashboard.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    backlog = read_csv(ROOT / "examples/registers/detection-backlog.csv")
    health = {
        row["detection_id"]: row
        for row in read_csv(ROOT / "examples/registers/detection-health-register.csv")
    }
    metrics = read_csv(ROOT / "examples/registers/metrics.csv")

    lines = [
        "---",
        "title: Detection Status Dashboard",
        "sidebar_label: Detection Status Dashboard",
        "---",
        "",
        "# Detection Status Dashboard",
        "",
        "Generated from `examples/registers/detection-backlog.csv`,",
        "`examples/registers/detection-health-register.csv`, and",
        "`examples/registers/metrics.csv`.",
        "",
        "Production coverage is not claimed unless a detection reaches DRL-9.",
        "",
        "## Detection Status",
        "",
        "| Detection | DRL | Release Status | Health | Test Status | Evidence Pack |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for row in backlog:
        detection_id = row["detection_id"]
        health_row = health.get(detection_id, {})
        lines.append(
            "| "
            f"`{detection_id}` {row['title']} | "
            f"{row['drl']} | "
            f"{row['release_status']} | "
            f"{health_row.get('health', 'Unknown')} | "
            f"{row['test_status']} | "
            f"`{row['drl_evidence_pack']}` |"
        )

    lines.extend(
        [
            "",
            "## Health Metrics",
            "",
            "| Metric | Value | Unit | Notes |",
            "| --- | --- | --- | --- |",
        ]
    )

    for row in metrics:
        lines.append(
            f"| `{row['metric_id']}` {row['metric_name']} | "
            f"{row['value']} | {row['unit']} | {row['notes']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `Hunt` means a query or rule is suitable for analyst-driven review.",
            "- `Pilot` means the detection has enough evidence for scoped SOC review.",
            "- `Production` is reserved for DRL-9 detections only.",
            "- Synthetic test rates do not replace tenant replay or customer false-positive analysis.",
            "",
        ]
    )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
