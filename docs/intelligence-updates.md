---
title: Intelligence Update Queue
sidebar_label: Intel Updates
---

# Intelligence Update Queue

This page summarizes the latest no-key public CTI feed pull. It is a review queue, not an automatic source of truth.

Feed candidates must be reviewed before they are promoted into `data/sources.csv`, actor profiles, evidence records, TTP mappings, hunts, or detections.

Generated: `2026-05-15`

## Connected Feeds

- MITRE ATT&CK Enterprise STIX: actor taxonomy and modified-date drift checks.
- CISA Known Exploited Vulnerabilities: exposure-prioritization leads.
- CISA Cybersecurity Advisories RSS: new government advisory leads.
- Optional: OTX subscribed pulses when `OTX_API_KEY` is configured.
- Optional: MISP and OpenCTI connector targets when trusted instance secrets are configured.

## Summary

| Metric | Value |
| --- | ---: |
| Total candidates | 32 |
| `FEED-CISA-ADVISORIES` candidates | 13 |
| `FEED-CISA-KEV` candidates | 1 |
| `FEED-MISP-OPTIONAL` candidates | 1 |
| `FEED-MITRE-ATTACK-ENTERPRISE` candidates | 15 |
| `FEED-OPENCTI-OPTIONAL` candidates | 1 |
| `FEED-OTX-OPTIONAL` candidates | 1 |
| `Needs analyst review` | 28 |
| `Needs exposure review` | 1 |
| `Not configured` | 3 |

## Candidate Review Rules

- Treat feed items as collection leads until a human analyst reviews source relevance.
- Do not create actor attribution from KEV or surface matches alone.
- Use CISA KEV matches for exposure review and asset-owner routing first.
- Use MITRE matches to check alias, description, and technique drift.
- Add a normal source/evidence record before changing an actor page or detection mapping.

## Current Candidates

