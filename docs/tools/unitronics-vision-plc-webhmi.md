---
title: Unitronics Vision PLC Web/HMI
sidebar_label: Unitronics Vision PLC Web/HMI
---

# Unitronics Vision PLC Web/HMI

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [CyberAv3ngers](../actors/cyberav3ngers.md)
- Tool type: Targeted technology
- Confidence: High
- Source: [`SRC-CISA-AA23-335A`](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- Source title: CISA, IRGC-affiliated CyberAv3ngers exploit Unitronics PLCs, 2023-12-01

## Behavior

Internet-exposed HMI-capable Unitronics PLCs targeted in IRGC-affiliated activity.

## Hash And IOC Status

- Status: Not malware; no hash. Exposure and configuration indicators only.
- Reference: `SRC-CISA-AA23-335A`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Inventory internet-exposed PLC/HMI paths, enforce passwords, restrict remote access, and monitor HMI defacement attempts.

## Handling Notes

Use for exposure management and OT triage.

## Crosslinks

- Actor profile: [CyberAv3ngers](../actors/cyberav3ngers.md)
- Actor workbench: [CyberAv3ngers](../navigation/actor-workbench.md#cyberav3ngers)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#cyberav3ngers)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T0883](../navigation/ttp-detection-matrix.md#t0883) Internet Accessible Device | Initial Access | M2 | `SRC-CISA-AA23-335A` |
| [T0836](../navigation/ttp-detection-matrix.md#t0836) Modify Parameter | Impact | M2 | `SRC-CISA-AA26-097A` |
| [T0832](../navigation/ttp-detection-matrix.md#t0832) Manipulation of View | Impact | M2 | `SRC-CISA-AA23-335A` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

- Source ID: `SRC-CISA-AA23-335A`
- Reliability in source register: A
- Source type: Government advisory
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
