---
title: Lyceum
sidebar_label: Lyceum
---

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Lyceum](../navigation/actor-workbench.md#lyceum)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](../navigation/surface-capability-matrix.md#ot-plc)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1071.004](../navigation/ttp-detection-matrix.md#t1071004) DNS (M2); [T1003.001](../navigation/ttp-detection-matrix.md#t1003001) LSASS Memory (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`DanBot`](../tools/danbot.md); [`Kevin`](../tools/kevin.md); [`Shark`](../tools/shark.md); [`BITSAdmin`](../tools/bitsadmin.md); [`DnsSystem`](../tools/dnssystem.md); [`Empire`](../tools/empire.md); [`ipconfig`](../tools/ipconfig.md); [`Milan`](../tools/milan.md); [`Mimikatz`](../tools/mimikatz.md); [`netstat`](../tools/netstat.md); [`Ping`](../tools/ping.md); [`PoshC2`](../tools/poshc2.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#lyceum) (12 mapped tool row(s))
- Evidence records: `EVD-021` / `CLM-LYCEUM-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G1001`

<!-- ACTOR-NAVIGATION:END -->

# Lyceum

Aliases: Lyceum, HEXANE, Spirlin, Siamesekitten. Some reporting places Lyceum within an OilRig-related subgroup or adjacent ecosystem.

Assessed sponsor: Iranian state-sponsored, likely OilRig/MOIS-adjacent based on current public source synthesis. Sponsor confidence is lower than core OilRig because public reporting has historically used cautious language and vendor taxonomies differ.

## Relevance

Lyceum is high priority for Israeli telecom, ISP, energy, and supplier environments. MITRE and industry reporting describe targeting in Israel and Middle Eastern telecom, oil/gas, and IT-provider environments. Even where newer incidents are published under broader OilRig subgrouping, the tradecraft remains relevant to Israeli public-sector dependencies.

## Defensive Focus

- Telecom, ISP, oil/gas, engineering, manufacturing, and IT-supplier environments.
- DNS and HTTP C2 from legacy DanBot/Kevin/Shark-style tooling.
- Supply-chain access through IT service providers.
- Cloud-service C2 overlap where Lyceum is grouped under OilRig-related operations.
- Credential theft and LSASS dumping from telecom or supplier networks.

## Associated Tooling

- **DanBot**: RAT/backdoor line associated with Lyceum/HEXANE reporting.
- **Kevin**: Backdoor line reported in Kaspersky/Lyceum material.
- **Shark**: Updated Milan-derived .NET backdoor in public Lyceum reporting.
- **OilBooster**: OilRig downloader included as adjacent context where sources group Lyceum under OilRig-related activity.

## Detection Ideas

- DNS C2 anomalies from telecom, ISP, or supplier servers that do not normally make high-entropy or high-frequency DNS queries.
- Job-offer or industry-themed lure delivery followed by downloads from impersonation infrastructure.
- WMI/MOF persistence or unusual writes to WMI repository paths on user workstations.
- LSASS access from newly observed C/C++ binaries or renamed credential tools.
- IT-provider credential access followed by downstream authentication into Israeli public-sector customers.

## Repository Sources

- `SRC-MITRE-G1001`: MITRE ATT&CK HEXANE / Lyceum group profile.
- `SRC-CLEARSKY-SIAMESEKITTEN-2021`: ClearSky Siamesekitten / Pay2Kitten reporting.
- `SRC-ESET-OILRIG-ISRAEL`: ESET OilRig downloader reporting used for adjacent OilRig subgroup context.
