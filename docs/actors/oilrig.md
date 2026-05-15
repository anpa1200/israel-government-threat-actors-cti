# OilRig

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [OilRig](../navigation/actor-workbench.md#oilrig)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Internet-Facing Servers, Webshells, And Passive Access](../navigation/surface-capability-matrix.md#edge-webshell); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1505.003](../navigation/ttp-detection-matrix.md#t1505003) Web Shell (M3); [T1049](../navigation/ttp-detection-matrix.md#t1049) System Network Connections Discovery (M1)
- Mapped detections: None currently mapped.
- Mapped hunts: None currently mapped.
- IOC reference sources: `SRC-MITRE-G0049` Technique references
- Malware and tools: `OilBooster` (Downloader); `Saitama` (DNS-tunneling backdoor)
- Evidence records: `EVD-013` / `CLM-OILRIG-001`; `EVD-014` / `CLM-OILRIG-002`
- Source IDs in structured data: `SRC-ESET-OILRIG-ISRAEL`, `SRC-MITRE-G0049`, `SRC-UNIT42-OILRIG-DNS-TUNNELING`

<!-- ACTOR-NAVIGATION:END -->

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

Sources: `SRC-MITRE-G0049`, `SRC-ESET-OILRIG-ISRAEL`, `SRC-UNIT42-OILRIG-DNS-TUNNELING`, `SRC-KASPERSKY-ICS-H2-2023`, `SRC-BRANDEFENSE-OILRIG-2025`.

Source note: ESET and Unit 42 are the preferred anchors for OilBooster/cloud-service and DNS-tunneling claims. Kaspersky ICS and Brandefense are supporting synthesis sources.
