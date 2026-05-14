---
title: Worked Cases
sidebar_label: Worked Cases
---

# Worked Cases

These worked cases show how the repository expects analysts to move from public
reporting to defensive action without overstating attribution or detection
readiness. They are still examples: each one needs local telemetry, owner
approval, and DRL evidence before production use.

## Case 1: MuddyWater Phishing To RMM / BugSleep / Fooder / MuddyViper

### Source Claim

Public reporting by INCD, Check Point, and ESET supports MuddyWater relevance to
Israeli cyber-domain defense through phishing, tooling evolution, backdoor use,
and critical-infrastructure targeting.

Source set:

- `SRC-INCD-MUDDYWATER-2024`
- `SRC-INCD-MUDDYWATER-PHISHING`
- `SRC-CP-BUGSLEEP`
- `SRC-ESET-MUDDYWATER-SNAKES`
- `SRC-KASPERSKY-ICS-Q4-2025` as supporting synthesis

Evidence IDs:

- `EVD-004`

Actor confidence:

- High for MuddyWater as an Israeli-relevant actor.
- Moderate for any single incident until local telemetry links the source claim
  to the environment.

### PIR / SIR

PIR:

- `PIR-002`: approve near-term threat-hunting sprint.

SIRs:

- `SIR-003`: identify approved and unauthorized RMM tools.
- Additional SIR required: identify which trusted senders recently delivered
  executable, archive, script, or cloud-link lures.

### Scenario Score

Scenario:

- `SCN-002`

Priority score:

- 19

Reason:

- Likelihood 4, impact 4, exposure 4, detection gap 3, time sensitivity 4.

### ATT&CK Mapping

Relevant mappings:

- `G0069 / T1566 / Phishing / M2`
- `G0069 / T1059.001 / PowerShell / M2`
- `G0069 / T1219 / Remote Access Software / M3`

Mapping rationale:

- Phishing and PowerShell remain M2 because they are broad actor behaviors.
- RMM abuse can be treated as M3 when tied to the repository's process-path and
  approved-tool inventory logic.

### Observable Chain

1. Email delivery from trusted or newly compromised sender.
2. URL click or attachment open.
3. Script, archive, or installer execution from user-controlled paths.
4. RMM binary, PowerShell, BugSleep, Fooder, MuddyViper, or other backdoor
   execution.
5. Cloud, proxy, or RMM service communication.

### Required Telemetry

- Email gateway and URL-click telemetry.
- EDR process and file events.
- DNS/proxy logs.
- Identity sign-in logs.
- Approved RMM inventory.

Required fields:

- `RecipientEmailAddress`, `SenderFromAddress`, `Url`, `Timestamp`.
- `DeviceName`, `FileName`, `FolderPath`, `ProcessCommandLine`.
- `InitiatingProcessFileName`, `RemoteUrl`, `RemoteIP`.

### Hunt Query / Detection Rule

Hunts:

- `HUNT-002`
- `HUNT-004`

Rules:

- `detections/kql/mail-click-to-exec-correlation.kql`
- `detections/kql/suspicious-rmm-file-sharing-download.kql`
- `detections/sigma/suspicious-rmm-file-sharing-download.yml`

Detection IDs:

- `DET-002`
- supporting correlation: `DET-004`

### Test Plan

Positive test:

- Execute an approved benign RMM installer from a user-controlled test path in a
  lab tenant and confirm the rule detects the path/parent-process behavior.

Negative test:

- Execute the same approved RMM from the enterprise software-distribution path
  and confirm the allowlist suppresses the event.

Replay / pilot:

- Replay 14 days of EDR process telemetry and compare hits against approved RMM
  inventory and helpdesk deployment tickets.

### SOC Triage

1. Confirm whether the RMM binary is approved and expected on that host.
2. Review parent process, user, source path, and network destination.
3. Preserve email, URL-click, process, file, and network evidence.
4. Isolate host if RMM is unauthorized and remote session is active.
5. Rotate credentials for the affected user and any accounts touched by the
   process tree.

### DRL Level

Current DRL:

- `DET-002`: DRL-6.
- `DET-004`: DRL-4.

Target DRL:

- DRL-7 after historical replay and false-positive review.
- DRL-9 only after pilot, owner approval, SOC triage, and rollback plan.

### Residual Gaps

- Need local approved-RMM inventory.
- Need customer-specific mail and EDR table names.
- Need positive and negative test outputs committed to a DRL evidence pack.
- Need source-specific separation of BugSleep, Fooder, and MuddyViper claims.

