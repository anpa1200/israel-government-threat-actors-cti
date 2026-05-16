# WIRTE

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [WIRTE](../navigation/actor-workbench.md#wirte)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M2); [T1574.001](../navigation/ttp-detection-matrix.md#t1574001) DLL Search Order Hijacking (M3); [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1105](../navigation/ttp-detection-matrix.md#t1105) Ingress Tool Transfer (M3); [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M3)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-CP-WIRTE-2024` Wiper references; trusted sender abuse; fake update artifacts; `SRC-UNIT42-ASHTAG-2025` Malware hashes; domains; C2 paths; tool behavior
- Malware and tools: [`SameCoin`](../tools/samecoin.md) (Wiper); [`AshTag`](../tools/ashtag.md) (Modular .NET malware suite)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#wirte) (2 mapped tool row(s))
- Tool detail pages: [`SameCoin`](../tools/samecoin.md); [`AshTag`](../tools/ashtag.md)
- Evidence records: `EVD-010` / `CLM-WIRTE-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-CP-WIRTE-2024`, `SRC-UNIT42-ASHTAG-2025`

<!-- ACTOR-NAVIGATION:END -->

Aliases: Ashen Lepus; Gaza Cybergang-linked reporting.

Assessed sponsor: Hamas-affiliated in Check Point public reporting.

## Relevance

WIRTE is high priority for Israeli public-sector defenders because Check Point reported expansion from espionage into disruptive activity against Israeli entities, including SameCoin-linked wiper activity.

## Defensive Focus

- Trusted sender abuse.
- Fake security or vendor update lures.
- Archive-to-execution chains.
- DLL sideloading.
- Wiper-preparation behavior.

## Detection Ideas

- Signed installer execution from archive or user download paths followed by same-directory DLL loads.
- Inbound mail from trusted regional senders that suddenly includes archives, XLL/PPAM files, or update-themed links.
- Fake ESET/Kaspersky/reseller update filenames.

Sources: `SRC-CP-WIRTE-2024`, `SRC-PROOFPOINT-TA402-IRONWIND`, `SRC-UNIT42-ASHTAG-2025`, `SRC-S1-ISRAEL-HAMAS-CYBER-2023`.
