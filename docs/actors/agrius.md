---
description: "Agrius is an Iran-aligned destructive threat actor targeting Israeli organizations with wiper malware disguised as ransomware, operating through the BlackShadow and Moneybird personas."
---

# Agrius

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Agrius](../navigation/actor-workbench.md#agrius)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact (M2)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs
- IOC reference sources: `SRC-MITRE-G1030` Technique references
- Tool detail pages: [`Moneybird`](../tools/moneybird.md); [`BlackShadow`](../tools/blackshadow.md); [`Apostle`](../tools/apostle.md); [`ASPXSpy`](../tools/aspxspy.md); [`BFG Agonizer`](../tools/bfg-agonizer.md); [`DEADWOOD`](../tools/deadwood.md); [`IPsec Helper`](../tools/ipsec-helper.md); [`Mimikatz`](../tools/mimikatz.md); [`MultiLayer Wiper`](../tools/multilayer-wiper.md); [`NBTscan`](../tools/nbtscan.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#agrius) (10 mapped tool row(s))
- Evidence records: `EVD-017` / `CLM-AGRIUS-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G1030`

<!-- ACTOR-NAVIGATION:END -->

## Background

Agrius emerged in public reporting around 2020-2021 as an Iran-aligned destructive threat actor targeting Israeli and Israeli-adjacent organizations. Unlike Iran's traditional espionage groups, Agrius specializes in destructive operations framed with ransomware aesthetics — deploying fake ransomware that is actually a wiper, and in some cases following up with extortion claims via the BlackShadow persona.

SentinelLabs documented "Operation Dreams Come True" (2021), identifying Apostle — malware initially observed behaving as a wiper before a later version was modified to function as actual ransomware, providing cover for destructive intent. The group also deployed DEADWOOD (a standalone wiper) and in 2022-2023 pivoted to BFG Agonizer and MultiLayer Wiper variants analyzed by Unit 42 under the "Agonizing Serpens" designation. Targeted sectors have included Israel's diamond industry, hospitality, and information technology firms — industries where operational disruption and data loss create compounding business impact.

A consistent pattern is initial access via internet-facing web application exploitation (ASPXSpy webshells), followed by credential theft (Mimikatz), internal reconnaissance (NBTscan), and then wiper deployment. The ransom note and extortion persona are assessed as cover for destructive intent rather than genuine financially-motivated ransomware. The BlackShadow persona was used to publish claimed stolen data to pressure victims and generate media attention.

The Ziv Hospital incident reported in Israeli media in 2023 has been mentioned alongside Agrius in some secondary reporting; primary-source technical confirmation from INCD/IDF/ISA remains absent as of repository review. Analysts should treat media-reported victim attributions as provisional until primary government or incident-response reporting is available.

Aliases: Pink Sandstorm, AMERICIUM, Agonizing Serpens, BlackShadow.

Assessed sponsor: Iran-aligned (assessed by some sources as MOIS-linked; firm MOIS attribution not established in primary reporting). SentinelLabs, Unit 42, and Microsoft use "Iran-aligned" or "Iran-nexus" language without confirming a specific Iranian intelligence service. Use evidence label `Assessed-by-source` rather than `Source-reported` for any MOIS claim.

## Relevance

Agrius is high priority because public reporting links the actor to ransomware and wiper operations in the Middle East with emphasis on Israeli targets.

## Defensive Focus

- Destructive staging and wiper-like activity.
- Backup deletion or backup access abuse.
- Security tool tampering.
- Ransomware-style encryption and extortion cover stories.

## Detection Ideas

- Privileged account deleting or modifying backup policies.
- Endpoint protection service tampering followed by mass file operations.
- Unexpected use of tunneling or admin tools from non-admin workstations.

Sources: `SRC-MITRE-G1030`, `SRC-S1-AGRIUS-WIPER`, `SRC-S1-APOSTLE`, `SRC-UNIT42-AGRIUS`, `SRC-ISRAELHAYOM-ZIV-2023`, `SRC-TOI-ZIV-2023`, `SRC-CENTRIPETAL-PREPOSITIONED-2025`, `SRC-ANVILOGIC-IRAN-CI-2026`.

Source note: Ziv Hospital and camera/BDA-related claims are not promoted here as high-confidence Agrius facts. Treat the news and supporting vendor sources as context until primary INCD/IDF/ISA or source telemetry is available.

## Public Reports

**MITRE ATT&CK:**

- [MITRE ATT&CK G1030 — Agrius](https://attack.mitre.org/groups/G1030/) — Technique mappings, software associations (Apostle, Moneybird, BFG Agonizer, DEADWOOD, MultiLayer Wiper), and alias registry.

**Primary vendor reporting:**

- SentinelLabs, "Agrius Targets the Israeli Higher Education and Technology Sectors" — 2022. Documents Fantasy wiper campaigns targeting Israeli sectors. Source ID `SRC-S1-AGRIUS-WIPER`.
- SentinelLabs, "Apostle: A Ransomware-Posing Wiper" — 2021. Original analysis of Apostle's dual wiper/ransomware functionality and its role in Agrius operations. Source ID `SRC-S1-APOSTLE`.
- Unit 42 / Palo Alto Networks, "Agonizing Serpens (Agrius) Targeting Israeli Organizations" — 2023. Documents expanded toolset including BFG Agonizer and MultiLayer Wiper, analysis of destructive campaign chains. Source ID `SRC-UNIT42-AGRIUS`.
- Microsoft, "Pink Sandstorm / AMERICIUM" — Attribution and technical analysis from Microsoft's actor tracking program.
- Centripetal, Iran cyber prepositioned 2025 reporting. Source ID `SRC-CENTRIPETAL-PREPOSITIONED-2025`.
- Anvilogic, Iranian cyber 2026 context. Source ID `SRC-ANVILOGIC-IRAN-CI-2026`.
