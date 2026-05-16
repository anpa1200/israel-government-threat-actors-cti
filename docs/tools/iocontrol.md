---
title: IOControl
sidebar_label: IOControl
---

# IOControl

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [CyberAv3ngers](../actors/cyberav3ngers.md)
- Tool type(s): OT/IoT malware
- Confidence level(s): High
- Source ID(s): `SRC-CLAROTY-IOCONTROL-2024`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Custom OT/IoT malware linked by Claroty Team82 to CyberAv3ngers-aligned activity; reported behavior includes MQTT over 8883 and DoH. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Hash not committed; use Claroty IOC appendix/current report. | `SRC-CLAROTY-IOCONTROL-2024` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Hunt OT/IoT devices with unusual MQTT/DoH, router persistence, and PLC/HMI manipulation indicators. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | Do not store samples; coordinate with OT owners. |

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
| [`SRC-CLAROTY-IOCONTROL-2024`](https://claroty.com/team82/research/inside-a-new-ot-iot-cyber-weapon-iocontrol) | Claroty Team82 | 2024-12-10 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
