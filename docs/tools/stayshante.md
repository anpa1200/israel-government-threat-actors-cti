---
title: STAYSHANTE
sidebar_label: STAYSHANTE
---

# STAYSHANTE

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [UNC1860](../actors/unc1860.md)
- Tool type: Web shell / handoff tooling
- Confidence: High
- Source: [`SRC-MANDIANT-UNC1860`](https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks)
- Source title: Google Cloud / Mandiant, UNC1860 and the Temple of Oats: Iran's Hidden Hand in Middle Eastern Networks, 2024-09-19

## Behavior

Mandiant reports STAYSHANTE as a UNC1860 web shell deployed on compromised servers and controlled by VIROGREEN; INCD March 2024 indicators included unique STAYSHANTE web shell activity against Israeli sectors.

## Hash And IOC Status

- Status: Mandiant publishes activity-level MD5 IOCs and a VT collection; this repo does not map every hash to STAYSHANTE.
- Reference: `SRC-MANDIANT-UNC1860`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt webroot changes, server-file-name masquerading, SharePoint/IIS anomalies, and web server process child shells.

## Handling Notes

Use source IOC list and local webroot baseline.

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

- Source ID: `SRC-MANDIANT-UNC1860`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
