---
title: Platform Query Variants
sidebar_label: Platform Query Variants
---

# Platform Query Variants

This page tracks platform-specific query status. The goal is to separate
portable detection logic from backend-specific deployment artifacts.

## Current Status

| Detection | Sentinel / Defender XDR | Splunk | Elastic | Status |
| --- | --- | --- | --- | --- |
| `DET-001` Intune Bulk Device Wipe Anomaly | KQL exists: `detections/kql/intune-bulk-device-wipe-anomaly.kql` | Not committed | Not committed | Hunt |
| `DET-002` Suspicious RMM Installer Download From User Context | KQL exists: `detections/kql/suspicious-rmm-file-sharing-download.kql` | Converted output exists in `detections/splunk/sigma-converted-splunk.spl` | Converted output exists in `detections/elastic/sigma-converted-lucene.txt` | Pilot |
| `DET-003` Unitronics PLC HMI Web Interface Access | Sigma source exists | Converted output exists in `detections/splunk/sigma-converted-splunk.spl` | Converted output exists in `detections/elastic/sigma-converted-lucene.txt` | Hunt |
| `DET-004` Mail Click To Execution Correlation | KQL exists: `detections/kql/mail-click-to-exec-correlation.kql` | Not committed | Not committed | Hunt |

## Validation Standard

A platform variant is considered validated only when all of the following are
committed:

- backend-specific query;
- source rule or analytic ID;
- field mapping;
- positive test output;
- negative test output;
- historical or representative benign replay;
- measured alert volume or false-positive rate;
- SOC triage and rollback procedure.

The current KQL and Sigma artifacts are suitable for hunt planning and pilot
design. They are not production variants.
