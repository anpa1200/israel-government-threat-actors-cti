---
description: "Magic Hound (APT35) is an IRGC-IO-attributed cyber espionage group targeting academics, journalists, diplomats, and Israeli government entities through persona-based spearphishing and credential theft."
---

# Magic Hound / APT35

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Magic Hound](../navigation/actor-workbench.md#magic-hound)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](../navigation/surface-capability-matrix.md#identity-mdm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link (M2); [T1583.001](../navigation/ttp-detection-matrix.md#t1583001) Acquire Domains (M1)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: None currently mapped.
- Tool detail pages: [`FRP / Plink`](../tools/frp-plink.md); [`Mimikatz / SQLMap / Havij`](../tools/mimikatz-sqlmap-havij.md); [`CharmPower`](../tools/charmpower.md); [`DownPaper`](../tools/downpaper.md); [`Impacket`](../tools/impacket.md); [`ipconfig`](../tools/ipconfig.md); [`Mimikatz`](../tools/mimikatz.md); [`Net`](../tools/net.md); [`netsh`](../tools/netsh.md); [`Ping`](../tools/ping.md); [`PowerLess`](../tools/powerless.md); [`PsExec`](../tools/psexec.md); [`Pupy`](../tools/pupy.md); [`Systeminfo`](../tools/systeminfo.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#magic-hound) (14 mapped tool row(s))
- Evidence records: `EVD-015` / `CLM-APT35-001`
- Imported research intakes: [OilRig And Magic Hound Deep Research Intake](../reports/oilrig-magic-hound-deep-research.md) (High, Needs source validation); [APT35 And OilRig Israel Deep Research Intake](../reports/apt35-oilrig-israel-deep-research.md) (High, Needs source validation)
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G0059`

<!-- ACTOR-NAVIGATION:END -->

## Background

Magic Hound (APT35) has been active since approximately 2014 and is among the most extensively reported Iranian threat actors in public vendor literature. The group's operational mandate centers on long-running surveillance and espionage targeting academics, journalists, human rights activists, think-tank researchers, policy makers, diplomatic officials, and regional political opponents of the Iranian government. U.S. Treasury OFAC and DOJ indictments, alongside multiple vendor attributions, tie the group to the Islamic Revolutionary Guard Corps Intelligence Organisation (IRGC-IO).

The group's initial public exposure came through iSIGHT Partners' 2014 "Newscaster" report, which documented an extensive network of fake journalist personas used to build trust with targets before credential theft or malware delivery. This persona-based, long-duration social engineering approach remains the group's signature even as the technical tooling has evolved. Notable campaigns include: spearphishing against U.S. defense contractors and State Department officials (2016-2018); the HBO phishing campaign that resulted in "Game of Thrones" script theft (2017); and a DOJ-attributed campaign against the 2020 U.S. presidential election infrastructure.

Microsoft's "Mint Sandstorm" reporting (2022-2023) documented the group's expansion into targeting critical infrastructure and healthcare organizations, as well as researchers connected to Middle East policy. The group has exploited Log4j vulnerabilities (CVE-2021-44228) and used CharmPower, a PowerShell-based backdoor, as part of this wave. ESET's "Ballistic Bobcat" reporting provides complementary coverage of simultaneous phishing infrastructure operations.

For Israeli government and regional diplomacy defenders, APT35 represents a persistent credential-theft and persona-based intelligence collection threat against senior officials, academics, and security researchers. The group's patience — running multiple-month persona relationships before deploying technical operations — means traditional phishing-indicator detection alone is insufficient.

Aliases: Charming Kitten, COBALT ILLUSION, Phosphorus, Newscaster, Mint Sandstorm, ITG18 (IBM), Ballistic Bobcat (ESET), Group 83.

Assessed sponsor: IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) per Proofpoint, Mandiant, and U.S. Treasury designations.

**Vendor naming caveat — TA453:** MITRE G0059 lists TA453 as a Magic Hound / APT35 alias. However, Proofpoint (2023), Volexity (2024), and Recorded Future map TA453 as roughly equivalent to APT42 rather than APT35. Analysts should note which vendor's taxonomy their source uses before attributing TA453 activity to this profile. See also the [APT42 profile](./apt42.md).

## Relevance

APT35-related reporting is highly relevant to Israeli government because the actor family is associated with credential phishing, persona-based social engineering, and targeting of policy, defense, academia, media, and regional entities.

## Defensive Focus

- Fake login portals and domain impersonation.
- Spearphishing links and long-running social engineering.
- Mailbox access after credential theft.
- OAuth consent and MFA reset attempts.

## Detection Ideas

- New inbox rules after risky sign-in.
- MFA method registration after impossible travel or new device sign-in.
- Lookalike domains targeting ministries, public agencies, or suppliers.

Sources: `SRC-MITRE-G0059`, `SRC-MS-MINT-SANDSTORM`, `SRC-MS-MINT-PROFILE`, `SRC-CP-EDUCATED-2023`, `SRC-CP-EDUCATED-2025`.

## Public Reports

**Own ecosystem:**

- [Deep Research Intake: APT35 and OilRig Israel](../reports/apt35-oilrig-israel-deep-research.md) — Internal repository synthesis covering Israeli-specific targeting context. High-priority, requires source validation.
- [Deep Research Intake: OilRig and Magic Hound](../reports/oilrig-magic-hound-deep-research.md) — Internal research intake with adjacent actor mapping.

**MITRE ATT&CK:**

- [MITRE ATT&CK G0059 — Magic Hound](https://attack.mitre.org/groups/G0059/) — Technique mappings, alias registry, and software associations. Note the TA453 alias caveat in the vendor naming section above.

**Government and law enforcement:**

- Microsoft Security Blog, "New Mint Sandstorm Campaign Targeting High-Profile Individuals" — 2023. Documents targeting of researchers, journalists, and government officials via social engineering and Log4j exploitation. Source ID `SRC-MS-MINT-SANDSTORM`.

**Primary vendor reporting:**

- Check Point Research, "Educated Manticore" — 2023 and 2025 campaigns targeting Israeli and regional academic and policy researchers. Source IDs `SRC-CP-EDUCATED-2023`, `SRC-CP-EDUCATED-2025`.
- ESET Research, "Ballistic Bobcat" — Credential-phishing infrastructure and spearphishing campaign analysis complementing the APT35 profile.
- Proofpoint, historical TA453 reporting — Credential phishing via lookalike domains and tailored lure content; note vendor taxonomy caveat before applying TA453 claims to this profile.
- iSIGHT Partners, "Newscaster" — 2014 original disclosure documenting persona-based espionage network.