| Candidate | Feed | Actor | Type | Title | Date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `UPD-CISA-ADV-SURFACE-55b87a3084` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [ABB AC500 V3 Multiple Vulnerabilities](https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-03) | Tue, 12 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-9ca9b26be0` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [ABB AC500 V3 Stack Buffer Overflow in Cryptographic Message Syntax](https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-05) | Tue, 12 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-43e003f77f` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [ABB Automation Builder Gateway for Windows](https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-04) | Tue, 12 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-ea26b4b278` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [ABB WebPro SNMP Card PowerValue Multiple Vulnerabilities](https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-06) | Tue, 12 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-8f5dc67818` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/05/15/cisa-adds-one-known-exploited-vulnerability-catalog) | Fri, 15 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-acf8a28800` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/05/07/cisa-adds-one-known-exploited-vulnerability-catalog) | Thu, 07 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-c2651eadf6` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/05/06/cisa-adds-one-known-exploited-vulnerability-catalog) | Wed, 06 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-51f61e1dc4` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens Ruggedcom Rox](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-12) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-2fb9ad63bb` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens Ruggedcom Rox](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-11) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-c2c9316d00` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens Ruggedcom Rox](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-02) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-5bb347d672` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens SIMATIC](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-10) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-5860784a6e` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens SIMATIC](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-07) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-CISA-ADV-SURFACE-ff7824dc56` | `FEED-CISA-ADVISORIES` | Surface | Government advisory | [Siemens SIMATIC S7 PLC Web Server](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-15) | Thu, 14 May 26 12:00:00 +0000 | Needs analyst review |
| `UPD-KEV-CVE-2026-42897` | `FEED-CISA-KEV` | Surface | Known exploited vulnerability | [CVE-2026-42897 - Microsoft Exchange Server Cross-Site Scripting Vulnerability](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | 2026-05-15 | Needs exposure review |
| `UPD-CONNECTOR-FEED-MISP-OPTIONAL` | `FEED-MISP-OPTIONAL` | Surface | Optional connector status | [MISP events](https://www.misp-project.org/openapi/) | 2026-05-15 | Not configured |
| `UPD-MITRE-G0049-60c08f71f0` | `FEED-MITRE-ATTACK-ENTERPRISE` | G0049 | ATT&CK intrusion-set taxonomy update | [OilRig](https://attack.mitre.org/groups/G0049) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-G0059-2eecb5256c` | `FEED-MITRE-ATTACK-ENTERPRISE` | G0059 | ATT&CK intrusion-set taxonomy update | [Magic Hound](https://attack.mitre.org/groups/G0059) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-G0069-03689cb0da` | `FEED-MITRE-ATTACK-ENTERPRISE` | G0069 | ATT&CK intrusion-set taxonomy update | [MuddyWater](https://attack.mitre.org/groups/G0069) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-G0087-01a9c7eebf` | `FEED-MITRE-ATTACK-ENTERPRISE` | G0087 | ATT&CK intrusion-set taxonomy update | [APT39](https://attack.mitre.org/groups/G0087) | 2024-04-11 | Needs analyst review |
| `UPD-MITRE-G1001-14a09dbf66` | `FEED-MITRE-ATTACK-ENTERPRISE` | G1001 | ATT&CK intrusion-set taxonomy update | [HEXANE](https://attack.mitre.org/groups/G1001) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-G1028-581b0024c5` | `FEED-MITRE-ATTACK-ENTERPRISE` | G1028 | ATT&CK intrusion-set taxonomy update | [APT-C-23](https://attack.mitre.org/groups/G1028) | 2024-11-17 | Needs analyst review |
| `UPD-MITRE-G1030-e96f8e578d` | `FEED-MITRE-ATTACK-ENTERPRISE` | G1030 | ATT&CK intrusion-set taxonomy update | [Agrius](https://attack.mitre.org/groups/G1030) | 2024-08-29 | Needs analyst review |
| `UPD-MITRE-G1044-e3ed64de89` | `FEED-MITRE-ATTACK-ENTERPRISE` | G1044 | ATT&CK intrusion-set taxonomy update | [APT42](https://attack.mitre.org/groups/G1044) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-HANDALA-72d63c6f04` | `FEED-MITRE-ATTACK-ENTERPRISE` | HANDALA | ATT&CK intrusion-set taxonomy update | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-IMPERIALKITTEN-bbb6cea576` | `FEED-MITRE-ATTACK-ENTERPRISE` | IMPERIALKITTEN | ATT&CK intrusion-set taxonomy update | [CURIUM](https://attack.mitre.org/groups/G1012) | 2024-10-02 | Needs analyst review |
| `UPD-MITRE-LEBANESECEDAR-872e0d8dcf` | `FEED-MITRE-ATTACK-ENTERPRISE` | LEBANESECEDAR | ATT&CK intrusion-set taxonomy update | [Volatile Cedar](https://attack.mitre.org/groups/G0123) | 2025-04-16 | Needs analyst review |
| `UPD-MITRE-PIONEERKITTEN-03d5c9032e` | `FEED-MITRE-ATTACK-ENTERPRISE` | PIONEERKITTEN | ATT&CK intrusion-set taxonomy update | [Fox Kitten](https://attack.mitre.org/groups/G0117) | 2026-05-12 | Needs analyst review |
| `UPD-MITRE-TA402-976749cc0a` | `FEED-MITRE-ATTACK-ENTERPRISE` | TA402 | ATT&CK intrusion-set taxonomy update | [Frankenstein](https://attack.mitre.org/groups/G0101) | 2025-04-18 | Needs analyst review |
| `UPD-MITRE-TA402-65b917d7e7` | `FEED-MITRE-ATTACK-ENTERPRISE` | TA402 | ATT&CK intrusion-set taxonomy update | [Molerats](https://attack.mitre.org/groups/G0021) | 2024-11-17 | Needs analyst review |
| `UPD-MITRE-WIRTE-7cc1aa86db` | `FEED-MITRE-ATTACK-ENTERPRISE` | WIRTE | ATT&CK intrusion-set taxonomy update | [WIRTE](https://attack.mitre.org/groups/G0090) | 2026-04-23 | Needs analyst review |
| `UPD-CONNECTOR-FEED-OPENCTI-OPTIONAL` | `FEED-OPENCTI-OPTIONAL` | Surface | Optional connector status | [OpenCTI indicators and reports](https://docs.opencti.io/latest/reference/api/) | 2026-05-15 | Not configured |
| `UPD-CONNECTOR-FEED-OTX-OPTIONAL` | `FEED-OTX-OPTIONAL` | Surface | Optional connector status | [AlienVault OTX pulses](https://otx.alienvault.com/api/v1/pulses/subscribed) | 2026-05-15 | Not configured |

Machine-readable queue: `data/intel-update-candidates.csv`.

Feed definitions: `data/intel-feeds.csv`.
