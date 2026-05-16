---
title: Actor Deep Research Prompts
sidebar_label: Actor Deep Research Prompts
---

# Actor Deep Research Prompts

These prompts are designed for LLM-assisted deep research with web search enabled. They are intended to refresh actor profiles, source registers, tool pages, ATT&CK mappings, hunting hypotheses, and detection backlog items without weakening evidence discipline.

Use them for public, defensive, TLP:CLEAR research only. Do not request malware samples, exploit code, leaked data, credentials, victim data, or instructions for unauthorized access.

## Common Research Contract

Apply this contract to every actor prompt below.

```text
You are a senior cyber threat intelligence analyst supporting a defensive CTI-to-detection framework for Israeli government, public-sector, municipal, telecom, critical-infrastructure, defense-adjacent, and supplier environments.

Research scope:
- Public reporting only: government advisories, vendor CTI, MITRE ATT&CK, academic research, regulator or CERT publications, and reputable sector reports.
- Time window: prioritize 2023-2026, but include older primary sources when they remain the best evidence for aliases, tooling, or attribution.
- Defensive output only: actor behavior, victimology, tools, IOCs as public references, detections, telemetry, hunt hypotheses, and gaps.
- Exclusions: no exploit code, malware source, malware samples, credential material, leaked victim data, or offensive operational instructions.

Evidence labels:
- Source-reported: the source directly states the fact.
- Assessed-by-source: the source makes an analytic assessment.
- Assessed-here: you infer from multiple cited sources; explain the reasoning.
- Inferred: weak inference requiring review.
- Gap: not publicly confirmed or not found.

For every cited URL:
- Confirm the URL is live or state the access problem.
- Record publication date, accessed date, publisher, title, URL, and whether the source appears superseded.
- Rate reliability: A = primary/government/vendor technical source, B = reputable synthesis, C = watchlist/context, D/F = weak or unusable for operational decisions.

Output sections:
1. Executive summary for Israeli public-sector defenders.
2. Actor identity: primary name, aliases, vendor naming caveats, and taxonomy conflicts.
3. Sponsor and command relationship: cite exact source language; separate state sponsor, proxy, contractor, and public persona.
4. Israeli or Israel-adjacent relevance: sectors, incidents, dates, confidence, and gaps.
5. Targeting and intrusion lifecycle: initial access, execution, persistence, privilege access, defense evasion, discovery, lateral movement, C2, exfiltration, impact.
6. ATT&CK mapping table: technique ID, name, tactic, observable, source, evidence label, mapping quality M1-M4.
7. Associated families and tools: tool name, type, actor confidence, behavior, public hash/IOC reference location, source, detection notes, handling notes.
8. Public IOCs: include only source-published indicators or pointers to official IOC appendices; do not invent or over-normalize indicators.
9. Detection and hunting: 5-10 hypotheses with required telemetry, fields, lookback, observable behavior, false positives, escalation criteria, and linked ATT&CK.
10. Source register updates: rows suitable for sources.csv.
11. Evidence register updates: claim_id, actor_id, source_id, quote/summary, evidence label, reliability, credibility, confidence, confidence reason, contradiction/gap.
12. Tool-intelligence updates: rows suitable for tool-intelligence.csv.
13. Navigation/crosslink recommendations: actor page, tool pages, TTP matrix, hunts, detections, worked cases, persona claims.
14. Gaps and follow-up collection plan.

Do not speculate beyond available evidence. Where evidence is insufficient, mark Gap and explain what source would be needed.
```

## Tag Index

Use these tags to choose the right actor prompt by defender need, sector, or research task.

### Government / Public Sector {#tag-government-public-sector}

