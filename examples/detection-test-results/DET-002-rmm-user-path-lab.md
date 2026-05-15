# DET-002 Lab Test Result: Suspicious RMM Installer Download From User Context

Detection ID: `DET-002`

Rule artifacts:

- `detections/sigma/suspicious-rmm-file-sharing-download.yml`
- `detections/kql/suspicious-rmm-file-sharing-download.kql`

Test date: 2026-05-15

Test type: synthetic lab logic test.

Safety note: this file does not contain malware, live infrastructure, customer
telemetry, credentials, or executable payloads. Process names and paths are
benign synthetic examples used to validate detection logic boundaries.

## Objective

Validate that the detection concept distinguishes suspicious RMM execution from
user-controlled locations from approved administrative deployment paths.

## Positive Test

Synthetic event summary:

| Field | Value |
| --- | --- |
| Event type | Windows process creation |
| Parent process | Browser or mail client |
| Process path | User Downloads, Temp, or AppData path |
| Process name | RMM-like installer or remote-access binary name |
| Network behavior | External remote-access or file-sharing destination after execution |
| Expected result | Match |

Expected alert rationale:

- RMM-like executable is launched from a user-controlled path.
- Parent process is consistent with a download or phishing chain.
- Execution is not from an approved software distribution path.
- The pattern supports the `T1219` Remote Access Software mapping used by
  `DET-002`.

Result: pass as synthetic logic test.

## Negative Test

Synthetic event summary:

| Field | Value |
| --- | --- |
| Event type | Windows process creation |
| Parent process | Approved software deployment agent |
| Process path | Approved enterprise software distribution directory |
| Process name | Approved RMM binary in local allowlist |
| Network behavior | Approved management subnet or vendor tenant |
| Expected result | Suppress or tune out |

Expected benign rationale:

- Execution is initiated by an approved deployment system.
- Path and signer should match local RMM inventory.
- Network destination is expected for the organization's management plane.

Result: pass as synthetic negative-boundary test.

## False-Positive Classes

Expected benign sources:

- Approved IT remote-support deployments.
- Software distribution or endpoint-management agents.
- Helpdesk-initiated break/fix sessions.
- Vendor maintenance windows.
- Security tooling that bundles remote-control components.

Required local tuning:

- Approved RMM inventory.
- Approved signer list.
- Approved deployment paths.
- IT admin groups and service accounts.
- Management subnets and vendor tenant destinations.

## Promotion Impact

This evidence supports DRL-6 for the public repository because it demonstrates
positive and negative lab logic boundaries without relying on private telemetry.

It does not support DRL-7, DRL-8, or DRL-9. Promotion still requires:

- target-backend conversion result;
- historical replay against local EDR telemetry;
- false-positive rate measurement;
- SOC pilot review;
- production owner and rollback plan.
