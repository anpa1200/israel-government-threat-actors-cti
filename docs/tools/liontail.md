---
title: Liontail
sidebar_label: Liontail
---

# Liontail

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Scarred Manticore](../actors/scarred-manticore.md)
- Tool type(s): Passive backdoor framework
- Confidence level(s): High
- Source ID(s): `SRC-CP-SCARRED-MANTICORE-2023`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | Check Point reports Liontail as Scarred Manticore passive server-side tooling using IIS/native-module or HTTP.sys-adjacent access patterns for stealthy inbound-controlled access rather than standard webshell request/response behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | Hash not committed; use Check Point source report references and local IIS module baselines. | `SRC-CP-SCARRED-MANTICORE-2023` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | Hunt IIS/native-module integrity changes, appcmd module registration, unexpected DLLs in IIS paths, HTTP.sys listener anomalies, worker-process child processes, and suspicious server DLL/service changes. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | Do not conflate generic phantom-DLL hijacking with Liontail unless source-backed. |

## Crosslinks

- Scarred Manticore: [profile](../actors/scarred-manticore.md), [workbench](../navigation/actor-workbench.md#scarred-manticore), [tool matrix](../malware-tool-intelligence.md#scarred-manticore)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-CP-VOID-2024` |
| [Scarred Manticore](../actors/scarred-manticore.md) | [T1505.004](../navigation/ttp-detection-matrix.md#t1505004) IIS Components | Persistence | M2 | `SRC-CP-VOID-2024` |
| [Scarred Manticore](../actors/scarred-manticore.md) | [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-CP-VOID-2024` |
| [Scarred Manticore](../actors/scarred-manticore.md) | [T1071.001](../navigation/ttp-detection-matrix.md#t1071001) Web Protocols | Command and Control | M2 | `SRC-CP-VOID-2024` |
| [Scarred Manticore](../actors/scarred-manticore.md) | [T1199](../navigation/ttp-detection-matrix.md#t1199) Trusted Relationship | Initial Access | M2 | `SRC-CP-VOID-2024` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Scarred Manticore](../actors/scarred-manticore.md) | HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CP-SCARRED-MANTICORE-2023`](https://research.checkpoint.com/2023/scarred-manticore-versus-mois-seeing-the-invisible/) | Check Point Research | 2023-10-31 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
