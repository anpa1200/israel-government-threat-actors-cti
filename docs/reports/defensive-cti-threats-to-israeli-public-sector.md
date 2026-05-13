# Defensive CTI Research on Threats to Israeli Government and Public-Sector Environments

Status: Research synthesis.

Handling: TLP:CLEAR. This report uses public sources and source IDs from `data/sources.csv`. Temporary citation markers from source research have been converted to repository source IDs.

## Executive Summary

FACT: Public reporting from 2024 through 2026 shows sustained Iran-nexus and Hamas- or Palestinian-aligned cyber activity focused on Israeli targets. Reporting emphasizes destructive operations, hack-and-leak activity, credential theft, targeted phishing, fake security updates, brand impersonation, and mobile espionage. Key source anchors include `SRC-CP-HANDALA-2026`, `SRC-MITRE-G1055`, `SRC-GOOGLE-APT42-PHISHING`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-CP-WEZRAT`, `SRC-CP-WIRTE-2024`, `SRC-ESET-ARIDSPY`, and `SRC-MANDIANT-MTRENDS-2025`.

ASSESSMENT: For Israeli government, municipal, critical infrastructure, telecom, defense-adjacent, and supplier environments, the highest-priority defensive concern is an ecosystem rather than a single actor. Iranian state-linked operators and personas blend espionage, access enablement, destructive activity, and information operations. The most operationally relevant clusters are Void Manticore / Handala, MuddyWater, APT42 / Mint Sandstorm, Agrius, CyberAv3ngers, Emennet Pasargad / Cotton Sandstorm, OilRig-adjacent clusters, WIRTE, and Arid Viper.

FACT: Current reporting also supports a second-tier watchlist of actors relevant to Israeli exposure: UNC3890, Lebanese Cedar / Volatile Cedar, TA402 / Molerats, and Cyber Toufan. These actors have either directly targeted Israeli sectors, targeted regional government ecosystems intersecting with Israeli interests, or used tactics directly portable into Israeli government and supplier environments.

ASSESSMENT: The most useful defensive framing is to organize collection and detections around five recurring risk patterns rather than actor names alone:

- Identity compromise and phishing.
- Malware-delivering fake installers and fake updates.
- Edge-system compromise and webshell persistence.
- Destructive or pseudo-ransomware impact operations.
- OT/ICS targeting of exposed management surfaces.

These patterns recur across the highest-priority actors and are more stable than public naming conventions.

## Actor Priority Table

| Priority | Actor / Persona | Assessed Sponsor Or Alignment | Why It Matters | Confidence | Key Sources |
| --- | --- | --- | --- | --- | --- |
| Critical | Void Manticore / Handala / Karma / Homeland Justice | MOIS-linked Iranian threat group in public reporting | Destructive and hack-and-leak activity against Israeli organizations; strong fit for municipal, public-sector, and supplier disruption risk. | High | `SRC-MITRE-G1055`, `SRC-CP-HANDALA-2026`, `SRC-CP-VOID-2024` |
| Critical | MuddyWater / Seedworm / Mango Sandstorm | MOIS-linked / MOIS subordinate in government and vendor reporting | Israel-specific INCD reporting, phishing waves, critical-infrastructure targeting, and government/telecom/supplier relevance. | High | `SRC-CISA-AA22-055A`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-ESET-MUDDYWATER-SNAKES` |
| Critical | APT42 / Mint Sandstorm / TA453 / Charming Kitten | IRGC-IO / Iran-sponsored in public reporting | Top identity and cloud-account risk for Israeli decision-makers, defense-linked users, NGOs, academics, and diplomats. | High | `SRC-GOOGLE-APT42-PHISHING`, `SRC-GOOGLE-APT42-UNCHARMED`, `SRC-MS-MINT-SANDSTORM` |
| High | Agrius / Pink Sandstorm / BlackShadow / Agonizing Serpens | Iran-linked / MOIS-linked in public reporting | Destructive and pseudo-ransomware operations against Israeli sectors, including healthcare, higher education, technology, and suppliers. | High | `SRC-MITRE-G1030`, `SRC-S1-AGRIUS-WIPER`, `SRC-UNIT42-AGRIUS`, `SRC-MS-IRAN-HAMAS` |
| High | CyberAv3ngers / Cyber Avengers | IRGC-affiliated persona/group | OT/ICS exposure threat, Israeli-made Unitronics targeting, and PLC/HMI disruption risk. | High | `SRC-CISA-AA23-335A`, `SRC-CISA-AA26-097A`, `SRC-MANDIANT-OT-HACKTIVISTS` |
| High | Emennet Pasargad / Cotton Sandstorm / Aria Sepehr Ayandehsazan | Iran-linked influence and intrusion actor/company | Fake INCD phishing, WezRat, and cyber-enabled influence operations against Israeli organizations. | High | `SRC-FBI-EMENNET-2024`, `SRC-CP-WEZRAT`, `SRC-MS-IRAN-IO` |
| High | OilRig / APT34 / Hazel Sandstorm ecosystem | Iran-linked espionage ecosystem | Government targeting, regional supply-chain exposure, webshells, passive backdoors, and potential access handoff activity. | Moderate-High | `SRC-MITRE-G0049`, `SRC-ESET-OILRIG-ISRAEL`, `SRC-CP-EDUCATED-2023` |
| High | APT-C-23 / Arid Viper / Desert Falcon | Hamas-linked or Palestinian-aligned in public reporting | Mobile espionage risk to field personnel, contractors, reservists, officials, and politically exposed users. | Moderate-High | `SRC-MITRE-G1028`, `SRC-ESET-ARIDSPY`, `SRC-META-ARIDVIPER` |
| High | WIRTE / Gaza Cybergang-linked cluster | Hamas-affiliated in Check Point reporting | Fake-update campaigns, compromised trusted senders, and disruptive SameCoin-linked activity against Israeli entities. | Moderate-High | `SRC-CP-WIRTE-2024` |
| Medium | TA402 / Molerats / Gaza Cybergang | Palestinian-aligned in public reporting | Trusted-account phishing and IronWind infection chains against Middle East government entities. | Moderate | `SRC-PROOFPOINT-TA402-IRONWIND` |
| Medium | UNC3890 | Suspected Iran-linked | Israeli shipping, logistics, healthcare, aviation, energy, and government targeting. | Moderate | `SRC-MANDIANT-UNC3890` |
| Watch | Lebanese Cedar / Volatile Cedar | Hezbollah-linked in public reporting | Webshell-centric regional espionage against government, telecom, and web estates; current Israel-specific urgency is lower. | Moderate | `SRC-CLEARSKY-LEBANESE-CEDAR` |
| Watch | Cyber Toufan | Pro-Palestinian / Iran-aligned persona in public reporting | Disruptive and psychological-operation persona; claims require corroboration before attribution. | Low-Moderate | `SRC-OPI-CYBER-TOUFAN`, `SRC-MANDIANT-MTRENDS-2025` |

