---
title: BiBi / BiBi Wiper lineage
sidebar_label: BiBi / BiBi Wiper lineage
---

# BiBi / BiBi Wiper lineage

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Void Manticore / Handala](../actors/handala.md)
- Tool type(s): Wiper / destructive malware lineage
- Confidence level(s): Medium
- Source ID(s): `SRC-AP-HANDALA`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Void Manticore / Handala](../actors/handala.md) | Handala/Void Manticore-related reporting discusses destructive wiper activity and BiBi-style lineage context. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Void Manticore / Handala](../actors/handala.md) | Hash not committed; use primary wiper reports for active IOCs. | `SRC-AP-HANDALA` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Void Manticore / Handala](../actors/handala.md) | Hunt extension renaming, destructive writes, VSS deletion, backup tampering, and ransom-note decoy behavior. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Void Manticore / Handala](../actors/handala.md) | Do not store samples. |

## Crosslinks

- Void Manticore / Handala: [profile](../actors/handala.md), [workbench](../navigation/actor-workbench.md#void-manticore-handala), [tool matrix](../malware-tool-intelligence.md#void-manticore-handala)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
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
| [Void Manticore / Handala](../actors/handala.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [Void Manticore / Handala](../actors/handala.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-AP-HANDALA`](https://medium.com/@1200km/cti-research-handala-hack-group-aka-handala-hack-team-ddbdd294cfb8) | Andrey Pautov | 2026-03-06 | B | Author CTI assessment | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
