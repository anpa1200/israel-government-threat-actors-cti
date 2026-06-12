# CyberAv3ngers

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [CyberAv3ngers](../navigation/actor-workbench.md#cyberav3ngers)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](../navigation/surface-capability-matrix.md#ot-plc)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T0883](../navigation/ttp-detection-matrix.md#t0883) Internet Accessible Device (M2); [T0836](../navigation/ttp-detection-matrix.md#t0836) Modify Parameter (M2); [T0832](../navigation/ttp-detection-matrix.md#t0832) Manipulation of View (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: `SRC-CISA-AA23-335A` IP; device exposure; affected product context
- Tool detail pages: [`Unitronics Vision PLC Web/HMI`](../tools/unitronics-vision-plc-webhmi.md); [`IOControl`](../tools/iocontrol.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cyberav3ngers) (2 mapped tool row(s))
- Evidence records: `EVD-002` / `CLM-CYBERAV3NGERS-001`; `EVD-009` / `CLM-CYBERAV3NGERS-002`; `EVD-026` / `CLM-CYBERAV3NGERS-003`
- Imported research intakes: None currently mapped.
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CISA-AA23-335A`, `SRC-CISA-AA26-097A`, `SRC-CLAROTY-IOCONTROL-2024`

<!-- ACTOR-NAVIGATION:END -->

## Background

CyberAv3ngers is the public persona of the Shahid Kaveh Group, a unit within the IRGC Cyber-Electronic Command (IRGC-CEC). The group was formally linked to IRGC-CEC by CISA advisory AA26-097A (April 2026), and six IRGC-CEC officials were sanctioned by U.S. Treasury OFAC in February 2024 for their roles in CyberAv3ngers operations. This makes CyberAv3ngers one of the few Iran-nexus OT threat actors with both sanctions-level organizational attribution and a named responsible unit.

The group gained significant public attention in November-December 2023 when it compromised internet-exposed Unitronics Vision Series PLCs at water and wastewater facilities across the United States, including the Municipal Water Authority of Aliquippa (MEWA) in Pennsylvania. Unitronics is an Israeli manufacturer, and the group's messaging displayed anti-Israeli text on compromised HMI interfaces ("You have been hacked, down with Israel"). CISA advisory AA23-335A (December 2023) specifically called out internet-exposed Unitronics PLCs and provided immediate mitigation guidance.

Claroty Team82's December 2024 research documented an expanded toolset: IOControl, a custom OT/IoT malware framework designed to target internet-facing OT devices including PLCs, HMIs, fuel management systems, IP cameras, and network edge devices. IOControl operates as a multi-stage implant with encrypted C2, enabling persistent access and potential manipulation of industrial equipment beyond the initial HMI display defacement seen in 2023. The April 2026 CISA advisory AA26-097A documented expanded targeting to include Rockwell Automation/Allen-Bradley equipment, broadening the OT risk surface.

The group's OT targeting model is opportunistic against internet-exposed devices with default or weak credentials, rather than requiring pre-positioned access. For Israeli government and critical infrastructure operators, the group's specific focus on Israeli-manufactured equipment and anti-Israeli messaging elevates it to a priority threat for water, energy, and industrial facility defenders.

Aliases: CyberAveng3rs, Cyber Avengers, Storm-0784 (Microsoft), Bauxite (Dragos), UNC5691 (Mandiant), Hydro Kitten, Shahid Kaveh Group, Soldiers of Solomon, Mr. Soul.

Assessed sponsor: IRGC-CEC (Islamic Revolutionary Guard Corps Cyber-Electronic Command), specifically the Shahid Kaveh Group, per CISA AA26-097A (April 2026), CISA AA23-335A (December 2023), and U.S. Treasury OFAC sanctions (February 2024) that named six IRGC-CEC officials.

## Relevance

CyberAv3ngers is high priority for Israeli government, municipal, and critical infrastructure defenders because CISA reported targeting of internet-accessible Unitronics Vision Series PLCs, including messaging focused on Israeli-made equipment.

## Defensive Focus

- Internet-exposed PLC/HMI interfaces.
- Default or weak passwords.
- Remote management access to OT environments.
- Public defacement and psychological effect.

## Required Controls

- Unitronics PLCs MUST NOT be directly exposed to the internet.
- Default passwords MUST be changed.
- Remote access SHOULD require MFA and network segmentation.
- OT asset owners SHOULD maintain offline configuration backups.

## Associated Malware

- **IOControl**: Custom OT/IoT malware targeting internet-facing OT devices (PLCs, HMIs, routers, IP cameras). Reported by Claroty Team82 in December 2024 and tracked in this repository as `SRC-CLAROTY-IOCONTROL-2024`.
- Unitronics Vision Series PLC default-credential exploitation (CISA AA23-335A, AA26-097A).
- Rockwell Automation / Allen-Bradley exploitation (CISA AA26-097A).

## Repository Sources

- `SRC-CISA-AA23-335A`: Joint advisory on Unitronics PLC exploitation (December 2023).
- `SRC-CISA-AA26-097A`: Joint advisory identifying IRGC-CEC sponsor, full alias list, and Rockwell/Allen-Bradley targeting (April 2026).
- `SRC-MANDIANT-OT-HACKTIVISTS`: OT hacktivist targeting claims context.

## Public Reports

**Government advisories:**

- [CISA Advisory AA23-335A — Unitronics PLCs Used in Water Systems](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) — CISA/FBI/EPA/NCSC-Israel, December 2023. Documents Unitronics PLC exploitation by CyberAv3ngers, provides specific mitigation steps, and calls out Israeli-manufactured equipment targeting. Source ID `SRC-CISA-AA23-335A`.
- [CISA Advisory AA26-097A — IRGC-CEC Cyber Operations](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) — CISA/FBI/DC3, April 2026. Formally attributes Shahid Kaveh Group to IRGC-CEC, documents full alias list, Rockwell/Allen-Bradley targeting expansion, and IOControl malware. Source ID `SRC-CISA-AA26-097A`.
- U.S. Treasury OFAC, Designation of Six IRGC-CEC Officials — February 2024. Sanctions action naming individuals responsible for CyberAv3ngers operations.

**Primary vendor reporting:**

- Claroty Team82, "IOControl: IRGC-Linked Custom OT/IoT Cyberweapon" — December 2024. Technical analysis of IOControl firmware implant targeting OT devices including PLCs, fuel management, and IP cameras. Source ID `SRC-CLAROTY-IOCONTROL-2024`.
- Dragos, "Bauxite" threat group profile — OT-focused analysis of CyberAv3ngers/Bauxite activity and industrial targeting patterns.
- Mandiant / Google Cloud, OT Hacktivists context — Analysis of hacktivist-framed OT operations by state-linked actors. Source ID `SRC-MANDIANT-OT-HACKTIVISTS`.
