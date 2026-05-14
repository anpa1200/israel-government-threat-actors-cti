# Defensive Cyber Threat Intelligence Report: Israeli Critical Infrastructure and Geopolitical Escalation (2024-2026)

Status: Research intake and defensive synthesis.

Handling: TLP:CLEAR. Do not use this report for attribution, blocking, or executive claims without claim-level source review.

## Executive Summary

The cyber threat landscape targeting Israeli government ministries, municipal authorities, telecommunications, critical infrastructure, and defense-adjacent suppliers has escalated between 2024 and 2026. Public reporting around Operation Epic Fury and related regional escalation describes increased activity from Iranian state-linked actors, Iran-aligned personas, Hamas-linked espionage groups, and proxy hacktivist clusters.

The dominant defensive trend is a shift from purely malware-centric destructive operations toward identity-plane and management-plane abuse. Instead of relying only on custom MBR wipers or ransomware-like payloads, actors increasingly seek privileged cloud identities, endpoint-management consoles, RMM tools, and legitimate administrative paths that can create destructive impact while producing fewer traditional malware artifacts.

Primary defensive implications:

- Identity and MDM platforms MUST be treated as Tier-0 systems.
- Standing Global Administrator and Intune Administrator privileges SHOULD be eliminated in favor of PIM/JIT access and phishing-resistant MFA.
- OT/ICS systems MUST NOT expose PLC/HMI management interfaces to the public internet.
- RMM, file synchronization, and cloud storage tools MUST be baselined and monitored.
- Public hacktivist claims MUST be separated from verified technical compromise.

## Actor Priority Table

| Primary Name | Aliases | Assessed Sponsor | Target Sectors | Priority |
| --- | --- | --- | --- | --- |
| Void Manticore | Handala, Storm-0842, Banished Kitten, Dune | Iran MOIS-linked in public reporting | Healthcare, defense suppliers, critical IT, Israeli entities | Critical |
| CyberAv3ngers | CyberAveng3rs, Storm-0784 | Iran IRGC-affiliated persona | OT/ICS, water, energy, manufacturing | Critical |
| MuddyWater | Boggy Serpens, Seedworm, Static Kitten, Mango Sandstorm | Iran MOIS-linked | Government, telecom, NGOs, IT supply chain | High |
| Cyber Toufan | Cyber Toufan Operations | Pro-Palestinian / Iran-aligned persona | Government, defense, finance, IT providers | High |
| Cotton Sandstorm | Emennet Pasargad, Altoufan Team | Iran IRGC-linked | Critical infrastructure, media, Gulf states | High |
| OilRig | APT34, Evasive Serpens, Hazel Sandstorm | Iran state-linked | Energy, government, finance, IT | High |
| Arid Viper | APT-C-23, Desert Falcon | Hamas-linked in public reporting | IDF-related targets, government officials, mobile users | High |
| UNC3890 | UNC3890 | Suspected Iran-linked | Shipping, logistics, healthcare, aviation | Elevated |
| Agrius | Pink Sandstorm, Agonizing Serpens | Iran MOIS-linked in public reporting | Higher education, technology, government | Elevated |
| Lebanese Cedar | Volatile Cedar | Hezbollah-linked in public reporting | Government, defense contractors, IT, telecom | Elevated |
| APT35 / APT42 | Mint Sandstorm, Magic Hound, Charming Kitten | Iran IRGC-linked in public reporting | Journalists, academics, diaspora, NGOs | Moderate |

## Source Register

