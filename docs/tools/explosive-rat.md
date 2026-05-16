---
title: Explosive RAT
sidebar_label: Explosive RAT
---

# Explosive RAT

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Lebanese Cedar](../actors/lebanese-cedar.md)
- Tool type(s): Remote Access Trojan
- Confidence level(s): Medium
- Source ID(s): `SRC-CLEARSKY-LEBANESE-CEDAR`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | Custom RAT associated with Lebanese Cedar / Volatile Cedar reporting. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | Hash not committed; use ClearSky report references. | `SRC-CLEARSKY-LEBANESE-CEDAR` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | Hunt Java web compromise leading to RAT staging and long-lived outbound access. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | Do not store samples. |

## Crosslinks

- Lebanese Cedar: [profile](../actors/lebanese-cedar.md), [workbench](../navigation/actor-workbench.md#lebanese-cedar), [tool matrix](../malware-tool-intelligence.md#lebanese-cedar)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-CLEARSKY-LEBANESE-CEDAR` |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-CLEARSKY-LEBANESE-CEDAR` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CLEARSKY-LEBANESE-CEDAR`](https://www.clearskysec.com/cedar/) | ClearSky Cyber Security | 2021-01-28 | B | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
