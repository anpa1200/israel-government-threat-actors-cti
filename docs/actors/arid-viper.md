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

## Background

APT-C-23 (Arid Viper) is a Palestinian-nexus mobile threat actor active since approximately 2015, when Kaspersky and Trend Micro first published analysis of the "Desert Falcon" cluster conducting espionage against Egyptian, Palestinian, and Israeli military targets. The group's primary capability is Android spyware development and social engineering, using fake apps, romantic baiting via fake social media profiles, and chat-based luring to install surveillance tools on target devices.

The group has developed an extensive portfolio of mobile malware over the decade since its discovery: FrozenCell (Android spyware with persistent surveillance), Desert Scorpion (targeting Palestinians and Jordanians), Micropsia (Android RAT), Phenakite (iOS-targeting), and AridSpy (2024, deployed via fake WhatsApp and Telegram apps). A recurring operational pattern is impersonating legitimate apps popular in the target community — most notably the "RedAlert" Israel rocket alarm application, which the group cloned with a backdoored version to target Israeli citizens concerned about missile alerts.

Meta's threat intelligence team has been a consistent source of disruption reporting, publishing network takedowns of APT-C-23 operations targeting Israeli military personnel, Palestinian civil society, and Egyptian political figures. ESET's 2024 AridSpy analysis documented campaigns targeting users in Egypt and Palestine via malicious apps deployed through dedicated websites and social engineering in WhatsApp groups, indicating the group's ongoing operational tempo.

For Israeli government and defense sector defenders, the primary risk surface is mobile devices used by personnel engaged in sensitive operations or with access to classified networks. The group's use of romantic baiting and professional persona cultivation means this is a human-factors threat as much as a technical one — effective countermeasures require both MDM enforcement and security awareness training for high-risk users.

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

## Public Reports

**Own ecosystem:**

- [Deep Research Intake: APT39, Arid Viper, UNC3890, Cyber Toufan](../reports/apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) — Internal repository synthesis. High-priority, requires source validation.

**MITRE ATT&CK:**

- [MITRE ATT&CK G1028 — APT-C-23](https://attack.mitre.org/groups/G1028/) — Technique mappings, software associations (AridSpy, Desert Scorpion, FrozenCell, Micropsia, Phenakite, SpyC23), and alias registry.

**Primary vendor reporting:**

- Meta Threat Intelligence, "Quarterly Adversarial Threat Report" — Ongoing disruption reporting on APT-C-23 networks targeting Israeli military, Palestinian civil society, and Egyptian political targets. Source ID `SRC-META-ARIDVIPER`.
- ESET Research, "AridSpy: Trojanized Applications Targeting Egypt and Palestine" — 2024. Analysis of fake WhatsApp/Telegram-based AridSpy distribution infrastructure. Source ID `SRC-ESET-ARIDSPY`.
- SentinelLabs, "The Cyber Dimension of the Israel-Hamas Conflict" — 2023. Actor context and mobile threat landscape overview for conflict-period operations. Source ID `SRC-S1-ISRAEL-HAMAS-CYBER-2023`.
- Cisco Talos, Micropsia analysis — Technical analysis of Android malware campaign targeting Israeli military-adjacent users.
- Kaspersky, "Desert Falcon" — 2015 original disclosure. Documents earliest known APT-C-23 operations and targeting patterns.
