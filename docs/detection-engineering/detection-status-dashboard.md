---
title: Detection Status Dashboard
sidebar_label: Detection Status Dashboard
---

# Detection Status Dashboard

Generated from `examples/registers/detection-backlog.csv`,
`examples/registers/detection-health-register.csv`, and
`examples/registers/metrics.csv`.

Production coverage is not claimed unless a detection reaches DRL-9.

## Detection Status

| Detection | DRL | Release Status | Health | Test Status | Evidence Pack |
| --- | --- | --- | --- | --- | --- |
| `DET-001` Intune Bulk Device Wipe Anomaly | 5 | Hunt | Needs Pilot | Synthetic positive/negative fixture tests committed; needs tenant replay test; Sigma companion is base event selector only | `examples/drl-evidence-packs/DET-001-intune-bulk-device-wipe-anomaly.md` |
| `DET-002` Suspicious RMM Installer Download From User Context | 6 | Pilot | Usable | Synthetic positive/negative fixture tests and synthetic 30-day replay committed | `examples/drl-evidence-packs/DET-002-suspicious-rmm-file-sharing-download.md` |
| `DET-003` Unitronics PLC HMI Web Interface Access | 4 | Hunt | Needs Telemetry | Synthetic positive/negative fixture tests committed; needs environment-specific field mapping | `examples/drl-evidence-packs/DET-003-unitronics-plc-hmi-web-interface-access.md` |
| `DET-004` Mail Click To Execution Correlation | 4 | Hunt | Needs Pilot | Synthetic positive/negative fixture tests committed; needs Defender XDR validation | `examples/drl-evidence-packs/DET-004-mail-click-to-exec-correlation.md` |

## Health Metrics

| Metric | Value | Unit | Notes |
| --- | --- | --- | --- |
| `MET-001` Mean detection readiness level | 4.75 | DRL | Average of current sample detections; production target is DRL-9 for deployed analytics. |
| `MET-002` ATT&CK mappings at M3 or better | 14 | count | Only M3/M4 rows should be counted as defensive coverage. |
| `MET-003` Evidence records with claim IDs | 27 | count | Expanded claim backbone; continue until every major actor-page assertion has an evidence ID. |
| `MET-004` Persona claims requiring corroboration | 3 | count | Tracks public claims separately from confirmed incidents. |
| `MET-005` Sources past review date | 0 | count | Calculated by scripts/check_source_freshness.py using repository review cadence. |
| `MET-006` Broken or unavailable download targets | 10 | count | Includes failed, failed_placeholder, and not_found records in data/research-downloads.csv. |
| `MET-007` Detections without positive tests | 0 | count | All four sample detections have committed synthetic positive fixture tests; real tenant/platform replay remains outstanding. |
| `MET-008` Detections without negative tests | 0 | count | All four sample detections have committed synthetic negative fixture tests; real benign baseline replay remains outstanding. |
| `MET-009` Actors without current 2024+ source | 4 | count | Watchlist estimate for actors needing recency review: APT39, Lebanese Cedar, UNC3890, Lyceum. |
| `MET-010` Detections with SOC triage coverage | 4 | count | Generic SOC triage playbooks cover the four sample detections; rule-specific triage still required for production. |
| `MET-011` Detection backlog rows with concrete DRL evidence packs | 4 | count | Each sample detection now points to a detection-specific DRL evidence pack rather than only the generic template. |
| `MET-012` Actor profiles with at least one evidence-register row | 21 | count | Every actor_id in data/actors.csv now has at least one corresponding evidence-register record. |
| `MET-013` Detections with committed lab test evidence | 4 | count | All four sample detections have committed synthetic positive and negative lab evidence; no production telemetry replay is claimed. |
| `MET-014` Detections with measured synthetic false-positive rate | 4 | count | All four sample detections report 0.00% false-positive rate on deterministic benign fixtures only. |
| `MET-015` Detections with real tenant or customer historical replay | 0 | count | No real tenant/customer telemetry replay is committed; this is a known production-readiness blocker. |

## Interpretation

- `Hunt` means a query or rule is suitable for analyst-driven review.
- `Pilot` means the detection has enough evidence for scoped SOC review.
- `Production` is reserved for DRL-9 detections only.
- Synthetic test rates do not replace tenant replay or customer false-positive analysis.
