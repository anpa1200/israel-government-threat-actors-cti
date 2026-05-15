# Changelog

## v0.1.7 - 2026-05-15

### New
- Added a public CTI feed update layer with no-key connectors for MITRE ATT&CK Enterprise STIX, CISA KEV, and CISA Cybersecurity Advisories RSS.
- Added optional OTX, MISP, and OpenCTI connector definitions for environments with API keys or trusted community instances.
- Added `scripts/fetch_intel_updates.py`, `data/intel-feeds.csv`, `data/intel-update-candidates.csv`, and `docs/intelligence-updates.md`.
- Added scheduled/manual GitHub Actions workflow `intel-update-check.yml` to publish update queue artifacts without auto-committing unreviewed feed content.

### Guardrails
- Feed hits are review candidates only and do not auto-promote into actor attribution, evidence, TTP, hunt, or detection records.

## v0.1.3 - 2026-05-14

### Fixed
- Re-scoped the Intune wipe Sigma rule as a base event selector and removed deprecated pipe aggregation syntax; bulk detection remains in the KQL companion.
- Added a validator guard for deprecated Sigma pipe aggregation so invalid count syntax fails repository validation.
- Retitled the Liontail-adjacent Sigma rule as a generic phantom-DLL service-control hunt instead of overclaiming IIS native-module coverage.
- Downgraded the IMAPLoader IMAP rule to a low-severity hunt starter because the selector is intentionally broad.
- Replaced published "imported research" provenance phrasing with primary-source-review or explicit gap language.
- Replaced the stale CyberAv3ngers IOControl source note with `SRC-CLAROTY-IOCONTROL-2024`.
- Replaced dead or automation-blocked source URLs with live primary/source-register alternatives and verified external URL reachability.
- Renamed the Cyber Toufan SMB KQL hunt to remove the actor name from the filename and updated documentation references.
- Added `.gitattributes` and normalized `data/ttps.csv` line endings to LF.
- Clarified that Arid Viper `T1456` is a Mobile ATT&CK mapping and should remain validated against campaign-specific mobile delivery evidence.
- Pointed the Intune bulk-wipe detection backlog item to the KQL implementation and tightened the `wbadmin` backup-deletion Sigma condition.
- Added an npm override for `serialize-javascript` 7.0.5 to clear the Docusaurus transitive high-severity audit finding.

## v0.1.2 - 2026-05-14

### New
- Added actor profiles for Imperial Kitten, Pioneer Kitten, DarkBit, Lyceum / HEXANE, and APT39.
- Added structured actor, source, TTP, and malware/tool references for the new profiles and related tooling.
- Added Sigma prototypes for IMAPLoader-style IMAP C2, Liontail-style service/DLL behavior, VSS/backup deletion, and BiBi-style file rename activity.
- Added primary source records for CrowdStrike Imperial Kitten, PwC Yellow Liderc, CISA AA24-241A, MITRE G1012/G1001/G0087, Claroty IOCONTROL, Unit 42 OilRig DNS tunneling, and U.S. Rana/APT39 attribution sources.

### Fixed
- Clarified Void Manticore / Handala actor-persona taxonomy.
- Fixed Scarred Manticore actor ID spelling in structured data.
- Replaced the executable RMM Sigma placeholder filter with documentation-only tuning guidance.
- Updated Unitronics PLC rule metadata to use ATT&CK for ICS T0883.
- Strengthened repository validation with actor/source cross-reference checks, ATT&CK ID checks, duplicate ID checks, and Sigma placeholder detection.
- Ignored local OpenAI/Gemini research-intake dumps so development materials are not committed as published reports.

## v0.1.1 - 2026-05-14

### New
- Added Scarred Manticore actor profile (MOIS initial-access cluster, Liontail IIS framework, Void Manticore handoff kill chain).
- Added `mapping_quality` column (M1/M2/M3) to `data/ttps.csv`.
- Added SRC-CP-SCARRED-MANTICORE-2023 source record.

