---
title: WezRat
sidebar_label: WezRat
---

# WezRat

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Cotton Sandstorm](../actors/cotton-sandstorm.md)
- Tool type(s): Modular infostealer / RAT
- Confidence level(s): High
- Source ID(s): `SRC-CP-WEZRAT`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Modular infostealer attributed to Emennet Pasargad and distributed in fake INCD phishing against Israeli organizations. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Hash not committed; use Check Point and government IOC references. | `SRC-CP-WEZRAT` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Hunt fake security updates, user-path execution, and modular infostealer C2. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Do not store payloads. |

## Crosslinks

- Cotton Sandstorm: [profile](../actors/cotton-sandstorm.md), [workbench](../navigation/actor-workbench.md#cotton-sandstorm), [tool matrix](../malware-tool-intelligence.md#cotton-sandstorm)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | [T1585](../navigation/ttp-detection-matrix.md#t1585) Establish Accounts | Resource Development | M1 | `SRC-MS-IRAN-IO` |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File | Execution | M3 | `SRC-CP-WEZRAT` |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M3 | `SRC-FBI-EMENNET-2024` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-CP-WEZRAT`](https://research.checkpoint.com/2024/wezrat-malware-deep-dive/) | Check Point Research | 2024-11-14 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
