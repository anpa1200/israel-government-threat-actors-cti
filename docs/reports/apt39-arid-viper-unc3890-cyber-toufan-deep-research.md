---
title: APT39 Arid Viper UNC3890 Cyber Toufan Deep Research Intake
sidebar_label: APT39 / Arid Viper / UNC3890 / Cyber Toufan
---

:::caution Analyst validation required
This page is an imported deep-research artifact. Treat it as lead-generation material until claims, citations, URLs, hashes, and detection logic are validated against primary public sources and repository evidence standards.
:::

# APT39 (Chafer / Remix Kitten)

**Executive Summary (Israeli public-sector focus):** APT39 is an Iran-linked cyber espionage group (affiliated with MOIS) active since ~2014, focused on intelligence collection from travel/telecom sectors and personal data.  Public sources (FBI, Treasury, MITRE) confirm its MOIS sponsorship and targeting of travel, hospitality, academic, and telecom industries【28†L28-L36】【31†L186-L194】.  Recent open intelligence on APT39 is very limited; no reports of new 2023–2026 intrusions were found.  In July 2025 a researcher (Nariman Gharib) reported an airline-system intrusion (“Trailblazer” malware) attributed to APT39, but this is not an official government or vendor report【24†L70-L78】【24†L93-L101】.  Overall, Israeli relevance appears low (no Israeli victims publicly reported); travel and logistics remain APT39’s core focus.  Known APT39 tools include web shells (ANTAK, ASPXSPY), backdoors (Seaweed, CacheMoney, POWBAT, MechaFlounder/Cachalote, *etc.*), credential-dumping tools (Mimikatz, WCE), and network scanners (CrackMapExec, BLUETORCH)【31†L152-L160】【42†L1-L4】.  Hunting should focus on detecting anomalous Office 365 Graph API traffic (as reported for Trailblazer【24†L84-L93】), BITS upload activity, unscheduled VBScript/AutoIt tasks (per FBI Flash), and AMSI bypass (as seen in memory-patching wiper variants).  Given the lack of public 2023+ reporting, APT39’s current activity level is a **Gap**: defenders should maintain readiness (given its MOIS ties) but have no confirmed recent incidents.

**Actor Identity:** APT39 (aka Chafer, ITG07, “Rana Intelligence” front) is an Iranian state-sponsored espionage group.  The US Treasury and FBI explicitly designate “Advanced Persistent Threat 39” as a fronted MOIS operation via Rana Intelligence Computing【28†L28-L36】. Public synonyms include Chafer, *Remix Kitten*, Cadelspy, Remexi, and ITG07【28†L28-L36】【24†L70-L78】.  Vendor naming (“Remix Kitten” etc.) aligns; no conflicting taxonomy was found.  

**Sponsor/Command:** APT39 is *directly sponsored by Iran’s Ministry of Intelligence and Security (MOIS)*.  The FBI/DOJ note: “Rana Intelligence…is a MOIS front company…known in the public domain as…APT39”【28†L28-L36】.  U.S. Treasury sanctions likewise tie APT39 and Rana to MOIS【27†L228-L236】【28†L28-L36】.  We found no evidence of any other sponsor or external contractors; all sources point to MOIS (not IRGC or proxy groups) as sponsor. No public “public persona” is used beyond the Rana cover. 

**Israel/Region Relevance:** APT39 has *no documented Israeli victims*.  All open reports highlight global targets (e.g. travel industry worldwide) and Iranian dissidents but do not mention Israeli entities【28†L33-L41】【31†L186-L194】.  A recent (July 2025) report of APT39 accessing airline reservation systems covered carriers in Jordan, Qatar, Russia and others【24†L70-L78】【24†L93-L101】 – still no Israel.  If anything, APT39’s threat to Israel would be indirect (e.g. exfiltrating global passenger data) rather than known domestic compromises. Therefore, *Israeli-sector relevance is low*, with this gap likely to remain unless future intel emerges. 

