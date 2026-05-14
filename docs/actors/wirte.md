# WIRTE

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
