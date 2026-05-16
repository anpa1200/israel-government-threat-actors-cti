---
title: NBTscan
sidebar_label: NBTscan
---

# NBTscan

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [APT39](../actors/apt39.md); [Agrius](../actors/agrius.md)
- Tool type(s): Network scanner
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G0087`, `SRC-MITRE-G1030`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT39](../actors/apt39.md) | MITRE ATT&CK lists NBTscan as software used by this actor; track it as NetBIOS/host discovery behavior. |
| [Agrius](../actors/agrius.md) | MITRE ATT&CK lists NBTscan as software used by this actor; track it as NetBIOS/host discovery behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT39](../actors/apt39.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0087` |
| [Agrius](../actors/agrius.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1030` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Hunt for NBTscan execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Agrius](../actors/agrius.md) | Hunt for NBTscan execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Agrius](../actors/agrius.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- APT39: [profile](../actors/apt39.md), [workbench](../navigation/actor-workbench.md#apt39), [tool matrix](../malware-tool-intelligence.md#apt39)
- Agrius: [profile](../actors/agrius.md), [workbench](../navigation/actor-workbench.md#agrius), [tool matrix](../malware-tool-intelligence.md#agrius)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [APT39](../actors/apt39.md) | [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M2 | `SRC-MITRE-G0087` |
| [APT39](../actors/apt39.md) | [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G0087` |
| [Agrius](../actors/agrius.md) | [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-MITRE-G1030` |
| [Agrius](../actors/agrius.md) | [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact | Impact | M2 | `SRC-MITRE-G1030` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Agrius](../actors/agrius.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Agrius](../actors/agrius.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G0087`](https://attack.mitre.org/groups/G0087/) | MITRE ATT&CK | 2026-05-14 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G1030`](https://attack.mitre.org/groups/G1030/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