### Fixed — Detection Rules
- `cloud-admin-mfa-backup-risk`: removed misleading "Followed By" title; rule fires on independent events (OR), KQL companion handles correlation; level set to `low`.
- `intune-bulk-device-wipe-anomaly`: added Sigma count aggregation (`> 20 by InitiatedBy` in 10 min window); was previously firing on every single device action.
- `pim-activation-stale-mfa-claim`: renamed to remove stale-claim overclaim; Sigma cannot evaluate token freshness.
- `unitronics-plc-hmi-web-access`: changed `or` → `and` condition; removed generic `/login.html`; added specific Unitronics paths (`/SetDateTime`, `/EthernetSetup`, `/ipinfo.html`).
- `fake-security-update-infostealer-execution`: switched `Image|contains` to `Image|endswith` with specific filenames; added `ParentImage` anchor (mail/browser/archive parents only).
- `trusted-sender-bulk-phishing-anomaly`: retitled as hunt starter; added known-benign sender filter; level set to `informational`.
- `suspicious-rmm-file-sharing-download`: replaced unrealistic `approved-rmm` filter string with documented tuning placeholder.
- All 13 Sigma rules: normalised `date:` fields to ISO `YYYY-MM-DD` format.

### Fixed — Actor Taxonomy
- CyberAv3ngers: sponsor updated to IRGC-CEC / Shahid Kaveh Group per CISA AA26-097A and OFAC Feb 2024; added aliases Storm-0784, Bauxite, UNC5691, Hydro Kitten, Shahid Kaveh Group, Soldiers of Solomon, Mr. Soul; noted IOControl malware (Claroty 2024).
- MuddyWater: added Boggy Serpens (current Microsoft name), TA450 (Proofpoint), Earth Vetala (Trend Micro); marked MERCURY as retired (April 2023).
- Arid Viper: removed Two-tailed Scorpion (not a confirmed alias in primary sources); added Renegade Jackal (CrowdStrike).
- UNC1860: removed "Temple of Oats cluster" (report title, not an actor alias); added TEMPLEPLAY and TEMPLEDROP to associated tooling.
- Handala: removed Storm-842 duplicate of Storm-0842; added Red Sandstorm, Karma, Homeland Justice per MITRE G1055.
- Agrius: softened MOIS attribution to "Iran-aligned (assessed by some sources; not firmly attributed in primary reporting)".
- APT35 / APT42: added IRGC-IO sponsor specificity; added TA453 cross-vendor naming caveat; added missing aliases (UNC788, Yellow Garuda, CharmingCypress, ITG18, Ballistic Bobcat, Damselfly).
- Cotton Sandstorm: added Aria Sepehr Ayandehsazan (ASA), Altoufan Team, Net Peygard Samavat; corrected sponsor to IRGC-linked / ASA front company per FBI-Treasury-INCD Oct 2024.
- CyberAv3ngers TTP: replaced incorrect T0811 (Collection) with T0883 (Initial Access: Internet Accessible Device); added T0836 and T0832 impact-phase techniques.

### Fixed — Documentation
- `docs/source-rating.md`: expanded from A/B/C/D to A/B/C/D/E/F to match `scoring-models.md`; added note on keeping source reliability and information credibility separate.
- `docs/methodology/scoring-models.md`: added NATO Admiralty Code (STANAG 2511) and Sherman Kent attribution.
- `docs/actors/lebanese-cedar.md`: added Repository Sources section with SRC-CLEARSKY-LEBANESE-CEDAR and CVE references.
- `docs/actors/cyber-toufan.md`: added SRC-OPI-CYBER-TOUFAN as primary source; linked SMB lateral movement KQL hunt.
- `docs/actors/cyberav3ngers.md`: added IOControl malware section; added full sources block.
- `docs/actors/handala.md`: reordered sources to lead with MITRE G1055; added Push Security Stryker reference.
- `scripts/validate_repo.py`: updated expected `ttps.csv` header to include `mapping_quality`.

## v0.1.0 - 2026-05-13

- Initial defensive CTI repository structure.
- Added actor register, source register, TTP mapping, IOC reference table, and malware/tool reference table.
- Added initial actor profiles for Iran-linked, Palestinian-linked, and hacktivist personas relevant to Israeli government exposure.
- Added Sigma and KQL defensive detection examples.
- Added validation script and GitHub Actions workflow.
