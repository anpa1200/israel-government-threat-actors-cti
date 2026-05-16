---
title: Cyber Toufan supplier-access playbook
sidebar_label: Cyber Toufan supplier-access playbook
---

# Cyber Toufan supplier-access playbook

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Cyber Toufan](../actors/cyber-toufan.md)
- Tool type(s): Credential and admin-interface abuse
- Confidence level(s): Medium
- Source ID(s): `SRC-OPI-CYBER-TOUFAN`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | OP Innovate reporting frames Cyber Toufan around exposed provider infrastructure, weak credentials, and leak-operation playbook behavior. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | Not malware; no hash. Track claims and exposure indicators. | `SRC-OPI-CYBER-TOUFAN` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | Hunt supplier VPN/firewall/admin-surface access, default credential exposure, SMB admin-share movement, and public-claim timing. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | Use persona-claim workflow before asserting compromise. |

## Crosslinks

- Cyber Toufan: [profile](../actors/cyber-toufan.md), [workbench](../navigation/actor-workbench.md#cyber-toufan), [tool matrix](../malware-tool-intelligence.md#cyber-toufan)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | [T1491](../navigation/ttp-detection-matrix.md#t1491) Defacement | Impact | M2 | `SRC-MS-IRAN-HAMAS` |
| [Cyber Toufan](../actors/cyber-toufan.md) | [T1595](../navigation/ttp-detection-matrix.md#t1595) Active Scanning | Reconnaissance | M1 | `SRC-OPI-CYBER-TOUFAN` |
| [Cyber Toufan](../actors/cyber-toufan.md) | [T1021.002](../navigation/ttp-detection-matrix.md#t1021002) SMB/Windows Admin Shares | Lateral Movement | M3 | `SRC-OPI-CYBER-TOUFAN` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Actor | Detection | Release Status | DRL | Rule |
| --- | --- | --- | ---: | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Actor | Hunt | Hypothesis | Query |
| --- | --- | --- | --- |
| [Cyber Toufan](../actors/cyber-toufan.md) | HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-OPI-CYBER-TOUFAN`](https://op-c.net/blog/cyber-toufan-attack-playbook/) | OP Innovate | 2025-05-26 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
