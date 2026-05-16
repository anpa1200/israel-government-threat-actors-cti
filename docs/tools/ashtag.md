---
title: AshTag
sidebar_label: AshTag
---

# AshTag

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [WIRTE](../actors/wirte.md)
- Tool type(s): Modular .NET malware suite
- Confidence level(s): High
- Source ID(s): `SRC-UNIT42-ASHTAG-2025`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [WIRTE](../actors/wirte.md) | Unit 42 reports AshTag as a WIRTE/Ashen Lepus modular .NET malware suite with AshenLoader, AshenStager, AshenOrchestrator, and modules; behavior includes DLL side-loading, HTML tag payload retrieval, AES/XOR-protected staging, modular collection, and Rclone exfiltration. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [WIRTE](../actors/wirte.md) | Representative Unit 42 SHA256s include f554c43707f5d87625a3834116a2d22f551b1d9a5aff1e446d24893975c431bc, 739a5199add1d970ba22d69cc10b4c3a13b72136be6d45212429e8f0969af3dc, 6bd3d05aef89cd03d6b49b20716775fe92f0cf8a3c2747094404ef98f96e9376, 30490ba95c42cefcca1d0328ea740e61c26eaf606a98f68d26c4a519ce918c99, and 66ab29d2d62548faeaeadaad9dd62818163175872703fda328bb1b4894f5e69e; use full Unit 42 IOC table for coverage. | `SRC-UNIT42-ASHTAG-2025` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [WIRTE](../actors/wirte.md) | Hunt DLL side-loading of dwampi.dll, wtsapi32.dll, srvcli.dll, or netutils.dll from unexpected paths, HTML-staged payload retrieval, AES/XOR decoding artifacts, modular C2, and Rclone execution after collection. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [WIRTE](../actors/wirte.md) | No samples; source-linked behavior only. |

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
| [`SRC-UNIT42-ASHTAG-2025`](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/) | Unit 42 | 2025-12-11 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
