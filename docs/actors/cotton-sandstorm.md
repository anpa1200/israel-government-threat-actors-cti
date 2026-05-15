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
- Malware and tools: `WezRat` (Modular infostealer / RAT)
- Evidence records: `EVD-022` / `CLM-COTTONSANDSTORM-001`
- Source IDs in structured data: `SRC-CP-WEZRAT`, `SRC-FBI-EMENNET-2024`, `SRC-MS-IRAN-IO`

<!-- ACTOR-NAVIGATION:END -->

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
