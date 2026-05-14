---
id: index
slug: /
title: Israel Government Threat Actors CTI
sidebar_label: Overview
sidebar_position: 1
---

# Israel Government Threat Actors CTI

This documentation organizes public-source threat intelligence for defensive use by Israeli government and public-sector defenders.

## Reading Order

1. [Threat Model](israel-government-threat-model.md)
2. [Source Rating](source-rating.md)
3. [Actor Index](actors/README.md)
4. [Report Index](reports/README.md)
5. [CTI-to-Detection Operating Standard](methodology/operating-standard.md)
6. [Threat Hunting Workflow](threat-hunting/hunt-workflow.md)
7. [Detection Lifecycle](detection-engineering/detection-lifecycle.md)
8. Scored source library in `sources/`
9. Detection examples in `detections/sigma/` and `detections/kql/`

## Operating Rules

- Analysts MUST distinguish source facts from analytic inference.
- Analysts SHOULD cite at least one source record for every actor claim.
- Detections MUST be validated against local telemetry before production deployment.
- IOC matches SHOULD be treated as leads, not final attribution.
- Threat hunts SHOULD start from a PIR, scenario, and evidence record.
- Production coverage MUST NOT be claimed below DRL-9.
