#!/usr/bin/env python3
"""Report source freshness and download availability metrics.

This script is intentionally non-networked. It evaluates the repository's own
source review dates and download manifest so CI can flag stale governance data
without depending on live publisher availability.
"""

from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 5, 14)

CADENCE_DAYS = {
    "Government advisory": 90,
    "Government report": 90,
    "Government sanctions": 180,
    "Government announcement": 180,
    "Government fact sheet": 90,
    "Knowledge base": 90,
    "Malware knowledge base": 90,
    "Vendor CTI": 180,
    "Vendor CTI synthesis": 90,
    "Vendor threat research": 90,
    "Vendor CTI mirror": 180,
    "News report": 90,
    "News / vendor coverage": 90,
    "News summary": 90,
    "Think tank report": 180,
    "Author CTI assessment": 180,
    "Author CTI case study": 180,
    "Author methodology": 365,
}


def parse_date(value: str) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    sources = read_csv("data/sources.csv")
    downloads = read_csv("data/research-downloads.csv")

    stale: list[str] = []
    missing_review_date: list[str] = []
    for row in sources:
        reviewed = parse_date(row["record_last_reviewed"])
        if not reviewed:
            missing_review_date.append(row["source_id"])
            continue
        cadence = CADENCE_DAYS.get(row["source_type"], 180)
        if reviewed + timedelta(days=cadence) < TODAY:
            stale.append(row["source_id"])

    broken_downloads = [
        row
        for row in downloads
        if row["status"] in {"failed", "failed_placeholder", "not_found"}
    ]

    print(f"sources_total={len(sources)}")
    print(f"sources_stale={len(stale)}")
    print(f"sources_missing_review_date={len(missing_review_date)}")
    print(f"download_records_total={len(downloads)}")
    print(f"download_records_unavailable={len(broken_downloads)}")

    if missing_review_date:
        print("missing_review_date_ids=" + ",".join(missing_review_date))
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
