---
title: Saitama
sidebar_label: Saitama
---

# Saitama

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [OilRig](../actors/oilrig.md)
- Tool type(s): DNS-tunneling backdoor
- Confidence level(s): High
- Source ID(s): `SRC-UNIT42-OILRIG-DNS-TUNNELING`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [OilRig](../actors/oilrig.md) | OilRig/APT34 DNS tunneling family that encodes command-and-control over DNS queries. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [OilRig](../actors/oilrig.md) | Hash not committed; use Unit 42 IOC references if needed. | `SRC-UNIT42-OILRIG-DNS-TUNNELING` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | Hunt high-entropy subdomains, long query names, and high-frequency single-domain DNS from one host. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [OilRig](../actors/oilrig.md) | DNS patterns require local baseline tuning. |

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
| [`SRC-UNIT42-OILRIG-DNS-TUNNELING`](https://unit42.paloaltonetworks.com/dns-tunneling-in-the-wild-overview-of-oilrigs-dns-tunneling/) | Unit 42 | 2022-03-15 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
