---
title: Impacket
sidebar_label: Impacket
---

# Impacket

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Magic Hound](../actors/apt35.md); [Void Manticore / Handala](../actors/handala.md)
- Tool type(s): Python network protocol toolkit
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G0059`, `SRC-MITRE-G1055`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Magic Hound](../actors/apt35.md) | MITRE ATT&CK lists Impacket as software used by this actor; track it as SMB, credential, and lateral movement behavior. |
| [Void Manticore / Handala](../actors/handala.md) | MITRE ATT&CK lists Impacket as software used by this actor; track it as SMB, credential, and lateral movement behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Magic Hound](../actors/apt35.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0059` |
| [Void Manticore / Handala](../actors/handala.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G1055` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Magic Hound](../actors/apt35.md) | Hunt for Impacket execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |
| [Void Manticore / Handala](../actors/handala.md) | Hunt for Impacket execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Magic Hound](../actors/apt35.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |
| [Void Manticore / Handala](../actors/handala.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- Magic Hound: [profile](../actors/apt35.md), [workbench](../navigation/actor-workbench.md#magic-hound), [tool matrix](../malware-tool-intelligence.md#magic-hound)
- Void Manticore / Handala: [profile](../actors/handala.md), [workbench](../navigation/actor-workbench.md#void-manticore-handala), [tool matrix](../malware-tool-intelligence.md#void-manticore-handala)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Magic Hound](../actors/apt35.md) | [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link | Initial Access | M2 | `SRC-MITRE-G0059` |
| [Magic Hound](../actors/apt35.md) | [T1583.001](../navigation/ttp-detection-matrix.md#t1583001) Acquire Domains | Resource Development | M1 | `SRC-MITRE-G0059` |
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
| [Void Manticore / Handala](../actors/handala.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Magic Hound](../actors/apt35.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G0059`](https://attack.mitre.org/groups/G0059/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |
| [`SRC-MITRE-G1055`](https://attack.mitre.org/groups/G1055/) | MITRE ATT&CK | 2026-05-12 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
