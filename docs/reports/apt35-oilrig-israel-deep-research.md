---
title: APT35 And OilRig Israel Deep Research Intake
sidebar_label: APT35 / OilRig Israel Research
---

:::caution Analyst validation required
This page is an imported deep-research artifact. Treat it as lead-generation material until claims, citations, URLs, hashes, and detection logic are validated against primary public sources and repository evidence standards.
:::

# Executive Summary  
Iranian-linked cyber–espionage groups pose a persistent threat to Israeli government, infrastructure, and media. In particular, the IRGC-affiliated **APT35** (aka Charming Kitten, Magic Hound) has conducted targeted spear-phishing campaigns against Israeli journalists, academics, and technology experts【8†L147-L155】【30†L65-L74】. The group uses elaborate social engineering to deliver custom backdoors (notably the “PowerStar” implant) via password-protected RAR/LNK attachments【8†L180-L187】【21†L142-L150】. Once inside, APT35 pursues credential theft, email compromise (Exchange/OWA/Office 365), and reconnaissance, using cloud services (Backblaze, IPFS, OneDrive) for C2 and exfiltration【8†L180-L187】【21†L77-L85】. Separately, the **APT34/OilRig** group (Iranian state-sponsored) has repeatedly targeted Israeli critical sectors (healthcare, manufacturing, local government) using custom downloader malware and cloud-based C2【9†L150-L159】【11†L47-L54】. Observed tactics include spear-phishing emails with malicious attachments, exploitation of vulnerabilities (e.g. Exchange ProxyShell, Ivanti CVEs), and re-use of compromised sites for C2【25†L101-L109】【28†L1202-L1211】. We rate the evidence strong (sources A–B) and note that published IOC lists are limited. Key defensive priorities are: monitoring for APT35-style spear-phish with LNKs, anomalous cloud traffic (IPFS/Backblaze), suspicious Exchange/GAL export activity, and credential-theft indicators (e.g. unusual OAuth flows or PowerShell activity)【28†L1249-L1257】【30†L65-L74】.

## Actor Identity  
- **Primary name:** APT35. Key aliases include *Charming Kitten*, *Imperial Kitten*, *Tortoiseshell* (reported by DarkReading)【8†L147-L155】; *Magic Hound* (MITRE cluster name)【19†L52-L61】; vendor labels: **Phosphorus/Mint Sandstorm** (Microsoft), **Ajax Security Team** (FireEye), **NewsBeef** (Kaspersky)【12†L150-L154】. Other monikers (from Wikpedia/CTI) include *Newscaster*, *COBALT ILLUSION*, *Educated Manticore*, *TA453*【30†L77-L81】【12†L150-L154】.  
- **Taxonomy conflicts:** Some vendors treat APT35 as part of broader “Magic Hound” cluster. CrowdStrike splits *TA453* vs *Magic Hound*; Check Point links APT35 with “Educated Manticore” sub-group【30†L77-L81】. We follow MITRE’s grouping: Magic Hound/TA453 cover APT35 activity【19†L52-L61】.  
- **Aliases table (examples):** Charming Kitten (APT35, **Iranian** group)【8†L147-L155】; Imperial Kitten/Tortoiseshell (used by DarkReading)【8†L147-L155】; Phosphorus/Mint Sandstorm (Microsoft)【12†L150-L154】; Ajax Security Team (FireEye)【12†L150-L154】; NewsBeef (Kaspersky)【12†L150-L154】.  

## Sponsor and Command Relationship  
APT35 is “Iranian-sponsored” and widely attributed to Iran’s Islamic Revolutionary Guard Corps (IRGC) cyber command【19†L52-L61】【21†L54-L60】. MITRE notes Magic Hound “likely on behalf of the IRGC”【19†L52-L61】, and open sources consistently link APT35 to IRGC operations. No public evidence suggests APT35 operates as a proxy for other states or non-state groups. The leaked APT35 documents show a highly bureaucratic structure with supervisors and analysts, implying a military/government chain of command rather than independent contractors【7†L75-L83】【28†L1258-L1267】. No public persona or front organization is confirmed. **Assessment:** State sponsor: IRGC (Iran); Proxy/Contractor: none identified; Persona: none publicly reported.

