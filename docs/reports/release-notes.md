---
title: Release Notes
sidebar_label: Release Notes
---

# Release Notes

This page records repository maturity changes. It is intentionally explicit
about what is and is not production-ready.

## v0.1.5

Status: stronger proof layer for public validation; still not production SOC
coverage.

Key changes:

- Added deterministic synthetic fixture tests for `DET-001` through `DET-004`.
- Expanded the synthetic fixture set to include multiple positive and benign
  boundary cases per detection.
- Added `scripts/run_detection_fixture_tests.py` to CI validation.
- Added committed synthetic positive/negative outputs and synthetic
  false-positive rates.
- Added synthetic 30-day replay substitute for `DET-002`.
- Added generated detection status dashboard.
- Added customer-environment usage guide.
- Added Sigma CLI semantic validation result with zero errors and zero issues.
- Added top-level known limitations page.
- Added platform query-variant status page.
- Added customer-style SOC handoff packet for `DET-002`.
- Added `release_status` to the detection backlog: Hunt / Pilot / Production /
  Retired.

Remaining production blockers:

- No detection is DRL-9.
- Synthetic tests are not customer telemetry.
- No real tenant or customer historical replay is committed.
- Backend-specific Splunk and Elastic conversion artifacts remain pending.
- False-positive rates are synthetic fixture rates only.

## v0.1.4

Status: professional public CTI-to-detection research repository; not a
production SOC analytics package.

Key changes:

- Fixed GitHub Pages slash-route 404s by switching Docusaurus to
  directory-style routes.
- Added three end-to-end worked cases:
  - MuddyWater phishing to RMM / BugSleep / Fooder / MuddyViper.
  - Scarred Manticore / UNC1860 access to Void Manticore destructive handoff.
  - CyberAv3ngers OT / PLC exposure.
- Added detection-specific DRL evidence packs for `DET-001` through `DET-004`.
- Added committed lab/synthetic test evidence for `DET-002`.
- Expanded the evidence register to cover every actor in `data/actors.csv` with
  at least one claim-backed evidence row.
- Hardened repository validation for evidence, hunt, detection, health, and DRL
  evidence-pack cross-references.
- Added public CI and Pages deployment evidence.

Remaining production blockers:

- No detection is DRL-9.
- `DET-001`, `DET-003`, and `DET-004` still need positive and negative
  environment tests.
- `DET-002` has committed lab/synthetic evidence, but still needs backend
  conversion, historical replay, pilot review, and measured false-positive
  rate before promotion.
- Sigma/KQL examples remain hunt starters or pilot candidates until local
  telemetry validation is complete.

## v0.1.3

Status: professional methodology and hunt-starter baseline.

Key changes:

- Added source provenance fields: publication, access, review, update, archive,
  and hash metadata.
- Added persona-claims register to separate public claims from verified
  compromise.
- Added ATT&CK mapping-quality discipline.
- Added platform field mapping, SOC triage playbooks, and detection health
  tracking.

## v0.1.2

Status: expanded actor and taxonomy coverage.

Key changes:

- Added missing high-priority actor profiles including Scarred Manticore,
  Imperial Kitten, Pioneer Kitten, DarkBit, Lyceum, and APT39.
- Corrected actor taxonomy and sponsor caveats.
- Added additional Sigma/KQL hunt examples.

## v0.1.0

Status: initial public CTI knowledge-base structure.

Key changes:

- Initial actor register, source register, ATT&CK mapping table, report pages,
  and detection examples.
