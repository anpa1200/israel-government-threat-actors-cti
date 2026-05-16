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
| [`AridSpy`](aridspy.md) | [APT-C-23](../actors/arid-viper.md) | Mobile RAT | High | Representative ESET-published SHA1s include 797073511A15EB85C1E9D8584B26BAA3A0B14C9E, 5F0213BA62B84221C9628F7D0A0CF87F27A45A28, E71F1484B1E3ACB4C8E8525BA1F5F8822AB7238B, and 16C8725362D1EBC8443C97C5AB79A1B6428FF87D; use full ESET IOC table for current coverage. |
| [`Desert Scorpion`](desert-scorpion.md) | [APT-C-23](../actors/arid-viper.md) | Mobile malware | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`FrozenCell`](frozencell.md) | [APT-C-23](../actors/arid-viper.md) | Mobile malware | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Micropsia`](micropsia.md) | [APT-C-23](../actors/arid-viper.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Phenakite`](phenakite.md) | [APT-C-23](../actors/arid-viper.md) | Mobile malware | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`RedAlert.apk`](redalertapk.md) | [APT-C-23](../actors/arid-viper.md) | Mobile spyware / trojanized app | Low | Hash not committed; provisional until primary Acronis reporting is available. |
| [`SpyC23`](spyc23.md) | [APT-C-23](../actors/arid-viper.md) | Mobile spyware | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ANTAK / ASPXSPY`](antak-aspxspy.md) | [APT39](../actors/apt39.md) | Web shells | Medium | Hash not committed; use source-linked IOCs and local webroot baselines. |
| [`Cadelspy`](cadelspy.md) | [APT39](../actors/apt39.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`CrackMapExec`](crackmapexec.md) | [APT39](../actors/apt39.md) | Post-exploitation / credential validation tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`MechaFlounder`](mechaflounder.md) | [APT39](../actors/apt39.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [APT39](../actors/apt39.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`NBTscan`](nbtscan.md) | [APT39](../actors/apt39.md) | Network scanner | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PsExec`](psexec.md) | [APT39](../actors/apt39.md) | Remote execution utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Remexi`](remexi.md) | [APT39](../actors/apt39.md) | Malware / collection tool | Medium | Hash not committed; use MITRE references and original vendor reports. |
| [`Windows Credential Editor`](windows-credential-editor.md) | [APT39](../actors/apt39.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ftp`](ftp.md) | [APT39](../actors/apt39.md) | Living-off-the-land utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`pwdump`](pwdump.md) | [APT39](../actors/apt39.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`NICECURL`](nicecurl.md) | [APT42](../actors/apt42.md) | Backdoor / C2 tool | Medium | Hash not committed; retrieve current IOCs from linked source or vendor appendix. |
| [`POWERPOST`](powerpost.md) | [APT42](../actors/apt42.md) | Script / collection tool | Medium | Hash not committed; source-linked behavior only. |
| [`TAMECAT`](tamecat.md) | [APT42](../actors/apt42.md) | Backdoor / C2 tool | Medium | Hash not committed; retrieve current IOCs from linked source or vendor appendix. |
| [`ASPXSpy`](aspxspy.md) | [Agrius](../actors/agrius.md) | Web shell | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Apostle`](apostle.md) | [Agrius](../actors/agrius.md) | Wiper / ransomware-like malware | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`BFG Agonizer`](bfg-agonizer.md) | [Agrius](../actors/agrius.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`BlackShadow`](blackshadow.md) | [Agrius](../actors/agrius.md) | Ransomware / persona | Medium | Hash not committed; persona claims require corroboration. |
| [`DEADWOOD`](deadwood.md) | [Agrius](../actors/agrius.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`IPsec Helper`](ipsec-helper.md) | [Agrius](../actors/agrius.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [Agrius](../actors/agrius.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Moneybird`](moneybird.md) | [Agrius](../actors/agrius.md) | Ransomware / destructive malware | Medium | Hash not committed; source IOC appendix should be used if needed. |
| [`MultiLayer Wiper`](multilayer-wiper.md) | [Agrius](../actors/agrius.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`NBTscan`](nbtscan.md) | [Agrius](../actors/agrius.md) | Network scanner | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`WezRat`](wezrat.md) | [Cotton Sandstorm](../actors/cotton-sandstorm.md) | Modular infostealer / RAT | High | Hash not committed; use Check Point and government IOC references for current sample hashes, lure senders, domains, and C2 paths. |
| [`Cyber Toufan supplier-access playbook`](cyber-toufan-supplier-access-playbook.md) | [Cyber Toufan](../actors/cyber-toufan.md) | Credential and admin-interface abuse | Medium | Not malware; no hash. Track claims and exposure indicators. |
| [`IOControl`](iocontrol.md) | [CyberAv3ngers](../actors/cyberav3ngers.md) | OT/IoT malware | High | Claroty-published SHA256 1b39f9b2b96a6586c4a11ab2fdbff8fdf16ba5a0ac7603149023d73f33b84498; VT enrichment found an ELF with public detections and label trojan.iocontrol/multiverze. |
| [`Unitronics Vision PLC Web/HMI`](unitronics-vision-plc-webhmi.md) | [CyberAv3ngers](../actors/cyberav3ngers.md) | Targeted technology | High | Not malware; no hash. Exposure and configuration indicators only. |
| [`DarkBit ransomware`](darkbit-ransomware.md) | [DarkBit](../actors/darkbit.md) | Pseudo-ransomware / destructive malware | Medium | Hash not committed; incident-specific IOCs should come from INCD/Microsoft source material. |
| [`IMAPLoader`](imaploader.md) | [Imperial Kitten](../actors/imperial-kitten.md) | .NET downloader / loader | High | Hash not committed; use PwC or vendor IOC appendix/current report for current sample hashes and mail-account indicators. |
| [`StandardKeyboard`](standardkeyboard.md) | [Imperial Kitten](../actors/imperial-kitten.md) | Backdoor / C2 tool | Medium | Hash not committed; use CrowdStrike source if available. |
| [`Caterpillar WebShell`](caterpillar-webshell.md) | [Lebanese Cedar](../actors/lebanese-cedar.md) | Web Shell | Medium | Hash not committed; use ClearSky report references. |
| [`Explosive RAT`](explosive-rat.md) | [Lebanese Cedar](../actors/lebanese-cedar.md) | Remote Access Trojan | Medium | Hash not committed; use ClearSky report references. |
| [`BITSAdmin`](bitsadmin.md) | [Lyceum](../actors/lyceum.md) | Living-off-the-land binary | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`DanBot`](danbot.md) | [Lyceum](../actors/lyceum.md) | Remote Access Trojan | Medium | Hash not committed; use MITRE references and primary reports. |
| [`DnsSystem`](dnssystem.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Empire`](empire.md) | [Lyceum](../actors/lyceum.md) | Post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Kevin`](kevin.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Low | Hash not committed; use MITRE references and primary reports. |
| [`Milan`](milan.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [Lyceum](../actors/lyceum.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Ping`](ping.md) | [Lyceum](../actors/lyceum.md) | Network utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PoshC2`](poshc2.md) | [Lyceum](../actors/lyceum.md) | Post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Shark`](shark.md) | [Lyceum](../actors/lyceum.md) | Backdoor | Low | Hash not committed; use MITRE references and primary reports. |
| [`ipconfig`](ipconfig.md) | [Lyceum](../actors/lyceum.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`netstat`](netstat.md) | [Lyceum](../actors/lyceum.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`CharmPower`](charmpower.md) | [Magic Hound](../actors/apt35.md) | PowerShell backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`DownPaper`](downpaper.md) | [Magic Hound](../actors/apt35.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`FRP / Plink`](frp-plink.md) | [Magic Hound](../actors/apt35.md) | Dual-use tunneling / proxy tooling | Medium | No malware hash; dual-use binary monitoring and local allowlisting required. |
| [`Impacket`](impacket.md) | [Magic Hound](../actors/apt35.md) | Python network protocol toolkit | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [Magic Hound](../actors/apt35.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz / SQLMap / Havij`](mimikatz-sqlmap-havij.md) | [Magic Hound](../actors/apt35.md) | Public offensive/security tooling | Medium | No stable actor-specific hash; use process, command-line, and control-plane telemetry. |
| [`Net`](net.md) | [Magic Hound](../actors/apt35.md) | System administration utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Ping`](ping.md) | [Magic Hound](../actors/apt35.md) | Network utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PowerLess`](powerless.md) | [Magic Hound](../actors/apt35.md) | Backdoor | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PsExec`](psexec.md) | [Magic Hound](../actors/apt35.md) | Remote execution utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Pupy`](pupy.md) | [Magic Hound](../actors/apt35.md) | RAT / post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Systeminfo`](systeminfo.md) | [Magic Hound](../actors/apt35.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ipconfig`](ipconfig.md) | [Magic Hound](../actors/apt35.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`netsh`](netsh.md) | [Magic Hound](../actors/apt35.md) | Network configuration utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`BlackBeard`](blackbeard.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Medium | Hash not committed; use INCD source-linked IOCs. |
| [`BugSleep`](bugsleep.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | High | Hash not committed from source page; use Check Point IOC appendix/current report if sample-level matching is required. |
| [`ConnectWise`](connectwise.md) | [MuddyWater](../actors/muddywater.md) | Remote monitoring and management tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`CrackMapExec`](crackmapexec.md) | [MuddyWater](../actors/muddywater.md) | Post-exploitation / credential validation tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`DCHSpy`](dchspy.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Dindoor`](dindoor.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Low | Hash not committed; use source-linked IOCs only. |
| [`Empire`](empire.md) | [MuddyWater](../actors/muddywater.md) | Post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Fakeset`](fakeset.md) | [MuddyWater](../actors/muddywater.md) | Backdoor | Low | Hash not committed; use source-linked IOCs only. |
| [`Fooder / MuddyViper`](fooder-muddyviper.md) | [MuddyWater](../actors/muddywater.md) | Loader and backdoor | Medium | Hash not committed; validate ESET IOC availability before IOC-level use. |
| [`Koadic`](koadic.md) | [MuddyWater](../actors/muddywater.md) | Post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`LP-Notes`](lp-notes.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`LaZagne`](lazagne.md) | [MuddyWater](../actors/muddywater.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [MuddyWater](../actors/muddywater.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mori`](mori.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Out1`](out1.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`POWERSTATS`](powerstats.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PowGoop`](powgoop.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PowerSploit`](powersploit.md) | [MuddyWater](../actors/muddywater.md) | PowerShell post-exploitation framework | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Rclone`](rclone.md) | [MuddyWater](../actors/muddywater.md) | Cloud sync / exfiltration utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Remote Monitoring and Management tools`](remote-monitoring-and-management-tools.md) | [MuddyWater](../actors/muddywater.md) | Living-off-the-land tooling | High | No malware hash; inventory and signed binary allowlist required. |
| [`RemoteUtilities`](remoteutilities.md) | [MuddyWater](../actors/muddywater.md) | Remote administration tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`RustyWater`](rustywater.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`SHARPSTATS`](sharpstats.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`STARWHALE`](starwhale.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Small Sieve`](small-sieve.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Tsundere Botnet`](tsundere-botnet.md) | [MuddyWater](../actors/muddywater.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`BONDUPDATER`](bondupdater.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Helminth`](helminth.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ISMInjector`](isminjector.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`LaZagne`](lazagne.md) | [OilRig](../actors/oilrig.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mango`](mango.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [OilRig](../actors/oilrig.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Net`](net.md) | [OilRig](../actors/oilrig.md) | System administration utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ODAgent`](odagent.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | High | Imported SHA1 seed 7E498B3366F54E936CB0AF767BFC3D1F92D80687 returned VT not_found and remains unpromoted pending primary hash verification. |
| [`OilBooster`](oilbooster.md) | [OilRig](../actors/oilrig.md) | Downloader | High | Primary source confirms tool behavior; imported SHA1 seed 1B2FEDD5F2A37A0152231AE4099A13C8D4B73C9E returned VT not_found and remains unpromoted pending primary hash verification. |
| [`OilCheck`](oilcheck.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | High | Imported SHA1 seed 8D84D32DF5768B0D4D2AB8B1327C43F17F182001 returned VT not_found and remains unpromoted pending primary hash verification. |
| [`OopsIE`](oopsie.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`POWRUNER`](powruner.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PowerExchange`](powerexchange.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`PsExec`](psexec.md) | [OilRig](../actors/oilrig.md) | Remote execution utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`QUADAGENT`](quadagent.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`RDAT`](rdat.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`RGDoor`](rgdoor.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Reg`](reg.md) | [OilRig](../actors/oilrig.md) | Registry utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`SEASHARPEE`](seasharpee.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Saitama`](saitama.md) | [OilRig](../actors/oilrig.md) | DNS-tunneling backdoor | High | Hash not committed; use Unit 42 IOC references if needed. |
| [`SampleCheck5000`](samplecheck5000.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`SideTwist`](sidetwist.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Solar`](solar.md) | [OilRig](../actors/oilrig.md) | MITRE-listed software/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Systeminfo`](systeminfo.md) | [OilRig](../actors/oilrig.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Tasklist`](tasklist.md) | [OilRig](../actors/oilrig.md) | Process discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ZeroCleare`](zerocleare.md) | [OilRig](../actors/oilrig.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`certutil`](certutil.md) | [OilRig](../actors/oilrig.md) | Living-off-the-land binary | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ftp`](ftp.md) | [OilRig](../actors/oilrig.md) | Living-off-the-land utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ipconfig`](ipconfig.md) | [OilRig](../actors/oilrig.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`netstat`](netstat.md) | [OilRig](../actors/oilrig.md) | System discovery utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ngrok`](ngrok.md) | [OilRig](../actors/oilrig.md) | Tunneling / proxy tooling | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`NGROK / Ligolo`](ngrok-ligolo.md) | [Pioneer Kitten](../actors/pioneer-kitten.md) | Tunneling / proxy tooling | High | No malware hash; monitor tool binary, process, account, and network usage against approved admin list. |
| [`Liontail`](liontail.md) | [Scarred Manticore](../actors/scarred-manticore.md) | Passive backdoor framework | High | Hash not committed; use Check Point source report references and local IIS module baselines. |
| [`IronWind`](ironwind.md) | [TA402](../actors/ta402.md) | Initial access downloader / staged malware | High | Proofpoint-published SHA256 indicators include 9b2a16cbe5af12b486d31b68ef397d6bc48b2736e6b388ad8895b588f1831f47, 5d773e734290b93649a41ccda63772560b4fa25ba715b17df7b9f18883679160, 19f452239dadcd7544f055d26199cb482c1f6ae5486309bde1526174e926146a, A4bf96aee6284effb4c4fe0ccfee7b32d497e45408e253fb8e1199454e5c65a3, and 26cb6055be1ee503f87d040c84c0a7cacb245b4182445e3eee47ed6e073eca47; use full Proofpoint IOC list for operational use. |
| [`CRYPTOSLAY`](cryptoslay.md) | [UNC1860](../actors/unc1860.md) | Associated family | Medium | Family confirmed by Malpedia; no per-sample hash committed in this repo. |
| [`PipeSnoop`](pipesnoop.md) | [UNC1860](../actors/unc1860.md) | Referenced tool/family term | Low | Reference confirmed by Malpedia; no per-sample hash committed in this repo. |
| [`SASHEYAWAY`](sasheyaway.md) | [UNC1860](../actors/unc1860.md) | Dropper / access-enablement tooling | High | Mandiant publishes activity-level MD5 IOCs and a VT collection; this repo does not map every hash to SASHEYAWAY. |
| [`STAYSHANTE`](stayshante.md) | [UNC1860](../actors/unc1860.md) | Web shell / handoff tooling | High | Mandiant publishes activity-level MD5 IOCs and a VT collection; this repo does not map every hash to STAYSHANTE. |
| [`TEMPLEDOOR`](templedoor.md) | [UNC1860](../actors/unc1860.md) | Passive backdoor family | High | Representative Mandiant MD5s include c57e59314aee7422e626520e495effe0 and b219672bcd60ce9a81b900217b3b5864. VT enrichment found b219672bcd60ce9a81b900217b3b5864 as Win32 EXE/System.dll with 47 malicious public detections; c57e59314aee7422e626520e495effe0 returned VT not_found. |
| [`TEMPLEDROP`](templedrop.md) | [UNC1860](../actors/unc1860.md) | Passive backdoor / driver-abuse implant | High | Mandiant reports related Sheed AV MD5 0c93cac9854831da5f761ee98bb40c37 and WINTAPIX/TOFUDRV MD5s 286bd9c2670215d3cb4790aac4552f22 and b4b1e285b9f666ae7304a456da01545e in the same report; VT enrichment found the Sheed AV reference as signed and not malicious by public verdicts. |
| [`TEMPLELOCK`](templelock.md) | [UNC1860](../actors/unc1860.md) | Defense-evasion utility | High | Hash not committed; use Mandiant activity-level IOC list. |
| [`TEMPLEPLAY`](templeplay.md) | [UNC1860](../actors/unc1860.md) | GUI malware controller | High | Mandiant reports MD5 c517519097bff386dc1784d98ad93f9d for TEMPLEPLAY; VT enrichment returned not_found on 2026-05-16. |
| [`VIROGREEN`](virogreen.md) | [UNC1860](../actors/unc1860.md) | GUI exploitation / post-exploitation framework | High | Hash not committed; use Mandiant source and technical annex where accessible. |
| [`SUGARUSH / SUGARDUMP`](sugarush-sugardump.md) | [UNC3890](../actors/unc3890.md) | Information stealer | Medium | Hash not committed; use Mandiant source references. |
| [`BiBi / BiBi Wiper lineage`](bibi-bibi-wiper-lineage.md) | [Void Manticore / Handala](../actors/handala.md) | Wiper / destructive malware lineage | Medium | Hash not committed; use primary wiper reports for active IOCs. |
| [`CHIMNEYSWEEP`](chimneysweep.md) | [Void Manticore / Handala](../actors/handala.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Handala-linked destructive installer chains`](handala-linked-destructive-installer-chains.md) | [Void Manticore / Handala](../actors/handala.md) | Installer-led destructive chain | Medium | Hash not committed; chain behavior matters more than static IOCs. |
| [`Impacket`](impacket.md) | [Void Manticore / Handala](../actors/handala.md) | Python network protocol toolkit | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`Mimikatz`](mimikatz.md) | [Void Manticore / Handala](../actors/handala.md) | Credential access tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ROADSWEEP`](roadsweep.md) | [Void Manticore / Handala](../actors/handala.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`RawDisk`](rawdisk.md) | [Void Manticore / Handala](../actors/handala.md) | Disk access driver/tool | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ZeroCleare`](zerocleare.md) | [Void Manticore / Handala](../actors/handala.md) | Wiper | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`ftp`](ftp.md) | [Void Manticore / Handala](../actors/handala.md) | Living-off-the-land utility | Medium | Hash not committed; use the linked MITRE references and original source reports for current IOCs. |
| [`AshTag`](ashtag.md) | [WIRTE](../actors/wirte.md) | Modular .NET malware suite | High | Representative Unit 42 SHA256s include f554c43707f5d87625a3834116a2d22f551b1d9a5aff1e446d24893975c431bc, 739a5199add1d970ba22d69cc10b4c3a13b72136be6d45212429e8f0969af3dc, 6bd3d05aef89cd03d6b49b20716775fe92f0cf8a3c2747094404ef98f96e9376, 30490ba95c42cefcca1d0328ea740e61c26eaf606a98f68d26c4a519ce918c99, and 66ab29d2d62548faeaeadaad9dd62818163175872703fda328bb1b4894f5e69e; use full Unit 42 IOC table for coverage. |
| [`SameCoin`](samecoin.md) | [WIRTE](../actors/wirte.md) | Wiper | High | Check Point publishes lure hash b7c5af2d7e1eb7651b1fe3a224121d3461f3473d081990c02ef8ab4ace13f785; component hashes should be pulled from the primary Check Point/HarfangLab references before blocking. |
