---
title: CI Validation Evidence
sidebar_label: CI Validation Evidence
---

# CI Validation Evidence

This page records public GitHub Actions evidence for repository validation and
site build health. It complements the README badge and local `npm run validate`
output.

## Latest Verified Runs

Checked on 2026-05-15.

| Workflow | Commit | Status | Conclusion | Run URL |
| --- | --- | --- | --- | --- |
| Validate CTI Repository | `6653aa4` | completed | success | https://github.com/anpa1200/israel-government-threat-actors-cti/actions/runs/25923044633 |
| Deploy Docusaurus to GitHub Pages | `6653aa4` | completed | success | https://github.com/anpa1200/israel-government-threat-actors-cti/actions/runs/25923044628 |

## Validation Scope

The validation workflow runs:

- `python3 scripts/validate_repo.py`
- `python3 scripts/check_source_freshness.py`
- `python3 scripts/run_detection_fixture_tests.py`
- `npm ci`
- `npm run build`

The local validation output for the same hardening cycle reported:

```text
Repository validation passed
sources_total=89
sources_stale=0
sources_missing_review_date=0
download_records_total=42
download_records_unavailable=10
DET-001: TP=1 FP=0 TN=1 FN=0 synthetic_fp_rate=0.00%
DET-002: TP=1 FP=0 TN=1 FN=0 synthetic_fp_rate=0.00%
DET-003: TP=1 FP=0 TN=1 FN=0 synthetic_fp_rate=0.00%
DET-004: TP=1 FP=0 TN=1 FN=0 synthetic_fp_rate=0.00%
Docusaurus build passed
```

The GitHub Actions workflows also opt in to Node.js 24 JavaScript actions
execution with `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` to avoid relying on the
deprecated Node.js 20 action runtime.

## Interpretation

CI success proves repository hygiene and site build health. It does not prove
that Sigma/KQL rules are production-ready, that detections are tuned, or that
the analytics have been validated against customer telemetry. Production claims
still require DRL evidence packs.
