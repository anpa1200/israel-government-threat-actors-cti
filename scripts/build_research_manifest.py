#!/usr/bin/env python3
"""Build a committed manifest for locally downloaded research files.

The raw research archive is intentionally ignored by Git. This script records
download status, canonical URLs, local archive paths, sizes, and SHA-256 hashes
so the repository keeps source provenance without vendoring third-party reports.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "research-downloads/2026-05-14/download-results.json"
DEFAULT_OUTPUT = ROOT / "data/research-downloads.csv"
SUPPLEMENTAL_DOWNLOADS = [
    {
        "actor": "Lebanese Cedar",
        "publisher": "Check Point via Kaspersky mirror",
        "title": "Volatile Cedar technical report PDF",
        "url": "https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf",
        "status": "downloaded_supplemental",
        "http": "200",
        "file": "research-downloads/2026-05-14/40-kaspersky-volatile-cedar-technical-report.pdf",
        "content_type": "application/pdf",
        "note": "Supplemental local archive. Original Check Point URL returned 404; public Kaspersky mirror URL identified from MISP/secondary references.",
    }
]

HEADER = [
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
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_source_rows() -> dict[str, str]:
    path = ROOT / "data/sources.csv"
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["url"]: row["source_id"] for row in csv.DictReader(handle)}


def main() -> int:
    if not DEFAULT_RESULTS.exists():
        raise SystemExit(f"missing download results: {DEFAULT_RESULTS}")

    records = json.loads(DEFAULT_RESULTS.read_text(encoding="utf-8"))
    source_rows = read_source_rows()
    rows: list[dict[str, str]] = []

    for record in records:
        rel_file = record.get("file", "")
        archive_path = ROOT / rel_file if rel_file else None
        size = ""
        digest = ""
        if archive_path and archive_path.exists() and archive_path.is_file():
            size = str(archive_path.stat().st_size)
            digest = sha256_file(archive_path)
            if (
                record.get("status") == "downloaded"
                and record.get("content_type", "").startswith("text/html")
                and archive_path.stat().st_size < 1024
            ):
                record = {
                    **record,
                    "status": "failed_placeholder",
                    "note": f"{record.get('note', '')}; downloaded body is too small to be a usable report",
                }

        rows.append(
            {
                "actor_or_topic": record.get("actor", ""),
                "source_id": source_rows.get(record.get("url", ""), ""),
                "publisher": record.get("publisher", ""),
                "title": record.get("title", ""),
                "url": record.get("url", ""),
                "status": record.get("status", ""),
                "http_status": record.get("http", ""),
                "content_type": record.get("content_type", ""),
                "local_archive_path": rel_file,
                "sha256": digest,
                "bytes": size,
                "note": record.get("note", ""),
            }
        )

    existing_files = {row["local_archive_path"] for row in rows if row["local_archive_path"]}
    for record in SUPPLEMENTAL_DOWNLOADS:
        if record["file"] in existing_files:
            continue
        archive_path = ROOT / record["file"]
        size = ""
        digest = ""
        if archive_path.exists() and archive_path.is_file():
            size = str(archive_path.stat().st_size)
            digest = sha256_file(archive_path)
        rows.append(
            {
                "actor_or_topic": record["actor"],
                "source_id": source_rows.get(record["url"], "SRC-CP-VOLATILE-CEDAR-2015"),
                "publisher": record["publisher"],
                "title": record["title"],
                "url": record["url"],
                "status": record["status"],
                "http_status": record["http"],
                "content_type": record["content_type"],
                "local_archive_path": record["file"],
                "sha256": digest,
                "bytes": size,
                "note": record["note"],
            }
        )

    DEFAULT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DEFAULT_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {DEFAULT_OUTPUT.relative_to(ROOT)} with {len(rows)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
