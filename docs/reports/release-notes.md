---
title: Release Notes
sidebar_label: Release Notes
---

# Release Notes

This page records repository maturity changes. It is intentionally explicit
about what is and is not production-ready.

## v1.1

Status: practical CTI-to-detection framework with connected public CTI update
intake. Still not a production SOC detection pack.

Key changes:

- Promoted the repository version to `v1.1`.
- Added `data/tool-intelligence.csv` as a defensive actor-to-tool intelligence
  layer with behavior summaries, hash/IOC status, source links, confidence, and
  detection notes.
- Added [Malware And Tool Intelligence](../malware-tool-intelligence.md), a
  generated page that lets analysts click from actor profiles to associated
  tools, behaviors, hash availability, and source-backed detection guidance.
- Added generated per-tool detail pages under `docs/tools/`, with behavior,
  hash/IOC status, actor profile links, mapped ATT&CK techniques, mapped
  detections, mapped hunts, source-review metadata, and handling notes.
- Expanded source-backed tool coverage from MITRE ATT&CK software mappings for
  MuddyWater, OilRig, Magic Hound/APT35, Agrius, Arid Viper, Lyceum, APT39,
  and VOID MANTICORE / Handala.
- Changed actor profiles to use tool-page crosslinks rather than carrying full
  tool behavior writeups inline.
- Enriched UNC1860 tool coverage for TEMPLEDOOR, TEMPLEPLAY, CRYPTOSLAY,
  PipeSnoop, STAYSHANTE, SASHEYAWAY, VIROGREEN, TEMPLEDROP, and TEMPLELOCK
  based on Mandiant-linked and Malpedia reporting.
- Updated generated actor navigation blocks to link every actor to the new
  tool intelligence matrix and individual tool detail pages where mapped.
- Refreshed the connected-feed queue from MITRE ATT&CK Enterprise STIX, CISA
  KEV, and CISA Cybersecurity Advisories RSS.
- Added [Connected TIPs And CTI Feeds](../connected-tips.md) with feed
  descriptions, optional connector setup, GitHub Actions behavior, and
  promotion workflow.
- Expanded [Intelligence Update Queue](../intelligence-updates.md) with actor
  update candidates and surface/exposure candidate summaries.
- Added current intel lead counts into actor navigation blocks and actor
  workbench tables.
- Added `data/research-intake-map.csv` to connect imported deep-research
  reports to relevant actors while keeping unvalidated LLM-derived claims out
  of authoritative source, evidence, tool, TTP, hunt, and detection records.
- Regenerated actor navigation blocks and the actor workbench with imported
  research-intake links, priority, and validation status.
- Added [Research Intake Upgrade Summary](research-intake-upgrade-summary.md)
  to show what was upgraded from the imported reports and which claims remain
  validation-gated.
- Added VirusTotal as an optional hash-enrichment connector using `VT_API_KEY`
  from the local environment only. The repository now tracks reviewed hash
  seeds in `data/virustotal-hash-seeds.csv`, reviewed enrichment candidates in
  `data/virustotal-enrichment-candidates.csv`, and the local
  `npm run intel:vt` workflow without committing keys, raw VT JSON, samples, or
  private telemetry.
- Added [VirusTotal Malware Enrichment](../virustotal-enrichment.md) with
  promotion rules and current reviewed enrichment for TEMPLEDOOR, TEMPLEPLAY,
  TEMPLEDROP, IOCONTROL, OilBooster, OilCheck, and ODAgent.
- Enriched tool behavior and hash/IOC status for BugSleep, Fooder/MuddyViper,
  OilBooster, OilCheck, ODAgent, IOCONTROL, AridSpy, WezRat, IronWind,
  SameCoin, AshTag, TEMPLEDOOR, TEMPLEPLAY, TEMPLEDROP, IMAPLoader, and
  Liontail.

Remaining production blockers:

- Feed candidates are leads and must be reviewed before promotion.
- No connected feed may create actor attribution by itself.
- OTX, VirusTotal, MISP, and OpenCTI require trusted local/community
  configuration before use beyond documented connector targets.
- VirusTotal verdicts are enrichment only and do not create actor attribution.
- No detection is DRL-9.

## v0.1.7

Status: public CTI update intake layer; still requires analyst review before
promotion into source, evidence, actor, hunt, or detection records.

Key changes:

- Added no-key public feed definitions for MITRE ATT&CK Enterprise STIX, CISA
  KEV, and CISA Cybersecurity Advisories RSS.
- Added optional connector definitions for OTX, MISP, and OpenCTI using local
  environment variables or GitHub Actions secrets.
- Added `scripts/fetch_intel_updates.py` and `npm run intel:update`.
- Added `data/intel-update-candidates.csv` as a machine-readable analyst review
  queue.