| Source ID | Source | Score | Use |
| --- | --- | --- | --- |
| `SRC-PUSH-STRYKER-HANDALA` | Push Security Stryker/Handala report | A | Identity weaponization and Intune destructive-action model. |
| `SRC-ARCTIC-EPIC-FURY` | Arctic Wolf escalation bulletin | A | Geopolitical cyber-risk context and defensive guidance. |
| `SRC-CISA-AA26-097A` | Joint CISA/FBI/NSA/EPA/DOE/USCYBERCOM PLC advisory | A | Rockwell/Allen-Bradley PLC exploitation and OT mitigations. |
| `SRC-CP-HANDALA-2026` | Check Point Handala modus operandi | A | Handala / Void Manticore source anchor. |
| `SRC-CP-MOIS-CRIME` | Check Point MOIS cyber-crime connection | A | MOIS actor/criminal ecosystem analysis. |
| `SRC-OPI-CYBER-TOUFAN` | OP Innovate Cyber Toufan playbook | A | Cyber Toufan external-exposure and leak-operation playbook. |
| `SRC-ESET-ARIDSPY` | ESET AridSpy report | A | Arid Viper mobile espionage details. |
| `SRC-MANDIANT-UNC3890` | Google/Mandiant UNC3890 report | A | Israeli shipping/logistics targeting and Punycode watering hole evidence. |
| `SRC-CISA-IRAN-THREAT-2025` | Joint CISA/FBI/NSA/DC3 Iranian cyber threat fact sheet | A | Heightened Iranian cyber-threat context and critical-infrastructure guidance. |
| `SRC-THREAT-HUNTER-V3` | ThreatHunter.ai Detection Pack v3 | B | Detection ideas and IOC hypotheses requiring corroboration. |
| `SRC-CLOUDSEK-EPIC-FURY` | CloudSEK Middle East escalation report | B | Supporting regional hacktivist and escalation context. |
| `SRC-CLEARSKY-LEBANESE-CEDAR` | ClearSky Lebanese Cedar report | B | Lebanese Cedar / Explosive RAT / Caterpillar WebShell source. |

## Actor Profiles

### Void Manticore / Handala

FACT: Public reporting by Check Point and Push Security associates Handala / Void Manticore with Iran-linked destructive or disruptive activity.

FACT: Push Security reports a March 2026 Stryker incident in which attackers abused Microsoft Intune remote wipe functionality through compromised Global Administrator access rather than deploying traditional malware.

ASSESSMENT: This identity weaponization model is strategically important because it bypasses many endpoint malware detections. Defenders should prioritize Intune audit logging, PIM authentication-context enforcement, multi-admin approval, and break-glass account monitoring.

LOW CONFIDENCE: Social-media-only claims about municipal access or broad victim lists require corroboration through victim statements, reputable reporting, or local telemetry.

### MuddyWater / Boggy Serpens

FACT: CISA and MITRE identify MuddyWater as an Iranian government-sponsored actor associated with MOIS-linked operations.

FACT: Public reporting describes frequent use of phishing, legitimate RMM tools, PowerShell, and living-off-the-land approaches.

ASSESSMENT: MuddyWater activity should be modeled as a long-dwell access and persistence threat that may enable later destructive operations by another persona or team.

### CyberAv3ngers

FACT: CISA AA23-335A documented CyberAv3ngers targeting internet-exposed Unitronics PLCs.

FACT: The 2026 joint advisory `SRC-CISA-AA26-097A` reports exploitation of internet-facing Rockwell Automation / Allen-Bradley PLCs across critical infrastructure.

ASSESSMENT: OT exposure management remains the highest-value mitigation. PLCs, HMIs, engineering workstations, and remote access paths must be isolated from the public internet and segmented from IT networks.

### Cyber Toufan

FACT: OP Innovate describes Cyber Toufan tradecraft focused on exposed VPN/firewall infrastructure, weak credential hygiene, lateral movement, and data-leak operations.

ASSESSMENT: This actor model rewards basic security failure. MFA gaps, unpatched edge devices, flat SMB networks, and poor logging create the highest practical risk.

### Arid Viper / APT-C-23

FACT: ESET reports Arid Viper use of AridSpy Android malware distributed through trojanized apps.

ASSESSMENT: Mobile security controls are central: prohibit sideloading, enforce MDM posture, monitor suspicious Android packages, and train high-risk users on persona-based lures.

### OilRig / APT34

FACT: ESET and MITRE describe OilRig as a long-running espionage actor with targeting in Israel and the broader Middle East.

ASSESSMENT: Prioritize public web, Exchange/IIS, credential access, webshell persistence, and cloud service abuse detections.

### Agrius / Pink Sandstorm

FACT: MITRE, SentinelOne, and Unit 42 associate Agrius / Agonizing Serpens with destructive or ransomware-style operations affecting Israeli sectors.

ASSESSMENT: This actor should drive wiper-preparation, backup-deletion, endpoint-tampering, and supply-chain-compromise hunts.

### Cotton Sandstorm / Emennet Pasargad

FACT: Microsoft and U.S. government reporting describe cyber-enabled influence, disruptive activity, and heightened network-access risk from Iran-linked actors including Cotton Sandstorm / Emennet Pasargad.

