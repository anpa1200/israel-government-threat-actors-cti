---
title: TEMPLEPLAY
sidebar_label: TEMPLEPLAY
---

# TEMPLEPLAY

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [UNC1860](../actors/unc1860.md)
- Tool type(s): GUI malware controller
- Confidence level(s): High
- Source ID(s): `SRC-MANDIANT-UNC1860`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [UNC1860](../actors/unc1860.md) | Mandiant reports TEMPLEPLAY as a .NET controller for TEMPLEDOOR with tabs for command execution, upload, download, HTTP proxying, URL endpoint selection, and backdoor testing. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [UNC1860](../actors/unc1860.md) | Mandiant reports MD5 c517519097bff386dc1784d98ad93f9d for TEMPLEPLAY; VT enrichment returned not_found on 2026-05-16. | `SRC-MANDIANT-UNC1860` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [UNC1860](../actors/unc1860.md) | Hunt operator tooling on admin workstations, rare .NET GUI execution, and outbound requests matching known TEMPLEDOOR endpoint behavior. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [UNC1860](../actors/unc1860.md) | Do not run or store controller samples; absence in VT does not reduce confidence in Mandiant-published hash. |

## Crosslinks

- UNC1860: [profile](../actors/unc1860.md), [workbench](../navigation/actor-workbench.md#unc1860), [tool matrix](../malware-tool-intelligence.md#unc1860)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [UNC1860](../actors/unc1860.md) | [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-MANDIANT-UNC1860` |
| [UNC1860](../actors/unc1860.md) | [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-MANDIANT-UNC1860` |
| [UNC1860](../actors/unc1860.md) | [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer | Command and Control | M2 | `SRC-MANDIANT-UNC1860` |
| [UNC1860](../actors/unc1860.md) | [T1021.001](../navigation/ttp-detection-matrix.md#t1021001) Remote Services: RDP | Lateral Movement | M2 | `SRC-MANDIANT-UNC1860` |
| [UNC1860](../actors/unc1860.md) | [T1078](../navigation/ttp-detection-matrix.md#t1078) Valid Accounts | Defense Evasion | M2 | `SRC-MANDIANT-UNC1860` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [UNC1860](../actors/unc1860.md) | DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [UNC1860](../actors/unc1860.md) | HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MANDIANT-UNC1860`](https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks) | Google Cloud / Mandiant | 2024-09-19 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
