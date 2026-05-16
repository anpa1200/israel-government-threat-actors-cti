---
title: SUGARUSH / SUGARDUMP
sidebar_label: SUGARUSH / SUGARDUMP
---

# SUGARUSH / SUGARDUMP

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [UNC3890](../actors/unc3890.md)
- Tool type(s): Information stealer
- Confidence level(s): Medium
- Source ID(s): `SRC-MANDIANT-UNC3890`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [UNC3890](../actors/unc3890.md) | UNC3890-linked tools reported for Israeli shipping, logistics, and adjacent sector data collection. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [UNC3890](../actors/unc3890.md) | Hash not committed; use Mandiant source references. | `SRC-MANDIANT-UNC3890` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [UNC3890](../actors/unc3890.md) | Hunt credential and browser-data collection from maritime/logistics environments. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [UNC3890](../actors/unc3890.md) | Use source-linked IOCs only. |

## Crosslinks

- UNC3890: [profile](../actors/unc3890.md), [workbench](../navigation/actor-workbench.md#unc3890), [tool matrix](../malware-tool-intelligence.md#unc3890)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [UNC3890](../actors/unc3890.md) | [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise | Initial Access | M2 | `SRC-SECWEEK-UNC3890` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-MANDIANT-UNC3890`](https://cloud.google.com/blog/topics/threat-intelligence/suspected-iranian-actor-targeting-israeli-shipping) | Google Cloud / Mandiant | 2022-07-27 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
