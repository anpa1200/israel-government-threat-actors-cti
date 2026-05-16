---
title: Kevin
sidebar_label: Kevin
---

# Kevin

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Lyceum](../actors/lyceum.md)
- Tool type: Backdoor
- Confidence: Low
- Source: [`SRC-MITRE-G1001`](https://attack.mitre.org/groups/G1001/)
- Source title: MITRE ATT&CK, HEXANE G1001, 2026-05-14

## Behavior

Lyceum-associated backdoor line referenced by public reporting.

## Hash And IOC Status

- Status: Hash not committed; use MITRE references and primary reports.
- Reference: `SRC-MITRE-G1001`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Use as enrichment term for Lyceum hunting until behavior is source-backed locally.

## Handling Notes

Do not create hash-only production rules.

## Crosslinks

- Actor profile: [Lyceum](../actors/lyceum.md)
- Actor workbench: [Lyceum](../navigation/actor-workbench.md#lyceum)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#lyceum)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1071.004](../navigation/ttp-detection-matrix.md#t1071004) DNS | Command and Control | M2 | `SRC-MITRE-G1001` |
| [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory | Credential Access | M2 | `SRC-MITRE-G1001` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-MITRE-G1001`
- Reliability in source register: A
- Source type: Knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
