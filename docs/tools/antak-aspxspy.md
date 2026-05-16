---
title: ANTAK / ASPXSPY
sidebar_label: ANTAK / ASPXSPY
---

# ANTAK / ASPXSPY

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [APT39](../actors/apt39.md)
- Tool type: Web shells
- Confidence: Medium
- Source: [`SRC-MITRE-G0087`](https://attack.mitre.org/groups/G0087/)
- Source title: MITRE ATT&CK, APT39 G0087, 2026-05-14

## Behavior

MITRE reports APT39 installed ANTAK and ASPXSPY web shells.

## Hash And IOC Status

- Status: Hash not committed; use source-linked IOCs and local webroot baselines.
- Reference: `SRC-MITRE-G0087`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt webroot integrity changes, web server child processes, and suspicious ASPX/JSP server-side files.

## Handling Notes

Do not treat common webshell names as attribution alone.

## Crosslinks

- Actor profile: [APT39](../actors/apt39.md)
- Actor workbench: [APT39](../navigation/actor-workbench.md#apt39)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#apt39)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment | Initial Access | M2 | `SRC-MITRE-G0087` |
| [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G0087` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-MITRE-G0087`
- Reliability in source register: A
- Source type: Knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
