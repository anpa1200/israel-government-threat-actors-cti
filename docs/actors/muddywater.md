---
description: "MuddyWater is a MOIS-attributed Iranian cyber espionage group explicitly designated by CISA advisory AA22-055A, active since 2017 targeting Israeli government, defense, and critical infrastructure."
---

# MuddyWater

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [MuddyWater](../navigation/actor-workbench.md#muddywater)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M2); [T1059.001](../navigation/ttp-detection-matrix.md#t1059001) PowerShell (M2); [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software (M3); [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M2)
- Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context (Pilot, DRL-6); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MITRE-G0069` Technique references; `SRC-AP-MUDDYWATER` Malware/tool references; ATT&CK mappings; campaign IOCs; `SRC-THREAT-HUNTER-V3` Domains; IPs; Rclone destinations; Dindoor/Fakeset references; `SRC-INCD-MUDDYWATER-2024` Domains; hashes; tools; infrastructure; TTPs
- Tool detail pages: [`Remote Monitoring and Management tools`](../tools/remote-monitoring-and-management-tools.md); [`Dindoor`](../tools/dindoor.md); [`Fakeset`](../tools/fakeset.md); [`BugSleep`](../tools/bugsleep.md); [`BlackBeard`](../tools/blackbeard.md); [`Fooder / MuddyViper`](../tools/fooder-muddyviper.md); [`ConnectWise`](../tools/connectwise.md); [`CrackMapExec`](../tools/crackmapexec.md); [`DCHSpy`](../tools/dchspy.md); [`Empire`](../tools/empire.md); [`Koadic`](../tools/koadic.md); [`LaZagne`](../tools/lazagne.md); [`LP-Notes`](../tools/lp-notes.md); [`Mimikatz`](../tools/mimikatz.md); [`Mori`](../tools/mori.md); [`Out1`](../tools/out1.md); [`PowerSploit`](../tools/powersploit.md); [`POWERSTATS`](../tools/powerstats.md); [`PowGoop`](../tools/powgoop.md); [`Rclone`](../tools/rclone.md); [`RemoteUtilities`](../tools/remoteutilities.md); [`RustyWater`](../tools/rustywater.md); [`SHARPSTATS`](../tools/sharpstats.md); [`Small Sieve`](../tools/small-sieve.md); [`STARWHALE`](../tools/starwhale.md); [`Tsundere Botnet`](../tools/tsundere-botnet.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#muddywater) (26 mapped tool row(s))
- Evidence records: `EVD-004` / `CLM-MUDDYWATER-001`
- Imported research intakes: [MuddyWater Deep Research Intake](../reports/muddywater-deep-research.md) (High, Needs source validation)
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-MUDDYWATER`, `SRC-CP-BUGSLEEP`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-MITRE-G0069`, `SRC-THREAT-HUNTER-V3`

<!-- ACTOR-NAVIGATION:END -->

## Background

MuddyWater has been active since approximately 2017, and is one of the most consistently documented Iranian cyber espionage groups in public reporting. CISA explicitly stated in advisory AA22-055A that MuddyWater is "a subordinate element within the Iranian Ministry of Intelligence and Security (MOIS)," making it one of the few Iranian actors with firm organizational attribution in a U.S. government advisory. The group targets government, local government, telecommunications, defense, and oil and gas organizations across the Middle East, Europe, Asia, and North America.

The group's operational evolution is well-documented. Early campaigns (2017–2019) relied on POWERSTATS — a PowerShell-based backdoor — distributed through malicious macro-embedded Office documents. By 2020–2022, MuddyWater shifted toward living-off-the-land approaches using PowerSploit, Empire, Koadic, and legitimate remote access tools. From 2022 onward, the group substantially expanded its abuse of commercial remote monitoring and management (RMM) tools — including Atera, ConnectWise, AnyDesk, and RemoteUtilities — delivered via phishing emails to serve as persistent C2 channels without deploying custom malware.

Two developments mark MuddyWater's 2023–2025 trajectory. First, Check Point's July 2024 BugSleep analysis documented a new custom implant replacing RMM abuse in some operations, with modular task-based execution and direct C2. Second, Microsoft attributed the February 2023 Technion University incident to MERCURY (the retired MuddyWater designator) acting together with DEV-1084 (Storm-1084) — a destructive affiliate that deployed the DarkBit ransomware persona. This indicates MuddyWater-linked activity can precede or enable destructive operations conducted by associated subgroups, not only persistent espionage.

For Israeli government defenders, the Israel National Cyber Directorate (INCD) issued a MuddyWater-specific advisory in 2024 documenting campaigns against Israeli entities using phishing and RMM tool abuse, making this the highest-confidence Israeli-targeting documentation in the primary source set.

Aliases: Mango Sandstorm, Boggy Serpens (Microsoft, current), Static Kitten, Seedworm, MERCURY (Microsoft, retired April 2023), TEMP.Zagros, TA450 (Proofpoint), Earth Vetala (Trend Micro).

Assessed sponsor: Iran MOIS-aligned in public reporting.

## Relevance

MuddyWater is high priority for Israeli government and regional public-sector defense because MITRE records targeting of government, local government, telecommunications, defense, and oil and gas organizations across the Middle East and other regions.

## Defensive Focus

- Spearphishing and malicious document delivery.
- PowerShell execution and script-based collection.
- Legitimate remote access tool abuse.
- Credential collection and lateral movement preparation.

## Field Manual Cross-Reference

Full public-source case study with PIR/SIR decomposition, alias table, sponsor assessment, ATT&CK mapping with quality levels, telemetry requirements, and DRL-1 hunt hypotheses: [CTI Analyst Field Manual — MuddyWater Worked Example](https://1200km.com/cti-analyst-field-manual/docs/worked-examples/actor-research).

## Detection Ideas

- RMM execution from user download folders.
- PowerShell encoded commands launched by Office, browser, archive, or script-host processes.
- New persistence from suspicious scheduled tasks or registry run keys.

Sources: `SRC-MITRE-G0069`, `SRC-CISA-AA22-055A`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-CP-BUGSLEEP`, `SRC-KASPERSKY-ICS-Q4-2025`, `SRC-BRANDEFENSE-MUDDYWATER-2025`, `SRC-AP-MUDDYWATER`.

Source note: Kaspersky ICS and Brandefense are Score B synthesis sources in this repository. Use them for collection planning and cross-checking, then anchor high-impact claims to ESET, INCD, CISA, MITRE, or Check Point.

## Public Reports

**Own ecosystem — read first:**

- [CTI Research: MuddyWater / Seedworm / Mango Sandstorm](https://medium.com/@1200km/cti-research-muddywater-seedworm-mango-sandstorm-ebf6af5ba061) — Andrey Pautov / 1200km. Defensive CTI profile with ATT&CK mapping, alias table, toolset analysis, and SOC-relevant IOC guidance. Source ID `SRC-AP-MUDDYWATER`.
- [CTI Analyst Field Manual — MuddyWater Worked Example](https://1200km.com/cti-analyst-field-manual/docs/worked-examples/actor-research) — 1200km CTI Analyst Field Manual. Full case study with PIR/SIR decomposition, sponsor assessment, ATT&CK quality levels, telemetry requirements, and DRL-1 hunt hypotheses.
- [Deep Research Intake: MuddyWater](../reports/muddywater-deep-research.md) — Internal repository research synthesis. High-priority intake requiring source validation.

**Government advisories:**

- [CISA Advisory AA22-055A — MuddyWater](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-055a) — CISA/CNMF/NCSC-UK/DC3, February 2022. Establishes MOIS attribution, describes TTPs, and provides IOCs. Source ID `SRC-CISA-AA22-055A`.
- INCD MuddyWater Advisory 2024 — Israel National Cyber Directorate. Israeli-facing campaign documentation with IOCs and phishing infrastructure. Source ID `SRC-INCD-MUDDYWATER-2024`.

**MITRE ATT&CK:**

- [MITRE ATT&CK G0069 — MuddyWater](https://attack.mitre.org/groups/G0069/) — Comprehensive technique mappings, software associations, and alias registry.

**Primary vendor reporting:**

- Check Point Research, "BugSleep: A New MuddyWater Backdoor" — July 2024. Analysis of post-RMM custom implant. Source ID `SRC-CP-BUGSLEEP`.
- ESET Research, "MuddyWater: New Snakes in the Mud" — Technical analysis of updated toolset and campaign evolution. Source ID `SRC-ESET-MUDDYWATER-SNAKES`.
- Microsoft MSTIC, "MERCURY and DEV-1084: Destructive Attack on Hybrid Environment" — April 2023. Documents MuddyWater/Storm-1084 joint destructive operation. Source ID `SRC-MS-MERCURY-DEV1084-2023`.