## Case 2: Scarred Manticore / UNC1860 Access To Void Manticore Destructive Scenario

### Source Claim

Check Point and Mandiant reporting support a model in which Iranian access and
persistence clusters can support later destructive activity, but incident-level
handoff attribution must remain source-specific and cautious.

Source set:

- `SRC-CP-SCARRED-MANTICORE-2023`
- `SRC-CP-VOID-2024`
- `SRC-MANDIANT-UNC1860`
- `SRC-MITRE-G1055`

Evidence IDs:

- `EVD-005`
- `EVD-006`
- `EVD-007`
- `EVD-008`

Actor confidence:

- High for Scarred Manticore and UNC1860 as access/persistence concerns.
- High for Void Manticore as destructive persona/cluster context.
- Moderate for any specific handoff until telemetry and primary reporting link
  the phases.

### PIR / SIR

PIR:

- `PIR-001`: prioritize identity and MDM protection.
- `PIR-002`: approve near-term threat-hunting sprint.

SIRs:

- `SIR-001`: identify sources describing identity-plane destructive tradecraft.
- Additional SIR required: identify internet-facing IIS, SharePoint, Exchange,
  and edge applications with incomplete file-integrity coverage.

### Scenario Score

Related scenario:

- `SCN-001` for destructive identity-plane actions.

Recommended additional scenario:

- `SCN-005`: edge access to destructive handoff.

Suggested score:

- Likelihood 3, impact 5, exposure 4, detection gap 4, time sensitivity 5.
- Priority score 21.

### ATT&CK Mapping

Relevant mappings:

- `SCARREDMANTICORE / T1190 / Exploit Public-Facing Application / M2`
- `SCARREDMANTICORE / T1505.004 / IIS Components / M2`
- `SCARREDMANTICORE / T1505.003 / Web Shell / M2`
- `HANDALA / T1485 / Data Destruction / M2`
- `HANDALA / T1490 / Inhibit System Recovery / M2`

Mapping rationale:

- IIS/native-module mappings remain M2 until a rule specifically detects module
  registration, HTTP.sys listener behavior, or a tested Liontail-like artifact.
- VSS and backup deletion detections can become M3 when tied to rule logic and
  command telemetry.

### Observable Chain

1. Public-facing web application exploitation.
2. Webroot, IIS, SharePoint, or module-level persistence.
3. Passive listener behavior or webshell access.
4. Internal RDP, service-account, or valid-account activity.
5. Backup deletion, recovery inhibition, mass file operations, or public claim.

### Required Telemetry

- WAF and reverse-proxy logs.
- IIS, Exchange, SharePoint, and webroot file-integrity logs.
- EDR process, file, and image-load telemetry.
- Authentication, RDP, and service-control logs.
- Backup, VSS, and shadow-copy command telemetry.
- Persona-claims register.

Required fields:

- `cs_uri_stem`, `cs_user_agent`, `src_ip`, `dest_ip`.
- `FileName`, `FolderPath`, `ProcessCommandLine`, `ParentImage`.
- `AccountName`, `LogonType`, `SourceNetworkAddress`.
- `OperationName`, `TargetResources`, `InitiatedBy`.

### Hunt Query / Detection Rule

Hunts:

- `HUNT-001` for destructive identity-plane activity.
- New hunt required: edge-to-destruction correlation.

Rules:

- `detections/sigma/exchange-webshell-post-exploitation.yml`
- `detections/sigma/vss-backup-deletion-chain.yml`
- `detections/sigma/liontail-system32-dll-service-load.yml`

Detection IDs:

- `DET-001` for identity-plane destructive actions.
- New detection required for IIS/native-module integrity.

### Test Plan

Positive test:

- In a lab IIS host, create a benign test module or controlled webroot file
  change and confirm file-integrity/image-load telemetry is collected.
- Execute benign `vssadmin` and `wmic shadowcopy` test commands in an isolated
  lab and confirm the VSS rule fires.

Negative test:

- Run approved IIS patching or module installation and confirm the allowlist
  prevents expected maintenance from becoming high severity.
- Run backup-administration scripts during approved maintenance and document
  expected false positives.

Replay / pilot:

- Replay 30 days of webroot file changes and backup-control commands across
  internet-facing servers.

### SOC Triage

1. Preserve server image, web logs, webroot, IIS configuration, and EDR history.
2. Identify whether persistence is webshell, native module, service hijack, or
   another mechanism.
