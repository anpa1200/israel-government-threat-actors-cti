---
title: SUGARUSH / SUGARDUMP
sidebar_label: SUGARUSH / SUGARDUMP
---

# SUGARUSH / SUGARDUMP

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [UNC3890](../actors/unc3890.md)
- Tool type: Information stealer
- Confidence: Medium
- Source: [`SRC-MANDIANT-UNC3890`](https://cloud.google.com/blog/topics/threat-intelligence/suspected-iranian-actor-targeting-israeli-shipping)
- Source title: Google Cloud / Mandiant, UNC3890: Suspected Iranian Threat Actor Targeting Israeli Shipping Healthcare Government and Energy Sectors, 2022-07-27

## Behavior

UNC3890-linked tools reported for Israeli shipping, logistics, and adjacent sector data collection.

## Hash And IOC Status

- Status: Hash not committed; use Mandiant source references.
- Reference: `SRC-MANDIANT-UNC3890`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt credential and browser-data collection from maritime/logistics environments.

## Handling Notes

Use source-linked IOCs only.

## Crosslinks

- Actor profile: [UNC3890](../actors/unc3890.md)
- Actor workbench: [UNC3890](../navigation/actor-workbench.md#unc3890)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#unc3890)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise | Initial Access | M2 | `SRC-SECWEEK-UNC3890` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-MANDIANT-UNC3890`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
