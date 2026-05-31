# CTI Project Ecosystem

## Purpose

This page connects the Israel Government Threat Actors CTI knowledge base to the broader CTI documentation ecosystem.

## The Ecosystem

| Project | Role | Use When You Need |
| --- | --- | --- |
| [CTI Analyst Field Manual](https://anpa1200.github.io/cti-analyst-field-manual/) | General CTI tradecraft and analyst operating manual | Evidence labels, source reliability, attribution discipline, infrastructure pivoting, actor research, CTI-to-detection method |
| [CTI as a Code](https://anpa1200.github.io/CTI_as_a_Code/) | Lab platform and training framework | Applying this sector intelligence in hands-on exercises — the A05–A08 NDSA assignments are directly grounded in the Israeli government threat model documented here |
| [Operation Desert Hydra](https://anpa1200.github.io/operation-desert-hydra/) | Complete CTI-to-detection pipeline on MuddyWater | Worked detection pipeline for an actor tracked in this knowledge base — source gathering to lab-validated Kibana rules |
| [Customer-Driven AI CTI Project](https://anpa1200.github.io/customer-driven-ai-cti-project/) | Delivery methodology and customer engagement operating model | Quality gates, project phases, acceptance criteria, detection readiness, replay and reporting workflow |
| [Israel Government Threat Actors CTI](https://anpa1200.github.io/israel-government-threat-actors-cti/) | Sector and actor knowledge base | Israeli public-sector threat model, actors, tools, TTPs, detections, hunts, source tracking, and evidence mapping |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | AI-powered offensive security automation platform | MCP agent-based tool orchestration, 150+ security tools, AI-driven penetration testing, adversarial validation of detection coverage |

## How This Project Fits

This project is the sector and actor knowledge base. It provides practical CTI material for Israeli government, municipal, telecom, critical infrastructure, defense-adjacent, and supplier exposure.

Use the [CTI Analyst Field Manual](https://anpa1200.github.io/cti-analyst-field-manual/) to understand the tradecraft behind evidence labels, attribution, ATT&CK mapping, and CTI-to-detection logic. Use the [Customer-Driven AI CTI Project](https://anpa1200.github.io/customer-driven-ai-cti-project/) when this knowledge base must become a structured customer delivery or internal program.

## Cross-Project Workflows

### Actor Page to Tradecraft Guidance

Start with an actor page such as [MuddyWater](actors/muddywater.md), [Void Manticore / Handala](actors/handala.md), or [OilRig](actors/oilrig.md). Use the Field Manual to review actor profiling, attribution, evidence labels, and confidence language.

### TTP to Detection Delivery

Start with the [TTP To Detection Matrix](navigation/ttp-detection-matrix.md), then use the Field Manual's CTI-to-detection guidance and the Customer project quality gates before production use.

### Sector Finding to Customer-Ready Output

Start with the [Israel Government Threat Model](israel-government-threat-model.md), then use the Customer project to convert findings into PIRs, SIRs, detection backlog items, SOC handoff, and executive reporting.

## Repository Links

- [CTI Analyst Field Manual repository](https://github.com/anpa1200/cti-analyst-field-manual)
- [CTI as a Code repository](https://github.com/anpa1200/CTI_as_a_Code)
- [Operation Desert Hydra repository](https://github.com/anpa1200/operation-desert-hydra)
- [Customer-Driven AI CTI Project repository](https://github.com/anpa1200/customer-driven-ai-cti-project)
- [Israel Government Threat Actors CTI repository](https://github.com/anpa1200/israel-government-threat-actors-cti)
- [HexStrike AI repository](https://github.com/0x4m4/hexstrike-ai)

## Boundary

The CTI documentation projects (Field Manual, Customer project, Israel CTI) are defensive and public-source oriented. They do not include malware source code, exploit instructions, leaked data, credentials, or unauthorized-access guidance. HexStrike AI is an authorized offensive security and penetration testing platform; use it only in authorized engagements.
