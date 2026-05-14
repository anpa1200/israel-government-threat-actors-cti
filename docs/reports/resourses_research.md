---
title: Resources Research
sidebar_label: Resources Research
---

# Israel Government Threat Actors CTI: Evidentiary Foundation Intake

TLP: TLP:CLEAR.

This file captures the supplied research-intake material and the follow-on source
collection pass performed on 2026-05-14. The filename intentionally preserves the
requested spelling: `resourses_research.md`.

## Analytic Handling

The supplied research text is useful as a collection map, but it mixes primary
reporting, secondary synthesis, unverified future-event claims, and several actor
taxonomy shortcuts. Treat it as an intake artifact, not as validated repository
truth.

Key handling rules:

- Do not promote any claim from this file into actor profiles without a live
  primary source or an explicit `Gap` label.
- Keep source strength separate from claim strength. A valid source URL does not
  automatically validate every claim in the intake text.
- Preserve actor taxonomy boundaries. MuddyWater is not APT33; CyberAv3ngers and
  Cyber Toufan are distinct tracked personas/clusters; UNC1860, ShroudedSnooper,
  and Scarred Manticore should not be treated as universal aliases without a
  source-specific caveat.
- Use ATT&CK for ICS for PLC/HMI techniques where appropriate; do not map OT
  effects only to Enterprise ATT&CK.
- Do not store malware samples or offensive tooling. The download pass collected
  public reports and web pages only.

## High-Value Intake Themes

### Handala / Void Manticore / Storm-0842 / Banished Kitten

The intake emphasizes identity-plane destruction, hack-and-leak messaging, NetBird
tunneling, wiper tradecraft, and claimed convergence with MOIS personas such as
Karma and Homeland Justice.

Validation status:

- Check Point's 2026 Handala report, Check Point's MOIS-crime report, and the
  Push Security Stryker/Handala report were downloaded successfully.
- The claimed DOJ/FBI seizure affidavit `1:26-mj-00683-CDA` was not located in
  the quick public search and remains a collection gap.
- The claimed INCD Storm-0842/Handala advisory had no accessible URL in the quick
  search and remains a collection gap.

Defensive value:

- Prioritize Entra ID, Intune, PIM, backup-control, and cloud-admin telemetry.
- Treat destructive operations as potentially identity-native, not only
  endpoint-malware-native.

### UNC1860 / ShroudedSnooper / Scarred Manticore

The intake links UNC1860-style passive access, ShroudedSnooper-style passive
backdoors, and Scarred Manticore/Liontail IIS-adjacent tradecraft.

Validation status:

- Mandiant/Google Cloud UNC1860 reporting downloaded successfully.
- Trellix's 2026 Iranian Cyber Capability page was reachable in search results
  but timed out during local download.
- CISA AA23-335A downloaded, but it primarily anchors CyberAv3ngers/Unitronics
  PLC activity; do not use it as a direct UNC1860/ShroudedSnooper source unless
  a specific overlap is cited by a primary publisher.

Defensive value:

- Preserve separate hunts for webshell/post-exploitation, passive backdoors,
  IIS/native module integrity, and long-lived access-provider behavior.

### MuddyWater / Boggy Serpens / Mango Sandstorm / Seedworm

The intake highlights MuddyWater's continuing Israeli and regional relevance,
including RMM-themed delivery, custom loaders, SOCKS5/proxying, and cloud-service
abuse.

Validation status:

- ESET "Snakes by the Riverbank", INCD MuddyWater 2024, Kaspersky ICS Q4 2025,
  MITRE G0069, and Brandefense MuddyWater 2025 were downloaded successfully.
- Brandefense is useful supporting context, but it is not a replacement for
  primary vendor/government technical reporting.

Defensive value:

- Hunt for suspicious RMM delivery, LOTS/legitimate cloud service staging,
  SOCKS/proxy infrastructure, and credential collection from trusted mail paths.

### OilRig / APT34 / Helix Kitten / Crambus

The intake emphasizes cloud-service-powered C2, Microsoft Graph/OneDrive/Outlook
abuse, and long-term Israeli targeting.

Validation status:

- ESET's OilRig cloud-service-powered downloader reporting, Kaspersky ICS H2
  2023, and Brandefense OilRig 2025 were downloaded successfully.
- The named NJCCIC "Iran Cyber Threat Operations: APT34" item was not located in
  the quick public search and remains a collection gap.

Defensive value:

