---
title: DarkBit
sidebar_label: DarkBit
---

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [DarkBit](../navigation/actor-workbench.md#darkbit)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact (M2); [T1490](../navigation/ttp-detection-matrix.md#t1490) Inhibit System Recovery (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Malware and tools: [`DarkBit ransomware`](../tools/darkbit-ransomware.md) (Pseudo-ransomware / destructive malware)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#darkbit) (1 mapped tool row(s))
- Tool detail pages: [`DarkBit ransomware`](../tools/darkbit-ransomware.md)
- Evidence records: `EVD-020` / `CLM-DARKBIT-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-INCD-DARKBIT-MUDDYWATER-2023`, `SRC-MS-MERCURY-DEV1084-2023`

<!-- ACTOR-NAVIGATION:END -->

# DarkBit

DarkBit is tracked here as a destructive extortion persona / pseudo-ransomware operation rather than a stable independent ransomware group.

Aliases and relationships: DarkBit persona; MuddyWater / MERCURY / Mango Sandstorm association in public reporting; DEV-1084 / Storm-1084 association in Microsoft reporting on destructive activity.

Assessed sponsor: Iran MOIS-linked through the MuddyWater/MERCURY ecosystem in public reporting. Incident-level claims should cite the specific source because DarkBit was also designed to present hacktivist or criminal-style messaging.

## Relevance

DarkBit is high priority for Israeli public-sector defenders because the persona was used in the February 2023 Technion incident and illustrates a recurring Iranian pattern: destructive or disruptive action framed as ransomware or hacktivism.

## Technion Incident

Current source review records the Technion ransom demand as 80 BTC, with anti-Israeli messaging, a claimed 4 TB data-theft narrative, and a recovery note named `RECOVERY_DARKBIT`. Treat these as source-reported claims pending direct primary-source verification before use in executive reporting.

## Defensive Focus

- Initial public-facing application compromise followed by tunneling and scheduled-task persistence.
- Microsoft Defender tampering or exclusions before impact.
- Azure AD Connect credential theft or sync-account abuse.
- Exchange Web Services and mailbox impersonation abuse.
- Mass encryption or cloud resource deletion masquerading as ransomware.

## Detection Ideas

- Sequence web compromise -> tunneling -> scheduled task creation -> security-control tampering -> mass encryption or Azure resource deletion.
- `Set-Mailbox` "send on behalf" or mailbox permission changes after privileged account compromise.
- Access to Azure AD Connect hosts followed by unusual sign-ins by synchronization or privileged service accounts.
- Rapid file modification and ransom-note creation from an unsigned or newly observed binary.

## Analytic Caution

Current primary-source review did not identify strong public evidence that DarkBit persisted as a standalone persona after 2023. Maintain detections on MuddyWater/Storm-1084 behaviors and destructive-operation chains rather than on the DarkBit brand alone.

## Repository Sources

- `SRC-INCD-DARKBIT-MUDDYWATER-2023`: INCD MuddyWater / Technion reporting.
- `SRC-MS-MERCURY-DEV1084-2023`: Microsoft MERCURY and DEV-1084 destructive-operations reporting.
- `SRC-UNIT42-BOGGY-SERPENS-2026`: Unit 42 Boggy Serpens assessment.
