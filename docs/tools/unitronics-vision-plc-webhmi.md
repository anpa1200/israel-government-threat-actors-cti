---
title: Unitronics Vision PLC Web/HMI
sidebar_label: Unitronics Vision PLC Web/HMI
---

# Unitronics Vision PLC Web/HMI

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [CyberAv3ngers](../actors/cyberav3ngers.md)
- Tool type(s): Targeted technology
- Confidence level(s): High
- Source ID(s): `SRC-CISA-AA23-335A`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Internet-exposed HMI-capable Unitronics PLCs targeted in IRGC-affiliated activity. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Not malware; no hash. Exposure and configuration indicators only. | `SRC-CISA-AA23-335A` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Inventory internet-exposed PLC/HMI paths, enforce passwords, restrict remote access, and monitor HMI defacement attempts. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Use for exposure management and OT triage. |

## Crosslinks

- CyberAv3ngers: [profile](../actors/cyberav3ngers.md), [workbench](../navigation/actor-workbench.md#cyberav3ngers), [tool matrix](../malware-tool-intelligence.md#cyberav3ngers)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | [T0883](../navigation/ttp-detection-matrix.md#t0883) Internet Accessible Device | Initial Access | M2 | `SRC-CISA-AA23-335A` |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | [T0836](../navigation/ttp-detection-matrix.md#t0836) Modify Parameter | Impact | M2 | `SRC-CISA-AA26-097A` |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | [T0832](../navigation/ttp-detection-matrix.md#t0832) Manipulation of View | Impact | M2 | `SRC-CISA-AA23-335A` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CISA-AA23-335A`](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) | CISA | 2023-12-01 | A | Government advisory | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
