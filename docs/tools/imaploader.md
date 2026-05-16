---
title: IMAPLoader
sidebar_label: IMAPLoader
---

# IMAPLoader

This is a defensive tool-intelligence page. It is intended for analyst navigation, source review, and hunt planning. It is not a malware-analysis report and does not contain sample code or binaries.

## Summary

- Associated actor(s): [Imperial Kitten](../actors/imperial-kitten.md)
- Tool type(s): .NET downloader / loader
- Confidence level(s): High
- Source ID(s): `SRC-PWC-YELLOW-LIDERC-2023`

## Behavior

| Actor | Behavior Summary |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | PwC and related reporting describe IMAPLoader as an Imperial Kitten/Yellow Liderc .NET loader using legitimate or compromised email accounts for IMAP-based C2 after strategic web compromise or lure execution; it identifies target systems and can deploy follow-on payloads. |

## Hash And IOC Status

| Actor | Status | Reference |
| --- | --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Hash not committed; use PwC or vendor IOC appendix/current report for current sample hashes and mail-account indicators. | `SRC-PWC-YELLOW-LIDERC-2023` |

Hashes and IOCs on this page are source pointers or representative public indicators. They SHOULD be refreshed from the linked source before operational use and MUST NOT be used alone for actor attribution.

## Defensive Hunting Notes

| Actor | Hunting Notes |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Hunt non-mail-client IMAP/IMAPS egress, high-frequency mailbox polling, encoded attachment retrieval by unusual processes, and Office/XLL to csc.exe chains after maritime/logistics web compromise. |

## Handling Notes

| Actor | Handling Notes |
| --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | Behavior must be locally allowlisted for legitimate IMAP applications. |

## Crosslinks

- Imperial Kitten: [profile](../actors/imperial-kitten.md), [workbench](../navigation/actor-workbench.md#imperial-kitten), [tool matrix](../malware-tool-intelligence.md#imperial-kitten)
- Detection status: [Detection Status Dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [Hunt Workflow](../threat-hunting/hunt-workflow.md)

## Mapped ATT&CK Techniques For Associated Actor(s)

| Actor | Technique | Tactic | Mapping Quality | Source |
| --- | --- | --- | --- | --- |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise | Initial Access | M2 | `SRC-CS-IMPERIAL-KITTEN-2023` |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1071.003](../navigation/ttp-detection-matrix.md#t1071003) Mail Protocols | Command and Control | M3 | `SRC-PWC-YELLOW-LIDERC-2023` |
| [Imperial Kitten](../actors/imperial-kitten.md) | [T1059.005](../navigation/ttp-detection-matrix.md#t1059005) Visual Basic | Execution | M2 | `SRC-PWC-YELLOW-LIDERC-2023` |

## Related Actor-Level Repository Detections

These detections are mapped through the associated actor or scenario and are not automatically tool-specific. Promote a tool-specific detection only after the behavior is tied to telemetry and test evidence.

No repository detection is currently mapped to the associated actor(s). Use the hunting notes and source references as backlog input.

## Related Actor-Level Hunts

These hunts are mapped through the associated actor or scenario and may need narrowing before they are used for this specific tool.

No repository hunt is currently mapped to the associated actor(s). Create a hunt from the behavior and telemetry notes before proposing a production detection.

## Source Review

| Source | Publisher | Date | Reliability | Type | Last Reviewed |
| --- | --- | --- | --- | --- | --- |
| [`SRC-PWC-YELLOW-LIDERC-2023`](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html) | PwC | 2023-10-25 | A | Vendor CTI | 2026-05-14 |

If a source publishes a large or frequently changing IOC appendix, keep the current IOC list in the source system or TIP and store only the pointer here.
