---
description: "Cyber Toufan emerged in October 2023 conducting data theft and wiper operations against Israeli organizations, claiming 100+ victims following Hamas's October 7 attack."
---

# Cyber Toufan

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Cyber Toufan](../navigation/actor-workbench.md#cyber-toufan)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](../navigation/surface-capability-matrix.md#ot-plc); [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1491](../navigation/ttp-detection-matrix.md#t1491) Defacement (M2); [T1595](../navigation/ttp-detection-matrix.md#t1595) Active Scanning (M1); [T1021.002](../navigation/ttp-detection-matrix.md#t1021002) SMB/Windows Admin Shares (M3)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Cyber Toufan supplier-access playbook`](../tools/cyber-toufan-supplier-access-playbook.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cyber-toufan) (1 mapped tool row(s))
- Evidence records: `EVD-023` / `CLM-CYBERTOUFAN-001`
- Imported research intakes: [APT39 Arid Viper UNC3890 Cyber Toufan Deep Research Intake](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) (High, Needs source validation)
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-MS-IRAN-HAMAS`, `SRC-OPI-CYBER-TOUFAN`

<!-- ACTOR-NAVIGATION:END -->

## Background

Cyber Toufan emerged publicly in October-November 2023, immediately following Hamas's October 7 attack on Israel. Within weeks, the group claimed to have compromised dozens of Israeli organizations and began publishing stolen data on a Telegram channel. At its peak activity, the group claimed over 100 victim organizations — an implausibly large number for a short timeframe that signals either pre-positioning, opportunistic exploitation of weakly defended systems, or claim inflation. The name "Toufan" (Arabic: flood) is a direct reference to Hamas's "Al-Aqsa Flood" operation naming.

OP Innovate's incident response analysis — the primary technical report for this actor — documented a consistent playbook: exploitation of internet-exposed systems (typically through compromised vendor or hosting credentials), lateral movement via SMB admin shares using credential-stuffing or harvested credentials, bulk data exfiltration, and Telegram publication of data dumps formatted with inflammatory messaging. The combination of stolen data, defacement claims, and coordinated Telegram amplification is consistent with the influence operation model seen across other Iran-affiliated conflict-period personas.

Attribution confidence for Cyber Toufan is assessed as medium. Consistent tooling, claim patterns, and operational tempo across the persona suggest coordination beyond a spontaneous hacktivist collective; some security researchers have noted infrastructure and operational timing overlaps with known Iran-affiliated infrastructure. However, as of repository review, no primary government or law enforcement attribution document has been published formally linking Cyber Toufan to a specific Iranian intelligence body. Analysts should apply `Assessed-by-source` labeling rather than `Confirmed` for any Iran agency-specific attribution.

Assessed sponsor: Iran-aligned persona / hacktivist persona in public reporting.

## Relevance

Cyber Toufan is relevant as a claimed activity persona around Israeli targets, especially where public claims, leaks, and disruptive messaging may affect public confidence. Treat claims as unverified until supported by forensic evidence or reputable reporting.

## Defensive Focus

- Leak claims and public data exposure.
- Website disruption and defacement.
- Psychological operations and media amplification.
- Incident communications coordination.

## Analytic Caution

Attribution confidence is medium or lower unless supported by independent technical evidence.

## Repository Sources

- `SRC-OPI-CYBER-TOUFAN`: OP Innovate primary playbook analysis — external exposure, credential abuse, SMB lateral movement via admin shares, Telegram leak operations.
- `SRC-MS-IRAN-HAMAS`: Microsoft Threat Intelligence, Iran influence operations context.

## Associated Detection Content

The KQL hunt `detections/kql/smb-admin-share-lateral-movement-anomaly.kql` covers the native SMB lateral movement pattern described in the OP Innovate playbook.

## Public Reports

**Own ecosystem:**

- [Deep Research Intake: APT39, Arid Viper, UNC3890, Cyber Toufan](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) — Internal repository synthesis. High-priority, requires source validation.

**Primary vendor reporting:**

- OP Innovate, "Cyber Toufan: Analysis of a Prolific Threat Actor" — Primary playbook analysis documenting initial access, lateral movement via SMB admin shares, data exfiltration, and Telegram operations. Source ID `SRC-OPI-CYBER-TOUFAN`.
- Microsoft Threat Intelligence, "Iran and Hamas: Cyber-Enabled Influence Operations" — Conflict-period context for Iran-aligned hacktivist and influence personas including patterns consistent with Cyber Toufan operations. Source ID `SRC-MS-IRAN-HAMAS`.
- SentinelLabs, "The Cyber Dimension of the Israel-Hamas Conflict" — Comprehensive overview of Iran-aligned and Hamas-affiliated cyber operations during the October 2023 conflict period, providing context for Cyber Toufan's emergence and operational patterns.
