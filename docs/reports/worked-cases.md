---
title: Worked Cases
sidebar_label: Worked Cases
---

# Worked Cases

These worked cases show how the repository expects analysts to move from public
reporting to defensive action without overstating attribution or detection
readiness.

## Case 1: MuddyWater Phishing To RMM / Backdoor Access

Source set:

- `SRC-INCD-MUDDYWATER-2024`
- `SRC-INCD-MUDDYWATER-PHISHING`
- `SRC-CP-BUGSLEEP`
- `SRC-ESET-MUDDYWATER-SNAKES`
- `SRC-KASPERSKY-ICS-Q4-2025` as supporting synthesis

Claim discipline:

- Evidence IDs: `EVD-004`.
- Evidence labels: source-reported for INCD campaign claims; assessed-by-source
  for actor attribution; gap for unverified secondary-only tooling details.

Scenario:

An Israeli public-sector user receives a credible phishing message from a
trusted or compromised sender. The initial access chain leads to RMM execution,
custom backdoor deployment, or cloud-service staging.

Observable chain:

1. Email delivery from trusted or newly compromised sender.
2. URL click or attachment open.
3. Script, archive, or installer execution from user-controlled paths.
4. RMM binary, PowerShell, or backdoor execution.
5. Cloud or proxy-based C2/staging.

Required telemetry:

- Email gateway and click telemetry.
- EDR process and file events.
- DNS/proxy logs.
- Identity sign-in logs.
- Approved RMM inventory.

Hunt and detection links:

- `detections/kql/mail-click-to-exec-correlation.kql`
- `detections/kql/suspicious-rmm-file-sharing-download.kql`
- `detections/sigma/suspicious-rmm-file-sharing-download.yml`

Mapping-quality decision:

Generic MuddyWater phishing and PowerShell rows are M2 unless tied to a concrete
query and telemetry contract. RMM execution can become M3 only where the rule
logic and approved-tool allowlist are documented.

SOC action:

Validate sender history, isolate the endpoint if unauthorized RMM is confirmed,
preserve email and endpoint evidence, and rotate credentials for the affected
user and any accounts touched by the process tree.

## Case 2: Scarred Manticore Access To Void Manticore Destructive Handoff

Source set:

- `SRC-CP-SCARRED-MANTICORE-2023`
- `SRC-CP-VOID-2024`
- `SRC-MANDIANT-UNC1860`
- `SRC-MITRE-G1055`

Claim discipline:

- Evidence IDs: `EVD-005`, `EVD-006`, `EVD-007`, `EVD-008`.
- Keep UNC1860, Scarred Manticore, and Void Manticore distinct unless a source
  explicitly links them for the incident.

Scenario:

An internet-facing web server is compromised and receives passive backdoor or
webshell persistence. Later, a second operational phase performs destructive
staging, recovery inhibition, or public leak/claim activity.

Observable chain:

1. Public-facing web application exploitation.
2. Webroot, IIS, or module-level persistence.
3. Passive listener behavior or webshell access.
4. Internal remote services or valid-account use.
5. Backup deletion, mass file operations, or public persona claim.

Required telemetry:

- WAF, IIS, webroot file integrity, Sysmon/EDR file and image-load telemetry.
- Authentication logs and RDP/service events.
- Backup and shadow-copy command telemetry.
- Persona-claims register for public claim handling.

Hunt and detection links:

- `detections/sigma/exchange-webshell-post-exploitation.yml`
- `detections/sigma/vss-backup-deletion-chain.yml`
- `detections/sigma/liontail-system32-dll-service-load.yml`

Mapping-quality decision:

IIS/native-module mappings stay M2 until a rule specifically detects module
registration or HTTP.sys/Liontail behavior. Generic webshell and VSS deletion
rules can be M3 when rule logic is explicitly linked.

SOC action:

Preserve server images and logs before cleanup, scope internal pivots, freeze
privileged accounts used after the edge compromise, and coordinate public-claim
review through the persona-claims workflow.

## Case 3: CyberAv3ngers OT / PLC Exposure

Source set:

- `SRC-CISA-AA23-335A`
- `SRC-CISA-AA26-097A`
- `SRC-CLAROTY-IOCONTROL-2024`

Claim discipline:

- Evidence IDs: `EVD-002`, `EVD-009`.
- Use ATT&CK for ICS where the observable is PLC/HMI or control-process
  specific.

Scenario:

An internet-exposed PLC, HMI, or engineering interface is accessed by external
infrastructure. The actor may deface the HMI, alter parameters, or abuse weak
remote access.

Observable chain:

1. PLC/HMI management surface exposed to the internet.
2. External access to OT management paths or OT ports.
3. Authentication using default or weak credentials.
4. HMI manipulation, parameter modification, or unexpected communication
   settings.
5. Public defacement or claim.

Required telemetry:

- External attack-surface inventory.
- Firewall and VPN logs.
- OT network flows.
- PLC/HMI web logs where available.
- Engineering workstation and configuration-backup records.

Hunt and detection links:

- `detections/sigma/unitronics-plc-hmi-web-access.yml`

Mapping-quality decision:

Internet-accessible device and HMI manipulation mappings remain M2 until local
OT telemetry and test evidence prove the observable. Production coverage needs
site-specific field mapping and an OT owner-approved response plan.

SOC action:

Remove direct internet exposure, rotate credentials, preserve OT network logs,
compare controller/HMI configuration to trusted backup, and involve OT owners
before making controller-state changes.