ASSESSMENT: Treat Cotton Sandstorm as a cyber-influence risk that may combine technical compromise, defacement, leaks, DDoS, and narrative amplification.

### UNC3890

FACT: Google/Mandiant reports UNC3890 targeting Israeli shipping, logistics, healthcare, aviation, and government-related sectors.

ASSESSMENT: Punycode monitoring, shipping-sector credential phishing detection, and webmail-based exfiltration hunts are appropriate.

### APT35 / APT42 / Mint Sandstorm

FACT: MITRE, Microsoft, Google, and Mandiant associate these clusters with Iran-linked espionage, credential phishing, social engineering, and targeting of high-value individuals.

ASSESSMENT: Protect individual officials and policy-adjacent users with phishing-resistant MFA, mailbox auditing, OAuth consent controls, and VIP account monitoring.

### Lebanese Cedar / Volatile Cedar

FACT: ClearSky reports Lebanese Cedar use of unpatched public-facing web servers, Explosive RAT, and Caterpillar WebShell.

ASSESSMENT: This threat is best handled through public-facing server patching, webshell hunting, legacy Oracle/Atlassian exposure reduction, and hosting-provider visibility.

## ATT&CK Mapping

| Tactic | Technique ID | Technique | Actor | Context |
| --- | --- | --- | --- | --- |
| Reconnaissance | T1595 | Active Scanning | Cyber Toufan | External VPN/firewall/admin surface discovery. |
| Initial Access | T1078.004 | Valid Accounts: Cloud Accounts | Void Manticore / Handala | Compromised cloud administrator credentials. |
| Initial Access | T1189 | Drive-by Compromise | UNC3890 | Watering-hole and Punycode lure infrastructure. |
| Initial Access | T1190 | Exploit Public-Facing Application | Lebanese Cedar | Legacy Oracle/Atlassian exploitation. |
| Execution | T1059.001 | PowerShell | Cyber Toufan / MuddyWater | Native execution and staging. |
| Execution | T1204.002 | User Execution: Malicious File | Arid Viper | Trojanized APK sideloading. |
| Persistence | T1505.003 | Web Shell | Lebanese Cedar / OilRig | Webshell persistence on public-facing servers. |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | Cyber Toufan | Native lateral movement through flat networks. |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MuddyWater | Rclone to cloud storage sinks. |
| Impact | T1485 | Data Destruction | Handala / Agrius | Wiper or management-plane destructive actions. |
| Impact | T1490 | Inhibit System Recovery | Handala / Agrius | Backup and recovery tampering. |

## Malware And Tool Reference

| Tool / Malware | Actor | Type | Defensive Relevance |
| --- | --- | --- | --- |
| AridSpy | Arid Viper | Mobile RAT | MDM controls, sideloading prevention, mobile telemetry. |
| Explosive RAT | Lebanese Cedar | RAT | Legacy web server compromise and espionage. |
| Caterpillar WebShell | Lebanese Cedar | Web shell | JSP/webshell hunting. |
| Dindoor | MuddyWater | Backdoor | Deno runtime monitoring. |
| Fakeset | MuddyWater | Backdoor | Python implant hunt hypothesis. |
| SUGARUSH / SUGARDUMP | UNC3890 | Info stealer | Shipping/logistics intrusion investigations. |
| Rclone | MuddyWater and others | Legitimate sync tool | Cloud exfiltration detection. |
| Apostle / Fantasy | Agrius | Wiper / ransomware-style payload | Destructive-preparation hunts. |
| BiBi / Cl Wiper lineage | Handala / Void Manticore | Wiper lineage | Historical destructive detection and response. |
| FactoryTalk | CyberAv3ngers-style OT activity | Legitimate ICS software | Suspicious ICS interaction from non-engineering assets. |

## IOC Reference Table

Static indicators age quickly. These entries are hunt leads, not attribution by themselves.

