---
title: Mimikatz
sidebar_label: Mimikatz
---

# Mimikatz

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [OilRig](../actors/oilrig.md); [Magic Hound](../actors/apt35.md); [MuddyWater](../actors/muddywater.md); [APT39](../actors/apt39.md); [Lyceum](../actors/lyceum.md); [Agrius](../actors/agrius.md); [Void Manticore / Handala](../actors/handala.md)
- Tool type(s): Credential access tool
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G0049`, `SRC-MITRE-G0059`, `SRC-MITRE-G0069`, `SRC-MITRE-G0087`, `SRC-MITRE-G1001`, `SRC-MITRE-G1030`, `SRC-MITRE-G1055`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT39](../actors/apt39.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [Agrius](../actors/agrius.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [Lyceum](../actors/lyceum.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [Magic Hound](../actors/apt35.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [MuddyWater](../actors/muddywater.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [OilRig](../actors/oilrig.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |
| [Void Manticore / Handala](../actors/handala.md) | MITRE ATT&CK lists Mimikatz as software used by this actor; track it as credential dumping behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT39](../actors/apt39.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0087` |
| [Agrius](../actors/agrius.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1030` |
| [Lyceum](../actors/lyceum.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1001` |
| [Magic Hound](../actors/apt35.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0059` |
| [MuddyWater](../actors/muddywater.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0069` |
| [OilRig](../actors/oilrig.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0049` |
| [Void Manticore / Handala](../actors/handala.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1055` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Agrius](../actors/agrius.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Lyceum](../actors/lyceum.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Magic Hound](../actors/apt35.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [MuddyWater](../actors/muddywater.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [OilRig](../actors/oilrig.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Void Manticore / Handala](../actors/handala.md) | Hunt for Mimikatz execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT39](../actors/apt39.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Agrius](../actors/agrius.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Lyceum](../actors/lyceum.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Magic Hound](../actors/apt35.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [MuddyWater](../actors/muddywater.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [OilRig](../actors/oilrig.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Void Manticore / Handala](../actors/handala.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- OilRig: [profile](../actors/oilrig.md), [workbench](../navigation/actor-workbench.md#oilrig), [tool matrix](../malware-tool-intelligence.md#oilrig)
- Magic Hound: [profile](../actors/apt35.md), [workbench](../navigation/actor-workbench.md#magic-hound), [tool matrix](../malware-tool-intelligence.md#magic-hound)
- MuddyWater: [profile](../actors/muddywater.md), [workbench](../navigation/actor-workbench.md#muddywater), [tool matrix](../malware-tool-intelligence.md#muddywater)
- APT39: [profile](../actors/apt39.md), [workbench](../navigation/actor-workbench.md#apt39), [tool matrix](../malware-tool-intelligence.md#apt39)
- Lyceum: [profile](../actors/lyceum.md), [workbench](../navigation/actor-workbench.md#lyceum), [tool matrix](../malware-tool-intelligence.md#lyceum)
- Agrius: [profile](../actors/agrius.md), [workbench](../navigation/actor-workbench.md#agrius), [tool matrix](../malware-tool-intelligence.md#agrius)
- Void Manticore / Handala: [profile](../actors/handala.md), [workbench](../navigation/actor-workbench.md#void-manticore-handala), [tool matrix](../malware-tool-intelligence.md#void-manticore-handala)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [OilRig](../actors/oilrig.md) | [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M3 | `SRC-MITRE-G0049` |
| [OilRig](../actors/oilrig.md) | [T1049](../navigation/ttp-detection-matrix.md#t1049) System Network Connections Discovery | Discovery | M1 | `SRC-MITRE-G0049` |
| [Magic Hound](../actors/apt35.md) | [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link | Initial Access | M2 | `SRC-MITRE-G0059` |
| [Magic Hound](../actors/apt35.md) | [T1583.001](../navigation/ttp-detection-matrix.md#t1583001) Acquire Domains | Resource Development | M1 | `SRC-MITRE-G0059` |
| [MuddyWater](../actors/muddywater.md) | [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1059.001](../navigation/ttp-detection-matrix.md#t1059001) PowerShell | Execution | M2 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software | Command and Control | M3 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage | Exfiltration | M2 | `SRC-THREAT-HUNTER-V3` |
| [APT39](../actors/apt39.md) | [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M2 | `SRC-MITRE-G0087` |
| [APT39](../actors/apt39.md) | [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G0087` |
| [Lyceum](../actors/lyceum.md) | [T1071.004](../navigation/ttp-detection-matrix.md#t1071004) DNS | Command and Control | M2 | `SRC-MITRE-G1001` |
| [Lyceum](../actors/lyceum.md) | [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G1001` |
| [Agrius](../actors/agrius.md) | [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-MITRE-G1030` |
| [Agrius](../actors/agrius.md) | [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact | Impact | M2 | `SRC-MITRE-G1030` |
| [Void Manticore / Handala](../actors/handala.md) | [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-AP-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1204](../navigation/ttp-detection-matrix.md#t1204) User Execution | Execution | M2 | `SRC-AP-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-AP-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1490](../navigation/ttp-detection-matrix.md#t1490) Inhibit System Recovery | Impact | M2 | `SRC-AP-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1567](../navigation/ttp-detection-matrix.md#t1567) Exfiltration Over Web Service | Exfiltration | M2 | `SRC-AP-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1078.004](../navigation/ttp-detection-matrix.md#t1078004) Valid Accounts: Cloud Accounts | Initial Access | M3 | `SRC-PUSH-STRYKER-HANDALA` |
| [Void Manticore / Handala](../actors/handala.md) | [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-PUSH-STRYKER-HANDALA` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Magic Hound](../actors/apt35.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |
| [MuddyWater](../actors/muddywater.md) | DET-002 - Suspicious RMM Installer Download From User Context | Pilot | 6 | [detections/sigma/suspicious-rmm-file-sharing-download.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) |
| [MuddyWater](../actors/muddywater.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |
| [Agrius](../actors/agrius.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Magic Hound](../actors/apt35.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |
| [MuddyWater](../actors/muddywater.md) | HUNT-002 | If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths | [detections/kql/suspicious-rmm-file-sharing-download.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) |
| [MuddyWater](../actors/muddywater.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |
| [Agrius](../actors/agrius.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G0049`](https://attack.mitre.org/groups/G0049/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G0059`](https://attack.mitre.org/groups/G0059/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G0069`](https://attack.mitre.org/groups/G0069/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G0087`](https://attack.mitre.org/groups/G0087/) | MITRE ATT&CK | 2026-05-14 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G1001`](https://attack.mitre.org/groups/G1001/) | MITRE ATT&CK | 2026-05-14 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G1030`](https://attack.mitre.org/groups/G1030/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G1055`](https://attack.mitre.org/groups/G1055/) | MITRE ATT&CK | 2026-05-12 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
