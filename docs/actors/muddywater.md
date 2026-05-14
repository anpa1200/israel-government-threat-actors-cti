# MuddyWater

Aliases: Mango Sandstorm, Boggy Serpens (Microsoft, current), Static Kitten, Seedworm, MERCURY (Microsoft, retired April 2023), TEMP.Zagros, TA450 (Proofpoint), Earth Vetala (Trend Micro).

Assessed sponsor: Iran MOIS-aligned in public reporting.

## Relevance

MuddyWater is high priority for Israeli government and regional public-sector defense because MITRE records targeting of government, local government, telecommunications, defense, and oil and gas organizations across the Middle East and other regions.

## Defensive Focus

- Spearphishing and malicious document delivery.
- PowerShell execution and script-based collection.
- Legitimate remote access tool abuse.
- Credential collection and lateral movement preparation.

## Detection Ideas

- RMM execution from user download folders.
- PowerShell encoded commands launched by Office, browser, archive, or script-host processes.
- New persistence from suspicious scheduled tasks or registry run keys.

Sources: `SRC-MITRE-G0069`, `SRC-CISA-AA22-055A`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-CP-BUGSLEEP`, `SRC-KASPERSKY-ICS-Q4-2025`, `SRC-BRANDEFENSE-MUDDYWATER-2025`, `SRC-AP-MUDDYWATER`.

Source note: Kaspersky ICS and Brandefense are Score B synthesis sources in this repository. Use them for collection planning and cross-checking, then anchor high-impact claims to ESET, INCD, CISA, MITRE, or Check Point.
