---
title: SameCoin
sidebar_label: SameCoin
---

# SameCoin

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [WIRTE](../actors/wirte.md)
- Tool type: Wiper
- Confidence: High
- Source: [`SRC-CP-WIRTE-2024`](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- Source title: Check Point Research, Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity, 2024-11-12

## Behavior

WIRTE-linked wiper used in disruptive activity against Israeli entities according to Check Point reporting.

## Hash And IOC Status

- Status: Hash not committed; use Check Point report references.
- Reference: `SRC-CP-WIRTE-2024`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt destructive file operations, suspicious desktop modification, and post-compromise wiper staging.

## Handling Notes

Do not store samples.

## Crosslinks

- Actor profile: [WIRTE](../actors/wirte.md)
- Actor workbench: [WIRTE](../navigation/actor-workbench.md#wirte)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#wirte)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-CP-WIRTE-2024` |
| [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking | Defense Evasion | M3 | `SRC-CP-WIRTE-2024` |
| [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-CP-WIRTE-2024` |
| [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer | Command and Control | M3 | `SRC-UNIT42-ASHTAG-2025` |
| [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage | Exfiltration | M3 | `SRC-UNIT42-ASHTAG-2025` |

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

- Source ID: `SRC-CP-WIRTE-2024`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
