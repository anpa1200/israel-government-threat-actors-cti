---
description: "OilRig (APT34) is one of Iran's most prolific espionage groups, active since 2014 targeting Middle Eastern government, energy, telecom, and financial sectors with custom backdoors and cloud-service C2."
head:
  - tag: script
    attributes:
      type: application/ld+json
    innerHTML: '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is OilRig (APT34)?","acceptedAnswer":{"@type":"Answer","text":"OilRig (APT34) is one of Iran's most prolific and longest-running cyber espionage groups, active since approximately 2014. The group targets Middle Eastern government, energy, telecom, and financial organizations. Also known as Helix Kitten, Hazel Sandstorm, and Crambus. Attributed to Iranian state-linked infrastructure across MITRE ATT&CK (G0049), Unit 42, ESET, Symantec, and Mandiant reporting."}},{"@type":"Question","name":"How to detect OilRig activity?","acceptedAnswer":{"@type":"Answer","text":"Key OilRig detection approaches: monitor IIS worker processes (w3wp.exe) spawning cmd.exe or PowerShell (webshell execution indicator); detect unexpected file creation under web application directories; watch for DNS queries with high-entropy subdomains in high volume (Saitama DNS tunneling C2); monitor Microsoft Graph API calls from non-browser processes (OilBooster cloud C2 via OneDrive); look for SEASHARPEE or RGDoor webshell artifacts in IIS access and error logs."}},{"@type":"Question","name":"What tools does OilRig use?","acceptedAnswer":{"@type":"Answer","text":"OilRig's tool portfolio includes: POWRUNER and BONDUPDATER (PowerShell backdoors); OopsIE and QUADAGENT (C#-based implants); Saitama (.NET backdoor with DNS tunneling C2); OilBooster (Microsoft Graph API / OneDrive C2); SEASHARPEE and RGDoor (IIS webshells for persistent access); ODAgent, OilCheck, SampleCheck5000, PowerExchange (additional custom tools); LaZagne, Mimikatz, and Mango for credential harvesting. The group actively develops and maintains custom tooling over multi-year periods."}}]}'
---

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

## Background

OilRig (APT34) is one of Iran's most operationally prolific cyber espionage groups, active since approximately 2014. The group's primary mandate is long-duration espionage against government, energy, financial services, telecommunications, and technology organizations in the Middle East and beyond. Iran-nexus attribution is consistent across MITRE, Unit 42, ESET, Symantec, and Mandiant; specific organizational attribution within the Iranian intelligence apparatus varies by source, with MOIS being the most commonly assessed sponsor in synthesis reporting.

OilRig's tradecraft is distinctive for its heavy investment in custom tooling — the group has an extensive portfolio of backdoors, downloaders, and credential harvesting utilities developed over a decade. Key tool families include POWRUNER and BONDUPDATER (PowerShell-based), OopsIE and QUADAGENT (C#-based), Saitama (DNS-abusing .NET backdoor), and OilBooster (cloud-service C2 using OneDrive and Microsoft Graph API). A recurring fingerprint is the use of DNS tunneling and cloud-service communications for C2, enabling the actor to blend into legitimate organizational traffic.

Initial access methods center on exploitation of internet-facing servers — particularly web applications, Exchange, and IIS — with subsequent webshell implantation (SEASHARPEE, RGDoor) as a persistent fallhold. The group uses credential harvesting tools (Mimikatz, LaZagne) and native Windows binaries for lateral movement, and has demonstrated the ability to maintain access across large enterprise environments for months to years.

In an Israeli and regional government context, ESET's reporting on OilRig's OilBooster campaign and Unit 42's DNS tunneling analysis are the primary anchors. The repository's deep research intakes synthesize claims from ESET, Kaspersky ICS, and Brandefense; analysts should apply the source rating before using synthesis claims in executive reporting.

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

## Public Reports

**Own ecosystem:**

- [Deep Research Intake: OilRig and Magic Hound](../reports/oilrig-magic-hound-deep-research.md) — Internal repository synthesis. High-priority, requires source validation.
- [Deep Research Intake: APT35 and OilRig Israel](../reports/apt35-oilrig-israel-deep-research.md) — Internal repository synthesis covering Israel-specific reporting. High-priority, requires source validation.

**MITRE ATT&CK:**

- [MITRE ATT&CK G0049 — OilRig](https://attack.mitre.org/groups/G0049/) — Technique mappings, software associations, and alias registry. Primary reference for cross-vendor technique mapping.

**Primary vendor reporting:**

- ESET Research, "OilRig's Persistent Footholds on Israeli Organizations Using OilBooster" — 2023. Primary source for cloud-service C2 via Microsoft Graph API, targeting of Israeli organizations. Source ID `SRC-ESET-OILRIG-ISRAEL`.
- Unit 42 / Palo Alto Networks, "OilRig Targets Middle Eastern Telecommunications Organization" — DNS tunneling C2 via custom subdomain patterns. Source ID `SRC-UNIT42-OILRIG-DNS-TUNNELING`.
- Symantec / Broadcom, Crambus (APT34) reporting — Coverage of PowerShell tooling evolution and Middle East government targeting.
- Mandiant, APT34 group profile — Historical coverage of initial OilRig campaigns and toolset documentation.

## Related Actors

- [Lyceum / HEXANE](./lyceum.md) — Assessed as a subgroup or parallel cluster within the broader OilRig/APT34 ecosystem; shares targeting of Middle Eastern telecommunications and energy organizations and overlapping C2 infrastructure patterns.
- [APT35 / Magic Hound](./apt35.md) — Parallel IRGC-attributed cluster with overlapping vendor naming (Crambus alias occasionally conflated); compare targeting and toolset divergence.
