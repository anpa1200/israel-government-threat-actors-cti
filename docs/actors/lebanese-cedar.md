# Lebanese Cedar

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
