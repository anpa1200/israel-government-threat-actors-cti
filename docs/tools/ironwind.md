---
title: IronWind
sidebar_label: IronWind
---

# IronWind

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [TA402](../actors/ta402.md)
- Tool type: Initial access downloader / staged malware
- Confidence: High
- Source: [`SRC-PROOFPOINT-TA402-IRONWIND`](https://www.proofpoint.com/us/blog/threat-insight/ta402-uses-complex-ironwind-infection-chains-target-middle-east-based-government)
- Source title: Proofpoint, TA402 Targets Middle East Entities with IronWind Malware, 2023-11-14

## Behavior

TA402 downloader and infection chain used against Middle East government entities.

## Hash And IOC Status

- Status: Hash not committed; use Proofpoint IOC appendix/current report.
- Reference: `SRC-PROOFPOINT-TA402-IRONWIND`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt PPAM, XLL, RAR, DLL side-loading, and actor-controlled C2 pivots.

## Handling Notes

Use behavior for defensive hunting.

## Crosslinks

- Actor profile: [TA402](../actors/ta402.md)
- Actor workbench: [TA402](../navigation/actor-workbench.md#ta402)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#ta402)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M3 | `SRC-PROOFPOINT-TA402-IRONWIND` |
| [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking | Defense Evasion | M3 | `SRC-PROOFPOINT-TA402-IRONWIND` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-PROOFPOINT-TA402-IRONWIND`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
