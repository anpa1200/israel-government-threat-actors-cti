---
title: Report Index
sidebar_label: Report Index
---

# Report Index

Use `data/sources.csv` as the authoritative machine-readable source register.

Use `sources/` as the analyst-facing scored source library:

- `sources/score-a-primary/` for high-reliability primary sources.
- `sources/score-b-supporting/` for supporting methodology, authored assessments, and secondary summaries.
- `sources/score-c-watchlist/` for claims and leads that require corroboration.

## Priority Report Categories

- Government advisories: CISA, FBI, NSA, INCD, CERT-IL, ENISA, NCSC.
- ATT&CK knowledge base: actor technique mappings and reference chains.
- Vendor CTI: Microsoft, Mandiant / Google Cloud, ESET, SentinelOne, Meta, Check Point Research, Palo Alto Unit 42, CrowdStrike, Recorded Future.
- Sector sources: WaterISAC, aviation, telecom, and government-sector information sharing groups.
- Authored Medium research from this project owner: [andrey-medium-articles.md](andrey-medium-articles.md).
- 2024-2026 escalation research intake: [2026-israel-critical-infrastructure-escalation.md](2026-israel-critical-infrastructure-escalation.md).
- 2023-2026 source-download and validation intake: [resourses_research.md](resourses_research.md).
- End-to-end CTI-to-detection examples: [worked-cases.md](worked-cases.md).
- CI and build evidence: [ci-validation-evidence.md](ci-validation-evidence.md).
- Versioned maturity notes: [release-notes.md](release-notes.md).
- Detection-readiness evidence packs:
  [../detection-engineering/drl-evidence-packs.md](../detection-engineering/drl-evidence-packs.md).
- Known limitations: [../known-limitations.md](../known-limitations.md).
- Sigma validation results:
  [../detection-engineering/sigma-validation-results.md](../detection-engineering/sigma-validation-results.md).
- SOC handoff packet:
  [../detection-engineering/soc-handoff-packet.md](../detection-engineering/soc-handoff-packet.md).
- Defensive CTI synthesis for Israeli public-sector environments: [defensive-cti-threats-to-israeli-public-sector.md](defensive-cti-threats-to-israeli-public-sector.md).

## Collection Rules

- Reports SHOULD be stored as links unless redistribution is explicitly allowed.
- Analyst notes MAY summarize key findings, but MUST preserve original URL and publisher.
- IOC lists SHOULD be referenced by location rather than duplicated wholesale.
- Raw downloaded reports SHOULD remain in ignored `research-downloads/`.
- Use `data/research-downloads.csv` as the committed manifest for download status,
  local archive path, byte size, and SHA-256.
- Use `scripts/convert_research_downloads.py` to create local searchable text
  under ignored `research-downloads/converted/` when analyst review requires it.
