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

