---
title: Additional Gemini Research Intake
sidebar_label: Additional Gemini Research
---

# Cyber Threat Intelligence Dossier: Iranian and Hamas-Aligned Operations Targeting Israeli and Allied Ecosystems (2023-2026)

:::caution Analyst validation required
This page is an imported research-intake artifact. Treat it as a lead-generation and validation queue, not as authoritative repository assessment. Claims below must be checked against primary public sources before they are promoted into actor pages, evidence records, source records, detection logic, or tool-intelligence rows.
:::

## 1. Executive Summary For Israeli Public-Sector Defenders

The cyber threat landscape directed against Israeli government, public-sector, municipal, telecommunications, critical infrastructure, and defense-adjacent environments has undergone a profound strategic and tactical evolution between 2023 and 2026. Analysis of primary intelligence reporting from this period reveals a transition from opportunistic, bespoke malware deployments toward highly integrated, hybrid warfare models. These models are characterized by identity weaponization, formalized access-broker handoffs, psychological operations (PSYOPS), and direct cyber-kinetic synchronization.

It is Assessed-here that the overarching strategic intent of Iranian Ministry of Intelligence and Security (MOIS), Islamic Revolutionary Guard Corps (IRGC), and Hamas-aligned cyber operations has shifted toward a "triple-threat" model. While historical campaigns prioritized long-term strategic espionage and custom-compiled disruptive wipers, current operations heavily emphasize living-off-the-land (LotL) techniques targeting the enterprise management plane, paired with deniable destructive hacktivism.

There is also reported integration of cyber operations into conventional kinetic warfare, including targeting regional IP cameras to facilitate real-time battle damage assessments (BDA) surrounding missile operations.

Three primary evolutionary trends demand immediate defensive recalibration by Israeli public-sector and critical-infrastructure organizations:

1. The threat ecosystem has formalized a state-sponsored access-broker economy. Threat clusters are increasingly specialized and compartmentalized. It is Assessed-by-source that groups such as UNC1860 function primarily as initial access and persistent foothold brokers. These groups use passive, inbound-listening backdoors to secure environments before handoffs to visible destructive personas such as Void Manticore / Handala or Cyber Toufan. Similarly, MuddyWater has been observed functioning as an initial access broker for Lyceum, facilitating deeper intrusion into Israeli manufacturing sectors. This segmentation complicates attribution and reduces the time to impact once a destructive team inherits access.
2. Identity weaponization and administrative abuse are superseding traditional compiled malware. Destructive operations are increasingly bypassing conventional EDR telemetry by pivoting away from deployable wipers. Actors operating under personas such as Void Manticore reportedly compromise highly privileged identities to issue authorized remote-wipe and factory-reset commands through cloud-based MDM and RMM consoles. Because these commands originate from trusted vendor infrastructure, they can evade traditional file-integrity and heuristic monitoring.
3. Malware developers are employing geographic and environmental geofencing to ensure localized execution. Tools such as WIRTE's SameCoin wiper reportedly generate cryptographic XOR keys by parsing live HTTP responses from Israeli infrastructure such as the Israel Home Front Command. This can prevent sandbox detonation outside the target environment and ensure payload execution within intended geopolitical boundaries.

Defenders should pivot from legacy file-integrity and perimeter-centric monitoring toward identity-plane telemetry, passive-backdoor detection, strict auditing of remote administrative tooling, and resilience against supplier and management-plane cascading failures.

## 2. Actor Identity: Taxonomy, Aliases, And Clustering Conflicts

