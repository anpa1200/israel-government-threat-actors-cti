---
title: StandardKeyboard
sidebar_label: StandardKeyboard
---

# StandardKeyboard

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Imperial Kitten](../actors/imperial-kitten.md)
- Tool type(s): Backdoor / C2 tool
- Confidence level(s): Medium
- Source ID(s): `SRC-CS-IMPERIAL-KITTEN-2023`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Public vendor reporting describes email-based C2 aligned with Imperial Kitten tooling. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Hash not committed; use CrowdStrike source if available. | `SRC-CS-IMPERIAL-KITTEN-2023` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Use as enrichment term until primary technical behavior is fully captured in repository evidence. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Avoid unsupported behavior claims. |

## Crosslinks

- Imperial Kitten: [profile](../actors/imperial-kitten.md), [workbench](../navigation/actor-workbench.md#imperial-kitten), [tool matrix](../malware-tool-intelligence.md#imperial-kitten)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise | Initial Access | M2 | `SRC-CS-IMPERIAL-KITTEN-2023` |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1071.003](../navigation/ttp-detection-matrix.md#t1071003) Mail Protocols | Command and Control | M3 | `SRC-PWC-YELLOW-LIDERC-2023` |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1059.005](../navigation/ttp-detection-matrix.md#t1059005) Visual Basic | Execution | M2 | `SRC-PWC-YELLOW-LIDERC-2023` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CS-IMPERIAL-KITTEN-2023`](https://www.crowdstrike.com/en-us/blog/imperial-kitten-deploys-novel-malware-families/) | CrowdStrike | 2023-11-09 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
