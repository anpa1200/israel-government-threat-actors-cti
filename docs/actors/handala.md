# Void Manticore / Handala

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
- `SRC-PUSH-STRYKER-HANDALA`: Push Security Stryker incident analysis — Intune Remote Wipe via compromised Global Administrator credentials (March 2026).
- `SRC-AP-HANDALA`: authored CTI assessment with SOC defensive guidance — rated B, trace primary references for operational decisions.
- `SRC-CYBERINT-HANDALA`: supporting vendor overview — rated B.
