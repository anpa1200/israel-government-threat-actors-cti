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
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CLEARSKY-LEBANESE-CEDAR`

<!-- ACTOR-NAVIGATION:END -->

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