| Primary Designation | Known Aliases And Vendor Naming | Taxonomy Conflicts And Caveats |
| --- | --- | --- |
| MuddyWater | Mango Sandstorm; Boggy Serpens; Static Kitten; Earth Vetala; TA450; MERCURY | Mature espionage cluster; increasingly observed acting as an initial access broker for other clusters such as Lyceum. |
| OilRig | APT34; Helix Kitten; Hazel Sandstorm; Earth Simnavaz; Crambus; COBALT GYPSY | Broadcom uses Crambus; Microsoft uses Hazel Sandstorm. Frequent operational overlap with MuddyWater and Agrius is reported, but should not be assumed without evidence. |
| Magic Hound / APT35 | Charming Kitten; TA453; Phosphorus; Mint Sandstorm; COBALT ILLUSION | Historically an umbrella term. Many vendors separate APT35 from APT42 based on tactical divergence, though phishing infrastructure overlaps persist. |
| APT42 | UNC788; Damselfly; Mint Sandstorm partial overlap | Focused on credential harvesting and high-value individual targeting. |
| Agrius | Pink Sandstorm; AMERICIUM; Agonizing Serpens; BlackShadow | Often masquerades as ransomware but operates with destructive and espionage intent. |
| CyberAv3ngers | Shahid Kaveh Group; Hydro Kitten; Storm-0784; Bauxite; UNC5691; Soldiers of Solomon | OT/ICS-focused. Often conflated with Cyber Toufan; keep separated unless sources explicitly link them. |
| Imperial Kitten | Yellow Liderc; Tortoiseshell; TA456; CURIUM; Crimson Sandstorm | Specialized focus on maritime, shipping, logistics, and supply-chain operations. |
| Pioneer Kitten | Fox Kitten; Lemon Sandstorm; UNC757; Parisite; RUBIDIUM | Opportunistic access broker exploiting edge appliances and selling or handing access to ransomware affiliates. |
| Lyceum | HEXANE; Spirlin; Siamesekitten | Some vendors evaluate it as OilRig-adjacent or a subgroup; telecom and energy focus. |
| Cotton Sandstorm | Emennet Pasargad; Aria Sepehr Ayandehsazan; ASA; Marnanbridge; Haywire Kitten | Iranian cyber-enabled influence operations group. |
| WIRTE | Ashen Lepus; Gaza Cybergang subgroup | Often tracked distinctly from TA402 due to operational maturity, though both may fall under Hamas-aligned Gaza Cybergang reporting. |
| APT-C-23 / Arid Viper | Desert Falcon; Desert Varnish | Uses distinct mobile spyware such as AridSpy. |
| UNC1860 | Related to Scarred Manticore, ShroudedSnooper, Storm-0861 | Initial access and persistence provider. Operates passive backdoors before possible handoff. |
| Void Manticore | STORM-842; Handala; Homeland Justice; Karma | Destructive cluster and persona ecosystem using access obtained by other actors in some reporting. |

It is Assessed-here that the distinction between actor and persona is critical for Israeli defenders. Void Manticore is the operational actor model, whereas Handala / Handala Hack is a psychological-operations persona designed to maximize fear and media visibility. Cyber Toufan should likewise be treated as a public persona or operation unless source-backed technical evidence supports a specific actor label.

## 3. Sponsor And Command Relationship

### MOIS Alignment

The MOIS apparatus historically favors long-term, methodical espionage, though it has increasingly embraced deniable destruction.

- MuddyWater: ESET source-reports that MuddyWater is aligned with the Ministry of Intelligence and National Security of Iran.
- UNC1860 and Void Manticore: Mandiant assesses UNC1860 is likely affiliated with Iran's MOIS. U.S. DOJ reporting reportedly links seized domains such as `Handala-Hack[.]to` to MOIS psychological operations.
- Agrius: The Israel National Cyber Directorate and Shin Bet reportedly attributed Israeli healthcare-sector attacks to the Iranian Ministry of Intelligence cyber attack group called Agrius.

### IRGC Alignment

IRGC-linked groups generally exhibit higher risk tolerance, engaging in disruptive, hack-and-leak, and kinetically aligned operations.

