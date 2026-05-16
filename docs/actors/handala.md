# Void Manticore / Handala

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Void Manticore / Handala](../navigation/actor-workbench.md#void-manticore-handala)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](../navigation/surface-capability-matrix.md#identity-mdm); [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M2); [T1204](../navigation/ttp-detection-matrix.md#t1204) User Execution (M2); [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1490](../navigation/ttp-detection-matrix.md#t1490) Inhibit System Recovery (M2); [T1567](../navigation/ttp-detection-matrix.md#t1567) Exfiltration Over Web Service (M2); [T1078.004](../navigation/ttp-detection-matrix.md#t1078004) Valid Accounts: Cloud Accounts (M3)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-AP-HANDALA` IP/CIDR; hashes; URLs; actor channels; soft IOCs; `SRC-THREAT-HUNTER-V3` Domains; IPs; file names; driver names; behavioral IOCs
- Malware and tools: [`BiBi / BiBi Wiper lineage`](../tools/bibi-bibi-wiper-lineage.md) (Wiper / destructive malware lineage); [`Handala-linked destructive installer chains`](../tools/handala-linked-destructive-installer-chains.md) (Installer-led destructive chain)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#void-manticore-handala) (2 mapped tool row(s))
- Tool detail pages: [`BiBi / BiBi Wiper lineage`](../tools/bibi-bibi-wiper-lineage.md); [`Handala-linked destructive installer chains`](../tools/handala-linked-destructive-installer-chains.md)
- Evidence records: `EVD-005` / `CLM-HANDALA-001`; `EVD-006` / `CLM-HANDALA-002`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-HANDALA`, `SRC-PUSH-STRYKER-HANDALA`, `SRC-THREAT-HUNTER-V3`

<!-- ACTOR-NAVIGATION:END -->

Primary cluster: Void Manticore.

Public personas and aliases: Handala Hack, Karma, Karma Below (Karmabelow80), Homeland Justice, Storm-0842, BANISHED KITTEN, Dune, COBALT MYSTIQUE, Red Sandstorm.

Note on naming: Handala, Karma, and Homeland Justice are treated here as public personas associated with Void Manticore, not interchangeable proof that every public claim is a confirmed Void Manticore intrusion. "Storm-842" appears in some secondary literature as a shorthand for Storm-0842; both refer to the same Microsoft-designated cluster. "Temple of Oats" is the title of the Mandiant/Check Point reporting on Void Manticore, not a tracked alias. Homeland Justice was used in Albania-targeting campaigns.

Assessed sponsor: Iran-aligned persona / MOIS-linked cluster in public reporting. Incident-level confidence varies by source and event.

## Relevance

Void Manticore / Handala is high priority for Israeli government and public-sector defenders because the related cluster and persona reporting focus heavily on Israeli organizations, civilian-impact sectors, public claims, leak pressure, and destructive or disruptive operations.

Andrey Pautov's Medium assessment `SRC-AP-HANDALA` frames Handala as an influence-enabled intrusion threat: compromise, leak or destructive action, rapid public claim publication, and narrative amplification. The profile also notes cross-vendor cluster convergence around Void Manticore / Storm-0842 / BANISHED KITTEN / Dune style naming, while warning that vendor naming overlap does not prove every incident-level attribution.

## Defensive Focus

- Public claim monitoring.
- Evidence preservation.
- Defacement and public web integrity monitoring.
- Communications playbooks for unverified claims.
- Wiper and destructive-activity first-response playbooks.
- Installer/archive execution chains from user-controlled locations.
- Commercial file-sharing and cloud-hosted payload delivery.
- Backup integrity, recovery controls, and privileged-account containment.

## Analytic Caution

Use low-to-medium confidence unless a primary technical source ties the persona to a confirmed incident.

## Detection Ideas

- Archive or installer execution after current-event lure delivery.
- `.msi`, `.exe`, or script execution from `Downloads`, `%TEMP%`, or mail attachment extraction paths.
- Commercial file-sharing download followed by child process creation.
- Backup deletion, recovery inhibition, or endpoint protection tampering near suspected compromise windows.
- Public claim timeline correlated with SIEM, EDR, WAF, identity, and email telemetry before external communications.

## Repository Sources

- `SRC-MITRE-G1055`: MITRE VOID MANTICORE profile — primary alias registry (Handala Hack, Homeland Justice, Karma, Karmabelow80, BANISHED KITTEN, Red Sandstorm, COBALT MYSTIQUE, Dune).
- `SRC-CP-HANDALA-2026`: Check Point Research Handala modus operandi report (March 2026).
- `SRC-CP-VOID-2024`: Check Point Research "Bad Karma No Justice" — Void Manticore destructive activity in Israel, Karma persona (May 2024).
- `SRC-CP-MOIS-CRIME`: Check Point Research analysis of MOIS-linked actors and criminal ecosystem convergence (March 2026).
- `SRC-PUSH-STRYKER-HANDALA`: Push Security Stryker incident analysis — Intune Remote Wipe via compromised Global Administrator credentials (March 2026).
- `SRC-AP-HANDALA`: authored CTI assessment with SOC defensive guidance — rated B, trace primary references for operational decisions.
