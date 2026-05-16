---
title: Actor Navigation Workbench
sidebar_label: Actor Workbench
---

# Actor Navigation Workbench

Use this page as the click-through hub from an actor to its structured TTPs, IOC reference locations, malware/tool references, mapped hunts, mapped detections, and evidence records.

The page is generated from repository CSV/register data. It is an analyst navigation aid, not an attribution shortcut.

## Actor Coverage Matrix

| Actor | Priority | TTPs | IOC refs | Tools | Hunts | Detections | Evidence | Intel leads |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [MuddyWater](../actors/muddywater.md) | High | 4 | 4 | 26 | 2 | 2 | 1 | 1 |
| [OilRig](../actors/oilrig.md) | High | 2 | 1 | 31 | 0 | 0 | 2 | 1 |
| [Magic Hound](../actors/apt35.md) | High | 2 | 0 | 14 | 1 | 1 | 1 | 1 |
| [APT42](../actors/apt42.md) | High | 3 | 2 | 3 | 1 | 1 | 2 | 1 |
| [Agrius](../actors/agrius.md) | High | 2 | 1 | 10 | 1 | 1 | 1 | 1 |
| [CyberAv3ngers](../actors/cyberav3ngers.md) | High | 3 | 1 | 2 | 1 | 1 | 3 | 0 |
| [Imperial Kitten](../actors/imperial-kitten.md) | High | 3 | 0 | 2 | 0 | 0 | 1 | 1 |
| [Pioneer Kitten](../actors/pioneer-kitten.md) | High | 3 | 0 | 1 | 2 | 2 | 1 | 1 |
| [DarkBit](../actors/darkbit.md) | High | 2 | 0 | 1 | 0 | 0 | 1 | 0 |
| [Lyceum](../actors/lyceum.md) | High | 2 | 0 | 12 | 0 | 0 | 1 | 1 |
| [Cotton Sandstorm](../actors/cotton-sandstorm.md) | High | 3 | 1 | 1 | 1 | 1 | 1 | 0 |
| [APT39](../actors/apt39.md) | Medium | 2 | 0 | 11 | 0 | 0 | 1 | 1 |
| [APT-C-23](../actors/arid-viper.md) | High | 2 | 3 | 7 | 0 | 0 | 1 | 1 |
| [UNC3890](../actors/unc3890.md) | Medium-High | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| [Cyber Toufan](../actors/cyber-toufan.md) | Medium-High | 3 | 0 | 1 | 1 | 1 | 1 | 0 |
| [Void Manticore / Handala](../actors/handala.md) | High | 7 | 2 | 9 | 2 | 2 | 2 | 1 |
| [Lebanese Cedar](../actors/lebanese-cedar.md) | Medium | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| [WIRTE](../actors/wirte.md) | High | 5 | 2 | 2 | 2 | 2 | 1 | 1 |
| [TA402](../actors/ta402.md) | Medium-High | 2 | 2 | 1 | 0 | 0 | 1 | 2 |
| [UNC1860](../actors/unc1860.md) | High | 5 | 2 | 9 | 1 | 1 | 2 | 0 |
| [Scarred Manticore](../actors/scarred-manticore.md) | High | 5 | 0 | 1 | 1 | 1 | 1 | 0 |

## Actor Drilldowns

### MuddyWater {#muddywater}

