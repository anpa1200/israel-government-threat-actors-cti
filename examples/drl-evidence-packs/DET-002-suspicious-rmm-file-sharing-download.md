# DRL Evidence Pack: DET-002

Detection ID: DET-002

Detection title: Suspicious RMM Installer Download From User Context

Target platform: Windows EDR process, file, and network telemetry

Current DRL: DRL-6

Target DRL: DRL-7 after pilot deployment and SOC review.

## Source And Claim Traceability

| Field | Value |
| --- | --- |
| Source IDs | `SRC-INCD-MUDDYWATER-PHISHING` |
| Evidence IDs | `EVD-004` |
| Scenario ID | `SCN-002` |
| Hunt ID | `HUNT-002` |
| ATT&CK technique | `T1219` Remote Access Software |
| Mapping quality | M3. Rule logic is tied to unauthorized RMM execution from user-controlled paths. M4 requires committed test output. |

## Rule Artifact

| Field | Value |
| --- | --- |
| Rule path | `detections/sigma/suspicious-rmm-file-sharing-download.yml` |
| Companion query | `detections/kql/suspicious-rmm-file-sharing-download.kql` |
| Backend conversion result | Sigma structure passes repository validation; backend conversion to target SIEM not yet recorded. |
| Query version / commit | Record release commit before pilot. |

## Test Evidence

| Requirement | Result | Evidence Location |
| --- | --- | --- |
| Positive test | Lab command-line simulation completed with benign RMM-like filenames and user-path execution. | Commit-level validation noted in detection backlog; raw test artifact not yet committed. |
| Negative test | Defined, not committed. Requires approved RMM deployment from software distribution paths and IT admin context. | Local EDR replay required. |
| Historical replay | Not run. | Run against 30 days of EDR telemetry with approved RMM inventory joined. |
| False-positive review | Partial. Approved RMM false-positive category is documented, but environment-specific allowlist is not committed. | SOC and endpoint engineering review required. |

## Operations

| Field | Value |
| --- | --- |
| Expected alert volume | Medium before tuning; low after approved tools, deployment shares, IT admin groups, and management subnets are allowlisted. |
| Tuning guidance | Maintain an approved RMM inventory. Exclude only signed approved binaries from approved deployment paths and expected parent processes. Do not suppress user Downloads, Temp, or AppData execution globally. |
| SOC triage steps | Confirm business approval, parent process, download source, user path, outbound connection, persistence artifacts, and whether the host belongs to an IT admin group. |
| Owner | Endpoint Engineer |
| Review date | 2026-05-15 |
| Rollback plan | Convert from alert to hunt-only mode if approved RMM noise is high; keep telemetry collection active. |

## Approval

Gate result: Pilot candidate, not production approved.

Approver: Pending endpoint engineering and SOC owner.

Remaining blockers:

- Commit positive and negative test outputs.
- Add target-backend conversion result.
- Complete historical replay with approved RMM inventory.
- Document alert-volume estimate and tuned false-positive examples.
