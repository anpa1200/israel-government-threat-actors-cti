# Agrius

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [Agrius](../navigation/actor-workbench.md#agrius)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Destructive Operations, Backup Deletion, And Wipers](../navigation/surface-capability-matrix.md#destructive-operations)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1485](../navigation/ttp-detection-matrix.md#t1485) Data Destruction (M2); [T1486](../navigation/ttp-detection-matrix.md#t1486) Data Encrypted for Impact (M2)
- Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly (Hunt, DRL-5)
- Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs
- IOC reference sources: `SRC-MITRE-G1030` Technique references
- Malware and tools: [`Moneybird`](../tools/moneybird.md) (Ransomware / destructive malware); [`BlackShadow`](../tools/blackshadow.md) (Ransomware / persona)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#agrius) (2 mapped tool row(s))
- Tool detail pages: [`Moneybird`](../tools/moneybird.md); [`BlackShadow`](../tools/blackshadow.md)
- Evidence records: `EVD-017` / `CLM-AGRIUS-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-MITRE-G1030`

<!-- ACTOR-NAVIGATION:END -->

Aliases: Pink Sandstorm, AMERICIUM, Agonizing Serpens, BlackShadow.

Assessed sponsor: Iran-aligned (assessed by some sources as MOIS-linked; firm MOIS attribution not established in primary reporting). SentinelLabs, Unit 42, and Microsoft use "Iran-aligned" or "Iran-nexus" language without confirming a specific Iranian intelligence service. Use evidence label `Assessed-by-source` rather than `Source-reported` for any MOIS claim.

## Relevance

Agrius is high priority because public reporting links the actor to ransomware and wiper operations in the Middle East with emphasis on Israeli targets.

## Defensive Focus

- Destructive staging and wiper-like activity.
- Backup deletion or backup access abuse.
- Security tool tampering.
- Ransomware-style encryption and extortion cover stories.

## Detection Ideas

- Privileged account deleting or modifying backup policies.
- Endpoint protection service tampering followed by mass file operations.
- Unexpected use of tunneling or admin tools from non-admin workstations.

Sources: `SRC-MITRE-G1030`, `SRC-S1-AGRIUS-WIPER`, `SRC-S1-APOSTLE`, `SRC-UNIT42-AGRIUS`, `SRC-ISRAELHAYOM-ZIV-2023`, `SRC-TOI-ZIV-2023`, `SRC-CENTRIPETAL-PREPOSITIONED-2025`, `SRC-ANVILOGIC-IRAN-CI-2026`.

Source note: Ziv Hospital and camera/BDA-related claims are not promoted here as high-confidence Agrius facts. Treat the news and supporting vendor sources as context until primary INCD/IDF/ISA or source telemetry is available.
