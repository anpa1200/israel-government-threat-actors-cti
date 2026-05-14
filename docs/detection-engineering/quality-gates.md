---
title: Quality Gates
sidebar_label: Quality Gates
---

# Quality Gates

Quality gates prevent weak CTI from becoming weak detections.

## Gate A: PIR Approval

Must prove:

- PIR supports a real defensive decision.
- Owner and time horizon are defined.
- Confidence threshold is stated.

## Gate B: Scenario Approval

Must prove:

- Source claims are traceable.
- Israeli relevance is explicit.
- Priority score is calculated.
- Alternative explanations and gaps are visible.

## Gate C: Hunt Approval

Must prove:

- Hypothesis is falsifiable.
- Telemetry and fields are identified.
- Query or procedure is scoped.
- Closure criteria are defined.

## Gate D: Detection Design Approval

Must prove:

- Observable maps to telemetry.
- ATT&CK mapping quality is M3 or better.
- False positives and SOC action are documented.
- Test plan exists.

## Gate E: Production Approval

Must prove:

- DRL-9 requirements are met.
- Pilot results are reviewed.
- Triage and rollback are documented.
- Owner and review date are assigned.

## Gate F: Final Delivery

Must prove:

- Claims, detections, hunts, gaps, and decisions are traceable.
- Metrics are reported.
- Remaining risk is explicit.
- Deprecated or weak items are not presented as production coverage.

