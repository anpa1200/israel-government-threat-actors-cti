---
title: SOC Handoff Packet
sidebar_label: SOC Handoff Packet
---

# SOC Handoff Packet

This packet models the handoff a detection engineer would give to a SOC lead for
pilot review. It is customer-style, but it does not contain customer telemetry.

## Scope

Detection: `DET-002` Suspicious RMM Installer Download From User Context

Release status: Pilot

Current DRL: DRL-6

Owner: Endpoint Engineer

SOC reviewer: SOC Lead

## Why This Matters

Iran-linked public reporting includes abuse of legitimate remote access and
management tooling after phishing or credential compromise. The detection hunts
for RMM-like execution from user-controlled paths where approved IT deployment
context is absent.

## Required Telemetry

- Windows process creation telemetry.
- Command line.
- Parent process.
- File path.
- User/account identity.
- Approved RMM inventory.
- Approved deployment paths and management subnets.

## Alert Criteria

Alert when all are true:

- command or process is associated with RMM download/execution;
- execution path or command line includes user-controlled locations;
- parent process is browser, mail client, shell, or script interpreter;
- event is not allowlisted as approved IT deployment.

## Immediate SOC Actions

1. Confirm whether the user or device belongs to IT or helpdesk.
2. Check whether the RMM tool is in the approved inventory.
3. Validate parent process and download source.
4. Review outbound network connections after execution.
5. Isolate host if RMM is unapproved and external connectivity is present.
6. Preserve command line, file hash, parent process, and network evidence.

## Expected False Positives

- Approved helpdesk support sessions.
- Endpoint-management deployment activity.
- Vendor maintenance windows.
- Security tooling with remote-control components.

## Tuning Inputs

- Approved RMM binary names and signers.
- Approved deployment paths.
- Approved management subnets.
- Helpdesk and IT admin groups.
- Change-management windows.

## Test Evidence

- Synthetic positive and negative tests:
  `examples/detection-test-results/synthetic-test-summary.md`.
- Synthetic 30-day replay substitute for `DET-002`:
  `examples/detection-test-results/synthetic-test-summary.md`.

## Pilot Exit Criteria

- Historical replay completed on at least 30 days of endpoint telemetry.
- False-positive rate measured and documented.
- Allowlist reviewed by endpoint engineering and SOC.
- Triage steps validated by at least one SOC analyst.
- Rollback plan approved.

## Rollback

If alert volume is too high, disable alerting and keep the query as a scheduled
hunt while tuning approved RMM inventory and deployment-path exclusions.
