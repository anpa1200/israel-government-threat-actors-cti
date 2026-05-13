# Handala Hack Team

Aliases: Handala, Void Manticore, Storm-0842, Storm-842, BANISHED KITTEN, Dune, COBALT MYSTIQUE.

Assessed sponsor: Iran-aligned persona / MOIS-linked cluster in public reporting. Incident-level confidence varies by source and event.

## Relevance

Handala is high priority for Israeli government and public-sector defenders because the persona and related cluster reporting focus heavily on Israeli organizations, civilian-impact sectors, public claims, leak pressure, and destructive or disruptive operations.

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

- `SRC-AP-HANDALA`: authored CTI assessment and SOC defensive guidance.
- `SRC-CP-HANDALA-2026`: Check Point Research Handala modus operandi report.
- `SRC-CP-VOID-2024`: Check Point Research Void Manticore destructive activity report.
- `SRC-MITRE-G1055`: MITRE VOID MANTICORE profile.
- `SRC-CYBERINT-HANDALA`: supporting vendor overview.