- CyberAv3ngers: CISA and FBI source-report CyberAv3ngers affiliation with Iran's IRGC Cyber-Electronic Command.
- Cotton Sandstorm / Emennet Pasargad: U.S. DOJ indictments source-report operators as Iranian nationals and IRGC employees; Microsoft assesses activity under IRGC auspices.
- OilRig and Imperial Kitten: Broadcom and CrowdStrike assess these groups operate in support of Iranian strategic intelligence and geopolitical requirements against regional rivals and maritime targets. Validate exact sponsor wording before promotion.

### Hamas And Hezbollah Alignment

- WIRTE and Arid Viper: SentinelOne and Check Point source-report these groups as subgroups of Hamas-affiliated Gaza Cybergang in some reporting. Palo Alto Networks refers to Ashen Lepus / WIRTE as a Hamas-affiliated threat actor in recent reporting.
- Lebanese Cedar: Israeli joint investigations linked this group to Hezbollah cyber units and highlighted joint activity with MOIS-linked Agrius.

## 4. Israeli Or Israel-Adjacent Relevance

### Government, Public Sector, And Municipalities

The Israeli public sector is a continuous target for both initial access and psychological operations. Check Point reportedly source-reports that in March 2026, Iran-linked actors conducted large password-spraying campaigns against more than 300 Israeli targets, with emphasis on city governments and disruption of municipal response to kinetic events.

The Hamas-affiliated WIRTE group reportedly conducted localized disruptive campaigns in October 2024, targeting Israeli municipalities and regional councils with the SameCoin wiper.

### Healthcare And Hospitals

Medical infrastructure has suffered direct destructive targeting. INCD and Shin Bet reportedly source-report that MOIS-linked Agrius, in collaboration with Hezbollah-linked Lebanese Cedar, conducted a destructive attack against Ziv Medical Center in Safed in late 2023. The attack reportedly failed to disrupt patient care but led to exfiltration of approximately 300,000 patient records.

### Critical Infrastructure, Energy, Logistics, And OT

CyberAv3ngers actively targets Israeli-made OT equipment globally, including Unitronics Vision PLCs, and has expanded reporting around Rockwell Automation and Siemens environments. These operations threaten water/wastewater systems and energy grids through OT manipulation, HMI defacement, and project-file access.

In maritime, Imperial Kitten / Yellow Liderc reportedly conducted strategic watering-hole attacks compromising Israeli maritime, shipping, and logistics websites to deploy IMAPLoader, correlating with threats to shipping lanes.

### Telecommunications And IT Supply Chain

Telecom and IT service providers are targeted to enable downstream compromise. Reporting references UNC2428 overlap with MOIS-linked Black Shadow and use of Rafael-themed social engineering to deliver MURKYTOUR. Cyber Toufan reportedly targeted Israeli IT hosting and technology suppliers and used POKYBLIGHT wiper activity to cascade damage into downstream environments. Evidence suggests MuddyWater has operated as an access broker within Israeli manufacturing, handing network control to Lyceum.

### Kinetic Integration And Battle Damage Assessment

Check Point researchers reportedly identified intensified targeting of IP cameras in Israel and Cyprus beginning February 28, 2026. It is Assessed-by-source that Iranian operators leverage such compromises for real-time battle damage assessment during missile operations.

### Identified Gap

Detailed primary-source telemetry regarding successful 2025-2026 breaches of core telecommunications infrastructure, such as SS7/Diameter networks, remains a public-domain gap. Treat claims about core-network compromise as Inferred unless supported by primary reporting.

## 5. Targeting And Intrusion Lifecycle

### Initial Access

- Edge exploitation: Pioneer Kitten and CyberAv3ngers bypass user interaction through internet-facing infrastructure. Pioneer Kitten reportedly targets edge appliances, including CVE-2024-24919 on Check Point gateways. CyberAv3ngers identifies exposed PLCs via internet scanning and authenticates through native OT ports such as 44818, 2222, and 102 using weak or default credentials.
- Strategic web compromise: Imperial Kitten embeds malicious JavaScript into compromised maritime and logistics websites. The script fingerprints visitors and selectively delivers IMAPLoader.
- Spearphishing and lures: MuddyWater uses targeted emails with PDF attachments linking to commercial RMM installers hosted on file-sharing platforms. WIRTE uses ZIP archives masquerading as ESET or INCD security updates.