| Indicator | Type | Context | Source |
| --- | --- | --- | --- |
| `xn--` Punycode domains | Domain pattern | Watering-hole and impersonation detection. | `SRC-MANDIANT-UNC3890` |
| `dnshook.site` | Domain | MOIS-linked detection-pack hypothesis. | `SRC-THREAT-HUNTER-V3` |
| `uppdatefile.com` | Domain | MuddyWater C2 hypothesis. | `SRC-THREAT-HUNTER-V3` |
| `serialmenot.com` | Domain | MuddyWater C2 hypothesis. | `SRC-THREAT-HUNTER-V3` |
| `moonzonet.com` | Domain | MuddyWater C2 hypothesis. | `SRC-THREAT-HUNTER-V3` |
| `wasabisys.com` | Domain | Legitimate cloud sink abused for exfiltration in reporting. | `SRC-THREAT-HUNTER-V3` |
| `backblazeb2.com` | Domain | Legitimate cloud sink abused for exfiltration in reporting. | `SRC-THREAT-HUNTER-V3` |
| `157.20.182.49` | IP | MOIS infrastructure claim in detection-pack reporting. | `SRC-THREAT-HUNTER-V3` |
| `ListOpenedFileDrv_32.sys` | File name | BYOVD / wiper-preparation hunt lead. | `SRC-THREAT-HUNTER-V3` |

## Defensive Detection Opportunities

### Identity Weaponization And MDM

- Monitor bulk `WipeDevice`, `RetireDevice`, and `DeleteDevice` actions.
- Require phishing-resistant MFA through PIM authentication context, not only a prior MFA claim.
- Enable Intune multi-admin approval for destructive device actions.
- Monitor Global Administrator, Intune Administrator, Cloud Device Administrator, and Privileged Role Administrator sessions.

### OT And SCADA

- Remove public exposure of PLC/HMI interfaces.
- Monitor EtherNet/IP `44818`, EtherNet/IP implicit messaging `2222`, S7 `102`, and Modbus `502`.
- Alert on IT-segment or VPS-origin traffic to OT assets.
- Maintain offline PLC project backups and incident-safe engineering images.

### Living-Off-The-Land And RMM Abuse

- Hunt for unauthorized Atera, AnyDesk, ScreenConnect, TeamViewer, NetBird, Tactical RMM, and RemoteUtilities.
- Hunt for `rclone.exe` execution to unapproved cloud destinations.
- Monitor PowerShell, Deno, Python, certutil, mshta, rundll32, and bitsadmin from user-controlled paths.

### Remote Access And Mobile Security

- Enforce MFA on all VPN/firewall/admin interfaces.
- Hunt for rapid failures followed by success.
- Monitor SMB access to `C$` and `ADMIN$` from VPN or workstation sources.
- Disable Android sideloading for managed devices.

## Sigma Rule Ideas Implemented

This report is accompanied by Sigma examples in `detections/sigma/`:

- `intune-bulk-device-wipe-anomaly.yml`
- `rclone-exfil-to-suspicious-cloud-sinks.yml`
- `pim-activation-stale-mfa-claim.yml`
- `deno-runtime-suspicious-child-process.yml`
- `byovd-listopenedfiledrv-driver-load.yml`

## SIEM Query Ideas Implemented

This report is accompanied by KQL examples in `detections/kql/`:

- `intune-bulk-device-wipe-anomaly.kql`
- `rclone-exfil-to-suspicious-cloud-sinks.kql`
- `smb-admin-share-lateral-movement-anomaly.kql`
- `punycode-domain-resolution-hunt.kql`

## Intelligence Gaps

- State versus hacktivist demarcation remains unclear for some personas.
- Arid Viper's current 2025/2026 lure tradecraft against high-value Israeli users requires continued collection.
- OilRig and other Iran-linked groups' zero-day access pipeline remains a blind spot.
- Lebanese Cedar current operational tempo after 2021 reporting requires updated telemetry.
- Identity-plane destructive tradecraft needs more cross-vendor incident confirmation.

## Recommended Next Collection Tasks

1. Monitor access broker and leak marketplaces for Israeli government, telecom, and defense-supplier access offers without collecting leaked private data.
2. Pivot from source-backed MOIS/IRGC infrastructure through passive DNS, TLS certificates, hosting providers, and registration patterns.
3. Deploy controlled OT deception assets that simulate Unitronics and Rockwell exposure without creating live critical-infrastructure risk.
4. Aggregate identity logs across Entra ID, AWS, Google Workspace, VPN, and MDM into SIEM and baseline privileged-account behavior.
5. Build release-quality Sigma/KQL detections for every high-priority actor scenario and test them against benign replay data.
