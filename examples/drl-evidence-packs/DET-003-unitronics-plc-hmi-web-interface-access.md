# DRL Evidence Pack: DET-003

Detection ID: DET-003

Detection title: Unitronics PLC HMI Web Interface Access

Target platform: Web/proxy/firewall/OT NDR logs

Current DRL: DRL-4

Target DRL: DRL-6 after local field mapping and benign validation; DRL-8 after monitored OT pilot.

## Source And Claim Traceability

| Field | Value |
| --- | --- |
| Source IDs | `SRC-CISA-AA23-335A`, `SRC-CISA-AA26-097A` |
| Evidence IDs | `EVD-002`, `EVD-009` |
| Scenario ID | `SCN-003` |
| Hunt ID | `HUNT-003` |
| ATT&CK technique | `T1190` Exploit Public-Facing Application |
| Mapping quality | M3 candidate for web-path detection; M4 requires local OT telemetry and test evidence. |

## Rule Artifact

| Field | Value |
| --- | --- |
| Rule path | `detections/sigma/unitronics-plc-hmi-web-access.yml` |
| Backend conversion result | Sigma structure passes repository validation; backend field mapping is not yet confirmed. |
| Query version / commit | Record release commit before OT pilot. |

## Test Evidence

| Requirement | Result | Evidence Location |
| --- | --- | --- |
| Positive test | Not run. Requires controlled access to lab or approved test PLC/HMI web interface path from an untrusted source segment. | OT lab or approved replay dataset required. |
| Negative test | Not run. Requires approved vendor remote session through VPN/jump host. | OT owner-approved test required. |
| Historical replay | Not run. | Review 30 days of firewall/proxy/OT NDR telemetry for public access to PLC/HMI services. |
| False-positive review | Not run. | OT owner and network engineering review required. |

## Operations

| Field | Value |
| --- | --- |
| Expected alert volume | Should be near zero for direct public access. Any internet-origin PLC/HMI management access is high-risk even if benign. |
| Tuning guidance | Exclude approved VPN concentrators, jump hosts, vendor maintenance windows, and monitoring scanners. Do not exclude direct internet-origin access without written OT owner approval. |
| SOC triage steps | Use `docs/detection-engineering/soc-triage-playbooks.md`, section `OT / PLC Exposure`. Preserve network logs, identify vendor/model/firmware, and compare controller/HMI configuration to trusted backup. |
| Owner | OT Security Lead |
| Review date | 2026-05-15 |
| Rollback plan | Convert to exposure-reporting mode while preserving OT perimeter logging. Coordinate any blocking with OT owner. |

## Approval

Gate result: Hunt starter only.

Approver: Pending OT owner.

Remaining blockers:

- Confirm available logsource and normalized fields.
- Validate Unitronics path matching in the local proxy/firewall/OT NDR backend.
- Run benign vendor-session negative test.
- Define OT escalation and change-control procedure before pilot.
