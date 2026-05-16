---
title: Saitama
sidebar_label: Saitama
---

# Saitama

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [OilRig](../actors/oilrig.md)
- Tool type: DNS-tunneling backdoor
- Confidence: High
- Source: [`SRC-UNIT42-OILRIG-DNS-TUNNELING`](https://unit42.paloaltonetworks.com/dns-tunneling-in-the-wild-overview-of-oilrigs-dns-tunneling/)
- Source title: Unit 42, DNS Tunneling in the Wild: Overview of OilRig's DNS Tunneling, 2022-03-15

## Behavior

OilRig/APT34 DNS tunneling family that encodes command-and-control over DNS queries.

## Hash And IOC Status

- Status: Hash not committed; use Unit 42 IOC references if needed.
- Reference: `SRC-UNIT42-OILRIG-DNS-TUNNELING`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt high-entropy subdomains, long query names, and high-frequency single-domain DNS from one host.

## Handling Notes

DNS patterns require local baseline tuning.

## Crosslinks

- Actor profile: [OilRig](../actors/oilrig.md)
- Actor workbench: [OilRig](../navigation/actor-workbench.md#oilrig)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#oilrig)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M3 | `SRC-MITRE-G0049` |
| [T1049](../navigation/ttp-detection-matrix.md#t1049) System Network Connections Discovery | Discovery | M1 | `SRC-MITRE-G0049` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-UNIT42-OILRIG-DNS-TUNNELING`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
