# CyberAv3ngers

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
