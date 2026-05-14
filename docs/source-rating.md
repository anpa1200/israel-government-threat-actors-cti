---
title: Source Rating
sidebar_position: 3
---

# Source Rating

The repository uses a six-level source reliability scale adapted from the NATO Admiralty Code (STANAG 2511). The full scale is defined in the [Scoring Models](methodology/scoring-models.md) page; this page provides quick-reference examples for the most common levels.

| Rating | Meaning | Examples |
| --- | --- | --- |
| A | Highly reliable — strong methodology or direct primary evidence | Government advisories (CISA, INCD, FBI), MITRE ATT&CK, primary vendor CTI reports (Mandiant, Check Point Research, SentinelLabs, ESET, Unit 42) |
| B | Generally reliable — strong secondary synthesis or well-evidenced vendor summary | Security news citing primary sources, secondary vendor summaries, authored CTI synthesis (including this repository's own Medium articles) |
| C | Mixed reliability — limited detail, weak methodology, or partial corroboration | Blog summaries, conference slides without technical appendix, aggregator posts |
| D | Unknown reliability — unverified public claim or source quality not assessed | Single-source vendor claims not independently corroborated |
| E | Known issues — weak sourcing, track record of inaccuracy, or significant methodology gaps | Do not use for decisions without independent evidence |
| F | Unreliable or deceptive — known false or adversarially manipulated | Exclude from decisions entirely |

Information credibility is tracked separately using a 1–6 scale (1 = Confirmed, 6 = Cannot be judged) defined in [Scoring Models](methodology/scoring-models.md). Do not collapse source reliability and information credibility into a single rating.

## Required Practice

- Public claims by hacktivist personas MUST be corroborated before being treated as confirmed compromise.
- Vendor actor names SHOULD be mapped carefully because naming taxonomies differ.
- Source publication date MUST be considered when using IOCs.
