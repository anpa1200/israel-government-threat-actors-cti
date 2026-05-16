---
title: BlackShadow
sidebar_label: BlackShadow
---

# BlackShadow

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Agrius](../actors/agrius.md)
- Tool type: Ransomware / persona
- Confidence: Medium
- Source: [`SRC-MITRE-G1030`](https://attack.mitre.org/groups/G1030/)
- Source title: MITRE ATT&CK, Agrius G1030, 2026-05-13

## Behavior

Agrius-linked destructive/extortion persona and malware reference depending on source context.

## Hash And IOC Status

- Status: Hash not committed; persona claims require corroboration.
- Reference: `SRC-MITRE-G1030`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Separate public claims from telemetry; hunt destructive preparation and data theft before leak publication.

## Handling Notes

Treat persona claims through the persona-claims register.

## Crosslinks

- Actor profile: [Agrius](../actors/agrius.md)
- Actor workbench: [Agrius](../navigation/actor-workbench.md#agrius)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#agrius)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction | Impact | M2 | `SRC-MITRE-G1030` |
| [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact | Impact | M2 | `SRC-MITRE-G1030` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-001 - Intune Bulk Device Wipe Anomaly | Hunt | 5 | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-001 | If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs | [detections/kql/intune-bulk-device-wipe-anomaly.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) |

## Source Review

- Source ID: `SRC-MITRE-G1030`
- Reliability in source register: A
- Source type: Knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
