# Israel Government Threat Actors CTI

[![Validate CTI Repository](https://github.com/anpa1200/israel-government-threat-actors-cti/actions/workflows/validate.yml/badge.svg)](https://github.com/anpa1200/israel-government-threat-actors-cti/actions/workflows/validate.yml)

Defensive cyber threat intelligence repository focused on public-source reporting about threat actors, personas, malware families, TTPs, and detection opportunities relevant to Israeli government, public-sector, municipal, critical infrastructure, and adjacent suppliers.

This repository is intentionally blue-team only. It contains source references, analytic summaries, ATT&CK mappings, IOC reference locations, and detection examples. It does not store malware binaries, leaked data, credentials, exploit code, or instructions for unauthorized access.

## Scope

- Iranian state-sponsored and state-aligned actors with reported Israel targeting.
- Palestinian, Lebanese, and regional activity clusters assessed as relevant to Israeli government exposure.
- Hacktivist and influence-operation personas where public reporting ties activity to Israeli entities or Israeli-made infrastructure.
- Defensive detections for common tradecraft: phishing, RMM abuse, PowerShell execution, webshell post-exploitation, identity abuse, OT exposure, and destructive/wiper preparation.

## Repository Map

| Path | Purpose |
| --- | --- |
| `docs/actors/` | Actor and persona profiles with aliases, relevance, TTPs, and source notes. |
| `docs/navigation/` | Generated actor and surface cross-reference pages for analyst navigation. |
| `docs/reports/` | Report index and source collection guidance. |
| `docs/reports/andrey-medium-articles.md` | Relevant Medium articles from `@1200km` included as authored CTI or methodology references. |
| `docs/reports/2026-israel-critical-infrastructure-escalation.md` | Research intake report on Israeli critical infrastructure and geopolitical escalation. |
| `docs/reports/defensive-cti-threats-to-israeli-public-sector.md` | Defensive CTI synthesis focused on Israeli government and public-sector environments. |
| `docs/reports/worked-cases.md` | End-to-end CTI-to-detection worked cases for MuddyWater, Scarred Manticore/UNC1860 to Void Manticore, and CyberAv3ngers OT exposure. |
| `docs/reports/ci-validation-evidence.md` | Public GitHub Actions validation and Pages build evidence. |
| `docs/reports/release-notes.md` | Versioned release notes and maturity changes. |
| `docs/methodology/` | CTI-to-detection operating standard, scoring models, and artifact contracts. |
| `docs/threat-hunting/` | Threat-hunting workflow and hypothesis rules. |
| `docs/detection-engineering/` | Detection lifecycle, DRL, quality gates, and production criteria. |
| `docs/known-limitations.md` | Top-level limitations and non-production caveats. |
| `docs/customer-environment-use.md` | How to use the project in a customer/SOC environment without overclaiming production readiness. |
| `docs/connected-tips.md` | Connected CTI/TIP feed descriptions, commands, optional secrets, and promotion workflow. |
| `docs/intelligence-updates.md` | Generated CTI feed update queue from no-key public sources. |
| `examples/registers/` | PIR, SIR, evidence, persona-claim, scenario, hunt, detection, health, and metrics register templates. |
| `examples/gates/` | Sample quality-gate evidence packs. |
| `examples/drl-evidence-packs/` | Detection-specific DRL evidence packs. |
| `examples/detection-test-results/` | Committed lab/synthetic detection test evidence where available. |
| `examples/replay-datasets/` | Small synthetic replay datasets for parser and rule-behavior checks. |
| `data/actors.csv` | Structured actor register. |
| `data/sources.csv` | Source register with reliability, publication/access/review dates, and archive hashes where available. |
| `data/research-downloads.csv` | Download manifest for local source archive, including status, local path, size, and SHA-256. |
| `data/intel-feeds.csv` | Public/free CTI feed definitions and optional connector targets. |
| `data/intel-update-candidates.csv` | Analyst review queue generated from CTI feeds. |
| `data/ttps.csv` | Actor-to-ATT&CK mapping table. |
| `data/ioc-references.csv` | Pointers to public IOC locations. |
| `data/malware-references.csv` | Malware/tool reference table without binaries. |
| `sources/` | Scored source library separated into Score A primary, Score B supporting, and Score C watchlist material. |
| `detections/sigma/` | Defensive Sigma examples and hunting rules. |
| `detections/kql/` | Microsoft Sentinel / Defender hunting examples. |
| `detections/splunk/` | Sigma-generated Splunk SPL conversion artifacts for review. |
| `detections/elastic/` | Sigma-generated Elastic Lucene conversion artifacts for review. |
| `scripts/validate_repo.py` | Local validation for CSV and Sigma hygiene. |
| `scripts/build_research_manifest.py` | Builds the committed source-download manifest from ignored local downloads. |
| `scripts/convert_research_downloads.py` | Converts ignored local HTML/PDF downloads into searchable analyst text. |
| `scripts/fetch_intel_updates.py` | Fetches no-key public CTI feeds and writes an analyst update queue. |

## Quick Start

```bash
python3 scripts/validate_repo.py
```

Review the starting threat model in [docs/israel-government-threat-model.md](docs/israel-government-threat-model.md), then work through [docs/actors/README.md](docs/actors/README.md).

For practical click-through use, start with the [Actor Navigation Workbench](docs/navigation/actor-workbench.md), [TTP To Detection Matrix](docs/navigation/ttp-detection-matrix.md), or [Surface And Capability Matrix](docs/navigation/surface-capability-matrix.md).

For CTI feed updates, start with [Connected TIPs And CTI Feeds](docs/connected-tips.md).

For source triage, start with [sources/README.md](sources/README.md).

To pull current public CTI update candidates:

```bash
npm run intel:update
```

This updates [docs/intelligence-updates.md](docs/intelligence-updates.md) and [data/intel-update-candidates.csv](data/intel-update-candidates.csv). Feed items are review leads only; promote them through source/evidence records before changing actor or detection content.

For threat hunting and CTI-based detection engineering, start with [docs/methodology/operating-standard.md](docs/methodology/operating-standard.md).

For end-to-end examples and proof artifacts, review:

- [Worked cases](docs/reports/worked-cases.md)
- [DRL evidence packs](docs/detection-engineering/drl-evidence-packs.md)
- [CI validation evidence](docs/reports/ci-validation-evidence.md)
- [Release notes](docs/reports/release-notes.md)
- [Known limitations](docs/known-limitations.md)
- [Customer environment use](docs/customer-environment-use.md)
- [Connected TIPs and CTI feeds](docs/connected-tips.md)
- [Intelligence update queue](docs/intelligence-updates.md)
- [Detection status dashboard](docs/detection-engineering/detection-status-dashboard.md)
- [Actor navigation workbench](docs/navigation/actor-workbench.md)
- [TTP to detection matrix](docs/navigation/ttp-detection-matrix.md)
- [Surface and capability matrix](docs/navigation/surface-capability-matrix.md)
- [Replay datasets](docs/detection-engineering/replay-datasets.md)

## Core Sources

This project starts from public reporting by MITRE ATT&CK, CISA, Microsoft Threat Intelligence, Mandiant / Google Cloud, ESET, SentinelOne, Meta, Check Point Research, and other reputable CTI publishers. Source records are maintained in [data/sources.csv](data/sources.csv).

Key starting references include:

- MITRE ATT&CK: [MuddyWater G0069](https://attack.mitre.org/groups/G0069/), [OilRig G0049](https://attack.mitre.org/groups/G0049/), [Magic Hound / APT35 G0059](https://attack.mitre.org/groups/G0059/), [APT42 G1044](https://attack.mitre.org/groups/G1044/), [Agrius G1030](https://attack.mitre.org/groups/G1030/), [APT-C-23 / Arid Viper G1028](https://attack.mitre.org/groups/G1028/)
- CISA: [AA23-335A IRGC-affiliated CyberAv3ngers Unitronics PLC activity](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- Microsoft: [Iran surges cyber-enabled influence operations in support of Hamas](https://www.microsoft.com/en-gb/security/security-insider/intelligence-reports/iran-surges-cyber-enabled-influence-operations-in-support-of-hamas/)
- Mandiant / Google Cloud: [UNC3890: Iranian actor targeting Israeli shipping and other sectors](https://www.securityweek.com/iranian-group-targeting-israeli-shipping-and-other-key-sectors/) and [APT42: Crooked Charms, Cons, and Compromises](https://cloud.google.com/blog/topics/threat-intelligence/apt42-charms-cons-compromises/)
- Andrey Pautov Medium research: [Handala](https://medium.com/@1200km/cti-research-handala-hack-group-aka-handala-hack-team-ddbdd294cfb8), [MuddyWater](https://medium.com/@1200km/cti-research-muddywater-seedworm-mango-sandstorm-ebf6af5ba061), and [Israeli telecom CTI-led defensive strategy](https://medium.com/@1200km/cti-led-defensive-strategy-for-a-fictional-cellular-provider-case-study-c77bc5765b31)

## Handling Rules

- Treat all content as `TLP:CLEAR` unless a future private branch explicitly states otherwise.
- Do not commit malware samples, password dumps, private victim data, or access tokens.
- Prefer links to vendor IOC appendices over copying large IOC lists that will become stale.
- Mark confidence and source reliability separately.
- Use normative language where the repository defines a control or process: `MUST`, `SHOULD`, `MAY`, `REQUIRED`, `OPTIONAL`.

## Version

Current version: `v1.1`
