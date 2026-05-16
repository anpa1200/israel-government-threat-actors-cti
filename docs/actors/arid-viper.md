# APT-C-23 / Arid Viper

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [APT-C-23](../navigation/actor-workbench.md#apt-c-23)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1660](../navigation/ttp-detection-matrix.md#t1660) Phishing (M2); [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File (M3)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-META-ARIDVIPER` Domains; apps; mobile indicators; `SRC-CYBERNEWS-REDALERT-2026` App names; package references; domains from secondary coverage; `SRC-S1-ISRAEL-HAMAS-CYBER-2023` Actor context; mobile and social-engineering references
- Tool detail pages: [`AridSpy`](../tools/aridspy.md); [`RedAlert.apk`](../tools/redalertapk.md); [`Desert Scorpion`](../tools/desert-scorpion.md); [`FrozenCell`](../tools/frozencell.md); [`Micropsia`](../tools/micropsia.md); [`Phenakite`](../tools/phenakite.md); [`SpyC23`](../tools/spyc23.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt-c-23) (7 mapped tool row(s))
- Evidence records: `EVD-011` / `CLM-ARIDVIPER-001`
- Imported research intakes: [APT39 Arid Viper UNC3890 Cyber Toufan Deep Research Intake](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) (High, Needs source validation)
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CYBERNEWS-REDALERT-2026`, `SRC-ESET-ARIDSPY`, `SRC-META-ARIDVIPER`, `SRC-MITRE-G1028`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`

<!-- ACTOR-NAVIGATION:END -->

Aliases: Desert Falcon, Mantis, TAG-63, Grey Karkadann, Renegade Jackal (CrowdStrike).

Note on removed alias: "Two-tailed Scorpion" does not appear as a tracked alias for APT-C-23 in MITRE G1028, ESET, Meta, Cisco Talos, or CrowdStrike reporting and has been removed to avoid taxonomy confusion.

Assessed sponsor: Hamas-linked / Palestinian regional actor in public reporting.

## Relevance

APT-C-23 is relevant to Israeli government and security-adjacent organizations because MITRE describes Middle East operations including Israeli military assets and mobile spyware development.

## Defensive Focus

- Mobile phishing and malicious app delivery.
- Social media personas and chat-based lures.
- Credential theft and surveillance.
- High-risk mobile users in government and defense roles.

## Detection Ideas

- MDM alerts for sideloaded or unapproved applications.
- User reports of suspicious social media recruitment or relationship-building approaches.
- Mobile DNS traffic to known campaign infrastructure from vendor reports.

Sources: `SRC-MITRE-G1028`, `SRC-META-ARIDVIPER`, `SRC-ESET-ARIDSPY`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`, `SRC-CYBERNEWS-REDALERT-2026`.

Source note: Cybernews/Acronis RedAlert coverage is Score B secondary reporting in this repository. Keep RedAlert.apk-specific claims provisional until a primary Acronis TRU report is available.
