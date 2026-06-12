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
- Tool detail pages: [`DarkBit ransomware`](../tools/darkbit-ransomware.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#darkbit) (1 mapped tool row(s))
- Evidence records: `EVD-020` / `CLM-DARKBIT-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-INCD-DARKBIT-MUDDYWATER-2023`, `SRC-MS-MERCURY-DEV1084-2023`

<!-- ACTOR-NAVIGATION:END -->

# DarkBit

## Background

DarkBit is not a stable independent threat group — it is a single-campaign ransomware persona used in the February 2023 Technion University incident. Microsoft's April 2023 report documented that MERCURY (MuddyWater) conducted initial access and staged the environment, while DEV-1084 (Storm-1084) executed the destructive payload using DarkBit ransomware — a deliberate hybrid of a politically-motivated wiper and a ransomware extortion tool.

The Technion incident is significant beyond its technical details. Technion is Israel's leading technology university and a strategic national asset with ties to defense research, cybersecurity, and Israel's technology sector pipeline. A 80 BTC ransom demand and an embedded anti-Israeli political message in the ransom note ("down with Israel") signaled that the operation's primary purpose was disruption, embarrassment, and psychological impact rather than financial return. The 4TB data theft claim and "RECOVERY_DARKBIT" note followed standard ransomware aesthetics to frame the incident as criminal rather than state-directed.

The broader pattern — MERCURY establishing initial access, a secondary team deploying destructive capability — is consistent with how MuddyWater appears to operate as an access broker enabling other MOIS-affiliated units to escalate from espionage to impact. Microsoft documented the same handoff model independently for MERCURY and DEV-1084. As of primary-source review, DarkBit has not reappeared as a distinct ransomware persona after 2023, supporting the assessment that this was a tailored persona for a specific operation rather than a reusable ransomware-as-a-service brand.

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

## Public Reports

**Own ecosystem:**

- [Deep Research Intake: MuddyWater](../reports/muddywater-deep-research.md) — Internal synthesis covering the MuddyWater/Storm-1084 ecosystem. DarkBit is documented as a tool within that cluster's destructive operations.
- [Actor Profile: MuddyWater](./muddywater.md) — Cross-reference for the parent cluster responsible for DarkBit's deployment context.

**Primary vendor reporting:**

- Microsoft MSTIC, "MERCURY and DEV-1084: Destructive Attack on Hybrid Environment" — April 2023. Documents the MERCURY (MuddyWater) initial access and DEV-1084 (Storm-1084) destructive handoff, including Exchange Web Services abuse, Azure AD Connect credential theft, and DarkBit deployment. Source ID `SRC-MS-MERCURY-DEV1084-2023`.
- INCD (Israel National Cyber Directorate), MuddyWater / Technion reporting — 2023. Israeli government reporting on the Technion incident and MuddyWater cluster activity in Israel. Source ID `SRC-INCD-DARKBIT-MUDDYWATER-2023`.
- Unit 42 / Palo Alto Networks, "Boggy Serpens" — 2026 reassessment of MuddyWater cluster under updated Microsoft naming. Source ID `SRC-UNIT42-BOGGY-SERPENS-2026`.
