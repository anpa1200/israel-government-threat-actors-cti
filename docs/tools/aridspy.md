---
title: AridSpy
sidebar_label: AridSpy
---

# AridSpy

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [APT-C-23](../actors/arid-viper.md)
- Tool type(s): Mobile RAT
- Confidence level(s): High
- Source ID(s): `SRC-ESET-ARIDSPY`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Android spyware framework used by Arid Viper for call log, message, location, and audio collection. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hash not committed; use ESET mobile IOC appendix/current report. | `SRC-ESET-ARIDSPY` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hunt sideloaded APKs, unknown-source installs, abusive permissions, and suspicious mobile C2. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Use for MDM policy and mobile defense mapping. |

## Crosslinks

- APT-C-23: [profile](../actors/arid-viper.md), [workbench](../navigation/actor-workbench.md#apt-c-23), [tool matrix](../malware-tool-intelligence.md#apt-c-23)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | [T1660](../navigation/ttp-detection-matrix.md#t1660) Phishing | Initial Access (Mobile) | M2 | `SRC-ESET-ARIDSPY` |
| [APT-C-23](../actors/arid-viper.md) | [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File | Execution | M3 | `SRC-ESET-ARIDSPY` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-ESET-ARIDSPY`](https://www.welivesecurity.com/en/eset-research/arid-viper-poisons-android-apps-with-aridspy/) | ESET Research | 2024-06-13 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
