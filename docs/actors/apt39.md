---
title: APT39
sidebar_label: APT39
---

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [APT39](../navigation/actor-workbench.md#apt39)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566.001](../navigation/ttp-detection-matrix.md#t1566001) Spearphishing Attachment (M2); [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Remexi`](../tools/remexi.md); [`ANTAK / ASPXSPY`](../tools/antak-aspxspy.md); [`Cadelspy`](../tools/cadelspy.md); [`CrackMapExec`](../tools/crackmapexec.md); [`ftp`](../tools/ftp.md); [`MechaFlounder`](../tools/mechaflounder.md); [`Mimikatz`](../tools/mimikatz.md); [`NBTscan`](../tools/nbtscan.md); [`PsExec`](../tools/psexec.md); [`pwdump`](../tools/pwdump.md); [`Windows Credential Editor`](../tools/windows-credential-editor.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt39) (11 mapped tool row(s))
- Evidence records: `EVD-027` / `CLM-APT39-001`
- Imported research intakes: [APT39 Arid Viper UNC3890 Cyber Toufan Deep Research Intake](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) (Medium, Needs source validation)
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G0087`

<!-- ACTOR-NAVIGATION:END -->

# APT39

## Background

APT39 (Chafer) has been active since approximately 2014, with operations documented across the Middle East, North Africa, Europe, and North America. The group is assessed as operating under the Iranian Ministry of Intelligence and Security (MOIS) through the front company Rana Intelligence Computing Company — a connection formally established through U.S. Treasury OFAC sanctions and a DOJ indictment unsealed in August 2020, which named nine Rana employees including senior leadership.

APT39's primary operational focus is bulk collection of identity-rich data: subscriber records from telecom operators, passenger name records from travel and hospitality firms, personnel data from government agencies, and credentials from IT service providers. This surveillance mandate distinguishes APT39 from Iran's destructive actors — the group is characterized by long-dwell access and mass data collection rather than rapid impact operations. Mandiant and FireEye tracking prior to the 2020 sanctions documented campaigns spanning at least 30 countries.

The 2020 U.S. law enforcement actions (OFAC sanctions, DOJ indictment, FBI flash) represented significant visibility into the group's organizational structure. Following the public exposure of the Rana Intelligence Computing connection, APT39/Chafer/Remix Kitten activity under these specific vendor labels became less visible in public incident reporting, likely reflecting operational security adjustments. Current analyst guidance is to maintain detection coverage based on established TTPs while explicitly marking recent operational evidence as limited until new primary reporting emerges.

Aliases: APT39, Chafer, Remix Kitten, ITG07. U.S. government and MITRE reporting connect APT39 activity to Rana Intelligence Computing.

Assessed sponsor: Iran MOIS via Rana Intelligence Computing in U.S. Treasury / DOJ and MITRE ATT&CK reporting.

## Relevance

APT39 is medium priority for Israeli public-sector defenders. The actor's strongest documented focus is telecom, travel, hospitality, IT, government, and identity-rich data collection across the Middle East and beyond. That is strategically relevant to Israeli border, civil aviation, telecom, and regional service-provider exposure. Current primary-source review preserves a gap for specific Israeli victim incidents in public reporting.

## Defensive Focus

- Surveillance-oriented access to telecom, travel, PNR, identity, and subscriber systems.
- Long-dwell credential harvesting rather than rapid destructive action.
- LSASS dumping and Sysinternals-style administrative tooling.
- Service execution and lateral movement inside telecom and travel networks.
- IT-provider compromise for supply-chain access.

## Detection Ideas

- `procdump.exe` or renamed dump utilities targeting `lsass.exe`, especially on domain controllers and critical application servers.
- PsExec or service-control lateral movement from non-admin subnets into telecom or public-sector segments.
- Bulk access to subscriber, travel, identity, or PNR data stores from unusual admin paths.
- Spearphishing attachment execution followed by credential collection or service installation.

## Operational Status

Current primary-source review did not identify high-confidence 2023-2025 incident reporting under the APT39 / Chafer / Remix Kitten label set. Keep recent operational evidence explicitly marked as limited until new primary reporting is added.

## Repository Sources

- `SRC-MITRE-G0087`: MITRE ATT&CK APT39 group profile.
- `SRC-US-TREASURY-RANA-2020`: U.S. Treasury sanctions announcement.
- `SRC-US-DOJ-RANA-2020`: U.S. DOJ Rana Intelligence Computing announcement.

## Public Reports

**MITRE ATT&CK:**

- [MITRE ATT&CK G0087 — APT39](https://attack.mitre.org/groups/G0087/) — Technique mappings, software associations (Remexi, MechaFlounder, Cadelspy), alias registry, and related campaigns.

**Government and law enforcement:**

- U.S. Department of Treasury OFAC, Rana Intelligence Computing Sanctions Designation — September 2020. Formally links Rana Intelligence Computing to MOIS and APT39 cluster. Source ID `SRC-US-TREASURY-RANA-2020`.
- U.S. Department of Justice, Indictment of Rana Intelligence Computing Employees — August 2020. Names nine individuals and details MOIS-tasked cyber operations. Source ID `SRC-US-DOJ-RANA-2020`.

**Primary vendor reporting:**

- Mandiant / FireEye, "APT39: An Iranian Cyber Espionage Group Focused on Personal Information" — 2019. Foundational profile documenting telecom, travel, and identity-data targeting across 30+ countries.
- Symantec / Broadcom, "Chafer" reporting — Technical analysis of Remexi RAT campaigns targeting Middle East organizations.
- Deep Research Intake: [APT39, Arid Viper, UNC3890, Cyber Toufan](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) — Internal repository synthesis. Medium priority, requires source validation.
