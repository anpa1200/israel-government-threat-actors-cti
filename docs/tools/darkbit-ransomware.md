---
title: DarkBit ransomware
sidebar_label: DarkBit ransomware
---

# DarkBit ransomware

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [DarkBit](../actors/darkbit.md)
- Tool type(s): Pseudo-ransomware / destructive malware
- Confidence level(s): Medium
- Source ID(s): `SRC-INCD-DARKBIT-MUDDYWATER-2023`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [DarkBit](../actors/darkbit.md) | Persona and payload associated with the Technion February 2023 incident and MuddyWater/MERCURY ecosystem reporting. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [DarkBit](../actors/darkbit.md) | Hash not committed; incident-specific IOCs should come from INCD/Microsoft source material. | `SRC-INCD-DARKBIT-MUDDYWATER-2023` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [DarkBit](../actors/darkbit.md) | Hunt pseudo-ransom notes, mass file changes, destructive cloud/on-prem actions, and MuddyWater/MERCURY overlap. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [DarkBit](../actors/darkbit.md) | Treat DarkBit primarily as operation/persona unless source proves payload linkage. |

## Crosslinks

- DarkBit: [profile](../actors/darkbit.md), [workbench](../navigation/actor-workbench.md#darkbit), [tool matrix](../malware-tool-intelligence.md#darkbit)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [DarkBit](../actors/darkbit.md) | [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact | Impact | M2 | `SRC-INCD-DARKBIT-MUDDYWATER-2023` |
| [DarkBit](../actors/darkbit.md) | [T1490](../navigation/ttp-detection-matrix.md#t1490) Inhibit System Recovery | Impact | M2 | `SRC-MS-MERCURY-DEV1084-2023` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-INCD-DARKBIT-MUDDYWATER-2023`](https://www.gov.il/en/pages/_muddywater) | Israel National Cyber Directorate | 2023-03-01 | A | Government report | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