## Source Register Summary

Use `data/sources.csv` for the full machine-readable register. This report adds or relies heavily on:

- `SRC-MITRE-G1055`: VOID MANTICORE MITRE ATT&CK profile.
- `SRC-INCD-MUDDYWATER-2024`: INCD MuddyWater 2024 evolution report.
- `SRC-INCD-MUDDYWATER-PHISHING`: INCD recent phishing report.
- `SRC-CISA-AA24-290A`: Iranian brute force and credential-access advisory.
- `SRC-CP-WEZRAT`: Check Point WezRat deep dive.
- `SRC-FBI-EMENNET-2024`: Joint Emennet Pasargad tradecraft advisory.
- `SRC-CP-WIRTE-2024`: Check Point WIRTE disruptive activity report.
- `SRC-PROOFPOINT-TA402-IRONWIND`: Proofpoint TA402 IronWind report.
- `SRC-MANDIANT-MTRENDS-2025`: Mandiant M-Trends 2025.
- `SRC-CP-BUGSLEEP`: Check Point BugSleep / MuddyWater report.

## Actor Profiles

### Void Manticore / Handala

FACT: MITRE and Check Point associate Void Manticore with MOIS-linked destructive activity and public-facing personas such as Handala, Karma, and Homeland Justice.

ASSESSMENT: The actor is a critical disruptive risk for public-sector environments where coercion and influence may matter more than monetization.

Detection ideas:

- Alert on mass file deletion, encryption-like behavior, or wipe-like activity after public-data exposure.
- Hunt for webshells and edge compromise preceding destructive actions.
- Correlate hack-and-leak claims with local telemetry before executive attribution.

### MuddyWater

FACT: INCD published Israel-specific MuddyWater reporting covering activity in the Israeli cyber domain and recent phishing campaigns.

ASSESSMENT: MuddyWater should be treated as a critical access, phishing, and persistence threat for government, telecom, NGOs, IT suppliers, academia, and critical infrastructure.

Detection ideas:

- Hebrew-localized phishing themes.
- Compromised organizational mailboxes sending high-volume links or attachments.
- PowerShell, WSF, Golang, and backdoor staging from user-writable paths.
- RMM, SOCKS, DNS tunneling, and suspicious C2 from systems that do not normally administer networks.

### APT42 / Mint Sandstorm / APT35-Adjacent Activity

FACT: Google reported intensified APT42 targeting of Israeli and U.S. high-value users in 2024, including Israeli military-, defense-, diplomatic-, academic-, and NGO-linked accounts.

