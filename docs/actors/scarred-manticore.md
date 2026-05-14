---
title: Scarred Manticore
sidebar_label: Scarred Manticore
---

# Scarred Manticore

Aliases: Storm-0861 (Microsoft), UNC1448 (Mandiant, some reporting), LIONTAIL cluster (Check Point tooling reference).

Assessed sponsor: Iran MOIS-aligned in Check Point and Microsoft reporting. Some reporting describes overlap or tasking coordination with Void Manticore (Handala) for destructive follow-on operations.

## Relevance

Scarred Manticore is high priority for Israeli government and public-sector defenders because:

1. Check Point Research ("Bad Karma No Justice", May 2024) and MITRE G1055 describe a documented MOIS dual-actor handoff: Scarred Manticore obtains initial access — frequently via exploitation of public-facing web applications — and then transfers that access to Void Manticore (Handala) for destructive operations.
2. This means Scarred Manticore activity in Israeli government or critical infrastructure networks is a **precursor indicator** for destructive wiper or data-destruction operations, not only espionage.
3. The actor has been linked to targeting of telecommunications, government, and critical infrastructure across the Middle East including Israel.

## Defensive Focus

- Public-facing web applications: SharePoint, IIS, Exchange, and government portals.
- IIS native module implants (Liontail framework) — passive backdoors that blend into legitimate server traffic.
- Exploitation of known CVEs in perimeter applications before patch deployment.
- Long-lived passive persistence that may show minimal outbound traffic.
- Handoff detection: correlate web-exploitation incidents with subsequent destructive staging activity across the same victim network.

## Associated Tooling

- **Liontail**: Custom passive backdoor framework loading malicious IIS native modules and HTTP.sys listeners. Low traffic-volume footprint. Reported by Check Point Research (October 2023).
- **TEMPODROP**: Dropper associated in some reporting with this cluster.
- SharePoint CVE-2019-0604 exploitation reported as an initial access vector.
- Additional web shell variants dropped via IIS module load path.

## Kill Chain Position

```text
Scarred Manticore (Initial Access / Persistence)
  → Void Manticore / Handala (Destruction / Leak / Psychological Effect)
```

This handoff structure means defenders MUST treat confirmed Scarred Manticore access as a potential pre-destruction scenario and initiate containment, not only monitoring.

## Detection Ideas

- New or modified files under `%SystemRoot%\System32\inetsrv\` outside approved deployment windows.
- IIS worker process (`w3wp.exe`) loading unsigned or unexpected native DLLs.
- HTTP.sys event log entries for unexpected filter registrations.
- Web server processes spawning scripting interpreters or staging tools.
- SharePoint-sourced file writes to non-SharePoint paths (lateral preparation).
- Long-lived low-volume C2 callbacks from web servers or DMZ hosts with no associated user activity.
- Cross-correlation: destructive activity (mass file operations, backup deletion, VSS deletion) appearing on networks where edge-application anomalies were recently observed.

## Analytic Caution

Scarred Manticore should not be used as a default label for every Iranian-linked webshell or IIS implant. Analysts SHOULD require: victimology match, Liontail-family tooling or IIS native module pattern, and where possible, source-backed infrastructure or malware-family linkage before attributing to this cluster rather than UNC1860 or OilRig.

## Repository Sources

- `SRC-CP-VOID-2024`: Check Point Research "Bad Karma No Justice" — documents Scarred Manticore as initial access provider handing off to Void Manticore for destructive operations in Israel.
- `SRC-MITRE-G1055`: MITRE Void Manticore profile — references Scarred Manticore collaboration and initial access role.
- `SRC-CP-SCARRED-MANTICORE-2023`: Check Point Research "Scarred Manticore versus MOIS: Seeing the Invisible" — primary Liontail framework analysis (October 2023).
