---
title: Liontail
sidebar_label: Liontail
---

# Liontail

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Scarred Manticore](../actors/scarred-manticore.md)
- Tool type: Passive backdoor framework
- Confidence: High
- Source: [`SRC-CP-SCARRED-MANTICORE-2023`](https://research.checkpoint.com/2023/scarred-manticore-versus-mois-seeing-the-invisible/)
- Source title: Check Point Research, Scarred Manticore versus MOIS: Seeing the Invisible, 2023-10-31

## Behavior

Scarred Manticore passive HTTP.sys / IIS-adjacent backdoor framework used for stealthy server-side access.

## Hash And IOC Status

- Status: Hash not committed; use Check Point source report references.
- Reference: `SRC-CP-SCARRED-MANTICORE-2023`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt IIS/native-module integrity, HTTP.sys listener anomalies, and suspicious server DLL/service changes.

## Handling Notes

Do not store samples.

## Crosslinks

- Actor profile: [Scarred Manticore](../actors/scarred-manticore.md)
- Actor workbench: [Scarred Manticore](../navigation/actor-workbench.md#scarred-manticore)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#scarred-manticore)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-CP-VOID-2024` |
| [T1505.004](../navigation/ttp-detection-matrix.md#t1505004) IIS Components | Persistence | M2 | `SRC-CP-VOID-2024` |
| [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-CP-VOID-2024` |
| [T1071.001](../navigation/ttp-detection-matrix.md#t1071001) Web Protocols | Command and Control | M2 | `SRC-CP-VOID-2024` |
| [T1199](../navigation/ttp-detection-matrix.md#t1199) Trusted Relationship | Initial Access | M2 | `SRC-CP-VOID-2024` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

- Source ID: `SRC-CP-SCARRED-MANTICORE-2023`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