- Prioritize Microsoft Graph, EWS, Outlook, OneDrive, OAuth application, and
  suspicious cloud API behavior by nonstandard processes.

### APT42 / Mint Sandstorm / Phosphorus / Charming Kitten

The intake focuses on high-touch social engineering, cloud account compromise,
and adversary-in-the-middle credential phishing.

Validation status:

- Proofpoint's March 2026 Iran-conflict espionage report, Mandiant/Google Cloud
  APT42 analysis, and Microsoft Mint Sandstorm reporting downloaded successfully.
- Claims about operations during domestic internet blackouts should remain
  source-bound and not generalized without primary support.

Defensive value:

- Prioritize VIP-targeted phishing, AitM credential theft, suspicious MFA method
  registration, OAuth consent, and cloud mailbox access detections.

### Agrius / Pink Sandstorm / Agonizing Serpens / BlackShadow

The intake frames Agrius as a destructive actor affecting Israeli healthcare,
higher education, and technology sectors.

Validation status:

- Unit 42 Agonizing Serpens, Centripetal AI pre-positioned-access analysis,
  Israel Hayom Ziv Hospital coverage, and Anvilogic Iran critical-infrastructure
  reporting downloaded successfully.
- Ziv Hospital attribution should be anchored to INCD/IDF/ISA where a primary
  government page is available; Israel Hayom/Times of Israel are useful
  secondary coverage.
- Claims about camera compromise for bomb damage assessment require careful
  validation before promotion to a high-confidence profile claim.

Defensive value:

- Hunt for webshell access, backup deletion, high-volume file operations,
  ransomware-style wipers, data theft, and public leak amplification.

### CyberAv3ngers / Cyber Toufan

The intake combines IRGC-CEC OT/ICS targeting with Cyber Toufan supplier and
hack-and-leak activity.

Validation status:

- CISA AA26-097A, CISA AA23-335A, Sophos search-result source, and OP Innovate
  Cyber Toufan reporting were identified. AA26/AA23 and OP Innovate downloaded.
- Sophos timed out during local download, despite a live search result.
- The named Netizen POKYBLIGHT bulletin was not located in the quick public
  search and remains a collection gap.

Defensive value:

- Separate OT exposure management from hack-and-leak persona tracking.
- Monitor internet-exposed PLC/HMI, engineering workstations, VPN/firewall
  infrastructure, leaked credentials, and supplier-admin paths.

### Arid Viper / APT-C-23 / Desert Falcon

The intake highlights mobile espionage, trojanized emergency-alert apps, and
social engineering against Israeli users.

Validation status:

- ESET AridSpy and SentinelOne Israel-Hamas cyber-domain reporting downloaded.
- Acronis TRU was identified through secondary coverage, but a primary Acronis
  report URL was not located in the quick public search.
- Cybernews/Acronis coverage downloaded as secondary reporting.

Defensive value:

- Enforce mobile-device management, prohibit sideloading, detect suspicious APK
  installation paths, and train high-risk users on smishing/catfishing lures.

### WIRTE / TA402 / Molerats / Ashen Lepus

The intake emphasizes IronWind, SameCoin, AshTag, phishing, DLL side-loading, and
cloud or legitimate service abuse.

Validation status:

- Unit 42 AshTag, Proofpoint TA402 IronWind, Check Point WIRTE disruptive
  activity, and SentinelOne Gaza Cybergang context downloaded successfully.

Defensive value:

- Hunt for archive/Office lure execution, XLL/PPAM chains, DLL side-loading,
  geofenced delivery, Rclone usage, and unusual cloud staging.

### Lebanese Cedar / Volatile Cedar

The intake emphasizes older Lebanese Cedar/Volatile Cedar web compromise and the
reported Ziv Hospital joint operation context.

Validation status:

- Kaspersky's mirror of the Check Point Volatile Cedar PDF downloaded
  successfully.
- ClearSky's Lebanese Cedar page/PDF returned a WAF placeholder in local download,
  not a usable report.
- Times of Israel Ziv Hospital coverage downloaded as secondary reporting.

Defensive value:

- Use Lebanese Cedar as a regional supplier/web-compromise threat, but keep
  2023-2026 Israel-specific updates source-bound.

## Download Results

Files were downloaded to `research-downloads/2026-05-14/`. That directory is
ignored by Git and is intended for local analyst review only.

