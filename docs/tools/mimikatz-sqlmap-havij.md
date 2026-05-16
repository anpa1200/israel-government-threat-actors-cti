---
title: Mimikatz / SQLMap / Havij
sidebar_label: Mimikatz / SQLMap / Havij
---

# Mimikatz / SQLMap / Havij

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Magic Hound](../actors/apt35.md)
- Tool type: Public offensive/security tooling
- Confidence: Medium
- Source: [`SRC-MITRE-G0059`](https://attack.mitre.org/groups/G0059/)
- Source title: MITRE ATT&CK, Magic Hound / APT35 G0059, 2026-05-13

## Behavior

MITRE reports Magic Hound use of public tools including Mimikatz, sqlmap, Havij, Metasploit, and Plink.

## Hash And IOC Status

- Status: No stable actor-specific hash; use process, command-line, and control-plane telemetry.
- Reference: `SRC-MITRE-G0059`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt credential dumping, SQL injection tooling on admin hosts, and public tool execution after phishing or edge compromise.

## Handling Notes

Do not infer actor identity from common public tools.

## Crosslinks

- Actor profile: [Magic Hound](../actors/apt35.md)
- Actor workbench: [Magic Hound](../navigation/actor-workbench.md#magic-hound)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#magic-hound)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link | Initial Access | M2 | `SRC-MITRE-G0059` |
| [T1583.001](../navigation/ttp-detection-matrix.md#t1583001) Acquire Domains | Resource Development | M1 | `SRC-MITRE-G0059` |

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

- Source ID: `SRC-MITRE-G0059`
- Reliability in source register: A
- Source type: Knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