### Execution And Evasion

- Reflective loading and delay logic: MuddyWater uses Fooder to reflectively load MuddyViper into memory. Fooder reportedly implements Snake game logic and Sleep API calls to delay execution and evade sandboxes.
- Geofenced detonation: WIRTE's SameCoin wiper reportedly requests `oref.org.il` and uses response bytes as an XOR key to decrypt payload content only in Israeli-relevant environments.
- Kernel manipulation: UNC1860 demonstrates deep Windows OS knowledge by reportedly repurposing Iranian AV kernel-mode drivers such as WINTAPIX / TOFUDRV to protect malware artifacts from EDR deletion.

### Persistence And Passive C2

- Inbound-listening implants: UNC1860 uses passive backdoors such as TEMPLEDOOR that do not initiate outbound connections. They bind to local ports or hook Windows network drivers and wait for inbound packets with specific characteristics.
- GUI controllers: UNC1860 operators use TEMPLEPLAY, a custom .NET GUI controller, to interface with TEMPLEDOOR implants and proxy RDP traffic into internal networks.

### Credential Access And Identity Weaponization

- Browser storage abuse: MuddyWater deploys CE-Notes, reportedly targeting Chromium-based browsers and the Local State file to bypass app-bound encryption.
- Cloud identity theft: Void Manticore and APT42 target the identity plane using privileged OAuth tokens or session cookies, often through AitM phishing kits such as Evilginx2.

### Impact And Exfiltration

- Administrative remote wipes: Void Manticore executes destructive impact by issuing legitimate factory-reset or wipe commands through compromised MDM portals such as Intune.
- Bespoke wipers: Reported destructive tools include POKYBLIGHT, Hatef, Hamsa, BiBi, and SameCoin. These may overwrite file headers, delete Volume Shadow Copies, and leave political or extortion-themed notes.
- OT/ICS manipulation: CyberAv3ngers interacts with OT project files such as Rockwell `.ACD` ladder logic/configuration files and may manipulate displayed SCADA/HMI data.

## 6. ATT&CK Mapping Candidates

| Technique ID | Name | Tactic | Observable / Procedure | Evidence Label | Mapping Quality Candidate |
| --- | --- | --- | --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Initial Access | Pioneer Kitten exploits edge appliances such as Check Point gateways. | Source-reported | M1 |
| T1189 | Drive-by Compromise | Initial Access | Imperial Kitten injects JavaScript into maritime sites to fingerprint targets and deliver IMAPLoader. | Source-reported | M1 |
| T1078.004 | Valid Accounts: Cloud Accounts | Initial Access | Void Manticore uses compromised administrator identities to access MDM consoles. | Assessed-by-source | M1 |
| T1027.010 | Obfuscated Files: Command Obfuscation | Defense Evasion | MuddyWater Fooder loader uses Snake game logic and Sleep APIs to delay execution. | Source-reported | M1 |
| T1480 | Execution Guardrails | Defense Evasion | WIRTE SameCoin uses `oref.org.il` HTTP response as XOR decryption input. | Assessed-here | M2 |
| T1505 | Server Software Component | Persistence | UNC1860 deploys passive listening backdoors such as TEMPLEDOOR on edge servers. | Source-reported | M1 |
| T1553.006 | Subvert Trust Controls: Code Signing | Defense Evasion | UNC1860 abuses legitimate Iranian AV kernel drivers such as WINTAPIX. | Source-reported | M1 |
| T1555.003 | Credentials From Web Browsers | Credential Access | MuddyWater CE-Notes extracts Chromium Local State encryption keys. | Source-reported | M1 |
| T1498.001 | Network Denial Of Service: Direct | Impact | Handala / Void Manticore conducts DDoS against Israeli infrastructure. | Assessed-by-source | M2 |
| T1485 | Data Destruction | Impact | Cyber Toufan uses POKYBLIGHT; WIRTE uses SameCoin. | Source-reported | M1 |
| T1562.001 | Impair Defenses: Disable Or Modify Tools | Defense Evasion | Void Manticore uses trusted MDM consoles to issue remote wipes. | Assessed-here | M1 |
| T0822 | Point And Tag Identification | Discovery (ICS) | CyberAv3ngers reads or manipulates Rockwell `.ACD` ladder logic project files. | Source-reported | M1 |
| T0889 | Modify Control Logic | Impact (ICS) | CyberAv3ngers manipulates configuration logic on Unitronics and Rockwell PLCs. | Source-reported | M1 |

