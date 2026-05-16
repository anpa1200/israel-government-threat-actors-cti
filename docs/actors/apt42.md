# APT42

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [APT42](../navigation/actor-workbench.md#apt42)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](../navigation/surface-capability-matrix.md#identity-mdm); [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1530](../navigation/ttp-detection-matrix.md#t1530) Data from Cloud Storage (M1); [T1102](../navigation/ttp-detection-matrix.md#t1102) Web Service (M1); [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link (M3)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MANDIANT-APT42` Domains; malware hashes; infrastructure; `SRC-PROOFPOINT-IRAN-CONFLICT-2026` Phishing infrastructure; lure domains; campaign indicators
- Tool detail pages: [`POWERPOST`](../tools/powerpost.md); [`NICECURL`](../tools/nicecurl.md); [`TAMECAT`](../tools/tamecat.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt42) (3 mapped tool row(s))
- Evidence records: `EVD-003` / `CLM-APT42-001`; `EVD-016` / `CLM-APT42-002`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-GOOGLE-APT42-PHISHING`, `SRC-MANDIANT-APT42`, `SRC-MITRE-G1044`, `SRC-PROOFPOINT-IRAN-CONFLICT-2026`

<!-- ACTOR-NAVIGATION:END -->

Aliases: UNC788 (Mandiant), Yellow Garuda (Recorded Future), Damselfly (Symantec), CharmingCypress (Volexity), Educated Manticore (Check Point), ITG18 (IBM, overlapping with APT35).

Assessed sponsor: IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) per Mandiant, Proofpoint, and U.S. Treasury designations.

**Vendor naming caveat — TA453 and Charming Kitten:** Proofpoint (2023) and Volexity (2024) map TA453 as roughly equivalent to APT42, while MITRE ATT&CK G0059 retains TA453 under Magic Hound / APT35. "Charming Kitten" is used by some vendors for APT35 and others for APT42. Analysts MUST note which vendor taxonomy their source uses before attributing TA453 or Charming Kitten activity to either profile.

## Relevance

APT42 is high priority because MITRE and Mandiant describe cyber espionage and surveillance operations focused on the Middle East, including spearphishing, cloud collection, and custom tooling.

## Defensive Focus

- Spearphishing and cloud-hosted lure delivery.
- Credential theft from browsers and cloud services.
- Microsoft 365 data collection.
- HTTPS-based command and control using custom tools.

## Detection Ideas

- Risky sign-in followed by cloud file access burst.
- Browser credential store access from unusual processes.
- New OAuth grants or suspicious cloud application consent.

Sources: `SRC-MITRE-G1044`, `SRC-MANDIANT-APT42`, `SRC-GOOGLE-APT42-UNCHARMED`, `SRC-GOOGLE-APT42-PHISHING`, `SRC-GOOGLE-AI-MISUSE`, `SRC-GOOGLE-AI-TRACKER`, `SRC-PROOFPOINT-IRAN-CONFLICT-2026`.
