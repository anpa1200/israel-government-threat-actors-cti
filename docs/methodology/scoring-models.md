---
title: Scoring Models
sidebar_label: Scoring Models
---

# Scoring Models

This project uses separate scores for source quality, claim quality, analyst confidence, threat priority, and detection readiness. These scores MUST NOT be collapsed into one generic risk number.

## Source Reliability

Adapted from the NATO Admiralty Code (STANAG 2511). See also Sherman Kent's words-of-estimative-probability framework for the parallel information-credibility scale.

| Score | Meaning | Use |
| --- | --- | --- |
| A | Highly reliable source with strong methodology or direct evidence. | May anchor actor profiles, scenarios, and detection logic. |
| B | Generally reliable source or strong secondary synthesis. | Useful for context and hypothesis development. |
| C | Mixed reliability, limited detail, or weak methodology. | Watchlist only unless corroborated. |
| D | Unknown reliability or unverified public claim. | Lead only. |
| E | Known issues or weak sourcing. | Do not use for decisions without independent evidence. |
| F | Unreliable or deceptive. | Exclude from decisions. |

## Information Credibility

| Score | Meaning |
| --- | --- |
| 1 | Confirmed by local telemetry or multiple independent reliable sources. |
| 2 | Probably true; strong single source or partial corroboration. |
| 3 | Possibly true; plausible but limited support. |
| 4 | Doubtful; weak, stale, or conflicting support. |
| 5 | Improbable based on stronger contrary evidence. |
| 6 | Cannot be judged with available evidence. |

## Analyst Confidence

| Level | Minimum Criteria |
| --- | --- |
| High | Direct or well-corroborated evidence, current reporting, short inference chain, no material unresolved contradiction. |
| Moderate | Credible but incomplete evidence, partial corroboration, or plausible alternatives. |
| Low | Thin, indirect, stale, weakly corroborated, or assumption-heavy evidence. |

## Threat Scenario Priority Score

Use a 1-5 scale for each dimension:

```text
Threat Scenario Priority Score = Likelihood + Impact + Exposure + Detection Gap + Time Sensitivity
```

| Total | Priority | Required Treatment |
| --- | --- | --- |
| 21-25 | Critical | MUST have a hunt, detection, control, or telemetry remediation plan. |
| 16-20 | High | SHOULD enter the detection backlog or active hunt plan. |
| 11-15 | Medium | Track and schedule based on capacity. |
| 5-10 | Low | Keep as context unless conditions change. |

## Detection Readiness Level

| DRL | Meaning |
| --- | --- |
| DRL-0 | Idea only; no observable defined. |
| DRL-1 | Observable behavior defined. |
| DRL-2 | Required telemetry identified. |
| DRL-3 | Telemetry exists and required fields are confirmed. |
| DRL-4 | Hunt query or prototype detection drafted. |
| DRL-5 | Positive and negative test cases defined. |
| DRL-6 | Tested in lab or replay dataset. |
| DRL-7 | Pilot deployed with SOC review. |
| DRL-8 | Tuned with false-positive review and documented triage. |
| DRL-9 | Production deployed, monitored, and owner assigned. |

Only DRL-9 detections MAY be described as production coverage.

