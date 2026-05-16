---
title: WezRat
sidebar_label: WezRat
---

# WezRat

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Cotton Sandstorm](../actors/cotton-sandstorm.md)
- Tool type: Modular infostealer / RAT
- Confidence: High
- Source: [`SRC-CP-WEZRAT`](https://research.checkpoint.com/2024/wezrat-malware-deep-dive/)
- Source title: Check Point Research, Malware Spotlight: A Deep-Dive Analysis of WezRat, 2024-11-14

## Behavior

Modular infostealer attributed to Emennet Pasargad and distributed in fake INCD phishing against Israeli organizations.

## Hash And IOC Status

- Status: Hash not committed; use Check Point and government IOC references.
- Reference: `SRC-CP-WEZRAT`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt fake security updates, user-path execution, and modular infostealer C2.

## Handling Notes

Do not store payloads.

## Crosslinks

- Actor profile: [Cotton Sandstorm](../actors/cotton-sandstorm.md)
- Actor workbench: [Cotton Sandstorm](../navigation/actor-workbench.md#cotton-sandstorm)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#cotton-sandstorm)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1585](../navigation/ttp-detection-matrix.md#t1585) Establish Accounts | Resource Development | M1 | `SRC-MS-IRAN-IO` |
| [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File | Execution | M3 | `SRC-CP-WEZRAT` |
| [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M3 | `SRC-FBI-EMENNET-2024` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

- Source ID: `SRC-CP-WEZRAT`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
