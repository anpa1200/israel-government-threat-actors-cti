---
title: Imperial Kitten
sidebar_label: Imperial Kitten
---

# Imperial Kitten

Aliases: Imperial Kitten (CrowdStrike), Yellow Liderc (PwC), Tortoiseshell / Tortoise Shell (Symantec / Microsoft reporting), TA456 (Proofpoint), CURIUM / Crimson Sandstorm (Microsoft / MITRE ATT&CK).

Assessed sponsor: IRGC-aligned in public reporting. The current repository assessment does not resolve the actor to IRGC-CEC or IRGC-IO because the imported research did not identify primary public evidence precise enough for that branch-level sponsor call.

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
- **StandardKeyboard**: Reported by the imported research as an email-C2 aligned implant.
- Discord API-based RAT: Reported by CrowdStrike/imported research as asynchronous C2 over a legitimate messaging service.

## Detection Ideas

- Non-mail-client process establishes repeated outbound connections to TCP/143 or TCP/993, especially from servers, developer workstations, or `AppVStreamingUX.exe`.
- Office or Excel/XLL process spawns `csc.exe`, followed by execution of a newly compiled DLL or managed payload.
- Scheduled task or Run-key persistence appears with naming similar to media or streaming update components on a host that recently executed an Office/XLL chain.
- User visits an Israeli logistics or transportation site and then downloads/executes content that diverges from normal website behavior.
- DNS/proxy telemetry shows commodity mail or Discord API usage from non-browser/non-mail processes in sensitive logistics or public-sector networks.

## Analytic Caution

The two imported research notes agree on a strong 2022-2023 Israeli transportation/logistics relevance. They also preserve a gap for specific 2024-2025 Israeli incidents under this exact alias set. Do not represent 2024-2025 Israel-specific activity as confirmed without an added primary source.

## Repository Sources

- `SRC-CS-IMPERIAL-KITTEN-2023`: CrowdStrike Imperial Kitten reporting.
- `SRC-PWC-YELLOW-LIDERC-2023`: PwC Yellow Liderc / IMAPLoader reporting.
- `SRC-MITRE-G1012`: MITRE ATT&CK CURIUM / Crimson Sandstorm profile.