3. Scope internal pivots through RDP, SMB, service accounts, and admin shares.
4. Freeze suspicious privileged sessions.
5. Correlate any public persona claim in `persona-claims-register.csv` with
   telemetry before making external statements.

### DRL Level

Current DRL:

- Identity-plane destructive detection: DRL-5.
- Webshell and VSS rules: hunt/prototype level unless locally tested.

Target DRL:

- DRL-7 after web/IIS baseline replay and command telemetry tests.
- DRL-9 after pilot, false-positive tuning, and SOC approval.

### Residual Gaps

- Need IIS/native-module-specific rule that aligns better with Liontail.
- Need local baseline of legitimate IIS modules and service DLL loads.
- Need incident-level handoff evidence before asserting Scarred Manticore to
  Void Manticore continuity.
- Need persona-claim legal/comms workflow tested in tabletop exercise.

## Case 3: CyberAv3ngers OT / PLC Exposure

### Source Claim

CISA joint advisories and Claroty reporting support CyberAv3ngers / IRGC-CEC
relevance to exposed PLC/HMI and OT/IoT defense.

Source set:

- `SRC-CISA-AA23-335A`
- `SRC-CISA-AA26-097A`
- `SRC-CLAROTY-IOCONTROL-2024`

Evidence IDs:

- `EVD-002`
- `EVD-009`

Actor confidence:

- High for CyberAv3ngers / IRGC-CEC relevance to exposed OT assets.
- Moderate for any local incident until asset logs and configuration evidence
  confirm targeting or manipulation.

### PIR / SIR

PIR:

- `PIR-003`: reduce exposed OT management risk.

SIR:

- `SIR-004`: identify which PLC/HMI interfaces are internet exposed.

### Scenario Score

Scenario:

- `SCN-003`

Priority score:

- 22

Reason:

- Likelihood 4, impact 5, exposure 5, detection gap 3, time sensitivity 5.

### ATT&CK Mapping

Relevant mappings:

- `CYBERAV3NGERS / T0883 / Internet Accessible Device / M2`
- `CYBERAV3NGERS / T0836 / Modify Parameter / M2`
- `CYBERAV3NGERS / T0832 / Manipulation of View / M2`

Mapping rationale:

- These remain M2 until a site has OT telemetry, known asset inventory, and test
  evidence for the observable. Use ATT&CK for ICS for PLC/HMI effects.

### Observable Chain

1. PLC/HMI management surface exposed to the internet.
2. External access to OT management paths or OT ports.
3. Authentication using default or weak credentials.
4. HMI manipulation, parameter modification, or unexpected communication
   settings.
5. Public defacement or claim.

### Required Telemetry

- External attack-surface inventory.
- Firewall and VPN logs.
- OT network flows.
- PLC/HMI web logs where available.
- Engineering workstation logs.
- Controller configuration backups.

Required fields:

- `src_ip`, `dest_ip`, `dest_port`, `protocol`, `action`.
- `url`, `user_agent`, `asset_owner`, `device_model`.
- `engineering_workstation`, `project_file`, `configuration_hash`.

### Hunt Query / Detection Rule

Hunt:

- `HUNT-003`

Rule:

- `detections/sigma/unitronics-plc-hmi-web-access.yml`

Detection ID:

- `DET-003`

### Test Plan

Positive test:

- In a lab or approved OT test segment, generate controlled access to known
  Unitronics/Rockwell management paths or OT ports and confirm firewall/proxy/OT
  logs contain required fields.

Negative test:

- Confirm approved vendor access through VPN/jump host is excluded while direct
  internet-origin access remains visible.

Replay / pilot:

- Review 30 days of firewall and external attack-surface data for direct PLC/HMI
  exposure.

### SOC Triage

1. Determine whether the asset is directly internet-accessible.
2. Confirm vendor, model, firmware, password state, and remote-access path.
3. Preserve OT network logs and controller/HMI configuration state.
4. Compare current configuration to trusted backup.
5. Involve OT owner before rebooting, changing state, or blocking traffic that
   may affect operations.

### DRL Level

Current DRL:

- `DET-003`: DRL-4.

Target DRL:

- DRL-6 after local field mapping and benign access validation.
- DRL-8 after pilot in monitored OT segment.
- DRL-9 only after OT owner approval, response plan, and rollback procedure.

### Residual Gaps

- Need site-specific OT asset inventory.
- Need approved vendor remote-access list.
- Need controller/HMI configuration backup process.
- Need safety-reviewed response playbook before automated blocking.
