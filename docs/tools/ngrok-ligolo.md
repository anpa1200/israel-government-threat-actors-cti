---
title: NGROK / Ligolo
sidebar_label: NGROK / Ligolo
---

# NGROK / Ligolo

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Pioneer Kitten](../actors/pioneer-kitten.md)
- Tool type: Tunneling / proxy tooling
- Confidence: High
- Source: [`SRC-CISA-AA24-241A`](https://www.ic3.gov/CSA/2024/240828.pdf)
- Source title: FBI / CISA / DC3, Iran-based Cyber Actors Enabling Ransomware Attacks on US Organizations, 2024-08-28

## Behavior

Dual-use tunneling tools used after edge compromise in Pioneer Kitten / Fox Kitten reporting.

## Hash And IOC Status

- Status: No malware hash; monitor tool binary, process, account, and network usage against approved admin list.
- Reference: `SRC-CISA-AA24-241A`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt unauthorized tunnels from edge servers, VPN appliances, or administrator workstations.

## Handling Notes

Dual-use; require local allowlisting.

## Crosslinks

- Actor profile: [Pioneer Kitten](../actors/pioneer-kitten.md)
- Actor workbench: [Pioneer Kitten](../navigation/actor-workbench.md#pioneer-kitten)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#pioneer-kitten)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-CISA-AA24-241A` |
| [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software | Command and Control | M2 | `SRC-CISA-AA24-241A` |
| [T1572](../navigation/ttp-detection-matrix.md#t1572) Protocol Tunneling | Command and Control | M2 | `SRC-CISA-AA24-241A` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

| Detection | Release Status | DRL | Rule |
| --- | --- | ---: | --- |
| DET-002 - Suspicious RMM Installer Download From User Context | Pilot | 6 | [detections/sigma/suspicious-rmm-file-sharing-download.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) |
| DET-003 - Unitronics PLC HMI Web Interface Access | Hunt | 4 | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

| Hunt | Hypothesis | Query |
| --- | --- | --- |
| HUNT-002 | If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths | [detections/kql/suspicious-rmm-file-sharing-download.kql](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) |
| HUNT-003 | If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access | [detections/sigma/unitronics-plc-hmi-web-access.yml](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) |

## Source Review

- Source ID: `SRC-CISA-AA24-241A`
- Reliability in source register: A
- Source type: Government advisory
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
