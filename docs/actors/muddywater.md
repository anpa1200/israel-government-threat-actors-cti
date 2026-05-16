# MuddyWater

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [MuddyWater](../navigation/actor-workbench.md#muddywater)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1566](../navigation/ttp-detection-matrix.md#t1566) Phishing (M2); [T1059.001](../navigation/ttp-detection-matrix.md#t1059001) PowerShell (M2); [T1219](../navigation/ttp-detection-matrix.md#t1219) Remote Access Software (M3); [T1567.002](../navigation/ttp-detection-matrix.md#t1567002) Exfiltration to Cloud Storage (M2)
- Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context (Pilot, DRL-6); [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MITRE-G0069` Technique references; `SRC-AP-MUDDYWATER` Malware/tool references; ATT&CK mappings; campaign IOCs; `SRC-THREAT-HUNTER-V3` Domains; IPs; Rclone destinations; Dindoor/Fakeset references; `SRC-INCD-MUDDYWATER-2024` Domains; hashes; tools; infrastructure; TTPs
- Malware and tools: [`Remote Monitoring and Management tools`](../tools/remote-monitoring-and-management-tools.md) (Living-off-the-land tooling); [`Dindoor`](../tools/dindoor.md) (Backdoor); [`Fakeset`](../tools/fakeset.md) (Backdoor); [`BugSleep`](../tools/bugsleep.md) (Backdoor); [`BlackBeard`](../tools/blackbeard.md) (Backdoor); [`Fooder / MuddyViper`](../tools/fooder-muddyviper.md) (Loader and backdoor)
- Tool behaviors and hash/IOC status: [tool intelligence matrix](../malware-tool-intelligence.md#muddywater) (6 mapped tool row(s))
- Tool detail pages: [`Remote Monitoring and Management tools`](../tools/remote-monitoring-and-management-tools.md); [`Dindoor`](../tools/dindoor.md); [`Fakeset`](../tools/fakeset.md); [`BugSleep`](../tools/bugsleep.md); [`BlackBeard`](../tools/blackbeard.md); [`Fooder / MuddyViper`](../tools/fooder-muddyviper.md)
- Evidence records: `EVD-004` / `CLM-MUDDYWATER-001`
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-AP-MUDDYWATER`, `SRC-CP-BUGSLEEP`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-MITRE-G0069`, `SRC-THREAT-HUNTER-V3`

<!-- ACTOR-NAVIGATION:END -->

Aliases: Mango Sandstorm, Boggy Serpens (Microsoft, current), Static Kitten, Seedworm, MERCURY (Microsoft, retired April 2023), TEMP.Zagros, TA450 (Proofpoint), Earth Vetala (Trend Micro).

Assessed sponsor: Iran MOIS-aligned in public reporting.

## Relevance

MuddyWater is high priority for Israeli government and regional public-sector defense because MITRE records targeting of government, local government, telecommunications, defense, and oil and gas organizations across the Middle East and other regions.

## Defensive Focus

- Spearphishing and malicious document delivery.
- PowerShell execution and script-based collection.
- Legitimate remote access tool abuse.
- Credential collection and lateral movement preparation.

## Detection Ideas

- RMM execution from user download folders.
- PowerShell encoded commands launched by Office, browser, archive, or script-host processes.
- New persistence from suspicious scheduled tasks or registry run keys.

Sources: `SRC-MITRE-G0069`, `SRC-CISA-AA22-055A`, `SRC-INCD-MUDDYWATER-2024`, `SRC-INCD-MUDDYWATER-PHISHING`, `SRC-ESET-MUDDYWATER-SNAKES`, `SRC-CP-BUGSLEEP`, `SRC-KASPERSKY-ICS-Q4-2025`, `SRC-BRANDEFENSE-MUDDYWATER-2025`, `SRC-AP-MUDDYWATER`.

Source note: Kaspersky ICS and Brandefense are Score B synthesis sources in this repository. Use them for collection planning and cross-checking, then anchor high-impact claims to ESET, INCD, CISA, MITRE, or Check Point.
