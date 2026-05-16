---
title: Desert Scorpion
sidebar_label: Desert Scorpion
---

# Desert Scorpion

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [APT-C-23](../actors/arid-viper.md)
- Tool type(s): Mobile malware
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G1028`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | MITRE ATT&CK lists Desert Scorpion as software used by this actor; track it as mobile surveillance behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1028` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hunt for Desert Scorpion execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- APT-C-23: [profile](../actors/arid-viper.md), [workbench](../navigation/actor-workbench.md#apt-c-23), [tool matrix](../malware-tool-intelligence.md#apt-c-23)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | [T1660](../navigation/ttp-detection-matrix.md#t1660) Phishing | Initial Access (Mobile) | M2 | `SRC-ESET-ARIDSPY` |
| [APT-C-23](../actors/arid-viper.md) | [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File | Execution | M3 | `SRC-ESET-ARIDSPY` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G1028`](https://attack.mitre.org/groups/G1028/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