- Actor workbench: [MuddyWater](actor-workbench.md#muddywater)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](ttp-detection-matrix.md#t1566) Phishing (M2); [T1059.001](ttp-detection-matrix.md#t1059001) PowerShell (M2); [T1219](ttp-detection-matrix.md#t1219) Remote Access Software (M3); [T1567.002](ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M2)
- Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context (Pilot, DRL-6); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MITRE-G0069` Technique references; `SRC-AP-MUDDYWATER` Malware/tool references; ATT&CK mappings; campaign IOCs; `SRC-THREAT-HUNTER-V3` Domains; IPs; Rclone destinations; Dindoor/Fakeset references; `SRC-INCD-MUDDYWATER-2024` Domains; hashes; tools; infrastructure; TTPs
- Tool detail pages: [`Remote Monitoring and Management tools`](../tools/remote-monitoring-and-management-tools.md); [`Dindoor`](../tools/dindoor.md); [`Fakeset`](../tools/fakeset.md); [`BugSleep`](../tools/bugsleep.md); [`BlackBeard`](../tools/blackbeard.md); [`Fooder / MuddyViper`](../tools/fooder-muddyviper.md); [`ConnectWise`](../tools/connectwise.md); [`CrackMapExec`](../tools/crackmapexec.md); [`DCHSpy`](../tools/dchspy.md); [`Empire`](../tools/empire.md); [`Koadic`](../tools/koadic.md); [`LaZagne`](../tools/lazagne.md); [`LP-Notes`](../tools/lp-notes.md); [`Mimikatz`](../tools/mimikatz.md); [`Mori`](../tools/mori.md); [`Out1`](../tools/out1.md); [`PowerSploit`](../tools/powersploit.md); [`POWERSTATS`](../tools/powerstats.md); [`PowGoop`](../tools/powgoop.md); [`Rclone`](../tools/rclone.md); [`RemoteUtilities`](../tools/remoteutilities.md); [`RustyWater`](../tools/rustywater.md); [`SHARPSTATS`](../tools/sharpstats.md); [`Small Sieve`](../tools/small-sieve.md); [`STARWHALE`](../tools/starwhale.md); [`Tsundere Botnet`](../tools/tsundere-botnet.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#muddywater) (26 mapped tool row(s))
- Evidence records: `EVD-004` / `CLM-MUDDYWATER-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-MUDDYWATER`, `SRC-CP-BUGSLEEP`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-MITRE-G0069`, `SRC-THREAT-HUNTER-V3`


### OilRig {#oilrig}

- Actor workbench: [OilRig](actor-workbench.md#oilrig)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm); [Internet-Facing Servers, Webshells, And Passive Access](surface-capability-matrix.md#edge-webshell); [Email, Cloud-Service, IMAP, And DNS C2](surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1505.003](ttp-detection-matrix.md#t1505003) Web Shell (M3); [T1049](ttp-detection-matrix.md#t1049) System Network Connections Discovery (M1)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-MITRE-G0049` Technique references
- Tool detail pages: [`OilBooster`](../tools/oilbooster.md); [`Saitama`](../tools/saitama.md); [`BONDUPDATER`](../tools/bondupdater.md); [`certutil`](../tools/certutil.md); [`ftp`](../tools/ftp.md); [`Helminth`](../tools/helminth.md); [`ipconfig`](../tools/ipconfig.md); [`ISMInjector`](../tools/isminjector.md); [`LaZagne`](../tools/lazagne.md); [`Mango`](../tools/mango.md); [`Mimikatz`](../tools/mimikatz.md); [`Net`](../tools/net.md); [`netstat`](../tools/netstat.md); [`ngrok`](../tools/ngrok.md); [`ODAgent`](../tools/odagent.md); [`OilCheck`](../tools/oilcheck.md); [`OopsIE`](../tools/oopsie.md); [`PowerExchange`](../tools/powerexchange.md); [`POWRUNER`](../tools/powruner.md); [`PsExec`](../tools/psexec.md); [`QUADAGENT`](../tools/quadagent.md); [`RDAT`](../tools/rdat.md); [`Reg`](../tools/reg.md); [`RGDoor`](../tools/rgdoor.md); [`SampleCheck5000`](../tools/samplecheck5000.md); [`SEASHARPEE`](../tools/seasharpee.md); [`SideTwist`](../tools/sidetwist.md); [`Solar`](../tools/solar.md); [`Systeminfo`](../tools/systeminfo.md); [`Tasklist`](../tools/tasklist.md); [`ZeroCleare`](../tools/zerocleare.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#oilrig) (31 mapped tool row(s))
- Evidence records: `EVD-013` / `CLM-OILRIG-001`; `EVD-014` / `CLM-OILRIG-002`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-ESET-OILRIG-ISRAEL`, `SRC-MITRE-G0049`, `SRC-UNIT42-OILRIG-DNS-TUNNELING`


### Magic Hound {#magic-hound}

- Actor workbench: [Magic Hound](actor-workbench.md#magic-hound)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](surface-capability-matrix.md#identity-mdm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566.002](ttp-detection-matrix.md#t1566002) Spearphishing Link (M2); [T1583.001](ttp-detection-matrix.md#t1583001) Acquire Domains (M1)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: None currently mapped.
- Tool detail pages: [`FRP / Plink`](../tools/frp-plink.md); [`Mimikatz / SQLMap / Havij`](../tools/mimikatz-sqlmap-havij.md); [`CharmPower`](../tools/charmpower.md); [`DownPaper`](../tools/downpaper.md); [`Impacket`](../tools/impacket.md); [`ipconfig`](../tools/ipconfig.md); [`Mimikatz`](../tools/mimikatz.md); [`Net`](../tools/net.md); [`netsh`](../tools/netsh.md); [`Ping`](../tools/ping.md); [`PowerLess`](../tools/powerless.md); [`PsExec`](../tools/psexec.md); [`Pupy`](../tools/pupy.md); [`Systeminfo`](../tools/systeminfo.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#magic-hound) (14 mapped tool row(s))
- Evidence records: `EVD-015` / `CLM-APT35-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G0059`


### APT42 {#apt42}

- Actor workbench: [APT42](actor-workbench.md#apt42)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](surface-capability-matrix.md#identity-mdm); [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1530](ttp-detection-matrix.md#t1530) Data from Cloud Storage (M1); [T1102](ttp-detection-matrix.md#t1102) Web Service (M1); [T1566.002](ttp-detection-matrix.md#t1566002) Spearphishing Link (M3)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MANDIANT-APT42` Domains; malware hashes; infrastructure; `SRC-PROOFPOINT-IRAN-CONFLICT-2026` Phishing infrastructure; lure domains; campaign indicators
- Tool detail pages: [`POWERPOST`](../tools/powerpost.md); [`NICECURL`](../tools/nicecurl.md); [`TAMECAT`](../tools/tamecat.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt42) (3 mapped tool row(s))
- Evidence records: `EVD-003` / `CLM-APT42-001`; `EVD-016` / `CLM-APT42-002`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-GOOGLE-APT42-PHISHING`, `SRC-MANDIANT-APT42`, `SRC-MITRE-G1044`, `SRC-PROOFPOINT-IRAN-CONFLICT-2026`


### Agrius {#agrius}

- Actor workbench: [Agrius](actor-workbench.md#agrius)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Destructive Operations, Backup Deletion, And Wipers](surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1485](ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1486](ttp-detection-matrix.md#t1486) Data Encrypted for Impact (M2)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs
- IOC reference sources: `SRC-MITRE-G1030` Technique references
- Tool detail pages: [`Moneybird`](../tools/moneybird.md); [`BlackShadow`](../tools/blackshadow.md); [`Apostle`](../tools/apostle.md); [`ASPXSpy`](../tools/aspxspy.md); [`BFG Agonizer`](../tools/bfg-agonizer.md); [`DEADWOOD`](../tools/deadwood.md); [`IPsec Helper`](../tools/ipsec-helper.md); [`Mimikatz`](../tools/mimikatz.md); [`MultiLayer Wiper`](../tools/multilayer-wiper.md); [`NBTscan`](../tools/nbtscan.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#agrius) (10 mapped tool row(s))
- Evidence records: `EVD-017` / `CLM-AGRIUS-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G1030`


### CyberAv3ngers {#cyberav3ngers}

- Actor workbench: [CyberAv3ngers](actor-workbench.md#cyberav3ngers)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](surface-capability-matrix.md#ot-plc)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T0883](ttp-detection-matrix.md#t0883) Internet Accessible Device (M2); [T0836](ttp-detection-matrix.md#t0836) Modify Parameter (M2); [T0832](ttp-detection-matrix.md#t0832) Manipulation of View (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: `SRC-CISA-AA23-335A` IP; device exposure; affected product context
- Tool detail pages: [`Unitronics Vision PLC Web/HMI`](../tools/unitronics-vision-plc-webhmi.md); [`IOControl`](../tools/iocontrol.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cyberav3ngers) (2 mapped tool row(s))
- Evidence records: `EVD-002` / `CLM-CYBERAV3NGERS-001`; `EVD-009` / `CLM-CYBERAV3NGERS-002`; `EVD-026` / `CLM-CYBERAV3NGERS-003`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CISA-AA23-335A`, `SRC-CISA-AA26-097A`, `SRC-CLAROTY-IOCONTROL-2024`


### Imperial Kitten {#imperial-kitten}

- Actor workbench: [Imperial Kitten](actor-workbench.md#imperial-kitten)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1189](ttp-detection-matrix.md#t1189) Drive-by Compromise (M2); [T1071.003](ttp-detection-matrix.md#t1071003) Mail Protocols (M3); [T1059.005](ttp-detection-matrix.md#t1059005) Visual Basic (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`IMAPLoader`](../tools/imaploader.md); [`StandardKeyboard`](../tools/standardkeyboard.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#imperial-kitten) (2 mapped tool row(s))
- Evidence records: `EVD-018` / `CLM-IMPERIALKITTEN-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CS-IMPERIAL-KITTEN-2023`, `SRC-PWC-YELLOW-LIDERC-2023`


### Pioneer Kitten {#pioneer-kitten}

- Actor workbench: [Pioneer Kitten](actor-workbench.md#pioneer-kitten)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](surface-capability-matrix.md#identity-mdm); [Internet-Facing Servers, Webshells, And Passive Access](surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1219](ttp-detection-matrix.md#t1219) Remote Access Software (M2); [T1572](ttp-detection-matrix.md#t1572) Protocol Tunneling (M2)
- Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context (Pilot, DRL-6); [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths; [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`NGROK / Ligolo`](../tools/ngrok-ligolo.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#pioneer-kitten) (1 mapped tool row(s))
- Evidence records: `EVD-019` / `CLM-PIONEERKITTEN-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CISA-AA24-241A`


### DarkBit {#darkbit}

- Actor workbench: [DarkBit](actor-workbench.md#darkbit)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Destructive Operations, Backup Deletion, And Wipers](surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1486](ttp-detection-matrix.md#t1486) Data Encrypted for Impact (M2); [T1490](ttp-detection-matrix.md#t1490) Inhibit System Recovery (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`DarkBit ransomware`](../tools/darkbit-ransomware.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#darkbit) (1 mapped tool row(s))
- Evidence records: `EVD-020` / `CLM-DARKBIT-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-INCD-DARKBIT-MUDDYWATER-2023`, `SRC-MS-MERCURY-DEV1084-2023`


### Lyceum {#lyceum}

- Actor workbench: [Lyceum](actor-workbench.md#lyceum)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](surface-capability-matrix.md#ot-plc)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1071.004](ttp-detection-matrix.md#t1071004) DNS (M2); [T1003.001](ttp-detection-matrix.md#t1003001) LSASS Memory (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`DanBot`](../tools/danbot.md); [`Kevin`](../tools/kevin.md); [`Shark`](../tools/shark.md); [`BITSAdmin`](../tools/bitsadmin.md); [`DnsSystem`](../tools/dnssystem.md); [`Empire`](../tools/empire.md); [`ipconfig`](../tools/ipconfig.md); [`Milan`](../tools/milan.md); [`Mimikatz`](../tools/mimikatz.md); [`netstat`](../tools/netstat.md); [`Ping`](../tools/ping.md); [`PoshC2`](../tools/poshc2.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#lyceum) (12 mapped tool row(s))
- Evidence records: `EVD-021` / `CLM-LYCEUM-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G1001`


### Cotton Sandstorm {#cotton-sandstorm}

- Actor workbench: [Cotton Sandstorm](actor-workbench.md#cotton-sandstorm)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1585](ttp-detection-matrix.md#t1585) Establish Accounts (M1); [T1204.002](ttp-detection-matrix.md#t1204002) User Execution: Malicious File (M3); [T1566](ttp-detection-matrix.md#t1566) Phishing (M3)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-CP-WEZRAT` Email sender; domains; hashes; C2 paths; malware behavior
- Tool detail pages: [`WezRat`](../tools/wezrat.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cotton-sandstorm) (1 mapped tool row(s))
- Evidence records: `EVD-022` / `CLM-COTTONSANDSTORM-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CP-WEZRAT`, `SRC-FBI-EMENNET-2024`, `SRC-MS-IRAN-IO`


### APT39 {#apt39}

- Actor workbench: [APT39](actor-workbench.md#apt39)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566.001](ttp-detection-matrix.md#t1566001) Spearphishing Attachment (M2); [T1003.001](ttp-detection-matrix.md#t1003001) LSASS Memory (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Remexi`](../tools/remexi.md); [`ANTAK / ASPXSPY`](../tools/antak-aspxspy.md); [`Cadelspy`](../tools/cadelspy.md); [`CrackMapExec`](../tools/crackmapexec.md); [`ftp`](../tools/ftp.md); [`MechaFlounder`](../tools/mechaflounder.md); [`Mimikatz`](../tools/mimikatz.md); [`NBTscan`](../tools/nbtscan.md); [`PsExec`](../tools/psexec.md); [`pwdump`](../tools/pwdump.md); [`Windows Credential Editor`](../tools/windows-credential-editor.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt39) (11 mapped tool row(s))
- Evidence records: `EVD-027` / `CLM-APT39-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G0087`


### APT-C-23 {#apt-c-23}

- Actor workbench: [APT-C-23](actor-workbench.md#apt-c-23)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1660](ttp-detection-matrix.md#t1660) Phishing (M2); [T1204.002](ttp-detection-matrix.md#t1204002) User Execution: Malicious File (M3)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-META-ARIDVIPER` Domains; apps; mobile indicators; `SRC-CYBERNEWS-REDALERT-2026` App names; package references; domains from secondary coverage; `SRC-S1-ISRAEL-HAMAS-CYBER-2023` Actor context; mobile and social-engineering references
- Tool detail pages: [`AridSpy`](../tools/aridspy.md); [`RedAlert.apk`](../tools/redalertapk.md); [`Desert Scorpion`](../tools/desert-scorpion.md); [`FrozenCell`](../tools/frozencell.md); [`Micropsia`](../tools/micropsia.md); [`Phenakite`](../tools/phenakite.md); [`SpyC23`](../tools/spyc23.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt-c-23) (7 mapped tool row(s))
- Evidence records: `EVD-011` / `CLM-ARIDVIPER-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CYBERNEWS-REDALERT-2026`, `SRC-ESET-ARIDSPY`, `SRC-META-ARIDVIPER`, `SRC-MITRE-G1028`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`


### UNC3890 {#unc3890}

- Actor workbench: [UNC3890](actor-workbench.md#unc3890)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1189](ttp-detection-matrix.md#t1189) Drive-by Compromise (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-MANDIANT-UNC3890` Punycode domains; malware references; infrastructure
- Tool detail pages: [`SUGARUSH / SUGARDUMP`](../tools/sugarush-sugardump.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#unc3890) (1 mapped tool row(s))
- Evidence records: `EVD-025` / `CLM-UNC3890-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-MANDIANT-UNC3890`, `SRC-SECWEEK-UNC3890`


### Cyber Toufan {#cyber-toufan}

- Actor workbench: [Cyber Toufan](actor-workbench.md#cyber-toufan)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](surface-capability-matrix.md#ot-plc); [Destructive Operations, Backup Deletion, And Wipers](surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1491](ttp-detection-matrix.md#t1491) Defacement (M2); [T1595](ttp-detection-matrix.md#t1595) Active Scanning (M1); [T1021.002](ttp-detection-matrix.md#t1021002) SMB/Windows Admin Shares (M3)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Cyber Toufan supplier-access playbook`](../tools/cyber-toufan-supplier-access-playbook.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cyber-toufan) (1 mapped tool row(s))
- Evidence records: `EVD-023` / `CLM-CYBERTOUFAN-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-MS-IRAN-HAMAS`, `SRC-OPI-CYBER-TOUFAN`


### Void Manticore / Handala {#void-manticore-handala}

- Actor workbench: [Void Manticore / Handala](actor-workbench.md#void-manticore-handala)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](surface-capability-matrix.md#identity-mdm); [Destructive Operations, Backup Deletion, And Wipers](surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](ttp-detection-matrix.md#t1566) Phishing (M2); [T1204](ttp-detection-matrix.md#t1204) User Execution (M2); [T1485](ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1490](ttp-detection-matrix.md#t1490) Inhibit System Recovery (M2); [T1567](ttp-detection-matrix.md#t1567) Exfiltration Over Web Service (M2); [T1078.004](ttp-detection-matrix.md#t1078004) Valid Accounts: Cloud Accounts (M3)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-AP-HANDALA` IP/CIDR; hashes; URLs; actor channels; soft IOCs; `SRC-THREAT-HUNTER-V3` Domains; IPs; file names; driver names; behavioral IOCs
- Tool detail pages: [`BiBi / BiBi Wiper lineage`](../tools/bibi-bibi-wiper-lineage.md); [`Handala-linked destructive installer chains`](../tools/handala-linked-destructive-installer-chains.md); [`CHIMNEYSWEEP`](../tools/chimneysweep.md); [`ftp`](../tools/ftp.md); [`Impacket`](../tools/impacket.md); [`Mimikatz`](../tools/mimikatz.md); [`RawDisk`](../tools/rawdisk.md); [`ROADSWEEP`](../tools/roadsweep.md); [`ZeroCleare`](../tools/zerocleare.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#void-manticore-handala) (9 mapped tool row(s))
- Evidence records: `EVD-005` / `CLM-HANDALA-001`; `EVD-006` / `CLM-HANDALA-002`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-HANDALA`, `SRC-MITRE-G1055`, `SRC-PUSH-STRYKER-HANDALA`, `SRC-THREAT-HUNTER-V3`


### Lebanese Cedar {#lebanese-cedar}

- Actor workbench: [Lebanese Cedar](actor-workbench.md#lebanese-cedar)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Internet-Facing Servers, Webshells, And Passive Access](surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1505.003](ttp-detection-matrix.md#t1505003) Web Shell (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: `SRC-CLEARSKY-LEBANESE-CEDAR` Webshell paths; malware references; vulnerable products
- Tool detail pages: [`Explosive RAT`](../tools/explosive-rat.md); [`Caterpillar WebShell`](../tools/caterpillar-webshell.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#lebanese-cedar) (2 mapped tool row(s))
- Evidence records: `EVD-012` / `CLM-LEBANESECEDAR-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CLEARSKY-LEBANESE-CEDAR`


### WIRTE {#wirte}

- Actor workbench: [WIRTE](actor-workbench.md#wirte)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](ttp-detection-matrix.md#t1566) Phishing (M2); [T1574.001](ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking (M3); [T1485](ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1105](ttp-detection-matrix.md#t1105) Ingress Tool Transfer (M3); [T1567.002](ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M3)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-CP-WIRTE-2024` Wiper references; trusted sender abuse; fake update artifacts; `SRC-UNIT42-ASHTAG-2025` Malware hashes; domains; C2 paths; tool behavior
- Tool detail pages: [`SameCoin`](../tools/samecoin.md); [`AshTag`](../tools/ashtag.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#wirte) (2 mapped tool row(s))
- Evidence records: `EVD-010` / `CLM-WIRTE-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CP-WIRTE-2024`, `SRC-UNIT42-ASHTAG-2025`


### TA402 {#ta402}

- Actor workbench: [TA402](actor-workbench.md#ta402)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](surface-capability-matrix.md#endpoint-rmm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566.001](ttp-detection-matrix.md#t1566001) Spearphishing Attachment (M3); [T1574.001](ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking (M3)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-PROOFPOINT-TA402-IRONWIND` Domains; payload hashes; attachment chain details; `SRC-S1-ISRAEL-HAMAS-CYBER-2023` Actor context; lure and malware family references
- Tool detail pages: [`IronWind`](../tools/ironwind.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#ta402) (1 mapped tool row(s))
- Evidence records: `EVD-024` / `CLM-TA402-001`
- Intel update candidates: [2 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-PROOFPOINT-TA402-IRONWIND`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`


### UNC1860 {#unc1860}

- Actor workbench: [UNC1860](actor-workbench.md#unc1860)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](surface-capability-matrix.md#ot-plc); [Internet-Facing Servers, Webshells, And Passive Access](surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1505.003](ttp-detection-matrix.md#t1505003) Web Shell (M2); [T1105](ttp-detection-matrix.md#t1105) Ingress Tool Transfer (M2); [T1021.001](ttp-detection-matrix.md#t1021001) Remote Services: RDP (M2); [T1078](ttp-detection-matrix.md#t1078) Valid Accounts (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: `SRC-MALPEDIA-UNC1860` Associated malware families; references; taxonomy; `SRC-MANDIANT-UNC1860` Tooling; passive backdoors; webshells; access-enablement references
- Tool detail pages: [`TEMPLEDOOR`](../tools/templedoor.md); [`TEMPLEPLAY`](../tools/templeplay.md); [`CRYPTOSLAY`](../tools/cryptoslay.md); [`PipeSnoop`](../tools/pipesnoop.md); [`STAYSHANTE`](../tools/stayshante.md); [`SASHEYAWAY`](../tools/sasheyaway.md); [`VIROGREEN`](../tools/virogreen.md); [`TEMPLEDROP`](../tools/templedrop.md); [`TEMPLELOCK`](../tools/templelock.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#unc1860) (9 mapped tool row(s))
- Evidence records: `EVD-001` / `CLM-UNC1860-001`; `EVD-008` / `CLM-UNC1860-002`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-MALPEDIA-UNC1860`, `SRC-MANDIANT-UNC1860`


### Scarred Manticore {#scarred-manticore}

- Actor workbench: [Scarred Manticore](actor-workbench.md#scarred-manticore)
- TTP-to-detection matrix: [all mapped techniques](ttp-detection-matrix.md)
- Surface and capability routes: [Internet-Facing Servers, Webshells, And Passive Access](surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1505.004](ttp-detection-matrix.md#t1505004) IIS Components (M2); [T1505.003](ttp-detection-matrix.md#t1505003) Web Shell (M2); [T1071.001](ttp-detection-matrix.md#t1071001) Web Protocols (M2); [T1199](ttp-detection-matrix.md#t1199) Trusted Relationship (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Liontail`](../tools/liontail.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#scarred-manticore) (1 mapped tool row(s))
- Evidence records: `EVD-007` / `CLM-SCARRED-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CP-SCARRED-MANTICORE-2023`, `SRC-CP-VOID-2024`
