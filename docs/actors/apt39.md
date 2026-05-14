---
title: APT39
sidebar_label: APT39
---

# APT39

Aliases: APT39, Chafer, Remix Kitten, ITG07. U.S. government and MITRE reporting connect APT39 activity to Rana Intelligence Computing.

Assessed sponsor: Iran MOIS via Rana Intelligence Computing in U.S. Treasury / DOJ and MITRE ATT&CK reporting.

## Relevance

APT39 is medium priority for Israeli public-sector defenders. The actor's strongest documented focus is telecom, travel, hospitality, IT, government, and identity-rich data collection across the Middle East and beyond. That is strategically relevant to Israeli border, civil aviation, telecom, and regional service-provider exposure. Current primary-source review preserves a gap for specific Israeli victim incidents in public reporting.

## Defensive Focus

- Surveillance-oriented access to telecom, travel, PNR, identity, and subscriber systems.
- Long-dwell credential harvesting rather than rapid destructive action.
- LSASS dumping and Sysinternals-style administrative tooling.
- Service execution and lateral movement inside telecom and travel networks.
- IT-provider compromise for supply-chain access.

## Detection Ideas

- `procdump.exe` or renamed dump utilities targeting `lsass.exe`, especially on domain controllers and critical application servers.
- PsExec or service-control lateral movement from non-admin subnets into telecom or public-sector segments.
- Bulk access to subscriber, travel, identity, or PNR data stores from unusual admin paths.
- Spearphishing attachment execution followed by credential collection or service installation.

## Operational Status

Current primary-source review did not identify high-confidence 2023-2025 incident reporting under the APT39 / Chafer / Remix Kitten label set. Keep recent operational evidence explicitly marked as limited until new primary reporting is added.

## Repository Sources

- `SRC-MITRE-G0087`: MITRE ATT&CK APT39 group profile.
- `SRC-US-TREASURY-RANA-2020`: U.S. Treasury sanctions announcement.
- `SRC-US-DOJ-RANA-2020`: U.S. DOJ Rana Intelligence Computing announcement.
