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
| [APT-C-23](../actors/arid-viper.md) | ESET reports AridSpy as a multi-stage Android spyware family distributed through trojanized apps; behavior includes payload download/decryption, Firebase C2, HTTPS exfiltration, camera capture, audio recording, location tracking, SMS/contact/call-log collection, accessibility abuse, and WhatsApp/Facebook Messenger collection. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Representative ESET-published SHA1s include 797073511A15EB85C1E9D8584B26BAA3A0B14C9E, 5F0213BA62B84221C9628F7D0A0CF87F27A45A28, E71F1484B1E3ACB4C8E8525BA1F5F8822AB7238B, and 16C8725362D1EBC8443C97C5AB79A1B6428FF87D; use full ESET IOC table for current coverage. | `SRC-ESET-ARIDSPY` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hunt sideloaded APKs from dedicated lure sites, unknown-source installs, Google Play Services impersonation, Firebase C2, suspicious accessibility-service grants, data.zip staging, and mobile apps requesting SMS/contact/location/audio/camera permissions together. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Use for MDM policy and mobile defense mapping; avoid storing APKs or private mobile telemetry. |

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
