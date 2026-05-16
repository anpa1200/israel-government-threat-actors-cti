---
title: Caterpillar WebShell
sidebar_label: Caterpillar WebShell
---

# Caterpillar WebShell

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Lebanese Cedar](../actors/lebanese-cedar.md)
- Tool type: Web Shell
- Confidence: Medium
- Source: [`SRC-CLEARSKY-LEBANESE-CEDAR`](https://www.clearskysec.com/cedar/)
- Source title: ClearSky Cyber Security, Lebanese Cedar APT, 2021-01-28

## Behavior

Modified JSP file browser/webshell used by Lebanese Cedar for persistence on public-facing servers.

## Hash And IOC Status

- Status: Hash not committed; use ClearSky report references.
- Reference: `SRC-CLEARSKY-LEBANESE-CEDAR`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt modified JSP files, unexpected upload paths, and web server process spawning shells.

## Handling Notes

Use behavior and webroot integrity monitoring.

## Crosslinks

- Actor profile: [Lebanese Cedar](../actors/lebanese-cedar.md)
- Actor workbench: [Lebanese Cedar](../navigation/actor-workbench.md#lebanese-cedar)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#lebanese-cedar)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application | Initial Access | M2 | `SRC-CLEARSKY-LEBANESE-CEDAR` |
| [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell | Persistence | M2 | `SRC-CLEARSKY-LEBANESE-CEDAR` |

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

- Source ID: `SRC-CLEARSKY-LEBANESE-CEDAR`
- Reliability in source register: B
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
