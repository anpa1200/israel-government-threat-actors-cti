---
description: "Lebanese Cedar (Volatile Cedar) is a Hezbollah-affiliated espionage group with multi-year persistent access to telecom, defense, media, and education organizations in the Middle East and Europe."
---

# Lebanese Cedar

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Lebanese Cedar](../navigation/actor-workbench.md#lebanese-cedar)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Internet-Facing Servers, Webshells, And Passive Access](../navigation/surface-capability-matrix.md#edge-webshell)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1190](../navigation/ttp-detection-matrix.md#t1190) Exploit Public-Facing Application (M2); [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell (M2)
- Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access (Hunt, DRL-4)
- Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access
- IOC reference sources: `SRC-CLEARSKY-LEBANESE-CEDAR` Webshell paths; malware references; vulnerable products
- Tool detail pages: [`Explosive RAT`](../tools/explosive-rat.md); [`Caterpillar WebShell`](../tools/caterpillar-webshell.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#lebanese-cedar) (2 mapped tool row(s))
- Evidence records: `EVD-012` / `CLM-LEBANESECEDAR-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CLEARSKY-LEBANESE-CEDAR`

<!-- ACTOR-NAVIGATION:END -->

## Background

Lebanese Cedar (Volatile Cedar) is a Hezbollah-affiliated cyber espionage group active since approximately 2012. Check Point's 2015 "Volatile Cedar" report was the first major public disclosure, documenting multi-year persistent access to telecommunications companies, defense contractors, media organizations, and educational institutions primarily in the Middle East, Europe, and North America. The group's alignment with Hezbollah places it in a distinct threat category from Iran's IRGC or MOIS actors — Hezbollah is an Iranian-backed Lebanese proxy with its own strategic intelligence mandate covering Israeli military, diplomatic, and logistical intelligence collection.

The group's technical signature is web-based initial access followed by long-lived passive persistence. Distinctive tools include Explosive RAT — a custom remote access trojan — and the Caterpillar WebShell, a JSP-based web shell that functions as a file browser and command execution interface. ClearSky's January 2021 report documented a campaign wave exploiting CVE-2019-3396 (Atlassian Confluence) and CVE-2019-2725 (Oracle WebLogic) against hosting providers, ISPs, and telecommunications companies in Israel, the United States, Egypt, Jordan, Saudi Arabia, and the United Kingdom.

The 2021 campaign's targeting of hosting providers and ISPs is strategically significant: compromise of these organizations enables passive access to communications, DNS records, hosting customer data, and potentially upstream network positions from which secondary targets can be identified or accessed. For Israeli government and public-sector defenders, any supplier dependency on hosting providers or ISPs with Lebanese Cedar exposure is a potential lateral access risk.

Lebanese Cedar is typically characterized by patient, low-noise operations oriented toward intelligence collection rather than destructive impact. Long-dwell access is a consistent pattern — the 2021 ClearSky report noted some implants had persisted undetected for extended periods across the targeted organizations.

Aliases: Volatile Cedar.

Assessed sponsor: Lebanon-linked / Hezbollah-linked in public reporting.

## Relevance

Lebanese Cedar is relevant as a regional espionage threat with public reporting around web compromise and telecom or hosting interest. Israel-government relevance is medium and depends on exposed web infrastructure, suppliers, and regional operations.

## Defensive Focus

- Webshell detection.
- Public-facing server patching.
- Hosting-provider visibility.
- Long-lived persistence on Linux and web servers.

## Detection Ideas

- Unexpected web server process spawning shell commands.
- New PHP/ASP files under upload directories.
- Long-lived outbound connections from web servers.
- Exploitation of unpatched Confluence (CVE-2019-3396) or Oracle WebLogic (CVE-2019-2725) for initial access.
- Caterpillar WebShell (JSP file browser) artefacts under web roots.

## Repository Sources

- `SRC-CLEARSKY-LEBANESE-CEDAR`: ClearSky primary research — Volatile Cedar / Lebanese Cedar, covering Explosive RAT, Caterpillar WebShell, and compromised web servers (January 2021).
- `SRC-CP-VOLATILE-CEDAR-2015`: Check Point Volatile Cedar technical report retrieved from a public Kaspersky-hosted mirror after the original Check Point PDF URL returned 404.
- `SRC-ISRAELHAYOM-ZIV-2023` and `SRC-TOI-ZIV-2023`: secondary coverage of Israeli government statements about the Ziv Hospital incident. Use as context only until a primary government technical report is available.

## Public Reports

**Primary vendor reporting:**

- ClearSky Cyber Security, "Lebanese Cedar APT: Sophisticated Persistent Actors Targeting Global Telecom and Hosting" — January 2021. Primary source for 2021 campaign wave including Confluence and WebLogic exploitation, Caterpillar WebShell deployment, and victim list spanning ISPs and hosting providers. Source ID `SRC-CLEARSKY-LEBANESE-CEDAR`.
- Check Point Research, "Volatile Cedar" — 2015. Original public disclosure of the group's Explosive RAT campaigns and long-running telecom espionage operations. Source ID `SRC-CP-VOLATILE-CEDAR-2015`.
- Recorded Future and other vendors have tracked Lebanese Cedar activity under various designations; cross-reference vendor-specific naming with the ClearSky/Check Point reporting for consistent attribution baseline.
