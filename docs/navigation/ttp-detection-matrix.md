---
title: TTP To Detection Matrix
sidebar_label: TTP Matrix
---

# TTP To Detection Matrix

Use this page when the starting point is a technique. Each technique links back to relevant actors, mapped repository detections, mapped hunts, and MITRE ATT&CK.

A missing detection means the technique is tracked for intelligence context but does not yet have a repository rule or hunt mapped to it.

## Coverage Summary

| Technique | Actors | Mapped Detections | Mapped Hunts |
| --- | ---: | ---: | ---: |
| [T0832](#t0832) | 1 | 0 | 0 |
| [T0836](#t0836) | 1 | 0 | 0 |
| [T0883](#t0883) | 1 | 0 | 0 |
| [T1003.001](#t1003001) | 2 | 0 | 0 |
| [T1021.001](#t1021001) | 1 | 0 | 0 |
| [T1021.002](#t1021002) | 1 | 0 | 0 |
| [T1049](#t1049) | 1 | 0 | 0 |
| [T1059.001](#t1059001) | 1 | 0 | 0 |
| [T1059.005](#t1059005) | 1 | 0 | 0 |
| [T1071.001](#t1071001) | 1 | 0 | 0 |
| [T1071.003](#t1071003) | 1 | 0 | 0 |
| [T1071.004](#t1071004) | 1 | 0 | 0 |
| [T1078](#t1078) | 1 | 0 | 0 |
| [T1078.004](#t1078004) | 1 | 0 | 0 |
| [T1102](#t1102) | 1 | 0 | 0 |
| [T1105](#t1105) | 2 | 0 | 0 |
| [T1189](#t1189) | 2 | 0 | 0 |
| [T1190](#t1190) | 4 | 1 | 1 |
| [T1199](#t1199) | 1 | 0 | 0 |
| [T1204](#t1204) | 1 | 0 | 0 |
| [T1204.002](#t1204002) | 2 | 0 | 0 |
| [T1219](#t1219) | 2 | 1 | 1 |
| [T1485](#t1485) | 3 | 1 | 1 |
| [T1486](#t1486) | 2 | 0 | 0 |
| [T1490](#t1490) | 2 | 0 | 0 |
| [T1491](#t1491) | 1 | 0 | 0 |
| [T1505.003](#t1505003) | 4 | 0 | 0 |
| [T1505.004](#t1505004) | 1 | 0 | 0 |
| [T1530](#t1530) | 1 | 0 | 0 |
| [T1566](#t1566) | 4 | 1 | 1 |
| [T1566.001](#t1566001) | 2 | 0 | 0 |
| [T1566.002](#t1566002) | 2 | 0 | 0 |
| [T1567](#t1567) | 1 | 0 | 0 |
| [T1567.002](#t1567002) | 2 | 0 | 0 |
| [T1572](#t1572) | 1 | 0 | 0 |
| [T1574.001](#t1574001) | 2 | 0 | 0 |
| [T1583.001](#t1583001) | 1 | 0 | 0 |
| [T1585](#t1585) | 1 | 0 | 0 |
| [T1595](#t1595) | 1 | 0 | 0 |
| [T1660](#t1660) | 1 | 0 | 0 |

## Technique Drilldowns

### T0832 - Manipulation of View {#t0832}

MITRE ATT&CK: [T0832](https://attack.mitre.org/techniques/T0832/)

Tactic(s): Impact

Mapped actors: [CyberAv3ngers](../actors/cyberav3ngers.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CISA-AA23-335A`

### T0836 - Modify Parameter {#t0836}

MITRE ATT&CK: [T0836](https://attack.mitre.org/techniques/T0836/)

Tactic(s): Impact

Mapped actors: [CyberAv3ngers](../actors/cyberav3ngers.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CISA-AA26-097A`

### T0883 - Internet Accessible Device {#t0883}

MITRE ATT&CK: [T0883](https://attack.mitre.org/techniques/T0883/)

Tactic(s): Initial Access

Mapped actors: [CyberAv3ngers](../actors/cyberav3ngers.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CISA-AA23-335A`

### T1003.001 - LSASS Memory {#t1003001}

MITRE ATT&CK: [T1003.001](https://attack.mitre.org/techniques/T1003/001/)

Tactic(s): Credential Access

Mapped actors: [APT39](../actors/apt39.md); [Lyceum](../actors/lyceum.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MITRE-G0087`, `SRC-MITRE-G1001`

### T1021.001 - Remote Services: RDP {#t1021001}

MITRE ATT&CK: [T1021.001](https://attack.mitre.org/techniques/T1021/001/)

Tactic(s): Lateral Movement

Mapped actors: [UNC1860](../actors/unc1860.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MANDIANT-UNC1860`

### T1021.002 - SMB/Windows Admin Shares {#t1021002}

MITRE ATT&CK: [T1021.002](https://attack.mitre.org/techniques/T1021/002/)

Tactic(s): Lateral Movement

Mapped actors: [Cyber Toufan](../actors/cyber-toufan.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M3

Source IDs: `SRC-OPI-CYBER-TOUFAN`

### T1049 - System Network Connections Discovery {#t1049}

MITRE ATT&CK: [T1049](https://attack.mitre.org/techniques/T1049/)

Tactic(s): Discovery

Mapped actors: [OilRig](../actors/oilrig.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-MITRE-G0049`

### T1059.001 - PowerShell {#t1059001}

MITRE ATT&CK: [T1059.001](https://attack.mitre.org/techniques/T1059/001/)

Tactic(s): Execution

Mapped actors: [MuddyWater](../actors/muddywater.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MITRE-G0069`

### T1059.005 - Visual Basic {#t1059005}

MITRE ATT&CK: [T1059.005](https://attack.mitre.org/techniques/T1059/005/)

Tactic(s): Execution

Mapped actors: [Imperial Kitten](../actors/imperial-kitten.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-PWC-YELLOW-LIDERC-2023`

### T1071.001 - Web Protocols {#t1071001}

MITRE ATT&CK: [T1071.001](https://attack.mitre.org/techniques/T1071/001/)

Tactic(s): Command and Control

Mapped actors: [Scarred Manticore](../actors/scarred-manticore.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CP-VOID-2024`

### T1071.003 - Mail Protocols {#t1071003}

MITRE ATT&CK: [T1071.003](https://attack.mitre.org/techniques/T1071/003/)

Tactic(s): Command and Control

Mapped actors: [Imperial Kitten](../actors/imperial-kitten.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M3

Source IDs: `SRC-PWC-YELLOW-LIDERC-2023`

### T1071.004 - DNS {#t1071004}

MITRE ATT&CK: [T1071.004](https://attack.mitre.org/techniques/T1071/004/)

Tactic(s): Command and Control

Mapped actors: [Lyceum](../actors/lyceum.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MITRE-G1001`

### T1078 - Valid Accounts {#t1078}

MITRE ATT&CK: [T1078](https://attack.mitre.org/techniques/T1078/)

Tactic(s): Defense Evasion

Mapped actors: [UNC1860](../actors/unc1860.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MANDIANT-UNC1860`

### T1078.004 - Valid Accounts: Cloud Accounts {#t1078004}

MITRE ATT&CK: [T1078.004](https://attack.mitre.org/techniques/T1078/004/)

Tactic(s): Initial Access

Mapped actors: [Void Manticore / Handala](../actors/handala.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M3

Source IDs: `SRC-PUSH-STRYKER-HANDALA`

### T1102 - Web Service {#t1102}

MITRE ATT&CK: [T1102](https://attack.mitre.org/techniques/T1102/)

Tactic(s): Command and Control

Mapped actors: [APT42](../actors/apt42.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-MITRE-G1044`

### T1105 - Ingress Tool Transfer {#t1105}

MITRE ATT&CK: [T1105](https://attack.mitre.org/techniques/T1105/)

Tactic(s): Command and Control

Mapped actors: [UNC1860](../actors/unc1860.md); [WIRTE](../actors/wirte.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-MANDIANT-UNC1860`, `SRC-UNIT42-ASHTAG-2025`

### T1189 - Drive-by Compromise {#t1189}

MITRE ATT&CK: [T1189](https://attack.mitre.org/techniques/T1189/)

Tactic(s): Initial Access

Mapped actors: [Imperial Kitten](../actors/imperial-kitten.md); [UNC3890](../actors/unc3890.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CS-IMPERIAL-KITTEN-2023`, `SRC-SECWEEK-UNC3890`

### T1190 - Exploit Public-Facing Application {#t1190}

MITRE ATT&CK: [T1190](https://attack.mitre.org/techniques/T1190/)

Tactic(s): Initial Access

Mapped actors: [Lebanese Cedar](../actors/lebanese-cedar.md); [Pioneer Kitten](../actors/pioneer-kitten.md); [Scarred Manticore](../actors/scarred-manticore.md); [UNC1860](../actors/unc1860.md)

Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)

Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access

Mapping quality levels in repository: M2

Source IDs: `SRC-CISA-AA24-241A`, `SRC-CLEARSKY-LEBANESE-CEDAR`, `SRC-CP-VOID-2024`, `SRC-MANDIANT-UNC1860`

### T1199 - Trusted Relationship {#t1199}

MITRE ATT&CK: [T1199](https://attack.mitre.org/techniques/T1199/)

Tactic(s): Initial Access

Mapped actors: [Scarred Manticore](../actors/scarred-manticore.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CP-VOID-2024`

### T1204 - User Execution {#t1204}

MITRE ATT&CK: [T1204](https://attack.mitre.org/techniques/T1204/)

Tactic(s): Execution

Mapped actors: [Void Manticore / Handala](../actors/handala.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-AP-HANDALA`

### T1204.002 - User Execution: Malicious File {#t1204002}

MITRE ATT&CK: [T1204.002](https://attack.mitre.org/techniques/T1204/002/)

Tactic(s): Execution

Mapped actors: [Cotton Sandstorm](../actors/cotton-sandstorm.md); [APT-C-23](../actors/arid-viper.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M3

Source IDs: `SRC-CP-WEZRAT`, `SRC-ESET-ARIDSPY`

### T1219 - Remote Access Software {#t1219}

MITRE ATT&CK: [T1219](https://attack.mitre.org/techniques/T1219/)

Tactic(s): Command and Control

Mapped actors: [MuddyWater](../actors/muddywater.md); [Pioneer Kitten](../actors/pioneer-kitten.md)

Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context (Pilot, DRL-6)

Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-CISA-AA24-241A`, `SRC-MITRE-G0069`

### T1485 - Data Destruction {#t1485}

MITRE ATT&CK: [T1485](https://attack.mitre.org/techniques/T1485/)

Tactic(s): Impact

Mapped actors: [Agrius](../actors/agrius.md); [Void Manticore / Handala](../actors/handala.md); [WIRTE](../actors/wirte.md)

Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5)

Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs

Mapping quality levels in repository: M2

Source IDs: `SRC-AP-HANDALA`, `SRC-CP-WIRTE-2024`, `SRC-MITRE-G1030`, `SRC-PUSH-STRYKER-HANDALA`

### T1486 - Data Encrypted for Impact {#t1486}

MITRE ATT&CK: [T1486](https://attack.mitre.org/techniques/T1486/)

Tactic(s): Impact

Mapped actors: [DarkBit](../actors/darkbit.md); [Agrius](../actors/agrius.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-INCD-DARKBIT-MUDDYWATER-2023`, `SRC-MITRE-G1030`

### T1490 - Inhibit System Recovery {#t1490}

MITRE ATT&CK: [T1490](https://attack.mitre.org/techniques/T1490/)

Tactic(s): Impact

Mapped actors: [DarkBit](../actors/darkbit.md); [Void Manticore / Handala](../actors/handala.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-AP-HANDALA`, `SRC-MS-MERCURY-DEV1084-2023`

### T1491 - Defacement {#t1491}

MITRE ATT&CK: [T1491](https://attack.mitre.org/techniques/T1491/)

Tactic(s): Impact

Mapped actors: [Cyber Toufan](../actors/cyber-toufan.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-MS-IRAN-HAMAS`

### T1505.003 - Web Shell {#t1505003}

MITRE ATT&CK: [T1505.003](https://attack.mitre.org/techniques/T1505/003/)

Tactic(s): Persistence

Mapped actors: [OilRig](../actors/oilrig.md); [Lebanese Cedar](../actors/lebanese-cedar.md); [Scarred Manticore](../actors/scarred-manticore.md); [UNC1860](../actors/unc1860.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-CLEARSKY-LEBANESE-CEDAR`, `SRC-CP-VOID-2024`, `SRC-MANDIANT-UNC1860`, `SRC-MITRE-G0049`

### T1505.004 - IIS Components {#t1505004}

MITRE ATT&CK: [T1505.004](https://attack.mitre.org/techniques/T1505/004/)

Tactic(s): Persistence

Mapped actors: [Scarred Manticore](../actors/scarred-manticore.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CP-VOID-2024`

### T1530 - Data from Cloud Storage {#t1530}

MITRE ATT&CK: [T1530](https://attack.mitre.org/techniques/T1530/)

Tactic(s): Collection

Mapped actors: [APT42](../actors/apt42.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-MITRE-G1044`

### T1566 - Phishing {#t1566}

MITRE ATT&CK: [T1566](https://attack.mitre.org/techniques/T1566/)

Tactic(s): Initial Access

Mapped actors: [Cotton Sandstorm](../actors/cotton-sandstorm.md); [MuddyWater](../actors/muddywater.md); [Void Manticore / Handala](../actors/handala.md); [WIRTE](../actors/wirte.md)

Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)

Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-AP-HANDALA`, `SRC-CP-WIRTE-2024`, `SRC-FBI-EMENNET-2024`, `SRC-MITRE-G0069`

### T1566.001 - Spearphishing Attachment {#t1566001}

MITRE ATT&CK: [T1566.001](https://attack.mitre.org/techniques/T1566/001/)

Tactic(s): Initial Access

Mapped actors: [APT39](../actors/apt39.md); [TA402](../actors/ta402.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-MITRE-G0087`, `SRC-PROOFPOINT-TA402-IRONWIND`

### T1566.002 - Spearphishing Link {#t1566002}

MITRE ATT&CK: [T1566.002](https://attack.mitre.org/techniques/T1566/002/)

Tactic(s): Initial Access

Mapped actors: [Magic Hound](../actors/apt35.md); [APT42](../actors/apt42.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-GOOGLE-APT42-PHISHING`, `SRC-MITRE-G0059`

### T1567 - Exfiltration Over Web Service {#t1567}

MITRE ATT&CK: [T1567](https://attack.mitre.org/techniques/T1567/)

Tactic(s): Exfiltration

Mapped actors: [Void Manticore / Handala](../actors/handala.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-AP-HANDALA`

### T1567.002 - Exfiltration to Cloud Storage {#t1567002}

MITRE ATT&CK: [T1567.002](https://attack.mitre.org/techniques/T1567/002/)

Tactic(s): Exfiltration

Mapped actors: [MuddyWater](../actors/muddywater.md); [WIRTE](../actors/wirte.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2, M3

Source IDs: `SRC-THREAT-HUNTER-V3`, `SRC-UNIT42-ASHTAG-2025`

### T1572 - Protocol Tunneling {#t1572}

MITRE ATT&CK: [T1572](https://attack.mitre.org/techniques/T1572/)

Tactic(s): Command and Control

Mapped actors: [Pioneer Kitten](../actors/pioneer-kitten.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-CISA-AA24-241A`

### T1574.001 - DLL Search Order Hijacking {#t1574001}

MITRE ATT&CK: [T1574.001](https://attack.mitre.org/techniques/T1574/001/)

Tactic(s): Defense Evasion

Mapped actors: [TA402](../actors/ta402.md); [WIRTE](../actors/wirte.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M3

Source IDs: `SRC-CP-WIRTE-2024`, `SRC-PROOFPOINT-TA402-IRONWIND`

### T1583.001 - Acquire Domains {#t1583001}

MITRE ATT&CK: [T1583.001](https://attack.mitre.org/techniques/T1583/001/)

Tactic(s): Resource Development

Mapped actors: [Magic Hound](../actors/apt35.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-MITRE-G0059`

### T1585 - Establish Accounts {#t1585}

MITRE ATT&CK: [T1585](https://attack.mitre.org/techniques/T1585/)

Tactic(s): Resource Development

Mapped actors: [Cotton Sandstorm](../actors/cotton-sandstorm.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-MS-IRAN-IO`

### T1595 - Active Scanning {#t1595}

MITRE ATT&CK: [T1595](https://attack.mitre.org/techniques/T1595/)

Tactic(s): Reconnaissance

Mapped actors: [Cyber Toufan](../actors/cyber-toufan.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M1

Source IDs: `SRC-OPI-CYBER-TOUFAN`

### T1660 - Phishing {#t1660}

MITRE ATT&CK: [T1660](https://attack.mitre.org/techniques/T1660/)

Tactic(s): Initial Access (Mobile)

Mapped actors: [APT-C-23](../actors/arid-viper.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Mapping quality levels in repository: M2

Source IDs: `SRC-ESET-ARIDSPY`