[MuddyWater](#muddywater), [OilRig](#oilrig), [Magic Hound / APT35](#magic-hound--apt35), [APT42](#apt42), [Agrius](#agrius), [Pioneer Kitten](#pioneer-kitten), [APT39](#apt39), [APT-C-23 / Arid Viper](#apt-c-23--arid-viper), [TA402](#ta402), [UNC1860](#unc1860), [Scarred Manticore](#scarred-manticore), [Void Manticore / Handala](#void-manticore--handala).

### Medical / Healthcare {#tag-medical-healthcare}

[Agrius](#agrius), [DarkBit](#darkbit), [Void Manticore / Handala](#void-manticore--handala), [Lebanese Cedar](#lebanese-cedar).

### Financial / Extortion / Ransomware-Adjacent {#tag-financial-extortion}

[Agrius](#agrius), [DarkBit](#darkbit), [Pioneer Kitten](#pioneer-kitten), [Void Manticore / Handala](#void-manticore--handala), [Cyber Toufan](#cyber-toufan).

### Telecom / ISP / Communications {#tag-telecom}

[OilRig](#oilrig), [Lyceum](#lyceum), [APT39](#apt39), [Cyber Toufan](#cyber-toufan), [UNC1860](#unc1860), [Scarred Manticore](#scarred-manticore), [Lebanese Cedar](#lebanese-cedar).

### OT / ICS / Critical Infrastructure {#tag-ot-ics}

[CyberAv3ngers](#cyberav3ngers), [Cyber Toufan](#cyber-toufan), [Lyceum](#lyceum), [MuddyWater](#muddywater), [UNC1860](#unc1860). Route technical questions through the [Surface And Capability Matrix](../navigation/surface-capability-matrix.md#ot-plc).

### Identity / Cloud / Mailbox {#tag-identity-cloud}

[APT42](#apt42), [Magic Hound / APT35](#magic-hound--apt35), [Pioneer Kitten](#pioneer-kitten), [Void Manticore / Handala](#void-manticore--handala), [OilRig](#oilrig), [Imperial Kitten](#imperial-kitten). Route detections through the [TTP To Detection Matrix](../navigation/ttp-detection-matrix.md).

### IOC / Tooling / Hash Review {#tag-ioc-tooling}

All actor prompts link to actor-specific sections in the [Malware And Tool Intelligence Matrix](../malware-tool-intelligence.md) and individual [tool pages](../tools/README.md).

### Persona Claims / Hack-And-Leak {#tag-persona-claims}

[Void Manticore / Handala](#void-manticore--handala), [Cyber Toufan](#cyber-toufan), [DarkBit](#darkbit), [Cotton Sandstorm](#cotton-sandstorm). Record outputs in the persona-claims workflow when claims are not independently verified.

### Supplier / Third Party / Edge Access {#tag-supplier-third-party}

[Imperial Kitten](#imperial-kitten), [Pioneer Kitten](#pioneer-kitten), [Cyber Toufan](#cyber-toufan), [UNC1860](#unc1860), [Scarred Manticore](#scarred-manticore), [OilRig](#oilrig).

## MuddyWater

Profile: [MuddyWater](../actors/muddywater.md). Tool matrix: [MuddyWater tools](../malware-tool-intelligence.md#muddywater).

Tags: [Government / Public Sector](#tag-government-public-sector), [OT / ICS](#tag-ot-ics), [IOC / Tooling](../malware-tool-intelligence.md#muddywater), [Hunting](../navigation/actor-workbench.md#muddywater).

```text
Use the Common Research Contract.

Actor: MuddyWater / Mango Sandstorm / Boggy Serpens / Static Kitten / Seedworm / TA450 / Earth Vetala / MERCURY (retired Microsoft alias).

Research goals:
- Refresh 2023-2026 reporting on Israeli, Egyptian, Saudi, regional government, energy, transportation, telecom, and critical-infrastructure targeting.
- Validate current sponsor assessment and whether sources describe MOIS alignment, broader Iran state alignment, or a contractor/proxy relationship.
- Prioritize reporting on RMM abuse, PowerShell, phishing, LOTS/cloud services, Fooder, MuddyViper, VAX-One, CE-Notes, LP-Notes, SimpleHelp, BugSleep, Havoc, Sad C2, and Starlink or resilient C2 claims.
- Separate confirmed public reporting from vendor clustering and from unattributed Iran-nexus overlap.
- Produce concrete updates for actor profile, ATT&CK mappings, tool-intelligence rows, hunt hypotheses, and source/evidence registers.

Special checks:
- Identify every primary source since 2023 that names Israeli or Israel-adjacent victims/sectors.
- Confirm whether any 2025-2026 claims are primary source, secondary synthesis, or unverified reporting.
- For each tool, state whether public hashes exist and point to the source appendix rather than duplicating large IOC sets.
```

## OilRig

Profile: [OilRig](../actors/oilrig.md). Tool matrix: [OilRig tools](../malware-tool-intelligence.md#oilrig).

Tags: [Government / Public Sector](#tag-government-public-sector), [Telecom](#tag-telecom), [Identity / Cloud](#tag-identity-cloud), [Supplier / Third Party](#tag-supplier-third-party), [IOC / Tooling](../malware-tool-intelligence.md#oilrig).

```text
Use the Common Research Contract.

Actor: OilRig / APT34 / Helix Kitten / Hazel Sandstorm / COBALT GYPSY / Crambus.

Research goals:
- Refresh 2023-2026 reporting on Israeli telecom, government, defense-adjacent, energy, and technology targeting.
- Validate current source-backed aliases and explain where Crambus, Hazel Sandstorm, and APT34 naming overlaps or diverges.
- Focus on webshells, credential access, cloud/API C2, Saitama DNS tunneling, OilBooster, OilCheck, ODAgent, SampleCheck5000, PowerExchange, Solar, Mango, RGDoor, SideTwist, and ZeroCleare references.
- Compare newer OilRig downloaders and cloud-service C2 patterns against older tooling.
- Generate defender-useful DNS, webshell, cloud API, and endpoint hunt hypotheses.

Special checks:
- Confirm Symantec/Broadcom Crambus Israeli telecom claims and any later superseding reporting.
- Identify tool-specific public hashes or IOC appendix locations from ESET, Symantec/Broadcom, Unit 42, Microsoft, MITRE, or other primary sources.
- Mark any destructive-tool overlap, such as ZeroCleare, as source-specific and avoid over-attribution.
```

## Magic Hound / APT35

Profile: [Magic Hound / APT35](../actors/apt35.md). Tool matrix: [Magic Hound tools](../malware-tool-intelligence.md#magic-hound).

Tags: [Government / Public Sector](#tag-government-public-sector), [Identity / Cloud](#tag-identity-cloud), [IOC / Tooling](../malware-tool-intelligence.md#magic-hound), [Hunting](../navigation/actor-workbench.md#magic-hound).

```text
Use the Common Research Contract.

Actor: Magic Hound / APT35 / Charming Kitten / TA453 / Phosphorus / Mint Sandstorm / COBALT ILLUSION.

Research goals:
- Refresh 2023-2026 reporting on phishing, credential theft, infrastructure acquisition, persona operations, and Israeli or Israel-adjacent targeting.
- Separate APT35, APT42, Mint Sandstorm, TA453, Charming Kitten, and Phosphorus naming with explicit vendor caveats.
- Focus on social engineering, fake login pages, mailbox compromise, FRP/Plink, CharmPower, DownPaper, PowerLess, Pupy, public tooling, and tunneling behavior.
- Produce identity, email, endpoint, and cloud telemetry hunt hypotheses.

Special checks:
- Identify which sources treat APT35 and APT42 as separate clusters and which use broader umbrella names.
- Do not use public offensive tools alone as attribution evidence.
- Capture persona and phishing infrastructure indicators only as source-published references.
```

## APT42

Profile: [APT42](../actors/apt42.md). Tool matrix: [APT42 tools](../malware-tool-intelligence.md#apt42).

Tags: [Government / Public Sector](#tag-government-public-sector), [Identity / Cloud](#tag-identity-cloud), [IOC / Tooling](../malware-tool-intelligence.md#apt42), [Hunting](../navigation/actor-workbench.md#apt42).

```text
Use the Common Research Contract.

Actor: APT42 / UNC788 / Charming Kitten-related reporting / Mint Sandstorm overlap in some taxonomies.

Research goals:
- Refresh 2023-2026 reporting on IRGC-IO-linked credential harvesting, social engineering, cloud account abuse, MFA bypass, AitM phishing, and high-value individual targeting.
- Focus on Israeli, U.S., Middle East, policy, NGO, academic, journalist, defense-adjacent, and government targets.
- Validate reporting on NICECURL, TAMECAT, POWERPOST, Evilginx2/AitM, Netlify/OneDrive-themed phishing, remote template injection, and cloud persistence.
- Generate detection and hunt ideas for mail, identity, OAuth/app registration, MFA method changes, session theft, impossible travel, and suspicious mailbox access.

Special checks:
- Separate actor tooling from commodity phishing infrastructure.
- Identify which claims are Mandiant/Microsoft/Proofpoint source-reported versus broader synthesis.
- Include a cloud-specific evidence and telemetry table.
```

## Agrius

Profile: [Agrius](../actors/agrius.md). Tool matrix: [Agrius tools](../malware-tool-intelligence.md#agrius).

Tags: [Government / Public Sector](#tag-government-public-sector), [Medical / Healthcare](#tag-medical-healthcare), [Financial / Extortion](#tag-financial-extortion), [IOC / Tooling](../malware-tool-intelligence.md#agrius), [Hunting](../navigation/actor-workbench.md#agrius).

```text
Use the Common Research Contract.

Actor: Agrius / Pink Sandstorm / AMERICIUM / Agonizing Serpens / BlackShadow.

Research goals:
- Refresh 2023-2026 reporting on destructive operations against Israeli organizations, higher education, healthcare, technology, and public-sector targets.
- Validate sponsor language: Iran-aligned, MOIS-linked by some sources, and any conflicting or cautious source assessments.
- Focus on BiBi Wiper/BiBi-Linux, Moneybird, Apostle, DEADWOOD, BFG Agonizer, MultiLayer Wiper, ASPXSpy, IPsec Helper, NBTscan, Mimikatz, backup deletion, VSS deletion, data exfiltration, and hack-and-leak behavior.
- Produce detection logic for pre-destruction staging, mass file operations, backup tampering, webshell activity, credential access, and destructive-encryption preparation.

Special checks:
- Confirm Ziv Medical Center, Technion/DarkBit overlap, and any post-2023 activity with primary sources.
- Separate ransomware-style extortion cover from destructive intent.
- Mark operational claims from persona channels as unverified unless corroborated by primary reporting.
```

## CyberAv3ngers

Profile: [CyberAv3ngers](../actors/cyberav3ngers.md). Tool matrix: [CyberAv3ngers tools](../malware-tool-intelligence.md#cyberav3ngers).

Tags: [OT / ICS](#tag-ot-ics), [Critical Infrastructure](../navigation/surface-capability-matrix.md#ot-plc), [IOC / Tooling](../malware-tool-intelligence.md#cyberav3ngers), [Hunting](../navigation/actor-workbench.md#cyberav3ngers).

```text
Use the Common Research Contract.

Actor: CyberAv3ngers / Cyber Avengers / CyberAveng3rs / Storm-0784 / Bauxite / UNC5691 / Hydro Kitten / Shahid Kaveh Group / Soldiers of Solomon / Mr. Soul.

Research goals:
- Refresh 2023-2026 government and vendor reporting on IRGC-CEC OT/ICS targeting, especially Unitronics, Rockwell Automation, Allen-Bradley, water/wastewater, energy, and Israeli-linked equipment.
- Validate sponsor and organizational language from CISA, FBI, NSA, EPA, OFAC, INCD, Claroty, Dragos, and MITRE.
- Focus on IOControl, Unitronics Vision PLC/HMI exposure, Rockwell/Allen-Bradley exposure, HMI defacement, default credentials, exposed engineering interfaces, and public internet scanning.
- Produce OT-safe detection/hunting guidance with passive monitoring, asset inventory, exposed-interface identification, and escalation criteria.

Special checks:
- Do not include exploit instructions or device manipulation steps.
- For IOControl, summarize behavior, target device classes, C2 mechanism, source-published IOCs, and defensive implications only.
- Separate CyberAv3ngers from Cyber Toufan unless a source explicitly links them.
```

## Imperial Kitten

Profile: [Imperial Kitten](../actors/imperial-kitten.md). Tool matrix: [Imperial Kitten tools](../malware-tool-intelligence.md#imperial-kitten).

Tags: [Supplier / Third Party](#tag-supplier-third-party), [Identity / Cloud](#tag-identity-cloud), [Transportation / Logistics](../navigation/surface-capability-matrix.md), [IOC / Tooling](../malware-tool-intelligence.md#imperial-kitten).

```text
Use the Common Research Contract.

Actor: Imperial Kitten / Yellow Liderc / Tortoiseshell / Tortoise Shell / TA456 / CURIUM / Crimson Sandstorm.

Research goals:
- Refresh 2023-2026 reporting on Iranian logistics, transportation, maritime, technology, defense-adjacent, and Israeli or Israel-adjacent targeting.
- Validate current sponsor assessment: IRGC-aligned, MOIS, or unresolved branch; cite exact source language.
- Focus on IMAPLoader, StandardKeyboard, supply-chain phishing, strategic web compromise, legitimate email-account C2, and any reported Discord/RAT behavior.
- Produce hunt hypotheses for IMAP/IMAPS C2 from non-mail clients, high-frequency polling, encoded attachment retrieval, unusual mail access, and phishing-to-loader chains.

Special checks:
- Confirm CrowdStrike, PwC, Symantec/Broadcom, Microsoft, and MITRE alias usage.
- Identify every public source after November 2023 that mentions Israeli sectors or logistics targeting.
- Mark 2024-2026 Israel-specific activity as Gap if not primary-source confirmed.
```

## Pioneer Kitten

Profile: [Pioneer Kitten](../actors/pioneer-kitten.md). Tool matrix: [Pioneer Kitten tools](../malware-tool-intelligence.md#pioneer-kitten).

Tags: [Government / Public Sector](#tag-government-public-sector), [Financial / Extortion](#tag-financial-extortion), [Identity / Cloud](#tag-identity-cloud), [Supplier / Third Party](#tag-supplier-third-party), [IOC / Tooling](../malware-tool-intelligence.md#pioneer-kitten).

```text
Use the Common Research Contract.

Actor: Pioneer Kitten / Fox Kitten / Lemon Sandstorm / UNC757.

Research goals:
- Refresh reporting around CISA AA24-241A and later sources on Iranian initial-access brokerage, ransomware affiliate handoff, edge-appliance exploitation, and critical-infrastructure targeting.
- Focus on Citrix, F5, Ivanti, Palo Alto, Check Point Gateway, Fortinet, VPNs, exposed appliances, webshells, compromised credentials, and ransomware-affiliate handoff.
- Identify any Israeli, Middle East, or Israel-adjacent critical-infrastructure references.
- Produce detection/hunt ideas for edge compromise, anomalous VPN access, new webshells, credential use after appliance exploitation, and broker-to-ransomware handoff signs.

Special checks:
- Quote exactly what CISA says about Israeli critical infrastructure.
- Separate initial-access brokerage from the ransomware actor's later behavior.
- Avoid exploit details; focus on patching, exposure management, and telemetry.
```

## DarkBit

Profile: [DarkBit](../actors/darkbit.md). Tool matrix: [DarkBit tools](../malware-tool-intelligence.md#darkbit).

Tags: [Medical / Healthcare](#tag-medical-healthcare), [Financial / Extortion](#tag-financial-extortion), [Persona Claims](#tag-persona-claims), [IOC / Tooling](../malware-tool-intelligence.md#darkbit).

```text
Use the Common Research Contract.

Actor/persona: DarkBit.

Research goals:
- Refresh public reporting on the February 2023 Technion attack, ransom demand, messaging, data-theft claims, and any assessed Iran/MuddyWater/MERCURY/DEV-1084/Storm-1084 relationship.
- Determine whether DarkBit remained active after 2023 or should be treated as a time-bounded persona/operation.
- Focus on ransomware-style extortion, destructive intent indicators, data leak claims, VSS deletion, encryption staging, and persona messaging.
- Produce evidence register entries that separate confirmed intrusion facts from public claims.

Special checks:
- Do not quote leaked data or link to leak material.
- Mark victim-data claims as persona claims unless verified by primary defenders/government reporting.
- State whether DarkBit should stay as an actor page, persona entry, or watchlist item.
```

## Lyceum

Profile: [Lyceum](../actors/lyceum.md). Tool matrix: [Lyceum tools](../malware-tool-intelligence.md#lyceum).

Tags: [Telecom](#tag-telecom), [OT / ICS](#tag-ot-ics), [Energy](../navigation/surface-capability-matrix.md), [IOC / Tooling](../malware-tool-intelligence.md#lyceum).

```text
Use the Common Research Contract.

Actor: Lyceum / HEXANE / Spirlin.

Research goals:
- Refresh reporting on telecom, ISP, oil/gas, energy, and ICS-adjacent targeting in the Middle East and North Africa.
- Validate current sponsor assessment and relationship, if any, to OilRig, Siamesekitten, Pay2Kitten, or other Iran-nexus clusters.
- Focus on DanBot, Kevin, Shark, Milan, DnsSystem, PoshC2, BITSAdmin, Empire, Mimikatz, DNS C2, and discovery tooling.
- Determine relevance to Israeli telecom and energy suppliers with explicit evidence labels.

Special checks:
- Promote Israel-specific evidence only when primary or reliable vendor reporting supports it.
- Separate historical MENA telecom relevance from current Israeli public-sector priority.
- Produce hunt hypotheses for DNS C2, telecom admin hosts, credential dumping, and PowerShell/C2 framework use.
```

## Cotton Sandstorm

Profile: [Cotton Sandstorm](../actors/cotton-sandstorm.md). Tool matrix: [Cotton Sandstorm tools](../malware-tool-intelligence.md#cotton-sandstorm).

Tags: [Government / Public Sector](#tag-government-public-sector), [Financial / Extortion](#tag-financial-extortion), [Persona Claims](#tag-persona-claims), [IOC / Tooling](../malware-tool-intelligence.md#cotton-sandstorm).

```text
Use the Common Research Contract.

Actor: Cotton Sandstorm / Emennet Pasargad and any source-confirmed aliases.

Research goals:
- Refresh 2023-2026 reporting on influence operations, hack-and-leak, persona activity, election or public-sector targeting, and Israeli relevance.
- Validate sponsor, contractor, or IRGC-linked assessments with primary sources such as U.S. Treasury, DOJ, Microsoft, Meta, or government advisories.
- Focus on persona infrastructure, fake media, account compromise, public claims, and psychological-operation timing.
- Produce defensive guidance for persona-claim handling, evidence preservation, social media monitoring, and comms/legal escalation.

Special checks:
- Keep persona claims separate from verified intrusions.
- Do not include leaked content or amplify propaganda.
- Add persona-claims-register rows where appropriate.
```

## APT39

Profile: [APT39](../actors/apt39.md). Tool matrix: [APT39 tools](../malware-tool-intelligence.md#apt39).

Tags: [Government / Public Sector](#tag-government-public-sector), [Telecom](#tag-telecom), [Financial / Travel Data](#tag-financial-extortion), [IOC / Tooling](../malware-tool-intelligence.md#apt39).

```text
Use the Common Research Contract.

Actor: APT39 / Chafer / Remix Kitten / Rana-linked reporting.

Research goals:
- Refresh current operational status and any 2023-2026 public reporting on telecom, travel, PNR, IT, government, and Middle East targeting.
- Validate MOIS/Rana sponsor assessment using U.S. Treasury, DOJ, FBI, MITRE, and vendor sources.
- Focus on ASPXSpy, Remexi, MechaFlounder, Cadelspy, credential dumping, PsExec, CrackMapExec, webshells, and travel/telecom data targeting.
- Determine whether APT39 should be operational priority, watchlist, or legacy reference for Israeli public-sector defenders.

Special checks:
- Clearly label lack of recent public reporting as Gap if found.
- Separate older high-confidence attribution from recent activity evidence.
- Produce source-register and evidence-register updates even if the main finding is inactivity or no public data.
```

## APT-C-23 / Arid Viper

Profile: [APT-C-23 / Arid Viper](../actors/arid-viper.md). Tool matrix: [APT-C-23 tools](../malware-tool-intelligence.md#apt-c-23).

Tags: [Government / Public Sector](#tag-government-public-sector), [Identity / Cloud](#tag-identity-cloud), [Mobile / MDM](../navigation/actor-workbench.md#apt-c-23), [IOC / Tooling](../malware-tool-intelligence.md#apt-c-23).

```text
Use the Common Research Contract.

Actor: APT-C-23 / Arid Viper / Desert Falcon / Hamas-linked reporting.

Research goals:
- Refresh 2023-2026 reporting on Israeli military, law enforcement, reservist, government, and public-safety targeting.
- Validate sponsor language: Hamas-linked, Gaza-based, Palestinian-aligned, or unresolved.
- Focus on AridSpy, RedAlert.apk, FrozenCell, Desert Scorpion, Micropsia, Phenakite, SpyC23, mobile phishing, catfishing, fake alert apps, and Windows/mobile spyware.
- Produce separate ATT&CK Enterprise and Mobile mappings; do not force mobile behavior into Enterprise technique IDs.
- Generate mobile, MDM, endpoint, DNS, and identity hunt hypotheses for defensive monitoring.

Special checks:
- Do not include APK samples, code, or installation steps.
- Public hashes may be referenced only from source-published IOC appendices.
- Highlight app-store/source-of-install validation and mobile telemetry requirements.
```

## UNC3890

Profile: [UNC3890](../actors/unc3890.md). Tool matrix: [UNC3890 tools](../malware-tool-intelligence.md#unc3890).

Tags: [Government / Public Sector](#tag-government-public-sector), [Supplier / Third Party](#tag-supplier-third-party), [Transportation / Maritime](../navigation/actor-workbench.md#unc3890), [IOC / Tooling](../malware-tool-intelligence.md#unc3890).

```text
Use the Common Research Contract.

Actor: UNC3890.

Research goals:
- Refresh post-2022 public reporting and determine whether the cluster remains separately tracked, has merged with another actor, or lacks recent public evidence.
- Focus on Israeli shipping, maritime, logistics, government, defense-adjacent, and critical-infrastructure targeting.
- Validate tools, malware, credential-harvesting infrastructure, and victimology from Mandiant/Google and any later primary sources.
- Produce a clear recommendation: active profile, watchlist, alias merge candidate, or gap requiring further collection.

Special checks:
- Mark absence of recent reporting as Gap rather than inferring inactivity.
- Identify source-backed overlap with Imperial Kitten, OilRig, or other Iran-nexus clusters only if a source states it.
```

## Cyber Toufan

Profile: [Cyber Toufan](../actors/cyber-toufan.md). Tool matrix: [Cyber Toufan tools](../malware-tool-intelligence.md#cyber-toufan).

Tags: [Telecom](#tag-telecom), [OT / ICS](#tag-ot-ics), [Financial / Extortion](#tag-financial-extortion), [Supplier / Third Party](#tag-supplier-third-party), [Persona Claims](#tag-persona-claims), [IOC / Tooling](../malware-tool-intelligence.md#cyber-toufan).

```text
Use the Common Research Contract.

Actor/persona: Cyber Toufan.

Research goals:
- Refresh reporting on Israeli supplier, telecom, hosting, government-adjacent, and third-party service-provider compromise claims.
- Validate whether Cyber Toufan is best modeled as actor, persona, campaign, or claim-heavy public front.
- Focus on supplier access, leaked credential reuse, VPN/firewall administration, SMB/admin-share movement, POKYBLIGHT references, DDoS, recycled data leaks, and psychological operations.
- Produce persona-claim workflow updates and defensive supplier-risk guidance.

Special checks:
- Do not link to leaked data or repeat victim-sensitive details beyond public defensive reporting.
- Separate claimed compromise, third-party corroboration, and local telemetry match.
- Produce clear comms/legal escalation guidance for public claims.
```

## Void Manticore / Handala

Profile: [Void Manticore / Handala](../actors/handala.md). Tool matrix: [Void Manticore / Handala tools](../malware-tool-intelligence.md#void-manticore-handala).

Tags: [Government / Public Sector](#tag-government-public-sector), [Medical / Healthcare](#tag-medical-healthcare), [Financial / Extortion](#tag-financial-extortion), [Identity / Cloud](#tag-identity-cloud), [Persona Claims](#tag-persona-claims), [IOC / Tooling](../malware-tool-intelligence.md#void-manticore-handala).

```text
Use the Common Research Contract.

Actor/persona model: Void Manticore as the assessed cluster; Handala Hack, Homeland Justice, Karma, BANISHED KITTEN, Red Sandstorm, and related names as source-confirmed personas where supported.

Research goals:
- Refresh 2023-2026 reporting on destructive Israeli operations, hack-and-leak, wipers, credential abuse, public personas, and Scarred Manticore/UNC1860 access handoff.
- Validate MOIS assessment and persona relationships using MITRE, Check Point, Mandiant, government, and law-enforcement sources.
- Focus on BiBi lineage where relevant, CHIMNEYSWEEP, ROADSWEEP, RawDisk, ZeroCleare, Impacket, Mimikatz, NetBird, VSS/backup deletion, Intune/identity-plane destructive actions, and public claim channels.
- Produce detections for identity-plane destruction, backup deletion, mass file operations, hack-and-leak staging, and persona-claim verification.

Special checks:
- Separate cluster behavior from persona messaging.
- Treat public victim claims as unverified unless corroborated.
- Do not include leaked content or operational details that enable harm.
```

## Lebanese Cedar

Profile: [Lebanese Cedar](../actors/lebanese-cedar.md). Tool matrix: [Lebanese Cedar tools](../malware-tool-intelligence.md#lebanese-cedar).

Tags: [Medical / Healthcare](#tag-medical-healthcare), [Telecom](#tag-telecom), [Government / Public Sector](#tag-government-public-sector), [IOC / Tooling](../malware-tool-intelligence.md#lebanese-cedar).

```text
Use the Common Research Contract.

Actor: Lebanese Cedar / Volatile Cedar and source-confirmed Hezbollah-linked cyber reporting.

Research goals:
- Refresh 2023-2026 reporting on Hezbollah-linked cyber activity, Lebanese Cedar continuity, and any joint activity with Iran-linked actors against Israeli healthcare, telecom, public-sector, or critical infrastructure.
- Validate whether older Caterpillar WebShell and Explosive RAT reporting remains the best primary source.
- Focus on Ziv Medical Center claims, Agrius/Lebanese Cedar cooperation, webshells, RATs, edge exploitation, data theft, and hack-and-leak amplification.
- Produce a recommendation on whether this profile should be current-priority, watchlist, or historical context.

Special checks:
- Separate Hezbollah cyber-unit reporting from Lebanese Cedar-specific tooling unless source-confirmed.
- Mark lack of specialized 2023-2026 Lebanese Cedar reporting as Gap if appropriate.
```

## WIRTE

Profile: [WIRTE](../actors/wirte.md). Tool matrix: [WIRTE tools](../malware-tool-intelligence.md#wirte).

Tags: [Government / Public Sector](#tag-government-public-sector), [Identity / Cloud](#tag-identity-cloud), [Persona Claims](#tag-persona-claims), [IOC / Tooling](../malware-tool-intelligence.md#wirte).

```text
Use the Common Research Contract.

Actor: WIRTE / Molerats overlap / Gaza Cybergang-related reporting where source-confirmed.

Research goals:
- Refresh 2023-2026 reporting on Middle East government targeting, Israeli disruption, Hamas-linked or Gaza-linked assessments, and overlap with TA402.
- Focus on IronWind, SameCoin, AshTag if source-confirmed, reflective loading, geofencing, Rclone exfiltration, phishing, and regional government targeting.
- Produce ATT&CK mappings, tool-intelligence rows, and hunt hypotheses for phishing, loader chains, cloud storage abuse, geofencing, and data exfiltration.

Special checks:
- Keep WIRTE and TA402 separate when sources distinguish them.
- Avoid assigning Hamas affiliation unless the source makes that assessment.
- Mark AshTag or newer claims as Gap if no primary source is found.
```

## TA402

Profile: [TA402](../actors/ta402.md). Tool matrix: [TA402 tools](../malware-tool-intelligence.md#ta402).

Tags: [Government / Public Sector](#tag-government-public-sector), [Identity / Cloud](#tag-identity-cloud), [IOC / Tooling](../malware-tool-intelligence.md#ta402), [Hunting](../navigation/actor-workbench.md#ta402).

```text
Use the Common Research Contract.

Actor: TA402 / Molerats / Gaza Cybergang-related reporting where source-confirmed.

Research goals:
- Refresh 2023-2026 Proofpoint, SentinelOne, ESET, and other vendor reporting on phishing and espionage against Middle East governments and Israel-adjacent targets.
- Focus on IronWind infection chains, PPAM/XLL/RAR delivery, cloud links, actor-controlled C2, Arabic-language and regional targeting, and overlap with WIRTE.
- Produce mail, endpoint, and network hunt hypotheses for attachment chains, archive execution, sideloading, and command-and-control.

Special checks:
- Separate TA402 from WIRTE if the source does not merge them.
- Identify any Israeli government/public-sector relevance and mark gaps honestly.
```

## UNC1860

Profile: [UNC1860](../actors/unc1860.md). Tool matrix: [UNC1860 tools](../malware-tool-intelligence.md#unc1860).

Tags: [Government / Public Sector](#tag-government-public-sector), [Telecom](#tag-telecom), [OT / ICS](#tag-ot-ics), [Supplier / Third Party](#tag-supplier-third-party), [IOC / Tooling](../malware-tool-intelligence.md#unc1860).

```text
Use the Common Research Contract.

Actor: UNC1860. Do not treat "Temple of Oats" as an alias; it is a report title unless a source explicitly says otherwise.

Research goals:
- Refresh reporting on UNC1860 as an Iranian persistent access / initial access / passive backdoor cluster in Middle Eastern networks.
- Validate sponsor language and relationship to MOIS, Scarred Manticore, Void Manticore, ShroudedSnooper, or other clusters.
- Focus on TEMPLEDOOR, TEMPLEPLAY, TEMPLEDROP, TEMPLELOCK, CRYPTOSLAY, PipeSnoop, STAYSHANTE, SASHEYAWAY, VIROGREEN, passive/listener implants, SharePoint exploitation references, webshells, and RDP proxying.
- Produce detection ideas for edge servers, IIS/SharePoint/Exchange paths, passive backdoors, inbound-controlled implants, webserver-to-internal RDP, and file-integrity deviations.

Special checks:
- Quote Mandiant caveats around handoff operations and uncertainty.
- List hashes only when published by source; otherwise provide source appendix pointers.
- Do not use UNC1860 as a default attribution label for every Iran-linked webshell.
```

## Scarred Manticore

Profile: [Scarred Manticore](../actors/scarred-manticore.md). Tool matrix: [Scarred Manticore tools](../malware-tool-intelligence.md#scarred-manticore).

Tags: [Government / Public Sector](#tag-government-public-sector), [Telecom](#tag-telecom), [Supplier / Third Party](#tag-supplier-third-party), [IOC / Tooling](../malware-tool-intelligence.md#scarred-manticore), [Hunting](../navigation/actor-workbench.md#scarred-manticore).

```text
Use the Common Research Contract.

Actor: Scarred Manticore and source-confirmed overlaps with ShroudedSnooper, UNC1860, Storm-0861, or MOIS-linked reporting.

Research goals:
- Refresh 2023-2026 reporting on Israeli government, telecom, local government, academia, and critical-infrastructure access operations.
- Validate the Scarred Manticore to Void Manticore handoff model and where sources state uncertainty.
- Focus on Liontail, IIS native modules, HTTP.sys or passive web backdoors, webshells, MOIS-linked access operations, and handoff to destructive actors.
- Produce detection logic for IIS native module integrity, appcmd/module registration, web root changes, worker-process anomalies, suspicious inbound-controlled HTTP patterns, and edge-to-internal movement.

Special checks:
- Do not conflate generic phantom-DLL hijacking with Liontail unless source-backed.
- Identify Windows/IIS logs, Sysmon fields, EDR fields, and expected false positives.
- Mark detection confidence separately from attribution confidence.
```

## Researcher Follow-Up Prompt

Use this after any actor response to harden the output.

```text
Review your prior answer for evidence quality.

For every source URL:
1. Confirm whether it returned HTTP 200 or state the access result.
2. Confirm the cited content supports the claim.
3. Identify whether the source is primary, secondary, or watchlist/context.
4. Identify any claims that should be downgraded to Gap, Inferred, or Assessed-here.
5. Produce corrected sources.csv, evidence-register.csv, tool-intelligence.csv, ttps.csv, and persona-claims-register.csv candidate rows.
6. List any actor-page, tool-page, detection, hunt, or navigation crosslinks that should be added.
```
