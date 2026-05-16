---
title: Research Intake Upgrade Summary
sidebar_label: Research Intake Upgrades
---

# Research Intake Upgrade Summary

This page records how the newly imported deep-research reports were converted into practical repository improvements. It is intentionally conservative: imported LLM research is treated as an intake queue until every claim is validated against primary public reporting.

## What Was Upgraded

### Actor Navigation

Actor pages and the [Actor Workbench](../navigation/actor-workbench.md) now expose imported research-intake links where a report is relevant to that actor.

The new structured map is maintained in `data/research-intake-map.csv`. It currently routes:

| Actor | Imported Research Intake | Action |
| --- | --- | --- |
| MuddyWater | [MuddyWater Deep Research](muddywater-deep-research.md) | Validate Fooder, MuddyViper, RMM, Sad C2, Starlink, and Israel/Egypt targeting claims before promotion. |
| OilRig | [OilRig And Magic Hound Deep Research](oilrig-magic-hound-deep-research.md); [APT35 And OilRig Israel Deep Research](apt35-oilrig-israel-deep-research.md) | Validate cloud API C2, downloader, Saitama, Exchange/webshell, and Israeli telecom/government claims. |
| Magic Hound / APT35 | [OilRig And Magic Hound Deep Research](oilrig-magic-hound-deep-research.md); [APT35 And OilRig Israel Deep Research](apt35-oilrig-israel-deep-research.md) | Validate PowerStar, LNK/RAR phishing, Israeli VIP targeting, OAuth/cloud-phishing, and identity telemetry claims. |
| Pioneer Kitten | [Pioneer Kitten Deep Research](pioneer-kitten-deep-research.md) | Validate CISA AA24-241A, edge-appliance exploitation, and ransomware-affiliate handoff claims. |
| APT39 | [APT39 / Arid Viper / UNC3890 / Cyber Toufan Deep Research](apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) | Validate current activity status and decide operational priority versus watchlist status. |
| APT-C-23 / Arid Viper | [APT39 / Arid Viper / UNC3890 / Cyber Toufan Deep Research](apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) | Validate mobile spyware, Israeli military/public-safety targeting, and Mobile ATT&CK updates. |
| UNC3890 | [APT39 / Arid Viper / UNC3890 / Cyber Toufan Deep Research](apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) | Validate whether post-2022 public activity exists or the profile should remain a gap/watchlist entry. |
| Cyber Toufan | [APT39 / Arid Viper / UNC3890 / Cyber Toufan Deep Research](apt39-arid-viper-unc3890-cyber-toufan-deep-research.md) | Validate supplier compromise, wiper, persona, and recycled leak claims before promotion. |

### Research Governance

The upgrade adds a formal distinction between:

- Committed actor/tool/source facts already represented in structured data.
- Imported research claims that need validation.
- Candidate upgrades that should become evidence records, source rows, tool rows, TTP rows, or detection backlog items only after source confirmation.

This prevents unverified LLM output from silently becoming authoritative CTI.

### Framework Navigation

The generated actor navigation block now contains:

- Actor workbench link.
- TTP matrix link.
- Surface/capability routes.
- Detection and hunt links.
- IOC reference sources.
- Tool detail pages.
- Evidence records.
- Imported research intakes.
- Intel update candidates.
- Structured source IDs.

This makes each actor page a single entry point for current repository knowledge and for pending research-review work.

## What Was Not Promoted Yet

The imported reports contain useful leads, but many claims require exact source verification before they should alter production-facing framework artifacts.

Not yet promoted automatically:

- New hashes and IOCs.
- New source-register rows.
- New evidence-register rows.
- New ATT&CK rows.
- New detections or Sigma/KQL logic.
- New actor attribution claims.
- Claims about 2026 incidents, kinetic integration, BDA, MDM mass wipe activity, or supplier compromise where primary source confirmation is not already in repository data.

## Next Validation Tasks

Use [Actor Deep Research Prompts](actor-deep-research-prompts.md) and the source-validation follow-up prompt to process each imported report.

Priority order:

1. Validate MuddyWater Fooder / MuddyViper / RMM reporting against ESET and Israeli sources.
2. Validate OilRig cloud downloader and Israeli telecom/government claims against ESET, Broadcom/Symantec, MITRE, and vendor reporting.
3. Validate APT35/Magic Hound PowerStar and Israeli VIP phishing claims against Volexity, Check Point, MITRE, and Microsoft.
4. Validate Pioneer Kitten edge-appliance and ransomware handoff claims against CISA AA24-241A and later advisories.
5. Validate APT-C-23 / Arid Viper mobile spyware claims against ESET, SentinelOne, and mobile-security primary reporting.
6. Validate Cyber Toufan supplier-compromise and wiper claims before adding persona-claim or evidence rows.

## Review Standard

Each promotion from intake to framework data must produce at least one of:

- `sources.csv` row with live URL, reliability, review date, and archive hash where available.
- `examples/registers/evidence-register.csv` row with claim ID, actor ID, evidence label, confidence reason, and contradiction/gap.
- `data/tool-intelligence.csv` row with source-backed behavior, IOC reference status, detection notes, and handling notes.
- `data/ttps.csv` row with conservative mapping quality.
- Detection backlog or hunt-backlog row only when the observable and telemetry are defensible.
