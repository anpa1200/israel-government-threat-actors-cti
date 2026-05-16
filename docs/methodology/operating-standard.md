---
title: CTI-To-Detection Operating Standard
sidebar_label: Operating Standard
---

# CTI-To-Detection Operating Standard

This repository is not only an actor encyclopedia. It is designed to support threat hunting and CTI-based detection engineering for Israeli government, public-sector, municipal, critical infrastructure, telecom, defense-adjacent, and supplier environments.

## Mandatory Rules

1. Every intelligence task MUST support a defensive decision, asset risk, hunt, detection, SOC workflow, or collection requirement.
2. Every major claim MUST identify source, evidence label, source reliability, information credibility, analyst confidence, and known gaps.
3. Actor attribution MUST NOT be based on IOC matching alone.
4. IOC references MUST NOT move directly to blocking without source review, freshness check, enrichment, customer relevance, expiry, owner, and operational-risk review.
5. A detection MUST NOT be accepted unless the required telemetry, fields, parsing, and retention are confirmed.
6. A detection MUST include positive tests, negative tests, expected false positives, triage instructions, severity logic, and rollback criteria.
7. ATT&CK mapping MUST NOT be counted as coverage unless there is tested hunt logic, tested detection logic, or validated telemetry coverage.
8. High-risk scenarios MUST remain visible even when telemetry is weak. Weak telemetry creates a remediation backlog item, not a reason to drop the scenario.
9. AI-assisted analysis MUST be treated as draft until reviewed by a human analyst against source evidence.
10. Public persona claims MUST be separated from verified compromise.

## Claim-To-Action Chain

Every high-value item SHOULD be traceable through this chain:

```text
Source -> Claim -> Evidence -> Assessment -> Israeli Relevance -> Scenario -> Observable -> Telemetry -> Hunt/Detection -> Test -> SOC Action -> Decision -> Metric
```

If an item cannot move across the chain, classify it as context, a lead, or an intelligence gap rather than a finished detection-engineering input.

## Evidence Labels

Use one evidence label per material claim:

| Label | Meaning |
| --- | --- |
| `Observed` | Confirmed in local telemetry, logs, malware analysis, or controlled testing. |
| `Source-reported` | Stated directly by a cited source. |
| `Assessed-by-source` | Analytic judgment made by a cited source. |
| `Assessed-here` | Repository analyst judgment based on available evidence. |
| `Inferred` | Reasonable interpretation from evidence, but not directly observed. |
| `Gap` | Missing evidence needed to increase confidence or rule out alternatives. |

## Required Output Pattern

For the canonical ATT&CK mapping rule, use the Field Manual [ATT&CK as a Working Tool](https://anpa1200.github.io/cti-analyst-field-manual/docs/frameworks/mitre-attack-as-working-tool/) page and this project's [Fact Correlation](../fact-correlation.md) page.


Any threat-hunting or detection-engineering item SHOULD include:

- PIR or defensive decision.
- Actor, persona, scenario, or behavior pattern.
- Claim IDs and evidence IDs.
- Behavior-backed ATT&CK technique and mapping quality when defensible, or `ATT&CK mapping: Gap / Not mapped` when evidence does not support a technique.
- Observable behavior.
- Required telemetry and fields.
- Detection Readiness Level.
- Test plan.
- SOC action.
- Owner and lifecycle status.

## Cross-Links

- [Fact Correlation](../fact-correlation.md) — shared rules and canonical owners across the three-project ecosystem
- [Source Rating](../source-rating.md) — Admiralty Code A-F and 1-6 scales used in evidence labels
- [CTI Analyst Field Manual — Evidence Labels](https://anpa1200.github.io/cti-analyst-field-manual/docs/01-cti-foundations/evidence-labels) — canonical evidence label definitions (Observed, Reported, Assessed, Inferred, Unknown, Gap)
- [CTI Analyst Field Manual — Source Reliability](https://anpa1200.github.io/cti-analyst-field-manual/docs/01-cti-foundations/source-reliability) — full Admiralty Code tables with warning on treating ratings as mathematical truth
- [CTI Analyst Field Manual — ATT&CK as a Working Tool](https://anpa1200.github.io/cti-analyst-field-manual/docs/frameworks/mitre-attack-as-working-tool/) — mapping quality M0–M4 scale
- [CTI Analyst Field Manual — Detection Readiness Levels](https://anpa1200.github.io/cti-analyst-field-manual/docs/08-cti-to-detection/detection-readiness-levels) — DRL model (DRL-9 = production only)
- [Customer project — Normative Language](https://anpa1200.github.io/customer-driven-ai-cti-project/docs/standard/normative-language/) — MUST/SHOULD/MAY definitions that align with mandatory rules above

