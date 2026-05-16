---
title: CRYPTOSLAY
sidebar_label: CRYPTOSLAY
---

# CRYPTOSLAY

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [UNC1860](../actors/unc1860.md)
- Tool type: Associated family
- Confidence: Medium
- Source: [`SRC-MALPEDIA-UNC1860`](https://malpedia.caad.fkie.fraunhofer.de/actor/unc1860)
- Source title: Malpedia, UNC1860 Threat Actor, 2026-05-14

## Behavior

Malpedia lists win.cryptoslay as an associated UNC1860 family and ties the reference set to Mandiant's UNC1860 reporting.

## Hash And IOC Status

- Status: Family confirmed by Malpedia; no per-sample hash committed in this repo.
- Reference: `SRC-MALPEDIA-UNC1860`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Use as taxonomy enrichment; do not create production detections until behavior is tied to a primary source or sample-level report.

## Handling Notes

Malpedia taxonomy confirms association; behavior remains source-gated.

## Crosslinks

- Actor profile: [UNC1860](../actors/unc1860.md)
- Actor workbench: [UNC1860](../navigation/actor-workbench.md#unc1860)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#unc1860)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-MANDIANT-UNC1860` |
| [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-MANDIANT-UNC1860` |
| [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer | Command and Control | M2 | `SRC-MANDIANT-UNC1860` |
| [T1021.001](../navigation/ttp-detection-matrix.md#t1021001) Remote Services: RDP | Lateral Movement | M2 | `SRC-MANDIANT-UNC1860` |
| [T1078](../navigation/ttp-detection-matrix.md#t1078) Valid Accounts | Defense Evasion | M2 | `SRC-MANDIANT-UNC1860` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

- Source ID: `SRC-MALPEDIA-UNC1860`
- Reliability in source register: A
- Source type: Malware knowledge base
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