## 7. Associated Families And Tools

| Tool Name | Type | Actor Association | Confidence | Behavior And Capabilities | Public Hash / IOC Reference Location |
| --- | --- | --- | --- | --- | --- |
| MuddyViper | Backdoor | MuddyWater | High | Collects system information, executes shell commands, and exfiltrates browser data; reflectively loaded into memory. | ESET appendix |
| Fooder | Loader | MuddyWater | High | Implements Snake-game delay loop to bypass sandbox timing and loads MuddyViper. | ESET appendix |
| TEMPLEDOOR | Passive backdoor | UNC1860 | High | Listens for inbound traffic without outbound C2. | Mandiant appendix |
| TEMPLEPLAY | Controller | UNC1860 | High | .NET GUI for controlling TEMPLEDOOR and proxying RDP. | MD5 reported: `c517519097bff386dc1784d98ad93f9d` |
| SameCoin | Wiper | WIRTE | High | Decrypts using Home Front Command response-derived XOR input; overwrites files. | Check Point appendix |
| AshTag | Backdoor | WIRTE | High | Sideloaded backdoor used for espionage in the Middle East. | Unit 42 appendix |
| Menorah | Backdoor | OilRig | High | Espionage backdoor dropped through malicious LNK files. | Trend Micro appendix |
| POKYBLIGHT | Wiper | Cyber Toufan | High | Destructive wiper used against Israeli IT suppliers. | Mandiant M-Trends reference |
| AridSpy | Mobile spyware | Arid Viper | High | Trojanized Android apps masquerading as dating or messaging apps for surveillance. | ESET / CFR appendix |
| VAX One | Backdoor | MuddyWater | High | Impersonates legitimate services such as Veeam, AnyDesk, Xerox, or OneDrive updater. | ESET appendix |
| CE-Notes | Credential stealer | MuddyWater | High | Targets Chromium Local State encryption keys. | ESET appendix |
| IMAPLoader | Downloader | Imperial Kitten | High | Drops follow-on payloads after maritime watering-hole compromise. | PwC appendix |
| IronWind | Loader | WIRTE / TA402 | High | Loader enabling C2 and execution of code hidden within HTML elements. | Proofpoint / Check Point |

## 8. Public IOCs

Large hash datasets and dynamic IP address collections should not be treated as durable claims in this narrative report. Defenders should ingest IOC appendices from primary vendor or government sources and track them through a TIP or source-specific IOC manifest.

The following are presented as research-intake indicators requiring validation before operational use.

### CyberAv3ngers OT/ICS Suspect IP Infrastructure

Active window reported: January 2025 to March 2026.

- `135.136.1[.]133`
- `185.82.73[.]162`
- `185.82.73[.]164`
- `185.82.73[.]165`
- `185.82.73[.]167`
- `185.82.73[.]168`
- `185.82.73[.]170`
- `185.82.73[.]171`

### Cotton Sandstorm VPS-Agent Infrastructure

Active window reported: mid-2024.

- `195.26.87[.]80`
- `213.109.147[.]97`
- `185.110.188[.]112`

### Handala / MOIS Seized PSYOPS Domains

