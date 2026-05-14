---
title: Threat Hunting Workflow
sidebar_label: Hunt Workflow
---

# Threat Hunting Workflow

Threat hunts in this repository begin with a PIR and end with one of four outcomes:

- Detection candidate.
- Confirmed benign baseline.
- Telemetry gap.
- Incident-response escalation.

## Workflow

1. Select a PIR and scenario from the registers.
2. Convert the scenario into one falsifiable hypothesis.
3. Identify required telemetry, fields, retention, and parsing.
4. Draft a query or manual analytic procedure.
5. Define expected true-positive and benign outcomes.
6. Run the hunt against scoped data.
7. Record findings in the evidence register.
8. Convert repeatable behavior into detection backlog items.
9. Close with a decision, metric, or telemetry remediation task.

## Hunt Hypothesis Format

```text
If [actor/pattern] is active against [asset/sector], then [observable behavior]
should appear in [telemetry source] within [time window], distinguishable from
baseline by [condition].
```

Example:

```text
If MuddyWater-style RMM abuse is active against a ministry supplier, then new
AnyDesk, Atera, or ScreenConnect execution should appear from user download or
temporary paths on non-helpdesk endpoints within the last 30 days, distinguishable
from baseline by absence from the approved RMM inventory.
```

## Hunt Closure States

| State | Meaning |
| --- | --- |
| `No Finding` | Query ran and did not identify suspicious activity. |
| `Benign Baseline` | Activity exists but is explained and documented. |
| `Suspicious Lead` | Activity requires enrichment or escalation. |
| `Detection Candidate` | Repeatable logic should move to detection engineering. |
| `Telemetry Gap` | Required telemetry is missing or unusable. |
| `IR Escalation` | Evidence suggests active compromise or material risk. |

