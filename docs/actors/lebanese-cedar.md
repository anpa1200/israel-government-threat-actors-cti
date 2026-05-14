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
- Check Point Research original Volatile Cedar report (2015) — precursor reporting establishing the actor; not in sources.csv but available at https://www.checkpoint.com/downloads/volatile-cedar-technical-report.pdf.
