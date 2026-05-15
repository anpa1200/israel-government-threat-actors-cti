---
title: Replay Datasets
sidebar_label: Replay Datasets
---

# Replay Datasets

The repository includes small synthetic, lab-realistic replay datasets under
`examples/replay-datasets/`.

These files support parser checks, rule walkthroughs, and reviewer validation of
expected positive and benign boundary cases. They do not contain customer
telemetry and do not establish production false-positive rates.

## Included Datasets

| Dataset | Detection | Positive Rows | Benign Boundary Rows |
| --- | --- | --- | --- |
| `det-001-intune-auditlogs.csv` | `DET-001` | 2 | 4 |
| `det-002-windows-process-events.csv` | `DET-002` | 2 | 4 |
| `det-003-ot-web-access.csv` | `DET-003` | 2 | 4 |
| `det-004-mail-click-exec.csv` | `DET-004` | 2 | 4 |

## Use

Use these datasets to:

- verify field parsing before adapting a query;
- demonstrate expected match and non-match cases;
- build local unit tests for SIEM content;
- explain detection behavior during SOC handoff.

Do not use them to claim DRL-7, DRL-8, or DRL-9. Promotion still requires
environment replay, measured alert volume, SOC review, and owner approval.