ASSESSMENT: Israeli defenders should treat this as a VIP identity and cloud-account problem. Actor naming varies by vendor, but the defensive problem remains credential phishing, rapport-building, cloud-hosted lures, and account takeover.

Detection ideas:

- New OAuth grants after cloud-hosted lure clicks.
- DocSend, Google Sites, Drive, Dropbox, or fake media/interview lures aimed at VIP users.
- Risky sign-ins, token reuse, impossible travel, and MFA fatigue.

### Emennet Pasargad / Cotton Sandstorm

FACT: The joint FBI / U.S. Treasury / INCD advisory and Check Point WezRat reporting tie Emennet Pasargad / Cotton Sandstorm to fake security-alert phishing and Israeli-themed lures.

ASSESSMENT: Public-sector recipients are likely to trust urgent security notifications. Fake INCD notices and browser update themes should be prioritized in mail and endpoint detection.

Detection ideas:

- Security-patch or browser-update executables launched from email paths.
- Sender-domain similarity to INCD, CERT, vendors, and trusted Israeli entities.
- WezRat-like modular infostealer traffic following fake update execution.

### WIRTE / Gaza Cybergang-Linked Cluster

FACT: Check Point reported WIRTE expansion into disruptive activity and SameCoin-linked wiper activity against Israeli organizations.

ASSESSMENT: WIRTE adds a high-priority Palestinian-aligned disruptive track beyond mobile espionage.

Detection ideas:

- Trusted sender becomes bulk phisher.
- Signed installer or utility loads unsigned same-directory DLL from archive extraction paths.
- Fake ESET/Kaspersky/reseller update naming.
- Exfiltration followed by destructive activity.

### TA402 / Molerats

FACT: Proofpoint reported TA402 targeting Middle East government entities with IronWind infection chains using compromised ministry accounts, Dropbox, PPAM/XLL, and archived lures.

ASSESSMENT: Israeli and regional diplomatic ecosystems should monitor partner-account abuse and rare Office add-in execution.

Detection ideas:

- PPAM, XLL, or RAR execution from email or download paths.
- Dropbox or file-sharing downloads following war-themed or ministry-themed emails.
- Request-inspector/check-in style staging infrastructure.

### Arid Viper / APT-C-23

FACT: MITRE and ESET describe Arid Viper as a regional espionage actor with mobile spyware capability, including AridSpy campaigns.

ASSESSMENT: This is a personnel and mobile-device risk, not only a perimeter risk.

Detection ideas:

- Block Android sideloading for managed devices.
- Alert on messaging, civil-registry, job, or relationship-themed APKs outside official stores.
- Prioritize users in government, defense, law enforcement, and field liaison roles.

### OilRig Ecosystem

FACT: MITRE and ESET describe OilRig / APT34 as a long-running Iran-linked espionage actor, while Check Point and Mandiant reporting on related or adjacent clusters reinforces regional government targeting.

ASSESSMENT: Direct current Israel-specific reporting is less visible than MuddyWater or Agrius, but the ecosystem remains important because government, telecom, regional partners, suppliers, MSPs, and edge infrastructure are recurring targets.

Detection ideas:

- IIS module and file integrity monitoring.
- Webshell detection on public web infrastructure.
- DNS tunneling, email-based C2, and passive backdoor hunts.

## ATT&CK Mapping

| Technique | Why It Matters | Representative Actors | Telemetry |
| --- | --- | --- | --- |
| T1566 Phishing | Spearphishing and fake updates recur across the threat set. | MuddyWater, APT42, WIRTE, TA402, Emennet Pasargad | Email security, proxy, EDR, user reports |
| T1078 Valid Accounts | Legitimate accounts reduce detection friction. | MuddyWater, APT42, WIRTE, Cyber Toufan | IdP, MFA, mailbox, VPN |
| T1110 Brute Force | Password spraying and MFA push abuse remain broad Iranian patterns. | Iran-linked actors broadly | IdP, VPN, cloud audit logs |
| T1190 Exploit Public-Facing Application | Edge compromise enables webshells and handoff. | Agrius, Void Manticore, Volatile Cedar, OilRig | WAF, IIS, Exchange, SharePoint, EDR |
| T1505.003 Web Shell | Repeated in Iranian and regional activity. | Agrius, OilRig, Volatile Cedar, UNC1860-adjacent | Webroot file changes, process creation |
| T1059.001 PowerShell | Staging and post-exploitation. | MuddyWater, WIRTE, OilRig | ScriptBlockLogging, AMSI, EDR |
| T1574.001 DLL Search Order Hijacking | Fake installer and archive-delivered payloads. | WIRTE, TA402, UNC2428-style campaigns | DLL load telemetry, file creation |
| T1021.001 Remote Services: RDP | Common after edge compromise or credential access. | Agrius, Void Manticore-adjacent intrusions | Windows events, VPN, EDR |
| T1485 Data Destruction | Israeli entities are recurring wiper targets. | Handala, Agrius, WIRTE | EDR, file events, backup logs |