- `Justicehomeland[.]org`
- `Handala-Hack[.]to`
- `Karmabelow80[.]org`
- `Handala-Redwanted[.]to`

## 9. Detection And Hunting Hypotheses

### H1: UNC1860 Passive Backdoor Listener Registration

- Telemetry required: endpoint network connections, EDR process events, Sysmon Event ID 3, IIS logs.
- Observable behavior: `System` or `w3wp.exe` binding to non-standard high-numbered ports or registering new HTTP.sys URL ACLs without corresponding deployment logs. Search for RDP traffic originating from web-facing IIS worker processes to internal networks.
- Lookback: 90 days.
- False positives: custom local web applications; authorized reverse-proxy configurations.
- Escalation: RDP from a DMZ web server to an internal domain controller.

### H2: WIRTE SameCoin Geofenced Execution Verification

- Telemetry required: web proxy logs, DNS logs, EDR network events.
- Observable behavior: untrusted binaries from `C:\Users\Public` or `AppData\Local\Temp` making HTTP/HTTPS requests to `oref.org.il`, followed by mass file modification.
- Lookback: 30 days.
- False positives: users checking Home Front Command alerts with standard browsers.
- Escalation: request made by a non-browser process such as `svchost.exe`, `powershell.exe`, or random binaries.

### H3: MuddyWater Fooder Delay Loop Evasion

- Telemetry required: EDR API telemetry, Windows API tracing if enabled, Sysmon Event ID 8.
- Observable behavior: newly downloaded executable from RMM context making many sequential Sleep API calls before memory allocation and thread creation.
- Lookback: 14 days.
- False positives: gaming software or commercial DRM.
- Escalation: child process creation or code injection after delay loop completion.

### H4: Void Manticore MDM/RMM Identity Weaponization

- Telemetry required: identity-provider logs, Entra ID `SigninLogs`, MDM audit logs.
- Observable behavior: successful MDM administrator login from anomalous geolocation or commercial VPN node, followed by bulk wipe, retire, or factory-reset commands.
- Lookback: 7 days; continuous alerting recommended.
- False positives: authorized offboarding or hardware refresh.
- Escalation: more than five devices wiped from an admin session with missing, weak, or suspicious MFA context.

### H5: CyberAv3ngers OT/ICS Malicious Interaction

- Telemetry required: Zeek/Suricata, firewall logs on OT boundaries.
- Observable behavior: inbound external connections to PLCs over ports `44818`, `2222`, `102`, or `502`.
- Lookback: 60 days.
- False positives: authorized remote engineering through secure enclaves.
- Escalation: SSH to PLC followed by transfer, modification, or extraction of `.ACD` project files.

### H6: MuddyWater CE-Notes Chromium Key Theft

- Telemetry required: EDR file access logs, Sysmon Event ID 11.
- Observable behavior: untrusted process accessing `\AppData\Local\Google\Chrome\User Data\Local State` and querying crypto APIs to decrypt browser data.
- Lookback: 30 days.
- False positives: browser migration or profile synchronization tools.
- Escalation: unsigned process recently dropped by RMM or macro-enabled document.

### H7: WIRTE AshTag Sideloading

- Telemetry required: EDR image-load events, Sysmon Event IDs 7 and 1.
- Observable behavior: legitimate signed executable vulnerable to DLL search-order hijacking loading unsigned DLL from `C:\ProgramData` or user temp directory, followed by sustained outbound HTTPS.
- Lookback: 45 days.
- False positives: legacy applications in user directories.
- Escalation: low-prevalence unsigned DLL connecting to newly registered dynamic DNS domain.

### H8: Pioneer Kitten VPN Exploitation To Payload

- Telemetry required: VPN gateway syslog, EDR process creation.
- Observable behavior: evidence of Check Point gateway exploitation followed by reconnaissance binaries or tunneling tools on adjacent internal network segments.
- Lookback: 90 days.
- False positives: vulnerability-management scanning.
- Escalation: privilege escalation, archive staging, or lateral movement after edge compromise.