The repository now keeps a committed manifest at `data/research-downloads.csv`.
That manifest records the canonical URL, download status, local ignored archive
path, content type, byte size, and SHA-256 hash for each candidate source. This
preserves provenance without redistributing full third-party reports.

## Full-Text Handling

Full vendor and media reports SHOULD NOT be committed into the published docs
unless the publisher clearly permits redistribution. The safer repository
pattern is:

1. Commit the source URL, reliability score, claim-level notes, and download
   manifest.
2. Keep raw HTML/PDF downloads under ignored `research-downloads/`.
3. Convert local copies only for analyst review and search.
4. Promote only short summaries, citations, and defensive implications into
   actor profiles or detection notes.

Local conversion was run with:

```bash
python3 scripts/convert_research_downloads.py
```

Converted text files were written to
`research-downloads/converted/2026-05-14/`. They remain ignored by Git for the
same redistribution reason.

## Source Promotion And Scoring Decisions

The downloaded sources were cross-linked into `data/sources.csv` and
`data/research-downloads.csv`. Source IDs in the manifest let analysts move from
an actor profile, to the source register, to the local ignored archive without
publishing full third-party text.

| Promotion | Source IDs | Use |
| --- | --- | --- |
| Score A primary | `SRC-PROOFPOINT-IRAN-CONFLICT-2026`, `SRC-UNIT42-ASHTAG-2025` | Can support actor profiles, ATT&CK mappings, malware references, and detection hypotheses after claim-level review. |
| Score B supporting | `SRC-KASPERSKY-ICS-Q4-2025`, `SRC-KASPERSKY-ICS-H2-2023`, `SRC-BRANDEFENSE-MUDDYWATER-2025`, `SRC-BRANDEFENSE-OILRIG-2025`, `SRC-CENTRIPETAL-PREPOSITIONED-2025`, `SRC-ANVILOGIC-IRAN-CI-2026`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`, `SRC-CYBERNEWS-REDALERT-2026`, `SRC-ISRAELHAYOM-ZIV-2023`, `SRC-TOI-ZIV-2023`, `SRC-CP-VOLATILE-CEDAR-2015` | Use for context, collection requirements, corroboration, and source discovery. Do not use alone for high-impact attribution or blocking. |
| Not promoted | BeyondTrust, Trellix, Sophos, DOJ/FBI affidavit, INCD Handala advisory, NJCCIC APT34, Netizen POKYBLIGHT, Acronis TRU RedAlert primary | Keep as collection requirements until a usable source URL or local copy is obtained. |

Repository integration performed from this intake:

- Added AshTag and RedAlert.apk to `data/malware-references.csv`.
- Added Unit 42 AshTag and selected conflict-compendium references to
  `data/ioc-references.csv`.
- Added WIRTE/AshTag ATT&CK mappings for staged tool transfer and cloud
  exfiltration.
- Replaced the Arid Viper mobile mapping with a mobile ATT&CK phishing mapping
  instead of the prior Enterprise technique ID.
- Cross-linked MuddyWater, OilRig, APT42, Agrius, Arid Viper, WIRTE, TA402,
  Lebanese Cedar, and Handala actor pages to the newly scored sources.

| Actor / Topic | Publisher | Report / Source | Status | Local file or reason |
| --- | --- | --- | --- | --- |
| Handala / Void Manticore | Check Point Research | Handala Hack - Unveiling Group Modus Operandi | Downloaded | `research-downloads/2026-05-14/01-check-point-research-handala-hack-unveiling-group-modus-operandi.html` |
| Handala / Void Manticore | Push Security | Stryker Handala Report | Downloaded | `research-downloads/2026-05-14/02-push-security-stryker-handala-report.html` |
| Handala / Void Manticore | Check Point Research | Iranian MOIS Actors and the Cyber Crime Connection | Downloaded | `research-downloads/2026-05-14/03-check-point-research-iranian-mois-actors-and-the-cyber-crime-connection.html` |
| Handala / Void Manticore | BeyondTrust | Threat Advisory Operation Epic Fury | Failed | HTTP 403 during download; URL found in search: `https://www.beyondtrust.com/blog/entry/threat-advisory-operation-epic-fury` |
| Handala / Void Manticore | DOJ / FBI | Case `1:26-mj-00683-CDA` affidavit | Not found | No public URL identified in quick search. |
| Handala / Void Manticore | INCD | Storm-0842 / Handala advisory | Not found | No public URL identified in quick search. |
| UNC1860 / Scarred Manticore | Trellix | The Iranian Cyber Capability 2026 | Failed | Read timeout during local download; URL found in search: `https://www.trellix.com/blogs/research/the-iranian-cyber-capability-2026/` |
| UNC1860 / Scarred Manticore | Mandiant / Google Cloud | UNC1860 and the Temple of Oats | Downloaded | `research-downloads/2026-05-14/08-mandiant-google-cloud-unc1860-and-the-temple-of-oats.html` |
| CyberAv3ngers / OT | CISA / partners | AA23-335A IRGC-affiliated actors exploit PLCs | Downloaded | `research-downloads/2026-05-14/09-cisa-fbi-nsa-epa-incd-irgc-affiliated-cyber-actors-exploit-plcs-aa23-335a.html` |
| MuddyWater | Kaspersky ICS CERT | APT and financial attacks on industrial organizations in Q4 2025 | Downloaded | `research-downloads/2026-05-14/10-kaspersky-ics-cert-apt-and-financial-attacks-on-industrial-organizations-in-q4-2025.html` |
| MuddyWater | ESET | Snakes by the Riverbank | Downloaded | `research-downloads/2026-05-14/11-eset-muddywater-snakes-by-the-riverbank.html` |
| MuddyWater | INCD | Technological Advancement and Evolution of MuddyWater in 2024 | Downloaded | `research-downloads/2026-05-14/12-incd-technological-advancement-and-evolution-of-muddywater-in-2024.pdf` |
| MuddyWater | Brandefense | MuddyWater APT 2025 | Downloaded | `research-downloads/2026-05-14/13-brandefense-muddywater-apt-2025.html` |
| MuddyWater | MITRE ATT&CK | MuddyWater G0069 | Downloaded | `research-downloads/2026-05-14/14-mitre-att-ck-muddywater-g0069.html` |
| OilRig | Kaspersky ICS CERT | APT and financial attacks on industrial organizations in H2 2023 | Downloaded | `research-downloads/2026-05-14/15-kaspersky-ics-cert-apt-and-financial-attacks-on-industrial-organizations-in-h2-2023.html` |
| OilRig | ESET | OilRig cloud service-powered downloaders | Downloaded | `research-downloads/2026-05-14/16-eset-oilrig-cloud-service-powered-downloaders.html` |
| OilRig | Brandefense | OilRig APT 2025 | Downloaded | `research-downloads/2026-05-14/17-brandefense-oilrig-apt-2025.html` |
| OilRig | NJCCIC | Iran Cyber Threat Operations: APT34 | Not found | No public URL identified in quick search. |
| APT42 | Proofpoint | Iran conflict drives heightened espionage activity | Downloaded | `research-downloads/2026-05-14/19-proofpoint-iran-conflict-drives-heightened-espionage-activity.html` |
| APT42 | Mandiant / Google Cloud | Uncharmed: Untangling Iran APT42 Operations | Downloaded | `research-downloads/2026-05-14/20-mandiant-google-cloud-uncharmed-untangling-iran-apt42-operations.html` |
| APT42 | Microsoft | Mint Sandstorm refines tradecraft | Downloaded | `research-downloads/2026-05-14/21-microsoft-mint-sandstorm-refines-tradecraft.html` |
| APT42 | Microsoft | Mint Sandstorm profile | Downloaded | `research-downloads/2026-05-14/22-microsoft-mint-sandstorm-profile.html` |
| Agrius | Unit 42 | Agonizing Serpens targets Israeli higher education and tech sectors | Downloaded | `research-downloads/2026-05-14/23-unit-42-agonizing-serpens-targets-israeli-higher-education-and-tech-sectors.html` |
| Agrius / Israel healthcare | Centripetal AI | Pre-positioned Access Cyber Threat Iran Conflict | Downloaded | `research-downloads/2026-05-14/24-centripetal-ai-pre-positioned-access-cyber-threat-iran-conflict.html` |
| Agrius / Lebanese Cedar | Israel Hayom | Iran Hezbollah behind Ziv Hospital cyber attack | Downloaded | `research-downloads/2026-05-14/25-israel-hayom-iran-hezbollah-behind-ziv-hospital-cyber-attack.html` |
| Agrius / Iran CI risk | Anvilogic | Iranian Cyber Threats Target U.S. Critical Infrastructure | Downloaded | `research-downloads/2026-05-14/26-anvilogic-iranian-cyber-threats-target-u-s-critical-infrastructure.html` |
| CyberAv3ngers / OT | CISA / partners | AA26-097A PLC exploitation | Downloaded | `research-downloads/2026-05-14/27-cisa-fbi-nsa-epa-doe-uscybercom-aa26-097a-plc-exploitation.html` |
| CyberAv3ngers / Cyber Toufan | Sophos | Increased Cyber Risk Amid U.S.-Israel-Iran Escalation | Failed | Read timeout during local download; URL found in search. |
| Cyber Toufan | OP Innovate | Cyber Toufan Attack Playbook | Downloaded | `research-downloads/2026-05-14/29-op-innovate-cyber-toufan-attack-playbook.html` |
| Cyber Toufan | Netizen | POKYBLIGHT wiper bulletin | Not found | No public URL identified in quick search. |
| Arid Viper | Acronis TRU | Red Alert spyware primary report | Not found | No primary Acronis URL identified in quick search. |
| Arid Viper | Cybernews / Acronis coverage | Israelis download malicious RedAlert app | Downloaded | `research-downloads/2026-05-14/32-cybernews-acronis-coverage-israelis-download-malicious-redalert-app.html` |
| Arid Viper | ESET | Arid Viper poisons Android apps with AridSpy | Downloaded | `research-downloads/2026-05-14/33-eset-arid-viper-poisons-android-apps-with-aridspy.html` |
| Arid Viper | SentinelOne | Israel-Hamas War Cyber Domain Activity of Interest | Downloaded | `research-downloads/2026-05-14/34-sentinelone-israel-hamas-war-cyber-domain-activity-of-interest.html` |
| WIRTE / TA402 | Unit 42 | Ashen Lepus uses new AshTag malware suite | Downloaded | `research-downloads/2026-05-14/35-unit-42-ashen-lepus-uses-new-ashtag-malware-suite.html` |
| WIRTE / TA402 | Proofpoint | TA402 uses complex IronWind infection chains | Downloaded | `research-downloads/2026-05-14/36-proofpoint-ta402-uses-complex-ironwind-infection-chains.html` |
| WIRTE | Check Point | Hamas-affiliated threat actor expands to disruptive activity | Downloaded | `research-downloads/2026-05-14/37-check-point-hamas-affiliated-threat-actor-expands-to-disruptive-activity.html` |
| WIRTE / Gaza Cybergang | SentinelOne | Israel-Hamas War Cyber Domain Activity of Interest | Downloaded | `research-downloads/2026-05-14/38-sentinelone-israel-hamas-war-cyber-domain-activity-of-interest.html` |
| Lebanese Cedar | ClearSky | Lebanese Cedar APT | Failed | Returned WAF placeholder HTML, not a usable report. |
| Lebanese Cedar / Volatile Cedar | Check Point via Kaspersky mirror | Volatile Cedar technical report PDF | Downloaded | `research-downloads/2026-05-14/40-kaspersky-volatile-cedar-technical-report.pdf` |
| Lebanese Cedar / Ziv Hospital | Times of Israel | Israel says Iran Hezbollah behind failed Ziv Hospital hack | Downloaded | `research-downloads/2026-05-14/41-times-of-israel-israel-says-iran-hezbollah-behind-failed-ziv-hospital-hack.html` |

## Download Summary

| Result | Count | Notes |
| --- | ---: | --- |
| Successfully downloaded usable public reports/pages | 32 | 31 direct downloads plus one supplemental Kaspersky-hosted mirror of the Check Point Volatile Cedar PDF. |
| Failed due to access control, timeout, or unusable placeholder | 5 | BeyondTrust 403, Trellix timeout, Sophos timeout, Check Point original Volatile Cedar 404, ClearSky WAF placeholder. |
| Not found in quick public search | 5 | DOJ/FBI affidavit, INCD Handala advisory, NJCCIC APT34 item, Netizen POKYBLIGHT item, Acronis primary RedAlert report. |

## Recommended Follow-Up

1. Re-query the five `Not found` items by exact title, publisher site search,
   and archive search before treating them as unavailable.
2. Retry Trellix and Sophos with a browser session or alternate network; both
   appear discoverable but failed local scripted download.
3. Replace secondary coverage with primary reporting wherever possible:
   especially Ziv Hospital, RedAlert.apk, BDA/IP-camera claims, POKYBLIGHT, and
   Operation Epic Fury situation reports.
4. Do not add the more dramatic intake claims to actor pages until each claim
   has a source row, evidence label, and confidence note.
