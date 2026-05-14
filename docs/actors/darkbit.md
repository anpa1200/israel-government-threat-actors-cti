---
title: DarkBit
sidebar_label: DarkBit
---

# DarkBit

DarkBit is tracked here as a destructive extortion persona / pseudo-ransomware operation rather than a stable independent ransomware group.

Aliases and relationships: DarkBit persona; MuddyWater / MERCURY / Mango Sandstorm association in public reporting; DEV-1084 / Storm-1084 association in Microsoft reporting on destructive activity.

Assessed sponsor: Iran MOIS-linked through the MuddyWater/MERCURY ecosystem in public reporting. Incident-level claims should cite the specific source because DarkBit was also designed to present hacktivist or criminal-style messaging.

## Relevance

DarkBit is high priority for Israeli public-sector defenders because the persona was used in the February 2023 Technion incident and illustrates a recurring Iranian pattern: destructive or disruptive action framed as ransomware or hacktivism.

## Technion Incident

Imported research records the Technion ransom demand as 80 BTC, with anti-Israeli messaging, a claimed 4 TB data-theft narrative, and a recovery note named `RECOVERY_DARKBIT`. Treat these as source-reported claims pending direct primary-source review before use in executive reporting.

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

The imported OpenAI research did not find strong public evidence that DarkBit persisted as a standalone persona after 2023. Maintain detections on MuddyWater/Storm-1084 behaviors and destructive-operation chains rather than on the DarkBit brand alone.

## Repository Sources

- `SRC-INCD-DARKBIT-MUDDYWATER-2023`: INCD MuddyWater / Technion reporting.
- `SRC-MS-MERCURY-DEV1084-2023`: Microsoft MERCURY and DEV-1084 destructive-operations reporting.
- `SRC-UNIT42-BOGGY-SERPENS-2026`: Unit 42 Boggy Serpens assessment.
