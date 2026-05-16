---
title: Cyber Toufan supplier-access playbook
sidebar_label: Cyber Toufan supplier-access playbook
---

# Cyber Toufan supplier-access playbook

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Cyber Toufan](../actors/cyber-toufan.md)
- Tool type: Credential and admin-interface abuse
- Confidence: Medium
- Source: [`SRC-OPI-CYBER-TOUFAN`](https://op-c.net/blog/cyber-toufan-attack-playbook/)
- Source title: OP Innovate, Eye of the Storm: Dissecting the Playbook of Cyber Toufan, 2025-05-26

## Behavior

OP Innovate reporting frames Cyber Toufan around exposed provider infrastructure, weak credentials, and leak-operation playbook behavior.

## Hash And IOC Status

- Status: Not malware; no hash. Track claims and exposure indicators.
- Reference: `SRC-OPI-CYBER-TOUFAN`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt supplier VPN/firewall/admin-surface access, default credential exposure, SMB admin-share movement, and public-claim timing.

## Handling Notes

Use persona-claim workflow before asserting compromise.

## Crosslinks

- Actor profile: [Cyber Toufan](../actors/cyber-toufan.md)
- Actor workbench: [Cyber Toufan](../navigation/actor-workbench.md#cyber-toufan)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#cyber-toufan)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1491](../navigation/ttp-detection-matrix.md#t1491) Defacement | Impact | M2 | `SRC-MS-IRAN-HAMAS` |
| [T1595](../navigation/ttp-detection-matrix.md#t1595) Active Scanning | Reconnaissance | M1 | `SRC-OPI-CYBER-TOUFAN` |
| [T1021.002](../navigation/ttp-detection-matrix.md#t1021002) SMB/Windows Admin Shares | Lateral Movement | M3 | `SRC-OPI-CYBER-TOUFAN` |

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

- Source ID: `SRC-OPI-CYBER-TOUFAN`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