## Israeli / Israel-Adjacent Relevance  
APT35 has **directly targeted Israeli individuals and organizations**. In mid-2023, APT35 spear-phished an Israeli journalist with a “draft report” lure delivering a PowerStar backdoor【8†L157-L166】【21†L142-L150】. In June 2025 (during the Iran–Israel conflict), Check Point reported APT35 campaigns against “journalists, high-profile cybersecurity experts, and computer science professors in Israel,” using AI-tailored phishing via email and WhatsApp【30†L65-L74】【30†L77-L85】. These attacks mimicked Google Meet invites and fake Gmail logins to harvest credentials【30†L69-L78】【30†L112-L121】. Overall, APT35 shows persistent interest in Israeli targets (media, tech sector, academia) with high confidence based on multiple reports. Similarly, *OilRig (APT34)* repeatedly compromised Israeli critical infrastructure in 2022–2023, including healthcare, manufacturing, and government, using new downloader tools【9†L150-L159】【11†L47-L54】. We assess **high confidence** in these linkages. **Gap:** No public reporting on APT35 targeting of other Israel-adjacent actors (e.g. Palestinian or Jordanian sectors), beyond noted campaigns. Further telemetry from Israeli CERTs or victim networks would clarify full victimology.

## Targeting & Intrusion Lifecycle  
**Initial Access:** APT35 primarily uses **targeted spear-phishing emails**. Victims are social-engineered (e.g. posing as colleagues or assistants) into opening malicious attachments or links【8†L157-L166】【21†L142-L150】. Notably, in 2023 APT35 sent a password-protected RAR containing an .LNK file to an Israeli reporter【8†L157-L166】【21†L142-L150】. They have also deployed fake account login pages (Gmail) via phishing links【30†L69-L78】. *OilRig* similarly gains access via spear-phish attachments or by compromising victim websites (watering holes)【25†L104-L112】【25†L117-L123】.     
**Execution:** The APT35 .LNK is a malicious Windows shortcut which, when clicked by the user, downloads the **PowerStar** backdoor from cloud storage (Backblaze)【8†L180-L187】. It then executes the payload. DomainTools leaked logs show APT35 also used ProxyShell/EWS exploits against Exchange servers (May–July 2022) for initial compromise【28†L1208-L1213】. OilRig 2021–22 campaigns dropped backdoors (“Solar”, “Mango”) via VBS droppers (likely from phishing)【25†L104-L112】.     
**Persistence:** PowerStar establishes a foothold by running from %AppData% or similar, and may inject into memory (Volexity notes OPSEC features). APT35 also maintains persistence by monitoring compromised email accounts and installing mailbox rules. The leak indicates long-term mailbox monitoring (“HERV” phishing framework and KPI logs) to sustain access【7†L89-L98】【28†L1236-L1242】.     
**Privilege Escalation:** The leak shows APT35 harvested credentials from LSASS dumps (Mimikatz) as early as April 2022, capturing plaintext admin passwords【28†L1202-L1211】. These were replayed across the network. There is also evidence of abused OAuth tokens and credential reuse to move laterally via RDP or other remote services.     
**Defense Evasion:** PowerStar variants employ encryption and fetch their configurations/code from IPFS and other cloud, hindering static detection【21†L77-L85】. The Mango backdoor (OilRig) includes an unused anti-debug flag to block security hooks【25†L123-L131】. APT35 also scatters activity (e.g. email, .env fetches) to blend with normal traffic【28†L1171-L1179】.     
**Discovery:** Once inside, APT35 collects host and network data. PowerStar “collects a small amount of system information” and exfiltrates it【8†L185-L189】. The leak shows automated scanning for WordPress user enumeration and RDP-probe cookies (e.g. “mstshash”)【28†L1171-L1179】. They searched for /.env or SendGrid configs on hosts【28†L1171-L1179】.     
**Lateral Movement:** Captured credentials (via LSASS dumps and PowerStar capture) were reused to compromise additional machines (“Credential Replay”)【28†L1202-L1211】. The timeline notes use of compromised mailboxes to pivot to other Exchange servers. OilRig repeated patterns on known victims rather than wide lateral jumps【11†L47-L54】.     
**Collection/Exfiltration:** The threat actors routinely harvested credentials from browsers and Windows Credential Manager (OilRig)【25†L99-L107】, and exfiltrated GAL (Global Address List) databases from Exchange for use in phishing【28†L1208-L1213】. PowerStar uses HTTP POST to send data to a C2 pulled from Backblaze【8†L185-L189】. OilRig’s downloaders exfiltrate data by uploading it through legitimate cloud APIs (OneDrive/Graph/EWS)【9†L162-L170】【25†L101-L109】.     
**Impact:** The end goal is strategic cyber-espionage. APT35’s activities gather intelligence from government, media, and tech sectors. OilRig’s toolset suggests credential theft and long-term access without immediate disruptive impact. There are no confirmed destructive payloads; impacts are collection and surveillance【25†L101-L109】【30†L65-L74】.  

