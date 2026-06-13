---
description: "Cotton Sandstorm (Emennet Pasargad / ASA) is an IRGC-affiliated influence operations actor combining intrusion, data theft, and media messaging campaigns targeting Israel and Western audiences."
---

# Cotton Sandstorm

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Cotton Sandstorm](../navigation/actor-workbench.md#cotton-sandstorm)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: None currently mapped.
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1585](../navigation/ttp-detection-matrix.md#t1585) Establish Accounts (M1); [T1204.002](../navigation/ttp-detection-matrix.md#t1204002) User Execution: Malicious File (M3); [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M3)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-CP-WEZRAT` Email sender; domains; hashes; C2 paths; malware behavior
- Tool detail pages: [`WezRat`](../tools/wezrat.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#cotton-sandstorm) (1 mapped tool row(s))
- Evidence records: `EVD-022` / `CLM-COTTONSANDSTORM-001`
- Imported research intakes: None currently mapped.
- Intel update candidates: None in current feed pull.
- Source IDs in structured data: `SRC-CP-WEZRAT`, `SRC-FBI-EMENNET-2024`, `SRC-MS-IRAN-IO`

<!-- ACTOR-NAVIGATION:END -->

## Background

Cotton Sandstorm operates through the Iranian front company Aria Sepehr Ayandehsazan (ASA), previously known as Emennet Pasargad — an IRGC-affiliated cyber contractor sanctioned by U.S. Treasury OFAC in October 2024. Unlike MOIS-linked actors focused on espionage or destructive operations, ASA's mandate is influence operations: combining intrusion, data theft, public claim-making, and media messaging into unified campaigns designed to shape public perception and sow confusion.

The group's operational signature is multi-stage information operations. A typical campaign involves unauthorized access to a target organization, data theft, defacement or disruption, Telegram channel publication of stolen data with inflammatory framing, and coordinated amplification across social media. This pattern was documented against Israeli streaming and media services during the 2023-2024 conflict period, including unauthorized streaming of propaganda content during high-visibility events.

In October 2024, FBI, CISA, and Israel's INCD jointly published an advisory formally attributing these campaigns to ASA and IRGC, naming specific ASA personnel and detailing operational infrastructure. Alongside this, Check Point Research published analysis of WezRat — a modular infostealer attributed to this cluster, deployed via phishing emails impersonating the Israel National Cyber Directorate. WezRat's modularity allows keylogging, credential harvesting, clipboard capture, and screenshot collection as plugin tasks requested from C2.

A key defensive consideration for Cotton Sandstorm is separating technically verified compromise from unverified public claims. The group's influence operation model means that a claim of compromise does not confirm compromise, and vice versa — forensic evidence must be sought independently of media announcements.

Aliases: Emennet Pasargad, Aria Sepehr Ayandehsazan (ASA), MarnanBridge, Haywire Kitten, Altoufan Team (Al-Toufan), Net Peygard Samavat.

Assessed sponsor: IRGC-linked, specifically associated with the front company Aria Sepehr Ayandehsazan (ASA) per the FBI / U.S. Treasury / INCD joint advisory (October 2024). ASA is an Iranian cyber contractor, not a direct IRGC unit — distinguish from IRGC-CEC (CyberAv3ngers) and MOIS-subordinate actors.

## Relevance

Cotton Sandstorm is relevant to Israeli government because Microsoft describes Iranian cyber-enabled influence operations that combine intrusion, leak claims, impersonation, and messaging designed to shape perceptions during conflict.

## Defensive Focus

- Separating verified compromise from public claims.
- Monitoring leak-site and persona claims without over-attribution.
- Preserving forensic evidence for public communications response.
- Coordinating cyber, legal, and communications teams.

## Detection Ideas

- Web defacement attempts.
- Bulk email or SMS impersonation campaigns.
- Unusual public data exposure followed by coordinated amplification.

Sources: `SRC-MS-IRAN-HAMAS`, `SRC-MS-IRAN-IO`, `SRC-FDD-IRAN-IO-ISRAEL`.

## Public Reports

**Government advisories:**

- FBI/CISA/INCD Joint Advisory on Emennet Pasargad / ASA — October 2024. Formal attribution to ASA and IRGC, named personnel, infrastructure details, and campaign timelines. Source ID `SRC-FBI-EMENNET-2024`.
- U.S. Treasury OFAC Designation of Aria Sepehr Ayandehsazan — October 2024. Sanctions designation with supporting narrative on ASA's role as IRGC contractor for cyber-enabled influence operations.

**Primary vendor reporting:**

- Check Point Research, "WezRat: New Modular Infostealer Targeting Israel" — November 2024. Technical analysis of WezRat malware attributed to Cotton Sandstorm/ASA, distributed via fake INCD phishing emails. Source ID `SRC-CP-WEZRAT`.
- Microsoft Threat Intelligence, "Iran Cyber-Enabled Influence Operations" — Documents Iranian influence operation patterns including Cotton Sandstorm's hack-and-leak methodology. Source ID `SRC-MS-IRAN-IO`.
- Microsoft Threat Intelligence, "Iran and Hamas" — Influence operation context for the conflict-period operation set. Source ID `SRC-MS-IRAN-HAMAS`.
- Foundation for Defense of Democracies (FDD), Iran IO Israel analysis — Policy-level analysis of Iranian information operations targeting Israel. Source ID `SRC-FDD-IRAN-IO-ISRAEL`.