**Intrusion Lifecycle:** Based on FBI and vendor reports【28†L28-L36】【31†L141-L149】, APT39 typically uses spearphishing with malicious Office attachments or links for initial access (T1566).  It also registers decoy domains and exploits public websites to drop web shells (ANTAK, ASPXSPY) for persistence【31†L141-L149】.  For execution, APT39 injects custom payloads (POWBAT C# backdoor, Seaweed, CacheMoney, Remexi/Cachelote, etc.) directly into memory【31†L152-L160】【37†L32-L40】. Privilege escalation and credential access use tools like Mimikatz, WCE, and Ncrack【31†L152-L160】.  Lateral movement is via RDP/SSH, PsExec, RemCom, WinRM, or custom proxies (REDTRIP, PINKTRIP, BLUETRIP)【31†L162-L168】.  Defense evasion includes AMSI/antivirus bypass (e.g. memory-patching in Trailblazer【24†L119-L128】).  C2 is HTTP(S) to impersonated services (the FBI flash shows HTTP GET/POST beacon patterns【33†L25-L34】【33†L36-L44】; recent media notes Graph API usage【24†L84-L93】).  Exfiltration uses BITS and compression (WinRAR/7z)【31†L162-L168】.  Impact so far is intelligence collection (PNR/travel data), with some reported operational effects (airline outages【24†L100-L109】), but no known data destruction in open sources. 

**ATT&CK Mapping:** We map APT39’s behaviors as follows (examples with evidence):

| Technique ID | Name                               | Tactic             | Observable Example               | Source (label)            | Quality |
|-------------|------------------------------------|--------------------|----------------------------------|--------------------------|---------|
| T1566.001   | Spearphishing Attachment           | Initial Access     | Phishing Office docs leading to POWBAT【31†L141-L149】 (source-reported) | M3      |
| T1190       | Exploit Public-Facing Application  | Initial Access     | Webshell installation on public sites【31†L141-L149】 (source) | M3      |
| T1543.003   | Windows Service                    | Persistence        | ASPXSPY webshell (maintains code execution)【31†L141-L149】 (assessed) | M2      |
| T1059.005   | Compiled HTML File                 | Execution          | VBS/AutoIt malware executing as dropped (FBI flash notes VBS)【17†L5-L14】 (source) | M3      |
| T1059.001   | PowerShell                         | Execution          | POWBAT (C# backdoor) via PowerShell or C#【31†L141-L149】 (source) | M3      |
| T1059.003   | Windows Command Shell              | Execution          | CLI commands in remediated tools (implied use)【31†L152-L160】 (assessed) | M3      |
| T1559.001   | Inter-Process (SOCKS) proxy        | Lateral Movement   | REDTRIP/PINKTRIP creating SOCKS proxies【31†L162-L168】 (source) | M3      |
| T1027.002   | Obfuscated Files or Info (C2)      | Defense Evasion    | Tools repacked (FBI: safe modifications)【31†L177-L184】 (source) | M3      |
| T1071.001   | Exfil over Web Service (HTTP)      | Exfiltration       | BITS exfil to HTTP C2【33†L25-L34】 (source) | M3      |
| T1071.004   | Exfil over FTP                     | Exfiltration       | (FBI: sending via FTP scripts)【33†L37-L44】 (source) | M3      |
| T1110       | Brute Force (Ncrack)              | Privilege Escal.   | Ncrack used for credential bruting【31†L152-L160】 (source) | M3      |

*(Sources: FBI/MITRE/Google Blog). Mapping quality: M3 = strong support from cited sources.*  

**Known Tools/Families:** APT39 uses custom and common tools:
- **Seaweed (Backdoor)** – custom C# backdoor for Windows【31†L152-L160】.
- **CacheMoney/Remexi (Backdoor)** – custom malware; documented by Symantec (2015) and Malpedia【37†L32-L40】.  We did not find direct modern references to Remexi except Malpedia labels.
- **POWBAT/Cachalote (Backdoor)** – custom memory-resident loader; used for initial payload delivery【31†L141-L149】.
- **ANTAK, ASPXSpy (Webshells)** – IIS webshells used to maintain access【31†L141-L149】.
- **CrackMapExec (Post-exploit tool)** – used to enumerate network shares【42†L7-L9】.
- **Mimikatz, WCE, Ncrack, ProcDump** – credential dumping and maintenance【31†L152-L160】.
- **REDTRIP/PINKTRIP/BLUETRIP (Custom HTTP(S) Tunnels)** – create SOCKS5 tunnels for lateral movement【31†L162-L168】.
- **Trailblazer (Proprietary C# loader)** – reported by researchers (July 2025) using AMSI patching【24†L119-L128】.
For each tool, no public malware hashes were provided by cited sources; IoCs (hashes/domains) appear only in the 2020 FBI flash (e.g. `jquery-stack.online` C2, etc.), which defenders should reference from official advisories. 

**Public IOCs:** We rely on vetted sources. The FBI **FLASH Alert (Sep 2020)** provides extensive IOCs (malware hashes, domains like `saveingone.com`, YARA rules)【33†L49-L58】.  Example IOC: APT39’s ASPX webshell beacon to `jquery-stack.online` (note: FBI has removed IOC list from this excerpt).  No new IOCs were found post-2020.  (For details, see the FBI’s APT39 ICS advisory and the Public Intelligence Alert【28†L28-L36】.) 

**Detection & Hunting Hypotheses:** 

1. **Suspicious Office 365 Telemetry:** Monitor outbound HTTPS to `graph.microsoft.com` or unusual Graph API calls by non-business processes (APT39’s 2025 “Trailblazer” C2 was camouflaged as Graph traffic【24†L84-L93】). *Telemtry:* Web proxy/DNS logs, Office 365 API logs. *False Positives:* Legitimate Azure functions. *Escalation:* identify if associated with known APT39 beacon patterns or start times.

2. **In-memory Patching/AMSI Bypass:** Hunt for processes hooking `AmsiScanBuffer` (user-mode code signature modifying AMSI)【24†L119-L128】. *Telemetry:* OS kernel events (ETW, Sysmon v10+), memory scanning via EDR. *False Positives:* Rare for benign apps. *Escalation:* Backup and inspect memory or dumps for unknown code.

3. **Scheduled Tasks Creating Apps:** APT39 used VBS/AutoIt scripts written to AppData Taskbar dirs【33†L1-L10】. Hunt for odd Scheduled Tasks (e.g. every 2 min) named like Windows tasks but residing in `%APPDATA%\microsoft\Taskbar\`【33†L1-L10】. *Telemetry:* Sysmon FileCreate on these paths; Task registration events. *False Positives:* Legit data; calibrate for known apps. *Escalation:* Investigate related process execution.

4. **BITS Transfer Jobs:** Detect abnormal BITS transfers to non-Microsoft domains. *Telemetry:* Windows Event 7033/7034 (BITS). *False Positives:* Legit downloads. *Escalation:* Investigate source/destination of payloads and registry of tasks after BITS job.

5. **Suspicious Admin Tools Execution:** Identify runs of WCE, ProcDump, any suspicious binaries (names from FBI table【33†L119-L128】). *Telemetry:* Process creation logs with parent=explorer for these tools. *False Positives:* Admin usage. *Escalation:* Check context; correlate with concurrent webshell or domain compromise.

6. **Credential Dumping:** Monitor authentication logs for Kerberos ticket misuse or LSASS memory reads by abnormal processes (e.g. Sysmon T1003 alerts). *Telemetry:* Event ID 4624 anomalies, LSA secret read. *False Positives:* Domain admin tasks. *Escalation:* If followed by external RDP/SMB connections.

7. **Webshell Access:** Look for IIS (w3wp.exe) loading atypical DLLs or calling unusual endpoints. *Telemetry:* IIS logs (POST to .asp/UPDATE); Sysmon network connect. *False Positives:* Admin scripts. *Escalation:* Compare with known ASPXSpy signatures.

8. **CME Usage:** CME often runs with metchium or network scanning patterns (accounts queries). *Telemetry:* Uncommon high-volume SMB/LDAP from workstation. *False Positives:* Pen-tester. *Escalation:* Confirm if authorized.

Each hunt ties to ATT&CK mappings (e.g. AMSI bypass=T1560.006, scheduled tasks=T1053.005, BITS=T1570, etc). False positives should be assessed by cross-checking against known admin activity. 

**Source Register Updates:**  

| Publisher        | Title                                                                        | Date        | URL                                                 | Accessed   | Superseded | Reliability |
|------------------|------------------------------------------------------------------------------|-------------|-----------------------------------------------------|------------|------------|-------------|
| US Dept. of Justice (FBI)【28】 | *Indicators of Compromise Associated with Rana Intelligence Computing…APT39* | 2020-09-17  | https://www.iranwatch.org/library/governments/...    | 2026-05-16 | No         | A           |
| MITRE ATT&CK【2】          | *APT39, ITG07, Chafer…Group G0087*                                      | 2024-04-??  | https://attack.mitre.org/groups/G0087/              | 2026-05-16 | No         | A           |
| Google Cloud (Mandiant)【31】 | *APT39 – Iranian Threat Group…*                                       | 2019-01-29  | https://cloud.google.com/blog/topics/threat-intelligence/apt39-iranian-cyber-espionage-group-focused-on-personal-information | 2026-05-16 | No         | B           |
| Nariman Gharib/CybersecurityNews【24】 | *Iran’s Cyber Actors Attacking Global Airlines…*                      | 2025-07-22  | https://cybersecuritynews.com/irans-cyber-actors-attacking-global-airlines | 2026-05-16 | No         | C           |
| Infoblox【11】       | *APT39 Malicious Activity and Tools*                                      | 2020-09-22  | https://labs.infoblox.com/...                        | 2026-05-16 | No         | B           |
| Huntress【5】       | *Remix Kitten Threat Actor Profile*                                       | 2023-06-01  | https://huntress.com/...                             | 2026-05-16 | No         | C           |

**Evidence Register:** (sample entries)

| Claim                                                                                     | Actor  | Source        | Quote/Paraphrase                                                                                                 | Label          | Reliability | Confidence | Notes/Gaps        |
|-------------------------------------------------------------------------------------------|--------|---------------|------------------------------------------------------------------------------------------------------------------|---------------|-------------|------------|------------------|
| APT39 (Rana) is a MOIS front company in Tehran【28†L28-L36】.                               | APT39  | FBI (2020)【28】  | “Rana… is a Ministry of Intelligence and Security (MOIS) front company… known as APT39, Chafer…”                  | Source-reported | A           | High       |                  |
| APT39 targets travel, hospitality, academic, and telecommunications industries【28†L33-L41】. | APT39  | FBI (2020)【28】  | “targeted… primarily in the travel, hospitality, academic, and telecommunications industries.”                     | Source-reported | A           | High       |                  |
| APT39 uses webshells (ANTAK, ASPXSPY) and stolen creds to infect OWA【31†L141-L149】.        | APT39  | Google/Mandiant【31】| “identified and exploited vulnerable web servers… to install web shells, such as ANTAK and ASPXSPY, and used stolen… credentials to compromise… Outlook Web Access.” | Source-reported | B           | High       |                  |
| APT39 has used CrackMapExec for network scanning/shares【42†L1-L4】.                        | APT39  | MITRE【42】      | “APT39 has used CrackMapExec… to enumerate network shares.”                                                       | Source-reported | A           | High       |                  |
| No recent public reports of APT39 activity found (post-2020)                              | APT39  | (none)        | — *No citation* —                                                                                               | Gap            | C (N/A)     | Low        | no source of recent ops |

**Tool-Intelligence Updates:** 

| Tool Name       | Type         | Confidence (Actor uses) | Behavior/Notes                                             | Hash/IOC Ref (if any) | Source             | Detection/Handling Notes                |
|-----------------|--------------|-------------------------|------------------------------------------------------------|-----------------------|--------------------|-----------------------------------------|
| Seaweed         | Backdoor     | Confirmed (source)      | Custom C# backdoor for data exfiltration【31†L152-L160】.   | —                     | Mandiant Google   | Monitor for Seaweed network patterns.   |
| CacheMoney/Remexi | Backdoor   | Confirmed (source)      | Windows backdoor (aka Remexi/Cachelote)【37†L32-L40】.      | —                     | Symantec (2015)   | Look for old Remexi YARA (if any).      |
| ASPXSpy (webshell) | WebShell  | Confirmed (source)      | IIS webshell used for persistence【31†L141-L149】.          | —                     | Mandiant Google   | Detect abnormal POSTs to .asp pages.    |
| ANTAK (webshell)| WebShell     | Confirmed (source)      | IIS webshell (documented by Google blog)【31†L141-L149】.    | —                     | Mandiant Google   | Same as above (IIS detection).          |
| CrackMapExec   | Pen-testing tool | Confirmed (source)   | Used for network share enumeration【42†L7-L9】.            | —                     | MITRE ATT&CK     | Flag CME runs outside pentests.         |
| POWBAT         | Loader       | Confirmed (source)      | .NET backdoor injection tool (named by FireEye)【31†L141-L149】. | —                  | Mandiant Google   | Monitor for PowerShell loads.           |

*(Hashes are not publicly provided in sources; use vendor YARAs where available.)*

**Navigation/Crosslinks:** Update actor page (APT39), link to “Chafer” detection stories; tool pages for Seaweed, CacheMoney, ASPXSpy; Att&CK TTP matrix; hunt/pat-hypothesis pages for travel sector; any case studies on travel data exfil; persona claims (e.g. leaked KASDA news? none public). 

**Gaps & Follow-up:** No public 2023+ technical reports were found. We lack evidence on whether APT39 is currently active (“Gap: no recent public reporting”). Official confirmation of Nariman Gharib’s airline campaign would help; obtaining that would require either vendor analysis (perhaps independent security lab report) or intel from a regional CERT. We also lack open attribution connecting APT39 directly to any Israeli victim (Gap for relevance). If activity is dormant, intelligence should revisit by 2026 for resumption.  

# APT-C-23 / Arid Viper

**Executive Summary:** APT-C-23 (aliases Arid Viper, Desert Falcon) is a Palestinian/Hamas-aligned espionage group active since ~2014. It has *specifically targeted Israeli military personnel* (often via social engineering) and regional targets with Android/iOS spyware.  Public sources (MITRE, SentinelOne) describe “Hamas-aligned” interests and a history of mobile malware use【49†L28-L36】【47†L154-L163】.  Recent reporting (2022–2023) confirms continued espionage campaigns: SentinelOne observed new **SpyC23** Android spyware (distributed as fake Telegram or “Skipped Messenger” apps) through 2023【49†L28-L36】【49†L49-L57】.  The group also developed “Arid Gopher” (Go-based stealer) and BarbWire (Windows backdoor) to target Israeli defense and law enforcement【51†L90-L100】.  No new *official* state-sponsored source emerged since 2023, so details are primarily from security vendors.  We assess APT-C-23’s sponsor as Hamas-linked (possibly IRGC-supported), per multiple sources【49†L28-L36】【51†L84-L90】. Tools include multiple Android spyware families (SpyC23, FrozenCell/VolatileVenom, Phenakite iOS implant) and some Windows malware. Detection should focus on mobile telemetry: DNS for known C2 domains (related to Skipped/Telegram lures), SMS/MMS content siphoning, and unusual app-store/MDM events. Phishing through social networks (e.g. catfishing via Facebook/Tinder) remains a primary initial vector. Because activity is ongoing and targeting Israeli interests (IDF, contractors), APT-C-23 is an **active threat**.

**Actor Identity:** Known as APT-C-23 (MITRE ID G1028) with aliases *AridViper, Desert Falcon, TAG-63, Two-tailed Scorpion*, etc【44†L50-L57】.  The MITRE description explicitly ties it to Israeli military targeting in the Middle East【44†L50-L57】. Vendor names include “Mantis” (Symantec) and “Gaza Cyber Gang”. No serious naming conflicts found.

**Sponsor/Command:** Public assessments label APT-C-23 as *Hamas-aligned*.  SentinelOne: “Hamas-aligned threat actor”【49†L28-L36】.  CFR’s tracker calls it “Pro-Hamas” with “suspected state sponsor: Palestine, State of” (implying Hamas)【47†L154-L163】.  No government has officially charged or designated this actor; sources are vendor/CERT analysis. No evidence of direct Iran/MOIS control, though regional alignment suggests indirect Iranian support is possible (some vendors have noted links to Gaza). We label “sponsor: Hamas or Hamas-affiliated” (analytic).

**Israel/Region Relevance:** High. APT-C-23 explicitly targets Israeli military and security sectors. For example, the CFR notes “Previously targeted Israeli soldiers by pretending to be women”【47†L154-L163】. The SpyC23 campaigns targeted users in Egypt and Palestine (ESET)【49†L28-L36】, and Symantec reported attacks on Israeli defense/law enforcement with Windows backdoors【51†L90-L100】. We have strong confidence in relevance. (Gap: No public Israeli victim names given, but attacker communications claim IDF targets.)

**Intrusion Lifecycle:**  Initial access is often via social engineering and mobile app trickery. Attackers catfish soldiers via social media and lure them to install spyware apps (fake Telegram, dating apps, “security update” apps)【49†L28-L36】.  Android spyware families (SpyC23, FrozenCell, VAMP, GnatSpy) request extensive permissions to harvest SMS, contacts, calls, location【49†L28-L36】【49†L43-L52】.  The iOS Phenakite malware (short-lived) also exfiltrated device data.  Some phishing emails are used (e.g. Windows BarbWire was delivered via spear-phish【51†L90-L100】).  No evidence of advanced privilege escalation or lateral movement is reported; they seem to keep data on mobile or local PCs.  Collected data (contacts, GPS, images, audio) is exfiltrated directly via the mobile apps’ C2.  C2 domains and push-notification systems (Firebase) have been identified in reports.  Impact: primarily intelligence collection on military targets and surveillance. We did not see destructive actions reported.

**ATT&CK Mapping:** Mapping is divided into Enterprise and Mobile:

- **Initial Access (Mobile Tactic):** T1204.002 *Malicious File*, T1566 (phishing) – via malicious apps/links【49†L28-L36】【51†L94-L101】.
- **Execution:** T1059 (unspecified) for BarbWire, T1532 (software development tools) for custom malware, T1625.001 *Match Legit Name* for fake apps【49†L28-L36】.
- **Persistence:** T1422 *System Network Configuration Discovery* – apps gather device info including IMSI【44†L124-L132】.
- **Privilege Escalation:** N/A (mobile, relies on user consent and permissions).
- **Defense Evasion:** T1609 *Network Proxy* – mobile proxies, T1560.001 *Archive Collected Data* (app compresses/exfiltrates data)【44†L129-L137】.
- **Credential Access:** T1422 (collect phone metadata)【44†L124-L132】, T1400 series (app auto collection).
- **Discovery:** T1056 (keylogging), T1083 (file discovery) – smartphone equivalents.
- **Lateral/Collection (Mobile):** T1475 *Boot or Logon Autostart Execution* – apps modify shortcuts, T1221 *Web Data* (browser/exfiltration)【44†L129-L137】.
- **Exfiltration:** T1422 (SMS), T1105 (download new code/run-time).
- **Mobile (non-enterprise) Techniques:** e.g. T1655.002 *Match Name*, T1660 *Phishing for info*【44†L112-L121】.

Each technique is backed by reports: e.g. SpyC23 uploads to AWS API and Firebase (Talos), and apps matching legitimate names【44†L113-L122】.  Mapping quality: M3 if directly cited (e.g. T1660 by MITRE【44†L119-L123】), M2 if inferred.

**Associated Families/Tools:** 
- **SpyC23** – Android spyware (distributed via fake Telegram/Update apps)【49†L28-L36】.
- **FrozenCell (VolatileVenom)** – Android espionage trojan (Symantec, Lookout【51†L77-L80】).
- **Phenakite** – iOS spyware (short-lived; see MITRE【44†L147-L157】).
- **Micropsia** (aka ViperRat) – Windows data stealer (TheHackerNews【51†L77-L80】).
- **BarbWire** – Custom Windows backdoor (Symantec, April 2022)【51†L90-L100】.
- **GnatSpy/VAMP** – older Android malware (Talos/Sentinel references GnatSpy, VAMP【49†L43-L52】).
- **RedAlert.apk** – rumored app (not confirmed in published sources; likely refers to telecom sector spyware, but we found no open docs).
- **AridSpy** – not found in open sources.
- **Delivery/Infrastructure:** Weaponized Telegram/Feb 2021 messaging apps, FCM endpoints for payloads.
No public IOC list is given; security reports list Google/Firebase hostnames (e.g. `skippedtestinapp.firebaseio.com`【49†L79-L87】).

**Public IOCs:** Security vendors have published limited IOCs. For example, SentinelOne noted non-malicious (“Skipped Messenger”) and malicious versions sharing a Firebase host【49†L79-L87】. Talos/Cisco and others have identified C2 domains. The OP Innovate playbook (May 2025) mentions targeted MSP domains and leaked credentials but cites no specific IOCs beyond “Bezeq, Partner” as affected entities. We find no official IOC appendices to cite; rely on vendor blogs. No IoC table here to avoid disallowed leaked data. 

**Detection & Hunting:**
1. **Mobile Installers:** Use MDM logs or Google Play Protect logs to detect unknown enterprise-signed or third-party apps (e.g. modified “Skipped Messenger”, “Telegram Update”). Monitor devices for installations outside corporate store (TidelOps).
2. **Excessive App Permissions:** Alert on new apps requesting Accessibility, SMS, location, call permissions on company-managed phones (tags from SpyC23 findings【49†L97-L106】).
3. **Firebase/FCM C2 Traffic:** Detect network flows to suspicious Firebase hosts (e.g. `skippedtestinapp.firebaseio.com`【49†L79-L87】) or AWS endpoints. Look for encrypted beacon patterns from mobile endpoints.
4. **Credential Harvesting Alerts:** Look for mass SMS/email exfiltration from a device after new app install. E.g. endpoints suddenly sending user SMS or contacts to external IPs.
5. **Catfish Social Media Monitoring:** While not technical telemetry, monitor for phishing lures (e.g. decoy social profiles) via threat intelligence feeds. (Escalation: notify SOC of targeted users.)
6. **Role-Based Alerts:** The group targets known Israeli soldier personnel. Monitor network activity or phishing attempts aimed at known reservists (if IDF personnel are on rosters).
7. **Windows BarbWire Detection:** On endpoints, alert on unknown executables receiving files via email from unknown addresses (see Symantec report on BarbWire delivery).
8. **MDM Anomaly:** For enterprise devices, monitor flagged devices that have offline enterprise MDM or sideloaded apps (since many victims might use personal devices).

**Source Register Updates:**  

| Publisher        | Title                                                        | Date        | URL                                         | Accessed   | Superseded | Reliability |
|------------------|--------------------------------------------------------------|-------------|---------------------------------------------|------------|------------|-------------|
| MITRE ATT&CK【44】       | *APT-C-23 (Arid Viper)*                              | 2024-11-17  | https://attack.mitre.org/groups/G1028/       | 2026-05-16 | No         | A           |
| SentinelOne【49】      | *Arid Viper: Android Spyware Continues to Target…*    | 2023-11-06  | https://sentinelone.com/labs/arid-viper…     | 2026-05-16 | No         | B           |
| TheHackerNews【51】    | *Arid Viper Hacking Group Using Upgraded Malware…*   | 2023-04-04  | https://thehackernews.com/2023/04/arid-viper... | 2026-05-16 | No         | C           |
| Lookout【49】         | *Malware Profile: ViperRat (Arid Viper)*             | 2023-08-21  | https://www.lookout.com/threat-intel/viperrat  | 2026-05-16 | No         | B           |
| OP Innovate【67】     | *Eye of the Storm: Cyber Toufan Playbook* (context)  | 2025-05-26  | https://op-c.net/blog/cyber-toufan-attack-playbook | 2026-05-16 | No         | B (professional blog) |

**Evidence Register (APT-C-23):**  

| Claim                                                           | Actor        | Source        | Quote                                                                                              | Label             | Reliability | Confidence | Contradictions/Gaps |
|-----------------------------------------------------------------|--------------|---------------|----------------------------------------------------------------------------------------------------|------------------|-------------|------------|--------------------|
| APT-C-23 is Hamas-aligned targeting Israeli military via fake social media personas【47†L154-L163】. | APT-C-23     | CFR/CyberOps【47】   | “Previously targeted Israeli soldiers by pretending to be women… Suspected state sponsor: Palestine, State of.” | Source-reported | B           | High       |                    |
| Uses Android spyware (SpyC23) via fake Telegram/dating apps【49†L28-L36】. | APT-C-23     | SentinelOne【49】    | “distributed SpyC23… through weaponized apps posing as Telegram or a dating app called Skipped.”          | Source-reported | B           | High       |                    |
| Employed custom Windows backdoor (BarbWire) in 2022 against IDF-related targets【51†L90-L100】. | APT-C-23     | TheHackerNews【51】 | “targeting Israeli individuals in defense, law enforcement… novel Windows backdoor BarbWire.”             | Source-reported | C           | Med        | Only vendor-level source |
| Focus on mobile C2 via Firebase and fake SMS alerts (Talos analysis) | APT-C-23     | SentinelOne【49】    | (Implied: Firebase use and messaging lures in SpyC23 campaign)                                         | Assessed        | C           | Medium     | Indirect inference  |

**Tool-Intelligence Updates (APT-C-23):**

| Tool Name           | Type           | Confidence | Behavior/Notes                            | IOC Ref (if any)  | Source           | Detection Notes                        |
|---------------------|----------------|------------|-------------------------------------------|-------------------|------------------|----------------------------------------|
| SpyC23 (Android)    | Mobile RAT     | Confirmed  | Collects SMS, contacts, location; C2 via FCM| —                | SentinelOne【49】| Look for known package names and net connections. |
| FrozenCell/Venmo    | Mobile RAT     | Confirmed  | Weaponized messenger app; FCM C2            | —                | TheHackerNews【51】| Monitor cloud messaging patterns.     |
| Phenakite (iOS)     | Mobile RAT     | Confirmed  | iOS backdoor (no longer active)            | —                | MITRE【44】      | Hard to detect (iOS forensic only).   |
| BarbWire (Windows)  | Backdoor       | Confirmed  | Auth stealing backdoor (delivered via phishing) | —            | TheHackerNews【51】| Flag unknown executables with network I/O. |

**Navigation/Crosslinks:** Update actor page (APT-C-23), TTP pages for Mobile espionage, tool pages (SpyC23, FrozenCell, BarbWire), detection guide (mobile hunting, see #14 strategy blogs), persona pages (social media catfishing). Link to youth outreach/counterphishing materials.

**Gaps/Follow-up:** No new classification beyond existing vendor reports. Public timeline: last big disclosure was 2023. Gap: no governmental or vendor updates since late 2023. Would benefit from official CERT advisories or published IoCs (none seen). Human intelligence on group’s sponsor (Hamas vs IRGC) remains “assessed” only. Acquire MDM logs from Israeli defense organizations for anomalous app installs as evidence.  

# UNC3890

**Executive Summary:** *UNC3890* is an uncategorized Iranian cyber cluster (per Mandiant) that targeted Israeli shipping and critical infrastructure sectors starting ~2020.  Mandiant’s 2022 report (Google Cloud blog) links UNC3890 to Iran【60†L90-L99】 and describes unique malware (SUGARUSH backdoor, SUGARDUMP credential harvester) used in spear-phish and watering-hole attacks.  ClearSky (2023) further associates it with a recent watering-hole on Israeli shipping sites【57†L30-L36】.  While active through 2022, we found **no public 2023–2026 updates** confirming ongoing UNC3890 activity.  No evidence suggests merger with other known clusters: Mandiant explicitly tracked it as separate【60†L123-L132】.  If UNC3890 is still operating, its targeting (maritime, energy, healthcare) remains highly relevant to Israeli critical infrastructure. We rate it as *Watchlist/Active*: technically significant, but lacking fresh public intel. Hunts should examine maritime-sector web servers and fake login pages tied to presumed UNC3890 C2. 

**Actor Identity:** *UNC3890* is a Mandiant label for an Iranian threat cluster (no other common name).  Malpedia: “Suspected Iranian threat activity cluster… aimed at Israeli shipping, government, energy, and healthcare”【58†L19-L27】.  No aliases known.  Occasional mention as related to “Tortoiseshell (Imperial Kitten)” watering holes, but UNC3890 remains distinct in literature. 

**Sponsor/Command:** Mandiant assesses UNC3890 as *Iranian-run*, possibly IRGC-linked.  The blog states “moderate confidence this actor is linked to Iran”【60†L80-L88】, citing Persian artifacts and targeting. The Times of Israel likewise reports “linked to Iran”【61†L175-L184】. No explicit mention of MOIS vs IRGC; Mandiant notes technical overlap with known IRGC-linked UNC2448 (APT35) but treats UNC3890 as standalone【60†L129-L138】. Thus: state sponsor = Iran (probable IRGC, not Hamas or Hezbollah). 

**Israel/Region Relevance:** Very high. UNC3890 specifically targeted Israeli shipping, ports, energy, and related sectors【60†L80-L89】【60†L150-L159】. The 2022 Mandiant study and ClearSky’s 2023 analysis both focus on Israeli waterborne logistics websites. Also attacked Israeli government and healthcare【60†L80-L89】【61†L162-L170】. Confidence: High. (No gap here.)

**Intrusion Lifecycle:** According to Mandiant【60†L100-L108】【58†L19-L27】, UNC3890 used *social engineering/watering holes* for access.  Spear-phishing (fake job offers, tech support) and compromised ports (watering-hole JavaScript) were observed.  The 2023 ClearSky report implicates watering-hole scripts (watering-hole tech to collect user data) on maritime sites【57†L30-L36】.  After initial compromise, unique tools were deployed: 
- **SUGARUSH:** custom backdoor (likely persists as Windows service or task)【58†L23-L30】. 
- **SUGARDUMP:** browser credential stealer (exfiltrates via email to Gmail/Yahoo/Yandex)【58†L23-L30】. 
Common tools like Metasploit and the NorthStar C2 framework were also used【60†L100-L108】. UNC3890 ran fake O365/LinkedIn login pages for credential harvesting【58†L23-L30】.  Impact appears limited to data collection (credentials, possibly initial staging); no destructive acts reported. 

**ATT&CK Mapping:** Based on Mandiant:

- **Initial Access:** T1190 (waterhole) – UNC3890 hosted malicious JS on legitimate shipping sites【57†L25-L33】. T1566 (phishing) – fake emails with fake job postings/coupons【61†L219-L228】.
- **Execution:** T1053.005 (Scheduled Task) – SUGARUSH likely installs as a task/service. T1059 (various) – SUGARDUMP executed via browser context.
- **Persistence:** T1547.001 (Registry Run Keys) – hypothetical for SUGARUSH (not explicitly stated).
- **Credential Access:** T1056 (Input Capture) – SUGARDUMP (browser stealer)。【58†L23-L30】.
- **Defense Evasion:** T1564.001 (Hidden Files) – fake domains masked in HTML. Watering-hole uses innocuous JS names (jQuery clones)【57†L37-L46】.
- **Discovery:** T1083 (File and Directory Discovery) – custom backdoor likely collects host info.
- **Lateral Movement:** (not heavily reported, likely limited).
- **Collection:** T1119 (Automated Collection) – browser data, network config, collected via SUGARDUMP.
- **Exfiltration:** T1041 (Exfil over C2) – SUGARDUMP sends to email via SMTP; T1570 (Exfil Over Network) – watering-hole sends data to attacker servers.
  
(Source references: [60], [58], [61], [57].) Mapping quality M2–M3.

**Associated Tools/Families:**  
- **SUGARUSH (Backdoor)** – custom Win32 backdoor (Mandiant origin, no public hash).
- **SUGARDUMP (Credential-Stealer)** – browser stealer (from UNC3890).
- **NorthStar C2** – multi-protocol framework used for C2【60†L100-L108】.
- **Metasploit** – publicly used exploit framework【60†L100-L108】.
- **jqury-stack.online** – domain attributed to TA456 but UNC3890 used similar domains【57†L25-L33】.
No IOC lists published; Table of contents or FBI YARA (from 2020 FBI alert) has specific C2 URLs (e.g. `jquery-stack.online`). 

**Public IOCs:** Mandiant and ClearSky posts contain examples: e.g. the ClearSky PDF lists `jquery-stack.online` as TA456 C2【57†L25-L33】, and noted jQuery impersonators (`jguery.net`, etc)【57†L25-L33】. Mandiant mentioned domains spoofing Office365/LinkedIn (but gave none by name). We would say “Official IOCs are in Mandiant 2022 and ClearSky 2023 reports (domains, email exfil addresses)【58†L23-L30】【57†L25-L33】.” No easy list here to quote without revealing all. 

**Detection & Hunting:** 

1. **Watering-Hole Indicators:** Monitor known Israeli maritime site code (e.g. embedded JS) for new external calls. *Telemetry:* Web proxy logs, DomainResolver. *False Positives:* Real analytics. *Escalation:* If analytics scripts call uncommon domains (e.g. malware IPs). 
2. **Web Credential Phishing:** Detect logins to O365/LinkedIn clones (domain register, HTTPS certs). *Telemetry:* TLS SNI logs, certificate monitoring. *False Positives:* Corporate login sites. *Escalation:* Host blocks, incident response.
3. **SMTP Exfil Signs:** Hunt for automated emails from endpoints to external accounts with large attachments (possible SUGARDUMP to Gmail/Yahoo)【58†L23-L30】. *Telemetry:* Email gateway logs. *False:* People using personal email. *Escalation:* Identify exfil contents, verify as malicious.
4. **Browser Memory Access:** On endpoints, look for unusual browser processes accessing memory or disk in suspicious ways. *Telemetry:* Endpoint EDR (T1056 monitoring). *False:* Some plugins. *Escalation:* Inspect process trees.
5. **Admin Tools on Shipping Infra:** Any Metasploit usage or network scanning from shipping companies (suggested by tools). *Telemetry:* NIDS, firewall logs. *False:* IT maintenance. *Escalation:* Review scanning vectors.
6. **Hash-based detection:** If available from private intelligence (e.g. SUGARUSH hash from Mandiant). We have none public, so skip.

**Source Register Updates:**  

| Publisher        | Title                                                               | Date        | URL                                    | Accessed   | Superseded | Reliability |
|------------------|---------------------------------------------------------------------|-------------|----------------------------------------|------------|------------|-------------|
| Mandiant (Google)【60】 | *UNC3890: Suspected Iranian Actor Targeting Israeli Shipping…* | 2022-08-17  | https://cloud.google.com/blog/...       | 2026-05-16 | No         | A           |
| ClearSky【57】   | *Fata Morgana: Watering hole attack on shipping and logistics…*      | 2023-05-??  | https://www.clearskysec.com/...         | 2026-05-16 | No         | A           |
| Times of Israel【61】 | *Iran-linked hacking group targeting Israeli shipping…*         | 2023-03-01  | https://www.timesofisrael.com/...       | 2026-05-16 | No         | B           |

**Evidence Register (UNC3890):**  

| Claim                                                               | Actor     | Source              | Quote                                                                                              | Label          | Reliability | Confidence | Notes/Gaps   |
|---------------------------------------------------------------------|-----------|---------------------|----------------------------------------------------------------------------------------------------|---------------|-------------|------------|--------------|
| UNC3890 targets Israeli shipping, gov’t, healthcare (2020–2022)【60†L78-L87】. | UNC3890   | Mandiant【60】        | “targeting Israeli shipping, government, energy and healthcare organizations”                      | Source-reported| A           | High       |              |
| UNC3890 linked to Iran (moderate confidence)【60†L90-L99】.         | UNC3890   | Mandiant【60】        | “assesses with moderate confidence this actor is linked to Iran”                                   | Source-reported| A           | High       |              |
| Uses proprietary SUGARUSH backdoor and SUGARDUMP stealer【58†L23-L30】. | UNC3890   | Malpedia (Mandiant data)【58】| “deployed… backdoor named ‘SUGARUSH’ and… credential stealer called ‘SUGARDUMP’”                 | Source-reported| A           | High       |              |
| Used watering-hole on Israeli shipping site (ClearSky 2023)【57†L30-L36】. | UNC3890   | ClearSky【57】       | “Mandiant… named UNC3890 was targeting shipping companies… using the same watering hole”           | Source-reported| A           | High       |              |
| No public reports after 2022 (post-2022: Gap)                       | UNC3890   | —                    | *No source*                                                                                        | Gap            | C           | Low        | No new intel  |

**Tool-Int Updates (UNC3890):**  

| Tool/Family  | Type        | Confidence | Behavior                                      | IOC Reference | Source    | Detection Notes                              |
|--------------|-------------|------------|-----------------------------------------------|---------------|-----------|----------------------------------------------|
| SUGARUSH     | Backdoor    | Confirmed  | Windows backdoor (presumably injected service)| —             | Mandiant【60】 | Monitor unknown services or process trees.    |
| SUGARDUMP    | Credential Stealer | Confirmed  | Browser credential exfil (emails to Gmail/Yahoo)| —           | Mandiant【60】 | Flag unusual SMTP from endpoints.             |
| NorthStar C2 | Framework   | Confirmed  | C2 framework (HTTP/C2 channels)               | —             | Mandiant【60】 | Hard to detect (TLS traffic analysis needed). |
| Watering-hole JS | Exploit kit | Confirmed | Malicious JS on Iranian sites (boats)         | —             | ClearSky【57】 | Compare web content against known libraries. |

**Navigation/Crosslinks:** Link UNC3890 page to “Maritime attacks” taxonomy, tool pages (SugarRush, Sugardump if exist), relevant logs/incidents, overlap with OilRig/ImperialKitten pages. 

**Gaps/Follow-up:** We have no public 2023+ updates on UNC3890. It’s unclear if the actor remains active or merged. We mark “Gap: no recent confirmed activity.” Further collection (e.g. from Israeli CERT, shipping industry CERT) would help. Also, we lack details on whether overlap with “Tortoiseshell (Imperial Kitten)” or others is real – current sources only note similarity in TTP (water-holing)【57†L30-L36】. Official data from victim networks (water-company logs) would strengthen detection.  

# Cyber Toufan

**Executive Summary:** *Cyber Toufan* is a self-proclaimed pro-Palestinian/Hamas hacktivist persona (active since late 2023) known for mass compromise claims and data destruction.  Sources (OP Innovate, FalconFeeds, Jerusalem Post) characterize it as an *Iran-linked, ideologically motivated* group【63†L75-L84】【67†L173-L182】.  It aggressively targets Israeli defense, telecom, infrastructure, and allied organizations, often via supply-chain breaches and exploiting basic security weaknesses【65†L114-L122】【67†L199-L207】.  The actor publicly leaks stolen data (via Telegram) and deploys destructive payloads (e.g. POKYBLIGHT wiper) on symbolic dates【63†L139-L148】【64†L19-L27】. Cyber Toufan’s TTPs are unsophisticated: no zero-days, but successful credential reuse, VPN abuse, and weak MFA exploitation. Israeli-sector defenders should treat Cyber Toufan as an active threat requiring aggressive detection of stolen credentials and secondary wiper deployments.  (Caveat: Much of what is “known” is from open-source and OP Innovate analysis, not a government advisory.)

**Actor Identity:** Cyber Toufan presents as a distinct group/persona; no other alias known. (FalconFeeds calls it “Cyber Toufan (CT)”【63†L75-L84】.) Some analysts caution it may be a *persona* for an Iranian proxy operation, but this is unresolved. For our purposes, we treat “Cyber Toufan” as the actor name, TLP:CLEAR persona.  

**Sponsor/Command:** All evidence suggests Iranian sponsorship. Microsoft Threat Intel Center calls Cyber Toufan “Iran-sponsored”【63†L163-L171】. OP Innovate and JP cite it as “pro-Hamas” or “Iran-linked”【65†L83-L91】【67†L138-L147】. No definitive proof is public (CT uses proxies and avoids direct links), but multiple intelligence teams (MTAC, OP Innovate) assess Iranian state backing【63†L163-L171】. We list Sponsor=Iran (likely via Hamas or allied proxies). 

**Israel/Region Relevance:** Extremely high. Cyber Toufan *primarily targets Israeli interests and global entities tied to Israel*. The group claims hundreds of Israeli (and US-linked) organizations as victims【63†L115-L124】. OP Innovate and JPost specifically note Israeli defense firms, telecom suppliers (Bezeq, Partner), and a major Israeli-Australian tank project【65†L83-L92】【67†L173-L182】. We have high confidence in its Israel focus (no suggestion of random global attacks). 

**Intrusion Lifecycle:** According to OP Innovate and FP blogs, Cyber Toufan’s campaigns share a modus operandi: **initial access via credential compromise** rather than exploits.  They exploit leaked/default passwords or missing MFA on VPN/routers of Israeli suppliers (e.g. Bezeq)【65†L114-L122】【67†L199-L207】.  Once inside, they move laterally (often flat networks, broad RDP/SMB abuse) and exfiltrate data.  Attack tools are mostly “living-off-the-land” (Mimikatz, RDP scripts), not elaborate malware.  However, for destructive operations they deploy a proprietary wiper (“POKYBLIGHT”) against Windows and Android【64†L9-L17】【64†L19-L27】.  Exfiltration is followed by public leaks (Telegram dumps). Impact has been both reputational (public leaks of tens of TBs) and occasional data destruction (reported by OP Innovate). 

**ATT&CK Mapping:**  
- **Initial Access:** T1078 (Valid Accounts) – use of default/stolen credentials【67†L199-L207】. T1110 (Brute Force) – likely low-tier password reuse. 
- **Execution:** T1204 (User Execution) – spear-phishing for POKYBLIGHT (emails posing as gov’t alerts【64†L19-L27】). T1059 (various shells) via PsExec or RDP.
- **Persistence:** T1053.005 (Scheduled Task) – possibly for wiper scheduling. 
- **Privilege Escalation:** (often none needed if admin creds obtained).
- **Defense Evasion:** T1564.002 (Hidden Files) – wiper deletes itself; known wiper tradecraft. 
- **Credential Access:** T1003 (LSASS) – Mimikatz or WCE for harvested creds (implied by juicing credentials out of VPNs).
- **Discovery:** T1082 (System Info) – wiper may collect info before wipe. 
- **Lateral Movement:** T1021.002 (SMB) – lateral using SMB/RDP on flat networks. 
- **Collection:** T1113 (Screen Capture), T1056 (Input) – wiper collects/erases data. 
- **Impact:** T1485 (Data Destruction) – POKYBLIGHT wipe, T1490 (Inhibit Response) possibly. 
  (Evidence: OP Innovate confirm no zero-days; credential use; POKYBLIGHT via phishing【64†L19-L27】.)

**Associated Tools/Families:** While “Cyber Toufan” uses generic tools, specific artifacts include: 
- **POKYBLIGHT (Wiper)** – Windows/Android wiper described by FalconFeeds【64†L9-L17】【64†L19-L27】. 
- **Remote tools:** Basic COTS (RDP, PsExec, Mimikatz) for movement. 
- **Exfil Dump Sites:** leak sites (Telegram-based, but not published).
No standard malware family beyond the wiper.  Public hashes: none available. 

**Public IOCs:** There are no vendor-published IoC lists.  OP Innovate and JPost mention victim domains (e.g. Maya tech site) but no indicators.  We note that one site was publicly reported compromised (MAYA), but listing it risks doxing a victim.  The wiper “POKYBLIGHT” is mentioned but no hash given; its distribution URLs (government-alert phishing) are unspecified. Thus we cite these reports conceptually, but do not enumerate IOCs beyond what’s in the narrative.

**Detection & Hunting:** 

1. **Credential Access Monitoring:** Flag any login to VPN/routers (e.g. Partner, Bezeq management systems) using known default credentials or from unusual IPs. *Telemetry:* VPN logs, AAA logs. *False:* Legit tech/support. *Escalation:* Check source IP geo (Saudi/Turkish?), correlate with other suspicious IoCs.
2. **Missing MFA Alerts:** Identify users logging in without MFA where MFA is normally required (failed push), especially on Israeli enterprise accounts. *Telemetry:* Auth logs (Azure AD/IDaaS). *False:* known exceptions. *Escalation:* Force reset and investigation.
3. **Wiper Detection:** Monitor for mass file deletion or modification events on endpoints (T1485). *Telemetry:* Endpoint detection rules for sudden NTFS changes on critical drives. *False:* Ransomware drills? *Escalation:* Rollback from backups, quarantine.
4. **Phishing Email Patterns:** Emails claiming to be from “government security unit” with executable attachments (T1566)【64†L19-L27】. *Telemetry:* Email gateway scanning. *False:* Real advisories. *Escalation:* Block similar emails, warn staff.
5. **Server Tunneling:** Outbound C2 beacons immediately before data deletion. *Telemetry:* Egress network logs, netflow (to unknown IP). *False:* Legit IT traffic. *Escalation:* Inspect payload (small wiper dropper).
6. **Third-Party Alert:** Work with MSPs to vet configurations. Specific measure: notification from Bezeq/Partner if their gear is used.

**Source Register Updates:**  

| Publisher        | Title                                                          | Date       | URL                                           | Accessed   | Superseded | Reliability |
|------------------|----------------------------------------------------------------|------------|-----------------------------------------------|------------|------------|-------------|
| OP Innovate【67】      | *Eye of the Storm: Cyber Toufan Playbook*                 | 2025-05-26 | https://op-c.net/blog/cyber-toufan-attack-playbook | 2026-05-16 | No         | B           |
| FalconFeeds【63】      | *Expert Threat Profile: Cyber Toufan…*                    | 2025-11-14 | https://falconfeeds.io/blogs/cyber-toufan-threat-profile | 2026-05-16 | No         | C           |
| Jerusalem Post【65】   | *Pro-Hamas hackers claim breach of Israeli-Australian...* | 2025-11-09 | https://www.jpost.com/defense-and-tech/article-873267 | 2026-05-16 | No         | B           |

**Evidence Register (Cyber Toufan):**  

| Claim                                                                | Actor        | Source            | Quote                                                                                        | Label           | Reliability | Confidence | Notes/Gaps         |
|----------------------------------------------------------------------|--------------|-------------------|----------------------------------------------------------------------------------------------|-----------------|-------------|------------|--------------------|
| Cyber Toufan claims ~100 breaches, data leaks via Telegram【63†L115-L124】. | Cyber Toufan | FalconFeeds【63】   | “since late 2023… 59 organizations on its Telegram… 40 via an MSP attack”                    | Source-reported | C           | Medium     | Non-primary source |
| Targets include Israeli govt contractors and vendors (Bezeq, Partner)【67†L199-L207】. | Cyber Toufan | OP Innovate【67】   | “attackers… focused on organizations… whose VPN/firewall infrastructure is managed by… Bezeq, Partner.” | Source-reported | B           | High       |                    |
| Uses POKYBLIGHT wiper in strategic phishing (govt alerts)【64†L19-L27】. | Cyber Toufan | FalconFeeds【64】   | “distribution of POKYBLIGHT… was… via phishing emails disguised as… Israeli government security fixes” | Source-reported | C           | Medium     | Single source    |
| Iran-linked hacktivist; multiple intell teams assess Iranian sponsorship【63†L163-L171】. | Cyber Toufan | FalconFeeds【63】   | “MTAC assesses the persona as Iran-sponsored… OP Innovate… Iranian-linked.”               | Source-reported | C           | Medium     | Lacks hard evidence |

**Tool-Int Updates (Cyber Toufan):**  

| Tool/Family   | Type        | Confidence | Behavior                                 | IOC Ref        | Source         | Detection Notes              |
|---------------|-------------|------------|------------------------------------------|----------------|----------------|------------------------------|
| POKYBLIGHT    | Wiper       | Confirmed  | Proprietary Windows/Android wiper【64†】   | —             | FalconFeeds【64】 | Monitor for WMI delete events |
| Mimikatz et al| Privilege   | Likely     | Used credential theft on compromised hosts | —             | OP Innovate【67】| Standard credential alerts    |
| Telegram leak sites | Exfil/distro | Confirmed | Public data dumps via Telegram channels【63†】 | —            | OP Innovate【67】| Not used for detection directly |

**Navigation/Crosslinks:** Link to pages on hacktivist threats (Handala, Iran hacktivists), wiper technique matrix, tools (POKYBLIGHT if added). Add to “Supply-chain risk” guides (VPN vendor security).  

**Gaps/Follow-up:** Much of Cyber Toufan’s “intelligence” comes from open blogs. We lack official confirmation or forensic reports. Key gap: concrete attribution (no forensic tie to Iran beyond assessment). Recommend coalition/industry alerts on credential hygiene, and traceroutes/forensic analysis of claimed wiper campaigns. Future collection: contacting Telegram channel maintainers for malware samples, or forensic triage of victim systems mentioned in news.
