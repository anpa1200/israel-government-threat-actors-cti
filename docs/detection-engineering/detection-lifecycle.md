---
title: Detection Lifecycle
sidebar_label: Detection Lifecycle
---

# Detection Lifecycle

Detection engineering in this repository uses CTI as input, but production deployment requires engineering evidence.

## Lifecycle

| Stage | Required Output |
| --- | --- |
| Intake | PIR, scenario, source/evidence IDs, ATT&CK technique, customer relevance. |
| Design | Observable, telemetry source, fields, expected false positives, severity, SOC action. |
| Prototype | Sigma, KQL, SPL, Elastic, or platform-native query. |
| Test | Positive test, negative test, edge case, replay or historical validation. |
| Pilot | Scoped deployment, false-positive review, SOC feedback. |
| Production | DRL-9, owner, rollback plan, health metric, change record. |
| Maintenance | Expiry review, source refresh, tuning, retirement decision. |

## Detection Quality Requirements

A detection MUST include:

- `what it detects`;
- `why it matters`;
- source/evidence IDs;
- ATT&CK technique and mapping quality;
- log source and fields;
- rule logic;
- false-positive assumptions;
- test method;
- SOC triage steps;
- owner and review date.

## Mapping Quality

| Level | Meaning |
| --- | --- |
| M0 | No ATT&CK mapping. |
| M1 | Actor-level mapping only. |
| M2 | Technique selected but observable is generic. |
| M3 | Technique and observable are explicitly tied to the rule logic. |
| M4 | Technique, observable, telemetry, and test evidence are all documented. |

Only M3 or M4 mappings SHOULD be counted as defensive coverage.

## Production Evidence Pack

A DRL-9 detection MUST have an evidence pack with:

- source and evidence IDs;
- platform-specific query or rule export;
- positive test result;
- negative test result;
- false-positive review;
- expected alert volume;
- tuning guidance;
- SOC triage procedure;
- owner and rollback plan;
- review date and expiry date.

Rules at DRL-4 to DRL-6 remain hunt starters or pilots even when their ATT&CK
mapping is strong. Do not market them as production coverage.

Use `examples/gates/drl-evidence-pack-template.md` before promoting any rule
above DRL-6.

The current detection-specific packs are summarized in
`docs/detection-engineering/drl-evidence-packs.md` and stored under
`examples/drl-evidence-packs/`.
