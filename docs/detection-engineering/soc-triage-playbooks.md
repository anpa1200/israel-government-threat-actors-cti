---
title: SOC Triage Playbooks
sidebar_label: SOC Triage Playbooks
---

# SOC Triage Playbooks

These playbooks define first-response actions for the repository's highest-risk
hunt patterns. They are not a substitute for local incident-response procedure.

## Identity-Plane Destruction

Relevant actors and personas: Void Manticore / Handala-style destructive
operations, destructive ransomware masquerade, and cloud-admin abuse.

Primary evidence: `EVD-005`, `EVD-006`.

Required telemetry:

- Entra ID sign-in and audit logs.
- PIM activation logs.
- Intune device action logs.
- Microsoft 365 unified audit logs.
- Backup control-plane logs.

Triage steps:

1. Confirm whether the privileged actor is expected for the tenant and time
   window.
2. Preserve all role activation, MFA method, Conditional Access, Intune wipe,
   retire, delete, and backup-policy events.
3. Freeze or revoke suspicious privileged sessions.
4. Disable further destructive device actions until ownership is confirmed.
5. Notify identity, endpoint, legal, and communications owners if public claims
   are involved.

Escalate when:

- more than one destructive device action is initiated by a newly elevated or
  recently changed account;
- MFA methods or Conditional Access settings changed shortly before destructive
  actions;
- backup policy or recovery controls changed in the same window.

## Edge Access To Destructive Handoff

Relevant actors: UNC1860, Scarred Manticore, Void Manticore / Handala.

Primary evidence: `EVD-006`, `EVD-007`, `EVD-008`.

Required telemetry:

- WAF and web server logs.
- EDR process, image load, and file creation telemetry.
- IIS configuration and module registration history.
- Authentication and remote-service logs.
- Backup and recovery-control logs.

Triage steps:

1. Identify the first external-facing server touched in the intrusion window.
2. Preserve webroot, IIS module, service-control, and suspicious DLL artifacts.
3. Check for passive webshell or listener behavior before assuming outbound C2.
4. Correlate edge compromise with later RDP, service-account, backup deletion,
   or wiper-preparation activity.
5. Treat destructive staging after edge persistence as a separate escalation
   even if attribution remains unresolved.

Escalate when:

- web exploitation is followed by new webshell/native-module persistence;
- a public-facing host becomes a pivot point for internal RDP or admin shares;
- destructive or recovery-inhibition commands appear after the access phase.

## OT / PLC Exposure

Relevant actors: CyberAv3ngers and related IRGC-CEC OT targeting.

Primary evidence: `EVD-002`, `EVD-009`.

Required telemetry:

- Internet exposure inventory.
- Firewall and remote-access logs.
- PLC/HMI web logs where available.
- OT engineering workstation logs.
- Configuration backup and controller change records.

Triage steps:

1. Determine whether the PLC/HMI is internet-accessible.
2. Confirm vendor, model, firmware, password state, and remote-access path.
3. Preserve network logs for OT ports and web-management access.
4. Compare current controller/HMI configuration to a trusted backup.
5. Coordinate with OT owner before rebooting or changing controller state.

Escalate when:

- internet-origin traffic touches PLC/HMI management services;
- default credentials, exposed web UI, or unapproved remote engineering access
  are present;
- HMI content, PLC parameter, or controller communication settings change
  unexpectedly.
