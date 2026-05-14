# APT-C-23 / Arid Viper

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
