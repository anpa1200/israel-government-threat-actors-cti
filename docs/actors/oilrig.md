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
- Tool detail pages: [`OilBooster`](../tools/oilbooster.md); [`Saitama`](../tools/saitama.md); [`BONDUPDATER`](../tools/bondupdater.md); [`certutil`](../tools/certutil.md); [`ftp`](../tools/ftp.md); [`Helminth`](../tools/helminth.md); [`ipconfig`](../tools/ipconfig.md); [`ISMInjector`](../tools/isminjector.md); [`LaZagne`](../tools/lazagne.md); [`Mango`](../tools/mango.md); [`Mimikatz`](../tools/mimikatz.md); [`Net`](../tools/net.md); [`netstat`](../tools/netstat.md); [`ngrok`](../tools/ngrok.md); [`ODAgent`](../tools/odagent.md); [`OilCheck`](../tools/oilcheck.md); [`OopsIE`](../tools/oopsie.md); [`PowerExchange`](../tools/powerexchange.md); [`POWRUNER`](../tools/powruner.md); [`PsExec`](../tools/psexec.md); [`QUADAGENT`](../tools/quadagent.md); [`RDAT`](../tools/rdat.md); [`Reg`](../tools/reg.md); [`RGDoor`](../tools/rgdoor.md); [`SampleCheck5000`](../tools/samplecheck5000.md); [`SEASHARPEE`](../tools/seasharpee.md); [`SideTwist`](../tools/sidetwist.md); [`Solar`](../tools/solar.md); [`Systeminfo`](../tools/systeminfo.md); [`Tasklist`](../tools/tasklist.md); [`ZeroCleare`](../tools/zerocleare.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#oilrig) (31 mapped tool row(s))
- Evidence records: `EVD-013` / `CLM-OILRIG-001`; `EVD-014` / `CLM-OILRIG-002`
- Imported research intakes: [OilRig And Magic Hound Deep Research Intake](../reports/oilrig-magic-hound-deep-research.md) (High, Needs source validation); [APT35 And OilRig Israel Deep Research Intake](../reports/apt35-oilrig-israel-deep-research.md) (High, Needs source validation)
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
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