### H9: Imperial Kitten Watering-Hole Fingerprinting

- Telemetry required: web proxy logs, endpoint browser telemetry.
- Observable behavior: corporate devices navigating to maritime/logistics websites and executing obfuscated JavaScript, followed by ISO, ZIP, or LNK download matching IMAPLoader profile.
- Lookback: 30 days.
- False positives: legitimate web analytics.
- Escalation: payload initiates IMAP/IMAPS connections to external email servers.

### H10: OilRig Menorah Phishing Chain

- Telemetry required: email gateway logs, EDR file creation.
- Observable behavior: spearphishing archive drops malicious `.LNK`; execution spawns PowerShell or CMD and downloads Menorah; follow-on reconnaissance commands such as `whoami` or `systeminfo`.
- Lookback: 60 days.
- False positives: user-created shortcut files running standard admin scripts.
- Escalation: file upload/download to infrastructure with no prior organizational reputation.

### H11: Cotton Sandstorm IP Camera Scraping

- Telemetry required: edge firewall logs, IoT device traffic logs.
- Observable behavior: high-volume outbound traffic from internet-connected cameras or DVRs to untrusted overseas VPS providers.
- Lookback: 30 days.
- False positives: authorized camera backup.
- Escalation: connections using default credentials or known Cotton Sandstorm VPS-agent infrastructure.

### H12: Lyceum Telecom Discovery

- Telemetry required: DNS query logs, EDR process creation.
- Observable behavior: PowerShell or BITSAdmin on telecom admin hosts followed by high-frequency TXT or A record lookups to anomalous domains suggestive of DNS tunneling.
- Lookback: 45 days.
- False positives: legitimate administrative scripts using BITSAdmin.
- Escalation: Mimikatz or Active Directory discovery concurrent with DNS tunneling.

## 10. Source Register Update Candidates

| Accessed Date | Publication Date | Publisher | Title | URL | Stated Status In Intake | Reliability Candidate |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-16 | 2025-12-02 | ESET | Iran-aligned MuddyWater targets critical infrastructure | `https://www.eset.com/us/about/newsroom/research/iran-muddywater-critical-infrastructure-israel-egypt-snake-game-eset-research/` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2024-09-19 | Mandiant | UNC1860: Iran's Middle Eastern Networks | `https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2026-03-23 | Palo Alto Unit 42 | Evolution of Iran Cyber Threats | `https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2024-11-12 | Check Point | WIRTE Expands To Disruptive Activity | `https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2026-04-07 | CISA / FBI | AA26-097A: CyberAv3ngers Exploit PLCs | `https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2024-10-30 | FBI / CISA | CSA 241030: Cotton Sandstorm Hack And Leak | `https://www.ic3.gov/CSA/2024/241030.pdf` | Reported HTTP 200 in imported research; must verify | A |
| 2026-05-16 | 2026-03-19 | U.S. DOJ | Justice Department Disrupts MOIS Operations | `https://www.justice.gov/opa/pr/justice-department-disrupts-iranian-cyber-enabled-psychological-operations` | Reported HTTP 200 in imported research; must verify | A |

## 11. Evidence Register Update Candidates

| Claim ID | Actor | Summary | Evidence Label | Reliability | Credibility | Confidence | Contradiction / Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CLM-GEMINI-001 | MuddyWater | MuddyWater uses Fooder loader with Snake game logic to delay execution. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-002 | UNC1860 | UNC1860 uses TEMPLEDOOR passive backdoor for inbound listening. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-003 | Void Manticore | Void Manticore abuses MDM/RMM for remote wipes, reducing reliance on custom wipers. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-004 | Handala | Handala persona domains were seized and operated by MOIS. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-005 | WIRTE | WIRTE deployed SameCoin wiper targeting Israel and uses `oref.org.il` XOR logic. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-006 | CyberAv3ngers | IRGC-CEC linked group targets Rockwell/Unitronics PLCs on ports `44818` and `102`. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-007 | Pioneer Kitten | Actor brokers access for ransomware affiliates against Israeli infrastructure. | Source-reported | A | High | High | Needs exact source quote. |
| CLM-GEMINI-008 | Cotton Sandstorm | Actor operates VPS-agent reseller network to support hack-and-leak activity. | Source-reported | A | High | High | Needs source URL validation. |
| CLM-GEMINI-009 | Imperial Kitten | Actor conducts maritime watering holes delivering IMAPLoader. | Source-reported | A | High | High | Needs source URL validation. |

