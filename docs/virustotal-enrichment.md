---
title: VirusTotal Malware Enrichment
sidebar_label: VirusTotal Enrichment
---

# VirusTotal Malware Enrichment

VirusTotal is connected as an optional enrichment source for reviewed malware and
tool hashes. It is not a primary attribution source and it is not used to fetch
or store malware samples.

## Connector Contract

| Item | Value |
| --- | --- |
| Feed ID | `FEED-VIRUSTOTAL-OPTIONAL` |
| Required secret | `VT_API_KEY` |
| Seed file | `data/virustotal-hash-seeds.csv` |
| Reviewed output | `data/virustotal-enrichment-candidates.csv` |
| Local command | `VT_API_KEY=... npm run intel:vt` |

## Promotion Rules

1. Add hashes only when they come from a primary public report or a clearly
   labelled research-intake seed.
2. Keep source context in `data/virustotal-hash-seeds.csv`.
3. Use VirusTotal to add public metadata such as file type, names, tags, and
   aggregate verdict counts.
4. Do not promote a VT label into actor attribution.
5. Do not treat `not_found` as benign.
6. Do not commit raw VT JSON, private telemetry, downloaded files, API keys, or
   sandbox artifacts.

## Current Reviewed Enrichment

| Tool | Actor | Hash | VT Status | Defensive Use |
| --- | --- | --- | --- | --- |
| [TEMPLEPLAY](tools/templeplay.md) | [UNC1860](actors/unc1860.md) | `c517519097bff386dc1784d98ad93f9d` | `not_found` | Keep Mandiant-published MD5 as source-backed IOC context; absence in VT does not reduce confidence. |
| [TEMPLEDOOR](tools/templedoor.md) | [UNC1860](actors/unc1860.md) | `c57e59314aee7422e626520e495effe0` | `not_found` | Keep Mandiant-published MD5 as source-backed IOC context; absence in VT does not reduce confidence. |
| [TEMPLEDOOR](tools/templedoor.md) | [UNC1860](actors/unc1860.md) | `b219672bcd60ce9a81b900217b3b5864` | `found` | VT metadata supports enrichment and triage, but Mandiant remains the source for UNC1860 association. |
| [TEMPLEDROP](tools/templedrop.md) | [UNC1860](actors/unc1860.md) | `0c93cac9854831da5f761ee98bb40c37` | `found` | Treat as a repurposed legitimate-driver reference in Mandiant TEMPLEDROP analysis; do not block solely from VT metadata. |
| [IOControl](tools/iocontrol.md) | [CyberAv3ngers](actors/cyberav3ngers.md) | `1b39f9b2b96a6586c4a11ab2fdbff8fdf16ba5a0ac7603149023d73f33b84498` | `found` | Use as historical enrichment for Claroty-published IOCONTROL sample; prioritize MQTT, DoH, router, and OT/IoT behavior. |
| [OilBooster](tools/oilbooster.md) | [OilRig](actors/oilrig.md) | `1B2FEDD5F2A37A0152231AE4099A13C8D4B73C9E` | `not_found` | Research-intake seed only; do not promote to blocking IOC until primary hash source is verified. |
| [OilCheck](tools/oilcheck.md) | [OilRig](actors/oilrig.md) | `8D84D32DF5768B0D4D2AB8B1327C43F17F182001` | `not_found` | Research-intake seed only; do not promote to blocking IOC until primary hash source is verified. |
| [ODAgent](tools/odagent.md) | [OilRig](actors/oilrig.md) | `7E498B3366F54E936CB0AF767BFC3D1F92D80687` | `not_found` | Research-intake seed only; do not promote to blocking IOC until primary hash source is verified. |

## Analyst Workflow

Start with the [Malicious Tools](tools/README.md) index or an actor page, pivot to
the relevant tool page, then use the hash seed and enrichment CSVs for IOC-level
triage. If a hash is useful for detection, add it as a low-priority historical
indicator and pair it with behavioral hunts from the tool page. Hash-only alerting
should remain an exception.
