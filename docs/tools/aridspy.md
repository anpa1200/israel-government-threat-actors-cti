---
title: AridSpy
sidebar_label: AridSpy
---

# AridSpy

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [APT-C-23](../actors/arid-viper.md)
- Tool type: Mobile RAT
- Confidence: High
- Source: [`SRC-ESET-ARIDSPY`](https://www.welivesecurity.com/en/eset-research/arid-viper-poisons-android-apps-with-aridspy/)
- Source title: ESET Research, Arid Viper poisons Android apps with AridSpy, 2024-06-13

## Behavior

Android spyware framework used by Arid Viper for call log, message, location, and audio collection.

## Hash And IOC Status

- Status: Hash not committed; use ESET mobile IOC appendix/current report.
- Reference: `SRC-ESET-ARIDSPY`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt sideloaded APKs, unknown-source installs, abusive permissions, and suspicious mobile C2.

## Handling Notes

Use for MDM policy and mobile defense mapping.

## Crosslinks

- Actor profile: [APT-C-23](../actors/arid-viper.md)
- Actor workbench: [APT-C-23](../navigation/actor-workbench.md#apt-c-23)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#apt-c-23)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1660](../navigation/ttp-detection-matrix.md#t1660) Phishing | Initial Access (Mobile) | M2 | `SRC-ESET-ARIDSPY` |
| [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File | Execution | M3 | `SRC-ESET-ARIDSPY` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-ESET-ARIDSPY`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
