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
- Tool detail pages: [`BiBi / BiBi Wiper lineage`](../tools/bibi-bibi-wiper-lineage.md); [`Handala-linked destructive installer chains`](../tools/handala-linked-destructive-installer-chains.md); [`CHIMNEYSWEEP`](../tools/chimneysweep.md); [`ftp`](../tools/ftp.md); [`Impacket`](../tools/impacket.md); [`Mimikatz`](../tools/mimikatz.md); [`RawDisk`](../tools/rawdisk.md); [`ROADSWEEP`](../tools/roadsweep.md); [`ZeroCleare`](../tools/zerocleare.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#void-manticore-handala) (9 mapped tool row(s))
- Evidence records: `EVD-005` / `CLM-HANDALA-001`; `EVD-006` / `CLM-HANDALA-002`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-HANDALA`, `SRC-MITRE-G1055`, `SRC-PUSH-STRYKER-HANDALA`, `SRC-THREAT-HUNTER-V3`

<!-- ACTOR-NAVIGATION:END -->

## Background

Void Manticore emerged publicly in October 2023, immediately following Hamas's attack on Israel, operating primarily through the "Handala Hack" and "Karma" public personas. The cluster is assessed in public reporting as Iran MOIS-linked, and follows a documented pattern of influence-enabled intrusion: compromise, destructive or data-theft action, public claim announcement on Telegram, and sustained narrative amplification. The name "Handala" references a Palestinian political cartoon symbol — a deliberate framing choice emphasizing psychological effect alongside technical operations.

The actor's most visible destructive tool is the BiBi Wiper family, first analyzed by Security Joes in October 2023. BiBi-Linux and BiBi-Windows variants were deployed against Israeli organizations in the weeks following the October 7 attack, overwriting files and corrupting master boot records. Subsequent Check Point research documented an operational handoff model: Scarred Manticore provides initial access through webshell implantation on edge systems, then transfers that access to Void Manticore for destructive and leak operations. This division of labor is analytically significant — Scarred Manticore indicators on an Israeli network should be treated as a potential pre-destruction precursor.

Beyond destructive operations, Void Manticore operates psychological pressure campaigns through Telegram leak channels, claiming victim data, hosting stolen files, and timing announcements to maximize public impact. The cluster has also been linked to Homeland Justice, the persona used against Albania in 2022 that disrupted Albanian government services with ROADSWEEP ransomware and CHIMNEYSWEEP backdoor. The Push Security "Stryker" case (March 2026) documented Global Administrator account compromise leading to mass Intune remote device wipe — a cloud-plane destructive pattern consistent with the overall cluster's escalation trajectory.

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

## Public Reports

**Own ecosystem — read first:**

- [CTI Research: Handala Hack Group aka Handala Hack Team](https://medium.com/@1200km/cti-research-handala-hack-group-aka-handala-hack-team-ddbdd294cfb8) — Andrey Pautov / 1200km. Defensive CTI assessment with IOC synthesis, actor mapping, alias table, and SOC guidance. Source ID `SRC-AP-HANDALA`.
- [CTI Kill Chain: An Analyst Guide With Real-World Evidence](https://infosecwriteups.com/cti-kill-chain-an-analyst-guide-with-real-world-evidence-c3bef6fd2979) — 1200km on Infosec Write-ups. Methodology reference for converting threat actor evidence into defensive decisions, applicable to Handala cluster analysis.

**MITRE ATT&CK:**

- [MITRE ATT&CK G1055 — Void Manticore](https://attack.mitre.org/groups/G1055/) — Authoritative alias registry, technique mappings, software references, and sub-group relationships including Handala Hack, Karma, Homeland Justice, BANISHED KITTEN, and Storm-0842.

**Primary vendor reporting:**

- Check Point Research, "Void Manticore's Destructive Operations Against Israel" (Bad Karma No Justice) — May 2024. Primary source for Scarred Manticore → Void Manticore handoff model, Karma persona, and wiper deployment sequences. Source ID `SRC-CP-VOID-2024`.
- Check Point Research, "Handala Modus Operandi" — March 2026. Updated operational profile. Source ID `SRC-CP-HANDALA-2026`.
- Check Point Research, "MOIS-Linked Actors and Criminal Ecosystem Convergence" — March 2026. Source ID `SRC-CP-MOIS-CRIME`.
- Push Security, "Stryker: Intune Remote Wipe via Compromised Global Administrator" — March 2026. Cloud-plane destructive pattern. Source ID `SRC-PUSH-STRYKER-HANDALA`.
