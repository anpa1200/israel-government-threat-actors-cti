---
title: Scarred Manticore
sidebar_label: Scarred Manticore
---

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Scarred Manticore](../navigation/actor-workbench.md#scarred-manticore)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Internet-Facing Servers, Webshells, And Passive Access](../navigation/surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1505.004](../navigation/ttp-detection-matrix.md#t1505004) IIS Components (M2); [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell (M2); [T1071.001](../navigation/ttp-detection-matrix.md#t1071001) Web Protocols (M2); [T1199](../navigation/ttp-detection-matrix.md#t1199) Trusted Relationship (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: None currently mapped.
- Tool detail pages: [`Liontail`](../tools/liontail.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#scarred-manticore) (1 mapped tool row(s))
- Evidence records: `EVD-007` / `CLM-SCARRED-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CP-SCARRED-MANTICORE-2023`, `SRC-CP-VOID-2024`

<!-- ACTOR-NAVIGATION:END -->

# Scarred Manticore

## Background

Scarred Manticore is an Iran MOIS-affiliated threat actor specializing in persistent access to high-value government, telecommunications, and critical infrastructure networks through passive IIS-based backdoors. The group became publicly prominent with Check Point Research's October 2023 report "Scarred Manticore versus MOIS: Seeing the Invisible," which documented the Liontail framework — a sophisticated set of custom IIS native modules and HTTP.sys listeners that intercept specially crafted HTTP requests while remaining invisible to standard process-level monitoring.

The Liontail framework's design reflects a mature operational security posture. By loading as a native IIS module rather than a separate process, the backdoor generates no anomalous process tree activity. Its HTTP.sys listener receives commands embedded in legitimate-looking HTTP request headers, producing minimal network-layer anomalies. The framework was found on Windows IIS servers in government and telecommunications networks across the Middle East, with Israeli organizations explicitly mentioned in Check Point's victimology.

Scarred Manticore's most strategically significant operational characteristic is its role as an initial access provider for Void Manticore (Handala). Check Point's May 2024 "Bad Karma No Justice" report documented a confirmed handoff pattern: Scarred Manticore establishes persistent access, then transfers that access to Void Manticore for destructive wiper deployment, data exfiltration, and public claim operations. This division of labor implies that Scarred Manticore detections on an Israeli government or critical infrastructure network should trigger not just an access investigation but a full destructive-operations response posture.

The group exploited CVE-2019-0604 (SharePoint) for initial access in documented campaigns, and has been linked to SharePoint, Exchange, and IIS exploitation as primary entry vectors. Its operational tempo aligns with MOIS tasking cycles, with campaigns observed over multiple years without major public disruption prior to the 2023 disclosure.

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

## Public Reports

**Own ecosystem:**

- [Actor Profile: Void Manticore / Handala](./handala.md) — Cross-reference for the downstream destructive actor that Scarred Manticore hands off access to.
- [Actor Profile: UNC1860](./unc1860.md) — Comparable MOIS-affiliated IIS-persistence and passive-access actor; compare Liontail family versus TEMPLEDOOR/TEMPLEPLAY toolsets and prioritize detection engineering across both clusters.

**MITRE ATT&CK:**

- [MITRE ATT&CK G1055 — Void Manticore](https://attack.mitre.org/groups/G1055/) — References Scarred Manticore collaboration and initial access role in the MOIS dual-actor model. Source ID `SRC-MITRE-G1055`.

**Primary vendor reporting:**

- Check Point Research, "Scarred Manticore versus MOIS: Seeing the Invisible" — October 2023. Primary public disclosure of the Liontail framework, IIS native module persistence, HTTP.sys listener technique, and government/telecom victimology in the Middle East. Source ID `SRC-CP-SCARRED-MANTICORE-2023`.
- Check Point Research, "Bad Karma No Justice: Void Manticore's Destructive Operations Against Israel" — May 2024. Documents the Scarred Manticore → Void Manticore handoff model with specific Israeli victim context. Source ID `SRC-CP-VOID-2024`.
- Check Point Research, "MOIS-Linked Actors and Criminal Ecosystem Convergence" — March 2026. Updated MOIS cluster mapping including Scarred Manticore's position in the broader ecosystem. Source ID `SRC-CP-MOIS-CRIME`.
