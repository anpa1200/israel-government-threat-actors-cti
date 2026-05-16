---
title: Platform Field Mapping
sidebar_label: Platform Field Mapping
---

# Platform Field Mapping

This page defines the minimum field mapping needed before a hunt starter can be
treated as a platform-specific analytic. It is intentionally conservative: a
query is not production-ready just because a concept exists in Sigma or KQL.

## Microsoft Defender XDR / Sentinel

| Use Case | Primary Tables | Required Fields |
| --- | --- | --- |
| Mail click to execution | `EmailEvents`, `UrlClickEvents`, `DeviceProcessEvents`, `SigninLogs` | `Timestamp` / `TimeGenerated`, `RecipientEmailAddress`, `Url`, `AccountUpn`, `DeviceName`, `FileName`, `ProcessCommandLine`, `InitiatingProcessFileName` |
| RMM abuse | `DeviceProcessEvents`, `DeviceFileEvents`, `DeviceNetworkEvents` | `DeviceName`, `FileName`, `FolderPath`, `ProcessCommandLine`, `InitiatingProcessFileName`, `RemoteUrl`, `RemoteIP` |
| Identity-plane destruction | `AuditLogs`, `CloudAppEvents`, Intune audit tables where available | `OperationName`, `InitiatedBy`, `TargetResources`, `Result`, `IPAddress`, `UserAgent` |
| DNS tunneling | `DeviceEvents`, DNS server logs, resolver logs | `DnsQueryName`, `DnsQueryType`, `DeviceName`, `InitiatingProcessFileName`, `RemoteUrl`, query count |

## Splunk

| Use Case | Likely Index / Sourcetype | Required Fields |
| --- | --- | --- |
| Windows process rules | Sysmon, Windows Security, EDR sourcetypes | `process_name`, `process`, `parent_process_name`, `dest`, `user`, `signature_status` |
| Webshell post-exploitation | IIS, Exchange, EDR, web proxy | `cs_uri_stem`, `cs_user_agent`, `process_name`, `parent_process_name`, `file_path`, `src_ip` |
| OT exposure | Firewall, proxy, OT NDR | `src_ip`, `dest_ip`, `dest_port`, `url`, `action`, `asset_owner` |

## Elastic

| Use Case | ECS Fields |
| --- | --- |
| Process execution | `process.name`, `process.command_line`, `process.parent.name`, `host.name`, `user.name` |
| Network connection | `destination.ip`, `destination.port`, `dns.question.name`, `url.domain`, `process.name` |
| File changes | `file.path`, `file.name`, `event.action`, `process.name`, `host.name` |

## Promotion Requirements

Before moving from hunt starter to pilot:

- confirm the table/index exists in the target environment;
- confirm all required fields are populated;
- define environment-specific allowlists;
- run one positive test or replay;
- run one negative test or benign baseline review;
- record the result in the detection health register.

## Cross-Links

- [Detection Lifecycle](detection-lifecycle.md)
- [Detection Status Dashboard](detection-status-dashboard.md)
- [CTI Analyst Field Manual — Telemetry Requirements](https://anpa1200.github.io/cti-analyst-field-manual/docs/08-cti-to-detection/telemetry-requirements) — field-level tables for Windows Security Event Log, Sysmon, EDR, DNS, proxy, identity provider, and cloud audit logs
- [CTI Analyst Field Manual — Sigma/KQL/SPL Examples](https://anpa1200.github.io/cti-analyst-field-manual/docs/08-cti-to-detection/sigma-kql-spl-examples) — two DRL-4 detection candidates with Sigma, KQL (MDE), and SPL (Sysmon) variants
- [CTI Analyst Field Manual — Detection Readiness Levels](https://anpa1200.github.io/cti-analyst-field-manual/docs/08-cti-to-detection/detection-readiness-levels) — DRL model that promotion requirements reference

## References

- [Sigma Documentation](https://sigmahq.io/docs/)
- [Microsoft Advanced Hunting Schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)
- [MITRE ATT&CK Data Sources](https://attack.mitre.org/datasources/)
