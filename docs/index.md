---
id: index
slug: /
title: Israel Government Threat Actors CTI
sidebar_label: Overview
sidebar_position: 1
---

# Israel Government Threat Actors CTI

This documentation organizes [public-source threat intelligence](https://1200km.com/cti-analyst-field-manual/docs/cti-foundations/what-is-cti/) for defensive use by Israeli government and public-sector defenders.

## CTI Ecosystem

This knowledge base is the Israel-focused actor and sector layer of a three-book CTI ecosystem. Use [CTI Project Ecosystem](ecosystem.md) to navigate between the books.

- [CTI Analyst Field Manual](https://1200km.com/cti-analyst-field-manual/) provides general CTI tradecraft for evidence, attribution, infrastructure pivoting, and CTI-to-detection work.
- [Customer-Driven AI CTI Project](https://1200km.com/customer-driven-ai-cti-project/) provides the gated delivery methodology for turning this intelligence into customer-ready outcomes.

## Reading Order

1. [Threat Model](israel-government-threat-model.md)
2. [Source Rating](source-rating.md)
3. [Actor Index](actors/README.md)
4. [Actor Navigation Workbench](navigation/actor-workbench.md)
5. [TTP To Detection Matrix](navigation/ttp-detection-matrix.md)
6. [Surface And Capability Matrix](navigation/surface-capability-matrix.md)
7. [Connected TIPs And CTI Feeds](connected-tips.md)
8. [VirusTotal Malware Enrichment](virustotal-enrichment.md)
9. [Intelligence Update Queue](intelligence-updates.md)
10. [Report Index](reports/README.md)
11. [CTI-to-Detection Operating Standard](methodology/operating-standard.md)
12. [Threat Hunting Workflow](threat-hunting/hunt-workflow.md)
13. [Detection Lifecycle](detection-engineering/detection-lifecycle.md)
14. Scored source library in `sources/`
15. Detection examples in `detections/sigma/` and `detections/kql/`

## Operating Rules

- Analysts MUST distinguish [source facts from analytic inference](https://1200km.com/cti-analyst-field-manual/docs/cti-foundations/evidence-labels/).
- Analysts SHOULD cite at least one source record for every actor claim.
- Detections MUST be validated against local telemetry before production deployment.
- IOC matches SHOULD be treated as leads, not final attribution.
- Threat hunts SHOULD start from a PIR, scenario, and evidence record.
- Production coverage MUST NOT be claimed below DRL-9.
