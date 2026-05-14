# Changelog

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
