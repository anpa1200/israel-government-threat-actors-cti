---
title: OilBooster
sidebar_label: OilBooster
---

# OilBooster

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [OilRig](../actors/oilrig.md)
- Tool type(s): Downloader
- Confidence level(s): High
- Source ID(s): `SRC-ESET-OILRIG-ISRAEL`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [OilRig](../actors/oilrig.md) | ESET reports OilBooster as an OilRig downloader deployed against Israeli organizations; it uses attacker-controlled Microsoft cloud service accounts and APIs for C2 and data exchange rather than victim internal mail infrastructure. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [OilRig](../actors/oilrig.md) | Primary source confirms tool behavior; imported SHA1 seed 1B2FEDD5F2A37A0152231AE4099A13C8D4B73C9E returned VT not_found and remains unpromoted pending primary hash verification. | `SRC-ESET-OILRIG-ISRAEL` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | Hunt Microsoft Graph, OneDrive, Outlook, Exchange Online, or EWS API use by non-standard processes, especially on healthcare, local-government, or manufacturing hosts with prior OilRig exposure. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | Prefer cloud-API behavior over hash-only detection; do not block on unverified research-intake hashes. |

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
