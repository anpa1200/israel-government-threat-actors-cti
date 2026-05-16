---
title: ODAgent
sidebar_label: ODAgent
---

# ODAgent

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [OilRig](../actors/oilrig.md)
- Tool type(s): MITRE-listed software/tool
- Confidence level(s): High
- Source ID(s): `SRC-ESET-OILRIG-ISRAEL`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [OilRig](../actors/oilrig.md) | ESET reports ODAgent in the network of an Israeli manufacturing company; it is part of the OilRig cloud-service-powered downloader set used to maintain access. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [OilRig](../actors/oilrig.md) | Imported SHA1 seed 7E498B3366F54E936CB0AF767BFC3D1F92D80687 returned VT not_found and remains unpromoted pending primary hash verification. | `SRC-ESET-OILRIG-ISRAEL` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | Hunt downloader execution on manufacturing, healthcare, or local-government hosts followed by Microsoft cloud API traffic and file staging. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | Use source-backed behavior for hunts; hash seed is not production-ready until primary hash source is confirmed. |

## Crosslinks

- OilRig: [profile](../actors/oilrig.md), [workbench](../navigation/actor-workbench.md#oilrig), [tool matrix](../malware-tool-intelligence.md#oilrig)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [OilRig](../actors/oilrig.md) | [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M3 | `SRC-MITRE-G0049` |
| [OilRig](../actors/oilrig.md) | [T1049](../navigation/ttp-detection-matrix.md#t1049) System Network Connections Discovery | Discovery | M1 | `SRC-MITRE-G0049` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-ESET-OILRIG-ISRAEL`](https://www.eset.com/sg/about/newsroom/press-releases1/awards/iran-linked-oilrig-attacks-israeli-organizations-with-cloud-service-powered-downloaders-eset-research-discovers/) | ESET Research | 2023-09-21 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