- Added [Intelligence Update Queue](../intelligence-updates.md) as the human
  review page for current feed candidates.
- Added a scheduled/manual GitHub Actions workflow that can fetch the update
  queue and publish it as an artifact without auto-committing unreviewed feed
  data.

Remaining production blockers:

- Feed matches are collection leads, not verified claims.
- KEV and surface matches must not be converted into actor attribution without
  primary-source evidence.
- OTX, MISP, and OpenCTI require trusted local/community instances or API keys.
- No feed item bypasses the repository's source/evidence review workflow.

## v0.1.6

Status: practical navigation layer for analyst use; still not production SOC
coverage.

Key changes:

- Added generated actor navigation blocks to every actor profile.
- Added an Actor Navigation Workbench that joins each actor to TTPs, IOC
  references, malware/tool references, hunts, detections, evidence records, and
  operational surfaces.
- Added a TTP To Detection Matrix so analysts can click from a technique to
  relevant actors, mapped repository detections, mapped hunts, and MITRE ATT&CK.
- Added a Surface And Capability Matrix so analysts can start from identity,
  endpoint, OT, internet-facing server, destructive-operations, or C2 surfaces
  and route to relevant actors and defensive content.
- Added `scripts/build_navigation_crosslinks.py` and wired it into local and CI
  validation so navigation pages are regenerated from structured repository
  data.

Remaining production blockers:

- Navigation coverage does not imply production detection coverage.
- Some actors and TTPs intentionally have no mapped repository detection yet.
- No detection is DRL-9.
- Customer telemetry validation is still required before production use.

## v0.1.5

Status: stronger proof layer for public validation; still not production SOC
coverage.

Key changes:

- Added deterministic synthetic fixture tests for `DET-001` through `DET-004`.
- Expanded the synthetic fixture set to include multiple positive and benign
  boundary cases per detection.
- Added `scripts/run_detection_fixture_tests.py` to CI validation.
- Added committed synthetic positive/negative outputs and synthetic
  false-positive rates.
- Added synthetic 30-day replay substitute for `DET-002`.
- Added generated detection status dashboard.
- Added customer-environment usage guide.
- Added Sigma CLI semantic validation result with zero errors and zero issues.
- Added top-level known limitations page.
- Added platform query-variant status page.
- Added customer-style SOC handoff packet for `DET-002`.
- Added `release_status` to the detection backlog: Hunt / Pilot / Production /
  Retired.

Remaining production blockers:

- No detection is DRL-9.
- Synthetic tests are not customer telemetry.
- No real tenant or customer historical replay is committed.
- Backend-specific Splunk and Elastic conversion artifacts remain pending.
- False-positive rates are synthetic fixture rates only.

## v0.1.4

Status: professional public CTI-to-detection research repository; not a
production SOC analytics package.

Key changes:

- Fixed GitHub Pages slash-route 404s by switching Docusaurus to
  directory-style routes.
- Added three end-to-end worked cases:
  - MuddyWater phishing to RMM / BugSleep / Fooder / MuddyViper.
  - Scarred Manticore / UNC1860 access to Void Manticore destructive handoff.
  - CyberAv3ngers OT / PLC exposure.
- Added detection-specific DRL evidence packs for `DET-001` through `DET-004`.
- Added committed lab/synthetic test evidence for `DET-002`.
- Expanded the evidence register to cover every actor in `data/actors.csv` with
  at least one claim-backed evidence row.
- Hardened repository validation for evidence, hunt, detection, health, and DRL
  evidence-pack cross-references.
- Added public CI and Pages deployment evidence.

Remaining production blockers:

- No detection is DRL-9.
- `DET-001`, `DET-003`, and `DET-004` still need positive and negative
  environment tests.
- `DET-002` has committed lab/synthetic evidence, but still needs backend
  conversion, historical replay, pilot review, and measured false-positive
  rate before promotion.
- Sigma/KQL examples remain hunt starters or pilot candidates until local
  telemetry validation is complete.

## v0.1.3

Status: professional methodology and hunt-starter baseline.

Key changes:

- Added source provenance fields: publication, access, review, update, archive,
  and hash metadata.
- Added persona-claims register to separate public claims from verified
  compromise.
- Added ATT&CK mapping-quality discipline.
- Added platform field mapping, SOC triage playbooks, and detection health
  tracking.

## v0.1.2

Status: expanded actor and taxonomy coverage.

Key changes:

- Added missing high-priority actor profiles including Scarred Manticore,
  Imperial Kitten, Pioneer Kitten, DarkBit, Lyceum, and APT39.
- Corrected actor taxonomy and sponsor caveats.
- Added additional Sigma/KQL hunt examples.

## v0.1.0

Status: initial public CTI knowledge-base structure.

Key changes:

- Initial actor register, source register, ATT&CK mapping table, report pages,
  and detection examples.
