---
title: DRL Evidence Packs
sidebar_label: DRL Evidence Packs
---

# DRL Evidence Packs

This page summarizes the current detection-readiness evidence packs. The packs
are intentionally conservative: they document what has been tested, what has not
been tested, and which blockers prevent a detection from being described as
production coverage.

Production coverage is not claimed for any detection in this repository unless
the detection reaches DRL-9 and has owner approval, rollback procedure, health
metric, and change record.

## Current Packs

| Detection | Current DRL | Pack | Production Status |
| --- | --- | --- | --- |
| `DET-001` Intune Bulk Device Wipe Anomaly | DRL-5 | `examples/drl-evidence-packs/DET-001-intune-bulk-device-wipe-anomaly.md` | Not production approved. Tenant replay and false-positive review required. |
| `DET-002` Suspicious RMM Installer Download From User Context | DRL-6 | `examples/drl-evidence-packs/DET-002-suspicious-rmm-file-sharing-download.md` | Pilot candidate. Backend conversion, negative tests, and historical replay required. |
| `DET-003` Unitronics PLC HMI Web Interface Access | DRL-4 | `examples/drl-evidence-packs/DET-003-unitronics-plc-hmi-web-interface-access.md` | Hunt starter only. OT telemetry mapping and owner-approved tests required. |
| `DET-004` Mail Click To Execution Correlation | DRL-4 | `examples/drl-evidence-packs/DET-004-mail-click-to-exec-correlation.md` | Hunt starter only. Defender XDR validation and replay required. |

## Minimum Promotion Rules

- DRL-6 requires positive and negative test cases, with at least lab or replay
  evidence.
- DRL-7 requires scoped pilot deployment and SOC review.
- DRL-8 requires false-positive tuning and documented triage.
- DRL-9 requires production owner, rollback plan, alert health metric, change
  record, review date, and expiry or maintenance date.

## Reviewer Interpretation

The presence of an evidence pack means the detection has a controlled promotion
path. It does not mean the detection is production-ready. The current packs are
designed to make the remaining work explicit enough for a SOC, detection
engineer, or reviewer to reproduce and challenge.
