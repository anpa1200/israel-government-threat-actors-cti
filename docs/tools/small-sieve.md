---
title: Small Sieve
sidebar_label: Small Sieve
---

# Small Sieve

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [MuddyWater](../actors/muddywater.md)
- Tool type(s): MITRE-listed software/tool
- Confidence level(s): Medium
- Source ID(s): `SRC-MITRE-G0069`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [MuddyWater](../actors/muddywater.md) | MITRE ATT&CK lists Small Sieve as software used by this actor; track it as source-backed software use by the actor. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [MuddyWater](../actors/muddywater.md) | Hash not committed; use the linked MITRE references and original source reports for current IOCs. | `SRC-MITRE-G0069` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [MuddyWater](../actors/muddywater.md) | Hunt for Small Sieve execution or artifacts only in context: unusual parent process, unexpected host role, suspicious account, external staging, or proximity to the actor intrusion chain. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [MuddyWater](../actors/muddywater.md) | Common or dual-use tools require local allowlisting and must not be used alone for actor attribution. |

## Crosslinks

- MuddyWater: [profile](../actors/muddywater.md), [workbench](../navigation/actor-workbench.md#muddywater), [tool matrix](../malware-tool-intelligence.md#muddywater)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [MuddyWater](../actors/muddywater.md) | [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1059.001](../navigation/ttp-detection-matrix.md#t1059001) PowerShell | Execution | M2 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software | Command and Control | M3 | `SRC-MITRE-G0069` |
| [MuddyWater](../actors/muddywater.md) | [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage | Exfiltration | M2 | `SRC-THREAT-HUNTER-V3` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [MuddyWater](../actors/muddywater.md) | DET-002 - Suspicious RMM Installer Download From User Context | Pilot | 6 | [detections/sigma/suspicious-rmm-file-sharing-download.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) |
| [MuddyWater](../actors/muddywater.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [MuddyWater](../actors/muddywater.md) | HUNT-002 | If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths | [detections/kql/suspicious-rmm-file-sharing-download.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) |
| [MuddyWater](../actors/muddywater.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MITRE-G0069`](https://attack.mitre.org/groups/G0069/) | MITRE ATT&CK | 2026-05-13 | A | Knowledge base | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