## MITRE ATT&CK Mapping  
| Technique ID     | Technique Name                   | Tactic               | Evidence (Source)                         | Label          | Quality |
|------------------|----------------------------------|----------------------|-------------------------------------------|----------------|---------|
| T1566.001        | Spearphishing Attachment         | Initial Access       | APT35 used spear-phish LNK attachment to deploy PowerStar【21†L142-L150】【8†L180-L187】 | Source-reported | M1      |
| T1204.002        | User Execution: Malicious File   | Execution            | Victim ran malicious LNK from a RAR archive【8†L180-L187】【21†L142-L150】 | Source-reported | M1      |
| T1105            | Ingress Tool Transfer            | Execution/C2         | LNK downloads PowerStar from Backblaze cloud【8†L180-L187】 | Source-reported | M1      |
| T1071.001        | Application Layer Protocol (Web) | Command & Control    | PowerStar POSTs data via HTTP to C2 host on Backblaze【8†L185-L189】 | Source-reported | M1      |
| T1562.001        | Impair Defenses: Disable or Modify Tools | Defense Evasion | Mango backdoor has unused flag to disable endpoint hooks【25†L123-L131】 | Source-reported | M1      |
| T1082            | System Information Discovery     | Discovery            | PowerStar collects system info (check OS, names)【8†L185-L189】 | Source-reported | M1      |
| T1007            | System Service Discovery         | Discovery            | Actors perform RDP-style scans (Cookie: mstshash probes)【28†L1171-L1179】 | Source-reported | M1      |
| T1190            | Exploit Public-Facing App        | Execution            | Used Exchange ProxyShell/EWS exploits to gain access【28†L1208-L1211】 | Source-reported | M1      |
| T1557.002        | Adversary-in-the-Middle         | Defense Evasion/Credential Access | Man-in-the-middle phishing with fake OAuth pages to capture creds【30†L69-L78】 | Source-reported | M2      |
| T1078.003        | Valid Accounts: Cloud Accounts   | Initial Access       | Phishing lures captured Google/Gmail login credentials for account takeover【30†L69-L78】 | Source-reported | M2      |

*(M1: techniques directly confirmed by sources; M2: inferred from reported behavior.)*

