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
- Malware and tools: [`Unitronics Vision PLC Web/HMI`](../tools/unitronics-vision-plc-webhmi.md) (Targeted technology); [`IOControl`](../tools/iocontrol.md) (OT/IoT malware)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#cyberav3ngers) (2 mapped tool row(s))
- Tool detail pages: [`Unitronics Vision PLC Web/HMI`](../tools/unitronics-vision-plc-webhmi.md); [`IOControl`](../tools/iocontrol.md)
- Evidence records: `EVD-002` / `CLM-CYBERAV3NGERS-001`; `EVD-009` / `CLM-CYBERAV3NGERS-002`; `EVD-026` / `CLM-CYBERAV3NGERS-003`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CISA-AA23-335A`, `SRC-CISA-AA26-097A`, `SRC-CLAROTY-IOCONTROL-2024`

<!-- ACTOR-NAVIGATION:END -->

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
