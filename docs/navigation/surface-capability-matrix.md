---
title: Surface And Capability Matrix
sidebar_label: Surface Matrix
---

# Surface And Capability Matrix

Use this page when the starting point is not an actor name. Pick the exposed surface or defender capability, then route to the relevant actors, hunts, detections, and telemetry fields.

## Identity, MDM, And Cloud Administration {#identity-mdm}

Capability route: Find privileged identity abuse, destructive device actions, risky MFA changes, and OAuth or session persistence.

Relevant actors: [Void Manticore / Handala](../actors/handala.md); [APT42](../actors/apt42.md); [Magic Hound](../actors/apt35.md); [Pioneer Kitten](../actors/pioneer-kitten.md)

Mapped detections: [DET-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) Intune Bulk Device Wipe Anomaly; [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation

Mapped hunts: [HUNT-001](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/intune-bulk-device-wipe-anomaly.kql) If identity-plane destructive tradecraft is attempted then privileged role activation or bulk device actions will appear in audit logs; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution

Required telemetry fields: AuditLogs; CloudAppEvents; Entra ID sign-in logs; Intune audit logs; TargetResources; InitiatedBy; OperationName.

## Endpoint RMM, Scripting, And User-Path Execution {#endpoint-rmm}

Capability route: Hunt unauthorized RMM, script execution, signed installer abuse, and phishing-to-execution chains.

Relevant actors: [MuddyWater](../actors/muddywater.md); [OilRig](../actors/oilrig.md); [APT42](../actors/apt42.md); [Imperial Kitten](../actors/imperial-kitten.md); [TA402](../actors/ta402.md); [WIRTE](../actors/wirte.md)

Mapped detections: [DET-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/suspicious-rmm-file-sharing-download.yml) Suspicious RMM Installer Download From User Context; [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation

Mapped hunts: [HUNT-002](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/suspicious-rmm-file-sharing-download.kql) If MuddyWater-style RMM abuse is active then unauthorized RMM execution will appear from user-controlled paths; [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution

Required telemetry fields: DeviceProcessEvents; DeviceFileEvents; FolderPath; ProcessCommandLine; Parent process; RemoteUrl; approved RMM inventory.

## OT, PLC, HMI, And Exposed Engineering Interfaces {#ot-plc}

Capability route: Route exposed industrial interfaces to responsible asset owners and relevant IRGC-aligned actor profiles.

Relevant actors: [CyberAv3ngers](../actors/cyberav3ngers.md); [Cyber Toufan](../actors/cyber-toufan.md); [Lyceum](../actors/lyceum.md); [UNC1860](../actors/unc1860.md)

Mapped detections: [DET-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) Unitronics PLC HMI Web Interface Access

Mapped hunts: [HUNT-003](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/sigma/unitronics-plc-hmi-web-access.yml) If exposed PLC/HMI surfaces are targeted then OT management paths or ports will show external access

Required telemetry fields: Firewall; proxy; OT NDR; VPN; URL; UserAgent; DestinationPort; AssetOwner; approved vendor remote access.

## Internet-Facing Servers, Webshells, And Passive Access {#edge-webshell}

Capability route: Pivot from exploited edge services to webshell, IIS module, passive backdoor, and handoff-risk guidance.

Relevant actors: [UNC1860](../actors/unc1860.md); [Scarred Manticore](../actors/scarred-manticore.md); [OilRig](../actors/oilrig.md); [Lebanese Cedar](../actors/lebanese-cedar.md); [Pioneer Kitten](../actors/pioneer-kitten.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Required telemetry fields: Web server logs; IIS configuration; appcmd activity; EDR module loads; file writes under web roots and inetsrv paths.

## Destructive Operations, Backup Deletion, And Wipers {#destructive-operations}

Capability route: Connect destructive personas and wiper tradecraft to VSS, backup, and mass file-operation hunts.

Relevant actors: [Void Manticore / Handala](../actors/handala.md); [Agrius](../actors/agrius.md); [DarkBit](../actors/darkbit.md); [Cyber Toufan](../actors/cyber-toufan.md)

Mapped detections: None currently mapped.

Mapped hunts: None currently mapped.

Required telemetry fields: Process creation; service control events; file rename/write telemetry; backup admin logs; cloud backup configuration logs.

## Email, Cloud-Service, IMAP, And DNS C2 {#email-c2-dns}

Capability route: Connect cloud-service C2, IMAPLoader behavior, DNS tunneling, and mail-driven intrusion chains.

Relevant actors: [Imperial Kitten](../actors/imperial-kitten.md); [OilRig](../actors/oilrig.md); [MuddyWater](../actors/muddywater.md); [APT42](../actors/apt42.md)

Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation

Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution

Required telemetry fields: DNS logs; proxy logs; IMAP/IMAPS egress; process network connections; mail click logs; cloud storage access logs.
