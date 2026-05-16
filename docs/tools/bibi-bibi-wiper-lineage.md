---
title: BiBi / BiBi Wiper lineage
sidebar_label: BiBi / BiBi Wiper lineage
---

# BiBi / BiBi Wiper lineage

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Void Manticore / Handala](../actors/handala.md)
- Tool type: Wiper / destructive malware lineage
- Confidence: Medium
- Source: [`SRC-AP-HANDALA`](https://medium.com/@1200km/cti-research-handala-hack-group-aka-handala-hack-team-ddbdd294cfb8)
- Source title: Andrey Pautov, CTI Research: Handala Hack Group aka Handala Hack Team, 2026-03-06

## Behavior

Handala/Void Manticore-related reporting discusses destructive wiper activity and BiBi-style lineage context.

## Hash And IOC Status

- Status: Hash not committed; use primary wiper reports for active IOCs.
- Reference: `SRC-AP-HANDALA`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt extension renaming, destructive writes, VSS deletion, backup tampering, and ransom-note decoy behavior.

## Handling Notes

Do not store samples.

## Crosslinks

- Actor profile: [Void Manticore / Handala](../actors/handala.md)
- Actor workbench: [Void Manticore / Handala](../navigation/actor-workbench.md#void-manticore-handala)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#void-manticore-handala)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-AP-HANDALA` |
| [T1204](../navigation/ttp-detection-matrix.md#t1204) User Execution | Execution | M2 | `SRC-AP-HANDALA` |
| [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-AP-HANDALA` |
| [T1490](../navigation/ttp-detection-matrix.md#t1490) Inhibit System Recovery | Impact | M2 | `SRC-AP-HANDALA` |
| [T1567](../navigation/ttp-detection-matrix.md#t1567) Exfiltration Over Web Service | Exfiltration | M2 | `SRC-AP-HANDALA` |
| [T1078.004](../navigation/ttp-detection-matrix.md#t1078004) Valid Accounts: Cloud Accounts | Initial Access | M3 | `SRC-PUSH-STRYKER-HANDALA` |
| [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-PUSH-STRYKER-HANDALA` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

- Source ID: `SRC-AP-HANDALA`
- Reliability in source register: B
- Source type: Author CTI assessment
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
