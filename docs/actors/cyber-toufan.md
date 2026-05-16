# Cyber Toufan

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Cyber Toufan](../navigation/actor-workbench.md#cyber-toufan)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [OT, PLC, HMI, And Exposed Engineering Interfaces](../navigation/surface-capability-matrix.md#ot-plc); [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1491](../navigation/ttp-detection-matrix.md#t1491) Defacement (M2); [T1595](../navigation/ttp-detection-matrix.md#t1595) Active Scanning (M1); [T1021.002](../navigation/ttp-detection-matrix.md#t1021002) SMB/Windows Admin Shares (M3)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Cyber Toufan supplier-access playbook`](../tools/cyber-toufan-supplier-access-playbook.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cyber-toufan) (1 mapped tool row(s))
- Evidence records: `EVD-023` / `CLM-CYBERTOUFAN-001`
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-MS-IRAN-HAMAS`, `SRC-OPI-CYBER-TOUFAN`

<!-- ACTOR-NAVIGATION:END -->

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

The KQL hunt `detections/kql/smb-admin-share-lateral-movement-anomaly.kql` covers the native SMB lateral movement pattern described in the OP Innovate playbook.