## Associated Families and Tools  
- **PowerStar** – Custom backdoor (managed by APT35). A .NET/PowerShell implant that collects system info and uses cloud/IPFS for C2【8†L180-L187】【21†L77-L85】. Actor confidence: High (directly observed in 2023 campaign【8†L180-L187】). Detection: Monitor for processes downloading from Backblaze/IPFS and HTTP POSTs of system data. *IOC Reference:* Vendor blogs mention its use but do not publish hashes.  
- **CharmPower** – Earlier version of PowerStar (Checkpoint name)【21†L142-L150】. (Classification: backdoor; APT35 linkage: confirmed by CheckPoint.)  
- **HERV Phishing Framework** – APT35’s internal email-harvesting system (described in leaks) used for iterative lure campaigns【7†L89-L98】. (Type: operational process, not malware.)  
- **Azure/Google OAuth Toolkit** – (Implied) The phishing kit (SPA-based) used by APT35 to harvest Gmail credentials【30†L113-L121】. (Conf: Medium; detection: look for unusual OAuth consent flows.)  
- **OilRig Downloaders** (for reference if OilRig considered): *SampleCheck5000*, *ODAgent*, *OilCheck*, *OilBooster* – custom downloaders used by APT34 in Israeli campaigns【9†L150-L159】【11†L43-L51】. (Type: downloader malware; APT confidence: High for OilRig.)  
- **Solar/Mango** – APT34 backdoors. Solar (novel C# backdoor, 2021) and Mango (evolved 2022) introduced via spear-phish VBS droppers【25†L104-L112】. (Type: backdoor; actor: OilRig/APT34.)

## Public IOCs  
No comprehensive IOC list for these campaigns is published. Vendors have not released SHA256 hashes or domains in sources above. However, analysts should **enrich detection** with: known APT35 domains (e.g. `*_kitten*` in phishing), IP addresses reported (e.g. Backblaze endpoint IPs from June 2023 campaign【8†L180-L187】, or scanning IPs 128.199.237.132 etc.【28†L1161-L1169】), and the malicious email lures (phishing URLs) when discovered. Official IOCs for APT35/PowerStar have appeared in closed intel feeds (see DomainTools analysis【27†L19-L27】【28†L1171-L1179】), but none are publicly sanitized here.  

## Detection and Hunting Hypotheses  
1. **Spear-Phish with LNK/RAR Attachments:** Monitor email gateways for password-protected archives containing `.LNK` files or other executables from external senders. *Telemetry:* Email headers, attachment metadata. *Fields:* subject lines referencing draft reports or meetings; attachment names. *Behavior:* unusual double-extension files. *False Positives:* benign attachments like scripted installers. *Escalation:* quarantine attachments, review user mailboxes (ATT&CK T1566, T1204).  
2. **Unusual Domain/Cloud Access:** Hunt for outbound connections to unknown or atypical cloud storage endpoints (e.g. Backblaze endpoints, IPFS gateways, newly registered OneDrive URLs). *Telemetry:* firewall/DNS logs. *Fields:* SNI or hostnames, X-Forwarded-* headers. *Behavior:* HTTP POST to cloud hosts, IPFS CIDs. *False Positives:* legitimate app updates. *Escalation:* manual review of domain, check context (T1071).  
3. **Exchange/GAL Export Activity:** Look for mass export of Global Address Lists or unusual admin API calls in Office 365/Exchange audit logs. *Telemetry:* mailbox audit logs, O365 Exchange diagnostic logs. *Fields:* commands like `Export-Mailbox` or long query strings. *Behavior:* A single user accessing many mailbox attributes. *False Positives:* legitimate mail migrations. *Escalation:* verify if user initiated; check group memberships (T1553).  
4. **Scanning and Reconnaissance:** Network IDS/IPS should flag web requests with patterns like `Cookie: mstshash=`, `/ ?author=`, `/wp-json/wp/v2/users`, or requests to `*.env`, `SendGrid` config files【28†L1171-L1179】. *Telemetry:* web proxy logs, WAF. *Fields:* URI paths, cookies. *Behavior:* internal scanning of web servers (T1595). *False Positives:* legitimate admin probes, crawling. *Escalation:* cross-correlate source IP (if external) with threat intel, block malicious source.  
5. **OAuth Abuse / Credential Harvesting:** In identity logs, detect new OAuth consents or session tokens from unusual sources (e.g. Google tokens accepted on Google Sites domains, per【30†L113-L121】). *Telemetry:* CASB/IDaaS logs. *Fields:* application IDs, redirect URIs. *Behavior:* grant tokens to unknown apps. *False Positives:* employee installs third-party apps. *Escalation:* revoke app tokens, prompt password resets (T1557, T1078).  
6. **Processes from Cloud-Hosted Binaries:** Endpoint sensors should look for processes spawned by cloud-hosted scripts (e.g. `powershell -EncodedCommand` that downloads from Backblaze/Dropbox). *Telemetry:* EDR process creation logs. *Fields:* command line substrings (Backblaze URL). *Behavior:* PowerShell or cURL child processes. *False Positives:* scheduled backups. *Escalation:* isolate host, obtain memory dump (T1027, T1059).  

Each hypothesis links to ATT&CK (e.g. T1566, T1071, T1553, T1595, T1557, T1059), and balances alert thresholds to avoid excessive false positives.

## Source Register Updates  
Key sources used (all live as of May 2026):  
- **DarkReading (30 Jun 2023)** – *“Iran-Linked APT35 Targets Israeli Media With Upgraded Spear-Phishing Tools”*【8†L147-L155】. Publisher: TechTarget (DarkReading); DOI: n/a; Reliability: B (trade publication, vendor quotes).  
- **Volexity Blog (28 Jun 2023)** – *“Charming Kitten Updates POWERSTAR with an InterPlanetary Twist”*【21†L142-L150】. Publisher: Volexity; Reliability: A (primary threat intel vendor).  
- **Recorded Future News (14 Dec 2023)** – *“Iran-linked hackers develop new malware downloaders to infect victims in Israel”*【11†L43-L51】. Publisher: Recorded Future (The Record); Reliability: B (journalistic outlet quoting ESET).  
- **ESET Research (21 Sep 2023)** – *“Iran-aligned OilRig group deployed new malware to its Israeli victims…”*【25†L101-L109】. Publisher: ESET; Reliability: A (vendor research).  
- **MITRE ATT&CK (last mod 12 May 2026)** – *Magic Hound (Group G0059, APT35)*【19†L52-L61】, *OilRig (Group G0049, APT34)*【17†L51-L59】. Reliability: A (consensus CTI).  
- **The Hacker News (26 Jun 2025)** – *“Iranian APT35 Hackers Targeting Israeli Tech Experts…”*【30†L65-L74】. Publisher: HackerNews (citations to Check Point); Reliability: B.  
- **DarkReading (14 Dec 2023)** – *“OilRig targets Israel’s critical infrastructure…”*【9†L150-L159】. Publisher: TechTarget; Reliability: B.  

## Evidence Register Updates  
- **Claim:** APT35 (Charming Kitten) is IRGC-affiliated and conducts targeted spear-phishing campaigns. **Source:** Volexity and MITRE【19†L52-L61】【21†L142-L150】. *Label:* Source-reported. *Reliability:* A (Volexity, MITRE). *Confidence:* High.  
- **Claim:** APT35 delivered the custom “PowerStar” backdoor via LNK attachments. **Source:** DarkReading (citing Volexity)【8†L180-L187】. *Label:* Source-reported. *Reliability:* B. *Confidence:* High.  
- **Claim:** APT35 targeted Israeli journalists and tech experts. **Source:** DarkReading【8†L157-L166】; TheHackerNews (CheckPoint)【30†L65-L74】. *Label:* Source-reported. *Reliability:* B. *Confidence:* High.  
- **Claim:** APT34 (OilRig) repeatedly attacks Israeli infrastructure with new cloud-based downloaders. **Source:** DarkReading【9†L150-L159】; Recorded Future【11†L43-L51】. *Label:* Source-reported. *Reliability:* B. *Confidence:* High.  
- **Contradictions/Gaps:** No sources link APT35 to destructive attacks; only espionage reported. Also, no official IOC feeds for APT35 campaigns were found. *Gap:* IoCs and campaign scope remain incomplete (need access to threat intel feeds or victim reports).

## Tool-Intel Updates  
- **PowerStar** – Type: Backdoor malware. Actor: APT35 (Charming Kitten)【8†L180-L187】. Behavior: Downloads from cloud (Backblaze, IPFS), collects system/browser credentials, exfiltrates to C2. *IOC:* detected by Volexity; no public hash. *Handling:* Monitor Endpoint for process outbounds to cloud storage; use behavioral ML for new PowerShell backdoors.  
- **CharmPower** – Older APT35 backdoor (Checkpoint). Actor: APT35. Behavior: similar to PowerStar (data collection). *IOC:* None public.  
- **OilRig Downloaders (SC5k, ODAgent, OilCheck, OilBooster)** – Type: Downloader. Actor: APT34/OilRig【9†L150-L159】【11†L43-L51】. Behavior: use OneDrive/Graph/EWS APIs for C2 and exfil; drop payloads. *IOC:* Reported by ESET (See WeLiveSecurity blog); none included here. *Handling:* Block known IOCs from ESET’s blog, restrict unusual use of MS cloud APIs.  
- **Solar/Mango** – Type: Backdoors. Actor: APT34/OilRig【25†L104-L112】. Behavior: execute tasks (download/execute files); Mango includes anti-heuristic flag. *IOC:* None public. Detection via heuristic analysis for VBS droppers and unusual office file activity.  

## Navigation/Crosslink Recommendations  
- **Actor pages:** Link to MITRE’s “Magic Hound (APT35)” and “OilRig (APT34)” pages【19†L52-L61】【17†L51-L59】 for consolidated TTP references. Include these as cross-links in the actor profile.  
- **Tool pages:** Create or update pages for the *PowerStar* backdoor and *OilRig downloader family*, linking to public analysis (e.g. Volexity’s blog).  
- **TTP matrix:** Incorporate the ATT&CK techniques above into the group’s ATT&CK mapping matrix (highlighting T1566, T1190, T1105, etc).  
- **Hunts/Detections:** Add hunt rules for spear-phishing and scanning behaviors to a central “Hunt Hypotheses” page; link the detection hypotheses above.  
- **Worked cases:** Reference public cases (Israeli journalist, June 2025 phishing) in an incidents page.  
- **Persona claims:** Cross-link Monica Witt (former U.S. defector) if including broader Charming Kitten context (Monica Witt case linked to APT35 historically).  

## Gaps and Follow-Up Collection Plan  
- **Gap:** No publicly available IOC repository or YARA for PowerStar or OilRig tools. *Plan:* Obtain samples via malware sharing communities (e.g. OTX) or request CISA/ISC feeds; analyze Indicators.  
- **Gap:** Limited visibility into non-Israeli targets of APT35. *Plan:* Collect open-source intelligence on APT35 campaigns in Europe/U.S. to infer broader patterns.  
- **Gap:** Attribution beyond IRGC is unclear. *Plan:* Seek HUMINT or SIGINT reports on unit assignments; review recent CISA/MSS advisories for links.  
- **Hunt plan:** Based on above hypotheses, implement detections for Exchange exploitation (log Correlate proxyShell indicators) and unusual cloud API usage (audit logs of OneDrive/Graph).  
- **Telemetry needs:** Ensure logging of Office 365 activities (GAL exports, OAuth grants), network HTTP/HTTPS logs (to identify Backblaze/IPFS), and endpoint process executions. Set long enough lookbacks (6–12 months) due to APT35’s slow campaigns.  
- **Priorities:** Validate APT35 presence by correlating an Israeli victim incident (via media or law enforcement) with these TTPs. Collect data from those victims’ logs as case studies.  

*This report synthesizes all public findings through 2025. Higher-confidence source-reported facts are distinguished from analyst inferences. Any claims marked as “Gap” require direct intelligence or forensic data not publicly available.*  

**Sources:** See Source Register above【8†L147-L155】【21†L142-L150】【25†L131-L134】【30†L65-L74】, among others, for dates and context.
