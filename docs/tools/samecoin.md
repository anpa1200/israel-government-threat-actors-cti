---
title: SameCoin
sidebar_label: SameCoin
---

# SameCoin

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [WIRTE](../actors/wirte.md)
- Tool type(s): Wiper
- Confidence level(s): High
- Source ID(s): `SRC-CP-WIRTE-2024`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [WIRTE](../actors/wirte.md) | Check Point reports SameCoin as a WIRTE-linked multi-platform wiper used in disruptive Israeli campaigns; behavior includes INCD/ESET security-update impersonation, oref.org.il reachability/XOR guardrail, Active Directory propagation through scheduled tasks, file overwrite with random bytes, Android zero-fill/delete logic, and propaganda wallpaper/video artifacts. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [WIRTE](../actors/wirte.md) | Check Point publishes lure hash b7c5af2d7e1eb7651b1fe3a224121d3461f3473d081990c02ef8ab4ace13f785; component hashes should be pulled from the primary Check Point/HarfangLab references before blocking. | `SRC-CP-WIRTE-2024` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [WIRTE](../actors/wirte.md) | Hunt non-browser requests to oref.org.il from newly dropped binaries, fake INCD/ESET update execution, mass file overwrite, remote scheduled-task propagation, suspicious desktop changes, and Android security-update APK side-loads. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [WIRTE](../actors/wirte.md) | Do not store samples; treat geofenced behavior as high-value defensive signal for Israeli environments. |

## Crosslinks

- WIRTE: [profile](../actors/wirte.md), [workbench](../navigation/actor-workbench.md#wirte), [tool matrix](../malware-tool-intelligence.md#wirte)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [WIRTE](../actors/wirte.md) | [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-CP-WIRTE-2024` |
| [WIRTE](../actors/wirte.md) | [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking | Defense Evasion | M3 | `SRC-CP-WIRTE-2024` |
| [WIRTE](../actors/wirte.md) | [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-CP-WIRTE-2024` |
| [WIRTE](../actors/wirte.md) | [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer | Command and Control | M3 | `SRC-UNIT42-ASHTAG-2025` |
| [WIRTE](../actors/wirte.md) | [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage | Exfiltration | M3 | `SRC-UNIT42-ASHTAG-2025` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [WIRTE](../actors/wirte.md) | DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [WIRTE](../actors/wirte.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [WIRTE](../actors/wirte.md) | HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |
| [WIRTE](../actors/wirte.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CP-WIRTE-2024`](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/) | Check Point Research | 2024-11-12 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
