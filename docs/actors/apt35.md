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

Aliases: Charming Kitten, COBALT ILLUSION, Phosphorus, Newscaster, Mint Sandstorm, ITG18 (IBM), Ballistic Bobcat (ESET), Group 83.

Assessed sponsor: IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) per Proofpoint, Mandiant, and U.S. Treasury designations.

**Vendor naming caveat — TA453:** MITRE G0059 lists TA453 as a Magic Hound / APT35 alias. However, Proofpoint (2023), Volexity (2024), and Recorded Future map TA453 as roughly equivalent to APT42 rather than APT35. Analysts should note which vendor's taxonomy their source uses before attributing TA453 activity to this profile. See also the APT42 profile.

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
