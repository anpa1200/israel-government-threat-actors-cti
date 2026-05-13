# OilRig

Aliases: APT34, Helix Kitten, Hazel Sandstorm, COBALT GYPSY, Crambus.

Assessed sponsor: Iran state-linked in public reporting.

## Relevance

OilRig is high priority for Israeli government exposure because public reporting describes long-running espionage campaigns against Middle Eastern government, critical infrastructure, technology, and telecom targets.

## Defensive Focus

- Webshell persistence on externally exposed systems.
- Credential theft and mailbox access.
- Custom downloader and command execution activity.
- Internal discovery using native commands.

## Detection Ideas

- `w3wp.exe` or web server worker processes spawning shells or scripting engines.
- Unexpected archive creation under web application directories.
- Authentication from unusual infrastructure after web exploitation.

Sources: `SRC-MITRE-G0049`, `SRC-ESET-OILRIG-ISRAEL`.
