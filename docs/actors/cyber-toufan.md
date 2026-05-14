# Cyber Toufan

Assessed sponsor: Iran-aligned persona / hacktivist persona in public reporting.

## Relevance

Cyber Toufan is relevant as a claimed activity persona around Israeli targets, especially where public claims, leaks, and disruptive messaging may affect public confidence. Treat claims as unverified until supported by forensic evidence or reputable reporting.

## Defensive Focus

- Leak claims and public data exposure.
- Website disruption and defacement.
- Psychological operations and media amplification.
- Incident communications coordination.

## Analytic Caution

Attribution confidence is medium or lower unless supported by independent technical evidence.

## Repository Sources

- `SRC-OPI-CYBER-TOUFAN`: OP Innovate primary playbook analysis — external exposure, credential abuse, SMB lateral movement via admin shares, Telegram leak operations.
- `SRC-MS-IRAN-HAMAS`: Microsoft Threat Intelligence, Iran influence operations context.

## Associated Detection Content

The KQL hunt `detections/kql/cyber-toufan-smb-admin-share-lateral-movement.kql` covers the native SMB lateral movement pattern described in the OP Innovate playbook.

