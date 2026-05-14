---
title: Deep Research Prompt
sidebar_label: Deep Research Prompt
---

# Deep Research Prompt — israel-government-threat-actors-cti

Use this prompt verbatim with OpenAI o3 (web search enabled), GPT-4o with browsing, or Google Gemini 2.5 Pro Deep Research. The goal is to fill the specific intelligence gaps identified in this repository's v0.1.1 review. All requested content is defensive and TLP:CLEAR.

---

## PROMPT

```
You are a senior cyber threat intelligence analyst performing deep, evidence-driven research for a defensive CTI knowledge base focused on threats to Israeli government, public-sector, municipal, critical infrastructure, telecom, and adjacent supplier environments.

The repository already covers: MuddyWater, OilRig, APT35, APT42, Agrius, CyberAv3ngers, Cotton Sandstorm, Arid Viper, UNC1860, Scarred Manticore, Cyber Toufan, Handala/Void Manticore, Lebanese Cedar, WIRTE, TA402, UNC3890.

All research must be:
- Defensive and blue-team only (TTPs, detections, actor behaviour — no exploit code, malware samples, or offensive tooling)
- Sourced from public reporting (vendor CTI, government advisories, academic research)
- Evidence-labelled per claim: Source-reported / Assessed-by-source / Assessed-here / Inferred / Gap
- TLP:CLEAR

---

### PART 1 — MISSING ACTOR PROFILES (highest priority)

For each actor below, provide a structured profile with these exact sections:
- Primary name and all confirmed vendor aliases (cite which vendor uses each alias)
- Assessed sponsor (be specific: IRGC-CEC / IRGC-IO / MOIS / Hamas / Hezbollah / contractor — with source)
- Relevance to Israeli government and public-sector (High / Medium / Low, with justification)
- Documented Israeli or Israel-adjacent targeting (specific incidents, sectors, dates)
- Primary TTPs mapped to MITRE ATT&CK (technique ID + name + tactic, with source per technique)
- Known malware and tools (name, type, brief behaviour description, primary source URL)
- Best available primary sources (publisher, title, date, URL — A-grade sources preferred: government advisories, MITRE ATT&CK, Mandiant, Check Point Research, SentinelLabs, ESET, Unit 42, ClearSky, Claroty Team82, Dragos)
- Defensive detection ideas (3–5 specific, testable hunt hypotheses)

#### Actor 1: Imperial Kitten / Tortoiseshell / Yellow Liderc
Focus: CrowdStrike "Imperial Kitten" (November 2023), PwC "Yellow Liderc", Symantec "Tortoiseshell". Iranian actor linked to Israeli transportation/logistics targeting, supply-chain phishing, IMAPLoader malware. What is the current sponsor assessment (IRGC? MOIS?)? What Israeli sectors were targeted in 2023–2025? What is the IMAPLoader kill chain?

#### Actor 2: Pioneer Kitten / Fox Kitten / Lemon Sandstorm / UNC757
Focus: CISA Advisory AA24-241A (August 2024). Iranian initial-access broker reported selling network access to ransomware affiliates. What Israeli or Middle East entities were targeted? What vulnerabilities are exploited? What is the handoff model to ransomware affiliates? What does the CISA advisory specifically say about Israeli critical infrastructure?

#### Actor 3: DarkBit
Focus: MuddyWater-linked ransomware/extortion persona that attacked Technion (Israel Institute of Technology) in February 2023. What is the confirmed or assessed link to MuddyWater / Iran? What was the ransom demand and operational messaging? What TTPs were used? Is DarkBit still active post-2023?

#### Actor 4: Lyceum / HEXANE / Spirlin
Focus: Iranian cluster targeting telecom, oil/gas, and ICS in MENA (Secureworks origin, Kaspersky Spirlin, ESET 2022). Relevance to Israeli telecom and energy suppliers. What is the current assessed sponsor? What is the primary malware (DanBot, Kevin, Shark)? What Israeli-adjacent targeting is documented?

#### Actor 5: APT39 / Chafer / Remix Kitten
Focus: Iran-nexus MOIS-linked actor sanctioned by U.S. Treasury (September 2020). Telecom, travel, IT targeting in Middle East. MITRE G0087. What Israeli or Israel-adjacent targeting is documented in primary sources? What is the current operational status and recent (2023–2025) activity?

---

### PART 2 — MALWARE AND TOOL INTELLIGENCE GAPS

For each tool/malware below, provide: confirmed actor attribution, malware type/category, brief technical behaviour (not code), primary source with URL and date, and one or two specific behavioral detection ideas (what to hunt in logs/telemetry).

1. **IOControl** (Claroty Team82, December 2024) — custom ICS malware attributed to CyberAv3ngers/IRGC-CEC. What devices does it target? How does it communicate? What does it do to PLC/HMI/router targets? What is the C2 mechanism?

2. **Liontail** (Check Point Research, October 2023) — Scarred Manticore's IIS native module passive backdoor framework. How does it load into IIS? What HTTP patterns does it use for C2? How does it differ from a standard webshell? What Windows event log or IIS log artefacts does it leave?

3. **BiBi Wiper / BiBi-Linux** (SentinelLabs, Security Joes — October 2023) — Agrius-linked wiper deployed post-October 7 against Israeli targets. What is the wiper behaviour (file extension, overwrite pattern)? What sectors were targeted? Is there a Windows variant?

4. **OilBooster** (ESET, December 2024) — new OilRig downloader. How is it delivered? What cloud service does it use for C2? How does it differ from previous OilRig downloaders (OuterSpace, Solar)?

5. **Fooder / MuddyViper** (ESET, December 2025 — "Snakes by the Riverbank") — MuddyWater implants targeting Israeli and Egyptian critical infrastructure. What are the delivery mechanism and C2 channels? What other tools were reported in the same campaign (VAXOne, CE-Notes, Blub, LP-Notes)?

6. **IMAPLoader** — Imperial Kitten/Tortoiseshell tool. IMAP-based C2 using legitimate email accounts. What is the delivery chain? What capabilities does it have post-compromise?

7. **Saitama** — OilRig DNS-tunneling backdoor. What is the DNS exfiltration mechanism? What detection opportunities does it create in DNS logs?

---

### PART 3 — DETECTION ENGINEERING GAPS

For each scenario below, provide a defensible detection hypothesis, required telemetry, specific observable behaviour, expected false-positive sources, and a Sigma or KQL rule skeleton (logic only — no need for production-ready code, just the key field selections and condition logic).

1. **IIS native module integrity** — detect Scarred Manticore / UNC1860 Liontail-style IIS native module implants. What Windows event IDs, IIS module load events, or file system paths should be monitored? What is the baseline of legitimate IIS module loads?

2. **VSS and backup deletion chain** — detect Handala / Agrius pre-destruction activity: shadow copy deletion (vssadmin, wmic, PowerShell), Windows Backup Service tampering, Azure Backup vault soft-delete disablement. What is the complete kill-chain observable sequence?

3. **Mass encryption staging** — detect Agrius / Handala destructive-encryption preparation: large-scale file read+write operations, unusual process opening thousands of file handles, endpoint protection service stopping before file operations. What EDR telemetry fields are relevant?

4. **BiBi Wiper behavioral pattern** — what file operation pattern (extension renaming, overwrite byte pattern, target file type selection) can be hunted in EDR file-operation telemetry without relying on hash or signature?

5. **IMAPLoader C2 via legitimate email** — detect Imperial Kitten IMAP-based C2: unusual process establishing IMAP/IMAPS connections (non-mail-client processes), high-frequency polling of an IMAP server, encoded attachments retrieved by non-standard processes.

6. **OilRig DNS tunneling (Saitama)** — detect high-entropy subdomain queries, unusually long DNS query names, high-frequency DNS queries to a single second-level domain from a single host. What DNS log fields are needed?

7. **Rockwell / Allen-Bradley PLC web interface exposure** — CyberAv3ngers / IRGC-CEC targeting per CISA AA26-097A. What Rockwell-specific URL paths or user-agent strings identify exposed engineering workstation interfaces, distinct from the Unitronics paths already covered?

---

### PART 4 — SOURCE VALIDATION AND NEW SOURCES

For each source below, confirm: Is the URL live? Is the content still accurate or has it been superseded? What is the appropriate reliability rating (A / B / C using NATO Admiralty Code — A = primary publisher with direct evidence, B = reliable synthesis, C = mixed)?

Also identify any major 2024–2026 primary-source publications NOT already listed that would significantly improve coverage of: MuddyWater, OilRig, Agrius, CyberAv3ngers, Arid Viper, Imperial Kitten, or Israeli public-sector targeting generally.

Sources to validate:
- Claroty Team82 IOControl report (December 2024)
- ESET "Snakes by the Riverbank" MuddyWater report (December 2025)
- ESET OilBooster report (December 2024)
- Symantec/Broadcom Crambus Israel telecom report (September 2024)
- CrowdStrike Imperial Kitten report (November 2023)
- CISA AA24-241A Pioneer Kitten joint advisory (August 2024)
- SentinelLabs BiBi Wiper report (October 2023)
- Security Joes BiBi-Linux report (October 2023)
- Check Point "Scarred Manticore versus MOIS: Seeing the Invisible" (October 2023)
- MITRE ATT&CK G1055 VOID MANTICORE (current version)

---

### PART 5 — ACTOR UPDATES (existing profiles that need new intelligence)

For each existing actor, report only what is NEW since 2023 that is not already common knowledge. Focus on: new malware families, new Israeli-specific incidents, updated sponsor attribution, new aliases, new TTPs, or significant OPSEC changes.

1. **OilRig** — What does the Symantec Crambus September 2024 report say about Israeli telecom targeting? What are OilBooster's new C2 techniques compared to OuterSpace and Solar? Any 2025 reporting?

2. **Agrius** — Full BiBi Wiper kill chain (both Windows and Linux variants). Moneybird ransomware details. Any 2024–2025 activity post the initial post-October 7 wave?

3. **MuddyWater** — What new tools did ESET December 2025 report? What does INCD ALERT-CERT-IL-W-1858 say that is not in the CISA/MITRE public record? Any 2026 activity?

4. **Arid Viper** — Any 2024–2026 Israeli military or reservist-targeting campaigns beyond AridSpy? New mobile malware? New social engineering patterns?

5. **UNC3890** — Any post-2022 primary reporting? Has the cluster been attributed or merged with another tracked group?

---

### OUTPUT FORMAT REQUIREMENTS

For each section, structure your response as:

**[Actor/Tool/Gap Name]**
- Claim: [specific fact]
- Evidence label: [Source-reported / Assessed-by-source / Inferred / Gap]
- Source: [Publisher, Title, Date, URL]
- Defensive implication: [what a SOC or detection engineer should do with this]

Where you cannot find primary source confirmation, explicitly label the claim as `Gap` and state what additional research is needed.

Do not speculate beyond available public evidence. Do not include offensive techniques, exploit code, or malware samples. All output is for defensive purposes only.
```

---

## Platform-specific notes

**OpenAI o3 / GPT-4o (web search enabled)**
Paste the prompt above directly. Enable web search. Ask follow-up: *"For each source URL you cited, confirm it returns HTTP 200 and the content matches the claim."*

**Google Gemini 2.5 Pro Deep Research**
Paste the prompt. Gemini Deep Research will generate a multi-step research plan — review and approve it before it runs. After the report is generated, ask: *"For Part 3 detection gaps, generate the Sigma condition logic and required logsource fields for each scenario."*

**Iteration tip (both platforms)**
After the first response, follow up with:
*"Focus on Part 1 Actor 1 (Imperial Kitten) and Part 3 item 1 (IIS native module integrity). Go deeper — find every primary source published between 2023 and 2026, list every confirmed alias, and write a complete actor profile in the style of a MITRE ATT&CK group page."*
