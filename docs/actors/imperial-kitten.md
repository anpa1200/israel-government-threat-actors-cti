---
title: Imperial Kitten
sidebar_label: Imperial Kitten
---

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Imperial Kitten](../navigation/actor-workbench.md#imperial-kitten)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1189](../navigation/ttp-detection-matrix.md#t1189) Drive-by Compromise (M2); [T1071.003](../navigation/ttp-detection-matrix.md#t1071003) Mail Protocols (M3); [T1059.005](../navigation/ttp-detection-matrix.md#t1059005) Visual Basic (M2)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: None currently mapped.
- Tool detail pages: [`IMAPLoader`](../tools/imaploader.md); [`StandardKeyboard`](../tools/standardkeyboard.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#imperial-kitten) (2 mapped tool row(s))
- Evidence records: `EVD-018` / `CLM-IMPERIALKITTEN-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CS-IMPERIAL-KITTEN-2023`, `SRC-PWC-YELLOW-LIDERC-2023`

<!-- ACTOR-NAVIGATION:END -->

# Imperial Kitten

## Background

Imperial Kitten (Tortoiseshell) was first publicly documented by Symantec in 2019, targeting IT companies serving the Saudi Aramco supply chain — an early indicator of the group's pattern of compromising trusted third parties to reach high-value ultimate targets. The IRGC attribution assessment is based on targeting patterns, operational tempo, and infrastructure overlap with IRGC-affiliated clusters; reviewed primary sources do not resolve the actor to IRGC-CEC or IRGC-IO specifically.

The group's defining technical characteristic is its use of strategic web compromise combined with IMAP-based command and control. IMAPLoader — documented by CrowdStrike in October 2023 — is a .NET downloader that retrieves tasking and delivers payloads via legitimate or compromised email accounts using IMAP. This technique makes C2 traffic difficult to distinguish from normal email connectivity, particularly in environments that permit direct IMAP access from servers and workstations. The complementary StandardKeyboard malware uses a similar mail-protocol C2 model, and CrowdStrike also documented use of a Discord API-based RAT in some campaigns.

A second distinctive technique is AppDomain Manager Injection — loading malicious managed-code assemblies into .NET processes via AppDomain manager configuration, enabling execution under the context of a legitimate application without direct DLL injection or process hollowing. This was documented in conjunction with XLL-based delivery chains targeting Israeli logistics and transportation websites in 2023.

For Israeli defenders, CrowdStrike's October 2023 report directly describes watering-hole and spearphishing campaigns against Israeli transportation, shipping, and logistics firms — sectors with direct public-sector dependencies through customs, ports, emergency services logistics, and supply chain operations. The group's combination of strategic web compromise (broad initial access) and targeted spearphishing suggests they are well-oriented to Israel's sector exposure.

Aliases: Imperial Kitten (CrowdStrike), Yellow Liderc (PwC), Tortoiseshell / Tortoise Shell (Symantec / Microsoft reporting), TA456 (Proofpoint), CURIUM / Crimson Sandstorm (Microsoft / MITRE ATT&CK).

Assessed sponsor: IRGC-aligned in public reporting. The current repository assessment does not resolve the actor to IRGC-CEC or IRGC-IO because reviewed primary public reporting does not support a branch-level sponsor call.

## Relevance

Imperial Kitten is high priority for Israeli government and public-sector defenders because public reporting describes targeting of Israeli or Israel-adjacent transportation, maritime, logistics, and technology environments. Those sectors intersect with ports, customs-adjacent suppliers, municipal logistics dependencies, emergency movement, and critical national supply-chain operations.

## Defensive Focus

- Strategic web compromise of Israeli or Israel-adjacent logistics and transportation websites.
- IMAP/IMAPS command and control from non-mail-client processes.
- Office/XLL delivery chains that lead to native C# compilation with `csc.exe`.
- AppDomain Manager Injection and unexpected managed-code execution under `AppVStreamingUX.exe`.
- Consumer or commodity mail-provider traffic from hosts that do not normally use IMAP.

## Associated Tooling

- **IMAPLoader**: .NET downloader/loader using IMAP-based tasking and payload retrieval through legitimate or compromised email accounts.
- **StandardKeyboard**: Reported in public vendor analysis as an email-C2 aligned implant; keep sample-specific details tied to the primary report used for the claim.
- Discord API-based RAT: Reported by CrowdStrike as asynchronous C2 over a legitimate messaging service.

## Detection Ideas

- Non-mail-client process establishes repeated outbound connections to TCP/143 or TCP/993, especially from servers, developer workstations, or `AppVStreamingUX.exe`.
- Office or Excel/XLL process spawns `csc.exe`, followed by execution of a newly compiled DLL or managed payload.
- Scheduled task or Run-key persistence appears with naming similar to media or streaming update components on a host that recently executed an Office/XLL chain.
- User visits an Israeli logistics or transportation site and then downloads/executes content that diverges from normal website behavior.
- DNS/proxy telemetry shows commodity mail or Discord API usage from non-browser/non-mail processes in sensitive logistics or public-sector networks.

## Analytic Caution

Current primary-source review supports strong 2022-2023 Israeli transportation/logistics relevance and preserves a gap for specific 2024-2025 Israeli incidents under this exact alias set. Do not represent 2024-2025 Israel-specific activity as confirmed without an added primary source.

## Repository Sources

- `SRC-CS-IMPERIAL-KITTEN-2023`: CrowdStrike Imperial Kitten reporting.
- `SRC-PWC-YELLOW-LIDERC-2023`: PwC Yellow Liderc / IMAPLoader reporting.
- `SRC-MITRE-G1012`: MITRE ATT&CK CURIUM / Crimson Sandstorm profile.

## Public Reports

**MITRE ATT&CK:**

- [MITRE ATT&CK G1012 — CURIUM](https://attack.mitre.org/groups/G1012/) — Technique mappings, software associations (IMAPLoader, StandardKeyboard), alias registry across CrowdStrike/PwC/Microsoft/Proofpoint naming conventions.

**Primary vendor reporting:**

- CrowdStrike Intelligence, "Imperial Kitten Deploys Novel Malware Families" — October 2023. Primary source for Israeli transportation/logistics targeting, IMAPLoader analysis, AppDomain Manager Injection, and XLL delivery chains. Source ID `SRC-CS-IMPERIAL-KITTEN-2023`.
- PwC Threat Intelligence, "Yellow Liderc: IMAPLoader and Strategic Web Compromises" — 2023. Complementary analysis of IMAPLoader and mail-protocol C2 tradecraft. Source ID `SRC-PWC-YELLOW-LIDERC-2023`.
- Symantec / Broadcom, "Tortoiseshell: New Iranian Threat Actor Targets IT Providers" — 2019. Original disclosure documenting supply chain compromise targeting Saudi Aramco IT vendors.
- Proofpoint, TA456 reporting — Social engineering and persona-based campaigns attributed to the Imperial Kitten cluster (note vendor taxonomy before cross-referencing).
