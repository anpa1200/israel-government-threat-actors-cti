---
title: Malicious Tools Index
sidebar_label: Tools Index
---

# Malicious Tools Index

This index links to one defensive page per malware family, implant, web shell, backdoor, wiper, or dual-use tool tracked in `data/tool-intelligence.csv`.

The tool pages are generated. They summarize behavior, hash/IOC availability, actor linkage, source references, hunting notes, mapped detections, and handling rules.

The repository does not store malware binaries, exploit code, credentials, or bulk copied IOC dumps. Hashes are included only when already present in public source reporting and are treated as pivots, not attribution proof.

| Tool | Actor | Type | Confidence | Hash / IOC Status |
| --- | --- | --- | --- | --- |
| [`AridSpy`](aridspy.md) | [APT-C-23](../actors/arid-viper.md) | Mobile RAT | High | Hash not committed; use ESET mobile IOC appendix/current report. |
| [`RedAlert.apk`](redalertapk.md) | [APT-C-23](../actors/arid-viper.md) | Mobile spyware / trojanized app | Low | Hash not committed; provisional until primary Acronis reporting is available. |
| [`ANTAK / ASPXSPY`](antak-aspxspy.md) | [APT39](../actors/apt39.md) | Web shells | Medium | Hash not committed; use source-linked IOCs and local webroot baselines. |
| [`Remexi`](remexi.md) | [APT39](../actors/apt39.md) | Malware / collection tool | Medium | Hash not committed; use MITRE references and original vendor reports. |
| [`NICECURL`](nicecurl.md) | [APT42](../actors/apt42.md) | Backdoor / C2 tool | Medium | Hash not committed; retrieve current IOCs from linked source or vendor appendix. |
| [`POWERPOST`](powerpost.md) | [APT42](../actors/apt42.md) | Script / collection tool | Medium | Hash not committed; source-linked behavior only. |
| [`TAMECAT`](tamecat.md) | [APT42](../actors/apt42.md) | Backdoor / C2 tool | Medium | Hash not committed; retrieve current IOCs from linked source or vendor appendix. |
| [`BlackShadow`](blackshadow.md) | [Agrius](../actors/agrius.md) | Ransomware / persona | Medium | Hash not committed; persona claims require corroboration. |
| [`Moneybird`](moneybird.md) | [Agrius](../actors/agrius.md) | Ransomware / destructive malware | Medium | Hash not committed; source IOC appendix should be used if needed. |
| [`WezRat`](wezrat.md) | [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Modular infostealer / RAT | High | Hash not committed; use Check Point and government IOC references. |
| [`Cyber Toufan supplier-access playbook`](cyber-toufan-supplier-access-playbook.md) | [Cyber Toufan](../actors/cyber-toufan.md) | Credential and admin-interface abuse | Medium | Not malware; no hash. Track claims and exposure indicators. |
| [`IOControl`](iocontrol.md) | [CyberAv3ngers](../actors/cyberav3ngers.md) | OT/IoT malware | High | Hash not committed; use Claroty IOC appendix/current report. |
| [`Unitronics Vision PLC Web/HMI`](unitronics-vision-plc-webhmi.md) | [CyberAv3ngers](../actors/cyberav3ngers.md) | Targeted technology | High | Not malware; no hash. Exposure and configuration indicators only. |
| [`DarkBit ransomware`](darkbit-ransomware.md) | [DarkBit](../actors/darkbit.md) | Pseudo-ransomware / destructive malware | Medium | Hash not committed; incident-specific IOCs should come from INCD/Microsoft source material. |
| [`IMAPLoader`](imaploader.md) | [Imperial Kitten](../actors/imperial-kitten.md) | .NET downloader / loader | High | Hash not committed; use PwC or vendor IOC appendix/current report. |
| [`StandardKeyboard`](standardkeyboard.md) | [Imperial Kitten](../actors/imperial-kitten.md) | Backdoor / C2 tool | Medium | Hash not committed; use CrowdStrike source if available. |
| [`Caterpillar WebShell`](caterpillar-webshell.md) | [Lebanese Cedar](../actors/lebanese-cedar.md) | Web Shell | Medium | Hash not committed; use ClearSky report references. |
| [`Explosive RAT`](explosive-rat.md) | [Lebanese Cedar](../actors/lebanese-cedar.md) | Remote Access Trojan | Medium | Hash not committed; use ClearSky report references. |
| [`DanBot`](danbot.md) | [Lyceum](../actors/lyceum.md) | Remote Access Trojan | Medium | Hash not committed; use MITRE references and primary reports. |
| [`Kevin`](kevin.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Low | Hash not committed; use MITRE references and primary reports. |
| [`Shark`](shark.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Low | Hash not committed; use MITRE references and primary reports. |
| [`FRP / Plink`](frp-plink.md) | [Magic Hound](../actors/apt35.md) | Dual-use tunneling / proxy tooling | Medium | No malware hash; dual-use binary monitoring and local allowlisting required. |
| [`Mimikatz / SQLMap / Havij`](mimikatz-sqlmap-havij.md) | [Magic Hound](../actors/apt35.md) | Public offensive/security tooling | Medium | No stable actor-specific hash; use process, command-line, and control-plane telemetry. |
| [`BlackBeard`](blackbeard.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Medium | Hash not committed; use INCD source-linked IOCs. |
| [`BugSleep`](bugsleep.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | High | Hash not committed; use Check Point IOC appendix/current report. |
| [`Dindoor`](dindoor.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Low | Hash not committed; use source-linked IOCs only. |
| [`Fakeset`](fakeset.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Low | Hash not committed; use source-linked IOCs only. |
| [`Fooder / MuddyViper`](fooder-muddyviper.md) | [MuddyWater](../actors/muddywater.md) | Loader and backdoor | Medium | Hash not committed; validate current ESET IOC availability before operational use. |
| [`Remote Monitoring and Management tools`](remote-monitoring-and-management-tools.md) | [MuddyWater](../actors/muddywater.md) | Living-off-the-land tooling | High | No malware hash; inventory and signed binary allowlist required. |
| [`OilBooster`](oilbooster.md) | [OilRig](../actors/oilrig.md) | Downloader | High | Hash not committed; use ESET IOC appendix/current source. |
| [`Saitama`](saitama.md) | [OilRig](../actors/oilrig.md) | DNS-tunneling backdoor | High | Hash not committed; use Unit 42 IOC references if needed. |
| [`NGROK / Ligolo`](ngrok-ligolo.md) | [Pioneer Kitten](../actors/pioneer-kitten.md) | Tunneling / proxy tooling | High | No malware hash; monitor tool binary, process, account, and network usage against approved admin list. |
| [`Liontail`](liontail.md) | [Scarred Manticore](../actors/scarred-manticore.md) | Passive backdoor framework | High | Hash not committed; use Check Point source report references. |
| [`IronWind`](ironwind.md) | [TA402](../actors/ta402.md) | Initial access downloader / staged malware | High | Hash not committed; use Proofpoint IOC appendix/current report. |
| [`CRYPTOSLAY`](cryptoslay.md) | [UNC1860](../actors/unc1860.md) | Associated family | Medium | Family confirmed by Malpedia; no per-sample hash committed in this repo. |
| [`PipeSnoop`](pipesnoop.md) | [UNC1860](../actors/unc1860.md) | Referenced tool/family term | Low | Reference confirmed by Malpedia; no per-sample hash committed in this repo. |
| [`SASHEYAWAY`](sasheyaway.md) | [UNC1860](../actors/unc1860.md) | Dropper / access-enablement tooling | High | Mandiant publishes activity-level MD5 IOCs and a VT collection; this repo does not map every hash to SASHEYAWAY. |
| [`STAYSHANTE`](stayshante.md) | [UNC1860](../actors/unc1860.md) | Web shell / handoff tooling | High | Mandiant publishes activity-level MD5 IOCs and a VT collection; this repo does not map every hash to STAYSHANTE. |
| [`TEMPLEDOOR`](templedoor.md) | [UNC1860](../actors/unc1860.md) | Passive backdoor family | High | Representative MD5s published by Mandiant for TEMPLEDOOR activity include c57e59314aee7422e626520e495effe0 and b219672bcd60ce9a81b900217b3b5864; use full source IOC list for current coverage. |
| [`TEMPLEDROP`](templedrop.md) | [UNC1860](../actors/unc1860.md) | Passive backdoor / driver-abuse implant | High | Mandiant reports related Sheed AV MD5 0c93cac9854831da5f761ee98bb40c37 and WINTAPIX/TOFUDRV hashes in the same report. |
| [`TEMPLELOCK`](templelock.md) | [UNC1860](../actors/unc1860.md) | Defense-evasion utility | High | Hash not committed; use Mandiant activity-level IOC list. |
| [`TEMPLEPLAY`](templeplay.md) | [UNC1860](../actors/unc1860.md) | GUI malware controller | High | Mandiant reports MD5 c517519097bff386dc1784d98ad93f9d for TEMPLEPLAY. |
| [`VIROGREEN`](virogreen.md) | [UNC1860](../actors/unc1860.md) | GUI exploitation / post-exploitation framework | High | Hash not committed; use Mandiant source and technical annex where accessible. |
| [`SUGARUSH / SUGARDUMP`](sugarush-sugardump.md) | [UNC3890](../actors/unc3890.md) | Information stealer | Medium | Hash not committed; use Mandiant source references. |
| [`BiBi / BiBi Wiper lineage`](bibi-bibi-wiper-lineage.md) | [Void Manticore / Handala](../actors/handala.md) | Wiper / destructive malware lineage | Medium | Hash not committed; use primary wiper reports for active IOCs. |
| [`Handala-linked destructive installer chains`](handala-linked-destructive-installer-chains.md) | [Void Manticore / Handala](../actors/handala.md) | Installer-led destructive chain | Medium | Hash not committed; chain behavior matters more than static IOCs. |
| [`AshTag`](ashtag.md) | [WIRTE](../actors/wirte.md) | Modular .NET malware suite | High | Hash not committed; use Unit 42 report references. |
| [`SameCoin`](samecoin.md) | [WIRTE](../actors/wirte.md) | Wiper | High | Hash not committed; use Check Point report references. |
