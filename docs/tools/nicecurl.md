---
title: NICECURL
sidebar_label: NICECURL
---

# NICECURL

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [APT42](../actors/apt42.md)
- Tool type: Backdoor / C2 tool
- Confidence: Medium
- Source: [`SRC-MITRE-G1044`](https://attack.mitre.org/groups/G1044/)
- Source title: MITRE ATT&CK, APT42 G1044, 2026-05-13

## Behavior

APT42-linked backdoor family used for command-and-control and post-compromise operations.

## Hash And IOC Status

- Status: Hash not committed; retrieve current IOCs from linked source or vendor appendix.
- Reference: `SRC-MITRE-G1044`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt uncommon HTTPS egress from user-path executables after credential phishing or social-engineering lures.

## Handling Notes

Track behavior and source references only.

## Crosslinks

- Actor profile: [APT42](../actors/apt42.md)
- Actor workbench: [APT42](../navigation/actor-workbench.md#apt42)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#apt42)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1530](../navigation/ttp-detection-matrix.md#t1530) Data from Cloud Storage | Collection | M1 | `SRC-MITRE-G1044` |
| [T1102](../navigation/ttp-detection-matrix.md#t1102) Web Service | Command and Control | M1 | `SRC-MITRE-G1044` |
| [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link | Initial Access | M3 | `SRC-GOOGLE-APT42-PHISHING` |

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

- Source ID: `SRC-MITRE-G1044`
- Reliability in source register: A
- Source type: Knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
