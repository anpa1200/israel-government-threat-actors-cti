---
title: IMAPLoader
sidebar_label: IMAPLoader
---

# IMAPLoader

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor: [Imperial Kitten](../actors/imperial-kitten.md)
- Tool type: .NET downloader / loader
- Confidence: High
- Source: [`SRC-PWC-YELLOW-LIDERC-2023`](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- Source title: PwC, Yellow Liderc ships its scripts and delivers IMAPLoader malware, 2023-10-25

## Behavior

IMAP-based command-and-control using legitimate or compromised email accounts; associated with Imperial Kitten / Yellow Liderc reporting.

## Hash And IOC Status

- Status: Hash not committed; use PwC or vendor IOC appendix/current report.
- Reference: `SRC-PWC-YELLOW-LIDERC-2023`

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

Hunt non-mail-client IMAP/IMAPS egress, high-frequency mailbox polling, and Office/XLL to csc.exe chains.

## Handling Notes

Behavior must be locally allowlisted for legitimate IMAP apps.

## Crosslinks

- Actor profile: [Imperial Kitten](../actors/imperial-kitten.md)
- Actor workbench: [Imperial Kitten](../navigation/actor-workbench.md#imperial-kitten)
- Tool matrix: [Malware And Tool Intelligence](../malware-tool-intelligence.md#imperial-kitten)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Actor

| Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- |
| [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise | Initial Access | M2 | `SRC-CS-IMPERIAL-KITTEN-2023` |
| [T1071.003](../navigation/ttp-detection-matrix.md#t1071003) Mail Protocols | Command and Control | M3 | `SRC-PWC-YELLOW-LIDERC-2023` |
| [T1059.005](../navigation/ttp-detection-matrix.md#t1059005) Visual Basic | Execution | M2 | `SRC-PWC-YELLOW-LIDERC-2023` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to this actor. Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to this actor. Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

- Source ID: `SRC-PWC-YELLOW-LIDERC-2023`
- Reliability in source register: A
- Source type: Vendor CTI
- Last reviewed: 2026-05-14

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
