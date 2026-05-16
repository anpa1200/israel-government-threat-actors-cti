---
title: RedAlert.apk
sidebar_label: RedAlert.apk
---

# RedAlert.apk

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [APT-C-23](../actors/arid-viper.md)
- Tool type(s): Mobile spyware / trojanized app
- Confidence level(s): Low
- Source ID(s): `SRC-CYBERNEWS-REDALERT-2026`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Secondary Cybernews/Acronis coverage describes malicious RedAlert-themed Android application delivery against Israeli users. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hash not committed; provisional until primary Acronis reporting is available. | `SRC-CYBERNEWS-REDALERT-2026` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Hunt smishing delivery, sideloaded alert apps, OTP/SMS access permissions, and spoofed app identities. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [APT-C-23](../actors/arid-viper.md) | Keep provisional and clearly labelled. |

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
| [`SRC-CYBERNEWS-REDALERT-2026`](https://cybernews.com/security/israel-malicious-redalert-app/) | Cybernews / Acronis coverage | 2026-03 | B | News / vendor coverage | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
