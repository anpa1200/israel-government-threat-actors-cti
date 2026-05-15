---
title: Known Limitations
sidebar_label: Known Limitations
---

# Known Limitations

This repository is a public defensive CTI-to-detection research project. It is
not a production SOC analytics package.

## Evidence

- Evidence coverage is broad but not exhaustive. Every actor has at least one
  evidence-register row, but not every sentence in every actor profile has a
  dedicated `claim_id`.
- Public persona claims remain unverified unless the persona-claims register
  records local telemetry or third-party corroboration.
- Secondary synthesis sources are useful for collection planning, but they must
  not override primary government, vendor, or victim reporting.

## Detection Engineering

- No detection is DRL-9.
- Synthetic fixture tests are committed for the four sample detections, but
  synthetic tests are not a substitute for customer telemetry, tenant replay, or
  SOC pilot review.
- Measured false-positive rates are currently synthetic fixture rates only.
  They do not predict production alert volume.
- Sigma rules pass local Sigma CLI semantic checks, but not every rule has a
  committed Splunk, Elastic, or Sentinel backend conversion artifact.
- KQL examples are hunt queries and require tenant-specific table, field, and
  permission validation.

## Source Collection

- Some publicly referenced sources could not be downloaded or promoted because
  stable primary URLs were not found.
- Raw research downloads are intentionally ignored and are represented by
  `data/research-downloads.csv` rather than committed full-page copies.
- Source freshness checks are deterministic and non-networked in CI; they check
  repository review dates, not live HTTP status.

## Operational Use

- Do not deploy detections from this repository directly into production without
  local field mapping, benign baseline replay, false-positive review, and owner
  approval.
- Do not use public actor labels as incident attribution without claim-level
  evidence review.
- Do not treat this project as legal, intelligence-community, or government
  attribution authority.
