---
title: IronWind
sidebar_label: IronWind
---

# IronWind

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [TA402](../actors/ta402.md)
- Tool type(s): Initial access downloader / staged malware
- Confidence level(s): High
- Source ID(s): `SRC-PROOFPOINT-TA402-IRONWIND`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [TA402](../actors/ta402.md) | Proofpoint reports IronWind as a TA402 infection chain using PPAM, XLL, RAR, cloud-link and actor-controlled C2 delivery; behavior includes staged downloader execution, geofencing/decoy delivery, and DLL side-loading in later related reporting. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [TA402](../actors/ta402.md) | Proofpoint-published SHA256 indicators include 9b2a16cbe5af12b486d31b68ef397d6bc48b2736e6b388ad8895b588f1831f47, 5d773e734290b93649a41ccda63772560b4fa25ba715b17df7b9f18883679160, 19f452239dadcd7544f055d26199cb482c1f6ae5486309bde1526174e926146a, A4bf96aee6284effb4c4fe0ccfee7b32d497e45408e253fb8e1199454e5c65a3, and 26cb6055be1ee503f87d040c84c0a7cacb245b4182445e3eee47ed6e073eca47; use full Proofpoint IOC list for operational use. | `SRC-PROOFPOINT-TA402-IRONWIND` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [TA402](../actors/ta402.md) | Hunt PPAM/XLL/RAR lure execution, DLL side-loading from user-writable paths, cloud-link retrieval, geofenced decoy behavior, and actor-controlled C2 pivots. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [TA402](../actors/ta402.md) | Use behavior for defensive hunting; keep hashes as historical triage pivots, not standalone attribution. |

## Crosslinks

- TA402: [profile](../actors/ta402.md), [workbench](../navigation/actor-workbench.md#ta402), [tool matrix](../malware-tool-intelligence.md#ta402)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [TA402](../actors/ta402.md) | [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M3 | `SRC-PROOFPOINT-TA402-IRONWIND` |
| [TA402](../actors/ta402.md) | [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking | Defense Evasion | M3 | `SRC-PROOFPOINT-TA402-IRONWIND` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-PROOFPOINT-TA402-IRONWIND`](https://www.proofpoint.com/us/blog/threat-insight/ta402-uses-complex-ironwind-infection-chains-target-middle-east-based-government) | Proofpoint | 2023-11-14 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