## Malware And Tool Reference

| Malware / Tool | Actor | Function | Detection Pivot |
| --- | --- | --- | --- |
| WezRat | Emennet Pasargad | Modular infostealer / RAT | Fake INCD security update chain. |
| BugSleep | MuddyWater | Backdoor | Recent MuddyWater campaign payload. |
| BlackBeard | MuddyWater | Backdoor | INCD-reported phishing follow-on payload. |
| IronWind | TA402 | Downloader / staged malware | PPAM/XLL/RAR delivery chain. |
| SameCoin | WIRTE | Wiper | Fake update and disruptive activity. |
| AridSpy | Arid Viper | Mobile RAT | Sideloaded APK with high-risk permissions. |
| SUGARUSH / SUGARDUMP | UNC3890 | Info stealer | Credential-harvest and shipping-sector investigations. |
| Explosive RAT / Caterpillar WebShell | Lebanese Cedar | RAT / webshell | JSP/ASPX file and webroot integrity monitoring. |

## IOC Starter Register

These values are defanged and non-exhaustive. Validate freshness before blocking.

| Indicator | Type | Association | Source |
| --- | --- | --- | --- |
| `alert@il-cert[.]net` | Email | Fake INCD / WezRat lure | `SRC-CP-WEZRAT` |
| `iqwebservice[.]com` | Domain | APT34-related Iraq campaign | `SRC-CP-EDUCATED-2023` / related Check Point reporting |
| `mofaiq[.]com` | Domain | APT34-related Iraq campaign | `SRC-CP-EDUCATED-2023` / related Check Point reporting |
| `theconomics[.]net` | Domain | TA402 / IronWind | `SRC-PROOFPOINT-TA402-IRONWIND` |
| `inclusive-economy[.]com` | Domain | TA402 / IronWind | `SRC-PROOFPOINT-TA402-IRONWIND` |
| `rafaelconnect[.]com` | Domain | UNC2428-style Rafael-themed deception reporting | `SRC-MANDIANT-MTRENDS-2025` |
| `RafaelConnect.exe` | Filename | Rafael-themed deception chain | `SRC-MANDIANT-MTRENDS-2025` |
| `MsDef.ese` | Filename | Rafael-themed deception chain | `SRC-MANDIANT-MTRENDS-2025` |

## Detection Engineering Opportunities

The common denominator is borrowed trust: trusted senders, brands, file-sharing services, admin utilities, web paths, and hardware-management interfaces. Detection should focus on use-context anomalies rather than only hashes.

Priority detections:

- Signed installer with malicious sibling DLL.
- Fake security update to infostealer.
- PowerShell plus drop in `C:\ProgramData\` masquerading as IT software.
- New webshell or IIS module under web application paths.
- Trusted sender suddenly becomes bulk phisher.
- Mail-to-click-to-exec correlation.
- Edge compromise to lateral movement.
- OT management anomalies.
- Sideloaded mobile applications with high-risk permissions.

## Implemented Detection Files

Additional Sigma rules:

- `signed-installer-sideload-from-user-path.yml`
- `fake-security-update-infostealer-execution.yml`
- `trusted-sender-bulk-phishing-anomaly.yml`

Additional KQL hunts:

- `mail-click-to-exec-correlation.kql`
- `trusted-sender-bulk-phishing-anomaly.kql`

## Intelligence Gaps

- Actor overlap and handoff remain unresolved. Public reporting suggests relationships among prior-access clusters, destructive personas, and espionage groups, but exact organizational boundaries are uncertain.
- Persona inflation remains a reporting risk. Handala, CyberAv3ngers, and Cyber Toufan may mix real intrusion activity with psychological amplification.
- Supplier and MSP visibility is insufficient. Third-party mailboxes, shared hosting, resellers, and municipal IT contractors can act as transitive exposure points.

## Recommended Collection Tasks

1. Build a crosswalk register mapping actor, persona, malware, IOC, ATT&CK technique, affected sector, and `verified intrusion` versus `public claim only`.
2. Build a Hebrew/Arabic/English phishing corpus covering urgent security patch, INCD notices, browser updates, ESET/reseller notifications, Rafael recruitment, procurement, municipal correspondence, and war-themed policy documents.
3. Inventory internet-exposed IIS, SharePoint, Exchange, VPN, and PLC/HMI surfaces across ministries, municipalities, education, healthcare, telecom, and strategic suppliers.
4. Run a mobile-risk review for officials, field personnel, defense-adjacent staff, and regional liaison roles.
5. Retro-hunt published infrastructure and filenames from source appendices, especially fake-INCD, TA402, APT34-adjacent, MuddyWater, and Rafael-themed deception indicators.

