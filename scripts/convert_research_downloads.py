#!/usr/bin/env python3
"""Convert locally downloaded public research files to analyst text.

Converted text is written under research-downloads/converted/, which is ignored
by Git. The goal is local review and search, not redistribution of full vendor
reports in the repository.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "research-downloads/2026-05-14/download-results.json"
OUT_DIR = ROOT / "research-downloads/converted/2026-05-14"
SUPPLEMENTAL_FILES = [
    ROOT / "research-downloads/2026-05-14/40-kaspersky-volatile-cedar-technical-report.pdf"
]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
        if tag in {"p", "br", "div", "section", "article", "h1", "h2", "h3", "li", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "li", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = data.strip()
        if text:
            self.parts.append(text)
            self.parts.append(" ")

    def text(self) -> str:
        raw = "".join(self.parts)
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip() + "\n"


def convert_html(src: Path, dst: Path) -> None:
    parser = TextExtractor()
    parser.feed(src.read_text(encoding="utf-8", errors="replace"))
    dst.write_text(parser.text(), encoding="utf-8")


def convert_pdf(src: Path, dst: Path) -> None:
    if shutil.which("pdftotext"):
        subprocess.run(["pdftotext", "-layout", str(src), str(dst)], check=True)
        return
    dst.write_text(
        f"PDF conversion skipped; pdftotext is not installed.\nSource: {src}\n",
        encoding="utf-8",
    )


def main() -> int:
    if not RESULTS.exists():
        raise SystemExit(f"missing download results: {RESULTS}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    converted = 0
    skipped = 0
    records = json.loads(RESULTS.read_text(encoding="utf-8"))
    for record in records:
        if record.get("status") != "downloaded" or not record.get("file"):
            skipped += 1
            continue
        src = ROOT / record["file"]
        if not src.exists():
            skipped += 1
            continue
        if src.suffix.lower() in {".html", ".htm"} and src.stat().st_size < 1024:
            skipped += 1
            continue
        dst = OUT_DIR / f"{src.stem}.txt"
        suffix = src.suffix.lower()
        if suffix in {".html", ".htm"}:
            convert_html(src, dst)
            converted += 1
        elif suffix == ".pdf":
            convert_pdf(src, dst)
            converted += 1
        else:
            skipped += 1

    for src in SUPPLEMENTAL_FILES:
        if not src.exists():
            skipped += 1
            continue
        dst = OUT_DIR / f"{src.stem}.txt"
        if src.suffix.lower() == ".pdf":
            convert_pdf(src, dst)
            converted += 1
        else:
            skipped += 1

    print(f"converted {converted} files into {OUT_DIR.relative_to(ROOT)}")
    print(f"skipped {skipped} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