## 12. Tool-Intelligence Update Candidates

| Tool Name | Type | Actor Association | Confidence | Behavior Summary | Hash / IOC Reference |
| --- | --- | --- | --- | --- | --- |
| MuddyViper | Backdoor | MuddyWater | High | Reflectively loaded backdoor for system information and command execution. | ESET appendix |
| Fooder | Loader | MuddyWater | High | Snake-game delay loop to evade sandbox execution. | ESET appendix |
| TEMPLEDOOR | Passive backdoor | UNC1860 | High | Listens for inbound traffic without outbound C2. | Mandiant appendix |
| TEMPLEPLAY | Controller | UNC1860 | High | .NET GUI to control TEMPLEDOOR and proxy RDP. | `c517519097bff386dc1784d98ad93f9d` |
| SameCoin | Wiper | WIRTE | High | Decrypts using Home Front Command XOR and overwrites files. | Check Point appendix |
| AshTag | Backdoor | WIRTE | High | Sideloaded backdoor used for Middle East espionage. | Unit 42 appendix |
| Menorah | Backdoor | OilRig | High | Espionage backdoor dropped by LNK. | Trend Micro appendix |
| AridSpy | Mobile spyware | Arid Viper | High | Trojanized Android apps for mobile surveillance. | ESET appendix |
| VAX One | Backdoor | MuddyWater | High | Impersonates legitimate services such as Veeam and AnyDesk. | ESET appendix |
| CE-Notes | Stealer | MuddyWater | High | Targets Chromium Local State encryption keys. | ESET appendix |

## 13. Navigation And Crosslink Recommendations

- Actor pages: link MuddyWater directly to Lyceum if primary-source reporting validates an access-broker or handoff relationship.
- Actor pages: link UNC1860 to Void Manticore and Cyber Toufan under a proposed MOIS handoff ecosystem tag only if source-backed.
- Tool pages: crosslink SameCoin and IronWind if shared development pipeline or XOR routines are source-confirmed.
- TTP matrix: map identity weaponization and MDM / Intune abuse to ransomware and destructive-operation playbooks.
- Persona claims workflow: route Handala, Cyber Toufan, and Cyber Court claims to a PSYOPS evaluation or persona-claims process.

## 14. Gaps And Follow-Up Collection Plan

### UNC1860 To Void Manticore Handoff Mechanics

While it is Assessed-by-source that UNC1860 may provide initial access later used by Void Manticore and Cyber Toufan, the precise technical handoff mechanism remains undocumented in public reporting.

Collection priority: analyze captured TEMPLEPLAY instances for multi-tenant features, credential-sharing mechanisms, or third-party authentication logs.

### Telecommunications Core Network Breach Depth

Reporting indicates OilRig and Lyceum target Israeli telecommunications. Public evidence remains insufficient to determine persistence in core switching infrastructure such as SS7 or Diameter networks versus standard corporate IT networks.

Collection priority: audit core network element logs for passive-listening tools that mimic telecom diagnostic protocols.

### OT/ICS Malicious Manipulation Threshold

CyberAv3ngers demonstrates capability to extract and manipulate Rockwell `.ACD` files. It remains unconfirmed whether the group has engineering competence for localized kinetic damage or primarily conducts HMI defacement and simple process disruption.

Collection priority: reverse engineer captured Rockwell project-file modifications to assess the actor's control-logic comprehension.
