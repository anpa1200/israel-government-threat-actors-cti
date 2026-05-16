---
title: MechaFlounder
sidebar_label: MechaFlounder
---

# MechaFlounder

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [APT39](../actors/apt39.md)
- Tool type(s): Backdoor
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G0087`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT39](../actors/apt39.md) | MITRE ATT&CK lists MechaFlounder as software used by this actor; track it as APT39-linked command execution and collection behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT39](../actors/apt39.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0087` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Hunt for MechaFlounder execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- APT39: [profile](../actors/apt39.md), [workbench](../navigation/actor-workbench.md#apt39), [tool matrix](../malware-tool-intelligence.md#apt39)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [APT39](../actors/apt39.md) | [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M2 | `SRC-MITRE-G0087` |
| [APT39](../actors/apt39.md) | [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G0087` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G0087`](https://attack.mitre.org/groups/G0087/) | MITRE ATT&CK | 2026-05-14 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
