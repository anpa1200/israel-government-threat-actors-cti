---
description: "WIRTE is a Hamas-affiliated threat actor that evolved from espionage to destructive operations, deploying the SameCoin wiper against Israeli financial institutions and hospitals in 2024."
head:
  - tag: script
    attributes:
      type: application/ld+json
    innerHTML: >-
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is WIRTE?","acceptedAnswer":{"@type":"Answer","text":"WIRTE is a Hamas-affiliated threat actor tracked since approximately 2018 that evolved from espionage to disruptive operations. In October 2024, Check Point Research documented WIRTE deploying the SameCoin wiper against Israeli financial institutions and hospital networks, using fake security software update lures impersonating ESET and Kaspersky. The group's trusted-sender abuse technique — compromising legitimate organizational email accounts to send phishing — makes it particularly dangerous for well-defended targets. Also known as Ashen Lepus."}},{"@type":"Question","name":"How to detect WIRTE and SameCoin wiper activity?","acceptedAnswer":{"@type":"Answer","text":"Key WIRTE detection approaches: detect signed executable launching from archive or user download paths followed by DLL loads from the same directory (fake vendor update pattern); watch for inbound email from trusted regional senders containing archives, XLL files, or PPAM files; monitor for suspicious DLL sideloading patterns associated with security software filenames (ESET, Kaspersky branding); detect mass file modification or destruction from workstation processes (wiper behavior); monitor Intune for bulk device wipe anomalies suggesting identity-plane destructive activity."}},{"@type":"Question","name":"What is the SameCoin wiper used by WIRTE?","acceptedAnswer":{"@type":"Answer","text":"SameCoin is a two-stage destructive payload deployed by WIRTE against Israeli targets in October 2024. Stage 1 is a custom downloader delivered via fake security software update lures. Stage 2 is the wiper module that overwrites files and renders systems inoperable. SameCoin was deployed against Israeli financial institutions and hospital networks in a deliberate escalation toward civilian-impact sectors during the active conflict period."}}]}
---

# WIRTE

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [WIRTE](../navigation/actor-workbench.md#wirte)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M2); [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking (M3); [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer (M3); [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M3)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-CP-WIRTE-2024` Wiper references; trusted sender abuse; fake update artifacts; `SRC-UNIT42-ASHTAG-2025` Malware hashes; domains; C2 paths; tool behavior
- Tool detail pages: [`SameCoin`](../tools/samecoin.md); [`AshTag`](../tools/ashtag.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#wirte) (2 mapped tool row(s))
- Evidence records: `EVD-010` / `CLM-WIRTE-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CP-WIRTE-2024`, `SRC-UNIT42-ASHTAG-2025`

<!-- ACTOR-NAVIGATION:END -->

## Background

WIRTE is a Hamas-affiliated threat actor that Check Point Research has tracked since approximately 2018 across multiple operational phases. The group began as a conventional espionage cluster targeting Middle East government entities — Palestinian Authority institutions, Israeli government, Jordanian, Saudi, and Iraqi organizations — using phishing and commodity malware. Through 2022-2023, WIRTE operated primarily as a credential harvester and document stealer, consistent with an intelligence collection mandate.

The group's most significant operational shift occurred in October 2024, documented by Check Point Research: WIRTE expanded from espionage into disruptive and destructive activity against Israeli targets. The SameCoin wiper — a two-stage payload using a custom downloader and a wiper module — was deployed against Israeli financial institutions and hospital networks using fake security software update lures impersonating ESET, Kaspersky, and regional IT vendors. The timing and target selection (hospitals, financial sector) during active conflict suggest deliberate escalation toward civilian-impact sectors.

WIRTE's trusted-sender abuse technique is particularly concerning: the group has compromised legitimate government and regional organization email accounts to send phishing from email addresses with established trust histories, bypassing sender-reputation defenses. Combined with fake security software update themes, this creates a high-conversion delivery chain even for security-aware users.

Unit 42's October 2025 analysis of the AshTag backdoor documented continued WIRTE operations with updated Python-based tooling featuring modular architecture and encrypted C2. AshTag represents a maturation in custom capability development, suggesting WIRTE's technical sophistication is increasing alongside its operational ambition.

WIRTE and TA402 (Molerats) are both tracked as Hamas-affiliated and share Gaza Cybergang umbrella classifications in some vendor reporting. Analysts should treat them as potentially distinct subgroups unless source reporting explicitly clusters a specific campaign under both designations.

Aliases: Ashen Lepus; Gaza Cybergang-linked reporting.

Assessed sponsor: Hamas-affiliated in Check Point public reporting.

## Relevance

WIRTE is high priority for Israeli public-sector defenders because Check Point reported expansion from espionage into disruptive activity against Israeli entities, including SameCoin-linked wiper activity.

## Defensive Focus

- Trusted sender abuse.
- Fake security or vendor update lures.
- Archive-to-execution chains.
- DLL sideloading.
- Wiper-preparation behavior.

## Detection Ideas

- Signed installer execution from archive or user download paths followed by same-directory DLL loads.
- Inbound mail from trusted regional senders that suddenly includes archives, XLL/PPAM files, or update-themed links.
- Fake ESET/Kaspersky/reseller update filenames.

Sources: `SRC-CP-WIRTE-2024`, `SRC-PROOFPOINT-TA402-IRONWIND`, `SRC-UNIT42-ASHTAG-2025`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`.

## Public Reports

**Primary vendor reporting:**

- Check Point Research, "WIRTE's Expanded Campaign Against Israel: From Espionage to Disruption" — October 2024. Documents the pivot to disruptive operations, SameCoin wiper deployment against Israeli financial and hospital sectors, trusted-sender-abuse technique, and fake security update lure themes. Source ID `SRC-CP-WIRTE-2024`.
- Unit 42 / Palo Alto Networks, "AshTag: New Python-Based Backdoor in WIRTE Operations" — October 2025. Analysis of modular Python backdoor with encrypted C2, documenting continued WIRTE technical development. Source ID `SRC-UNIT42-ASHTAG-2025`.
- SentinelLabs, "The Cyber Dimension of the Israel-Hamas Conflict" — 2023. Actor context for WIRTE within the Palestinian-affiliated threat landscape. Source ID `SRC-S1-ISRAEL-HAMAS-CYBER-2023`.
- Proofpoint, TA402/IronWind reporting — Context for the broader Hamas-affiliated phishing ecosystem that overlaps with WIRTE's operational environment. Source ID `SRC-PROOFPOINT-TA402-IRONWIND`.

## Related Actors

- [Arid Viper / APT-C-23](./arid-viper.md) — Parallel Hamas-affiliated cluster with mobile-focused (Android malware) capability profile, operating alongside WIRTE's Windows-enterprise tradecraft within the same adversarial ecosystem.
- [TA402](./ta402.md) — Hamas-affiliated phishing actor with overlapping operational environment; compare IronWind toolchain with WIRTE's SameCoin wiper and AshTag backdoor tradecraft.
