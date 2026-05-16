---
title: Fooder / MuddyViper
sidebar_label: Fooder / MuddyViper
---

# Fooder / MuddyViper

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [MuddyWater](../actors/muddywater.md)
- Tool type: Loader and backdoor
- Confidence: Medium
- Source: [`SRC-ESET-MUDDYWATER-SNAKES`](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- Source title: ESET Research, MuddyWater: Snakes by the riverbank, 2025-12-02

## Behavior

MuddyWater loader/backdoor pair from ESET research intake focused on Israeli and regional critical-infrastructure targeting.

## Hash And IOC Status

- Status: Hash not committed; validate current ESET IOC availability before operational use.
- Reference: `SRC-ESET-MUDDYWATER-SNAKES`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt phishing delivery, in-memory loader behavior, RMM pairing, and unusual cloud-service C2.

## Handling Notes

Research intake remains source-gated before production detections.

## Crosslinks

- Actor profile: [MuddyWater](../actors/muddywater.md)
- Actor workbench: [MuddyWater](../navigation/actor-workbench.md#muddywater)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#muddywater)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing | Initial Access | M2 | `SRC-MITRE-G0069` |
| [T1059.001](../navigation/ttp-detection-matrix.md#t1059001) PowerShell | Execution | M2 | `SRC-MITRE-G0069` |
| [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software | Command and Control | M3 | `SRC-MITRE-G0069` |
| [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage | Exfiltration | M2 | `SRC-THREAT-HUNTER-V3` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-002 - Suspicious RMM Installer Download From User Context | Pilot | 6 | [detections/sigma/suspicious-rmm-file-sharing-download.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) |
| DET-004 - Mail Click To Execution Correlation | Hunt | 4 | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-002 | If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths | [detections/kql/suspicious-rmm-file-sharing-download.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) |
| HUNT-004 | If VIP phishing is active then mail click events will correlate to risky sign-in or execution | [detections/kql/mail-click-to-exec-correlation.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) |

## Source Review

- Source ID: `SRC-ESET-MUDDYWATER-SNAKES`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
