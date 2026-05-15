# DRL Evidence Pack: DET-001

Detection ID: DET-001

Detection title: Intune Bulk Device Wipe Anomaly

Target platform: Microsoft Sentinel / Defender XDR tenant audit telemetry

Current DRL: DRL-5

Target DRL: DRL-7 before pilot use; DRL-9 only after production approval.

## Source And Claim Traceability

| Field | Value |
| --- | --- |
| Source IDs | `SRC-MITRE-G1055`, `SRC-CP-VOID-2024` |
| Evidence IDs | `EVD-005`, `EVD-006` |
| Scenario ID | `SCN-001` |
| Hunt ID | `HUNT-001` |
| ATT&CK technique | `T1485` Data Destruction |
| Mapping quality | M3 candidate after tenant field mapping; not M4 until replay evidence is captured. |

## Rule Artifact

| Field | Value |
| --- | --- |
| Rule path | `detections/kql/intune-bulk-device-wipe-anomaly.kql` |
| Companion rule | `detections/sigma/intune-bulk-device-wipe-anomaly.yml` is a base event selector only. |
| Backend conversion result | Not applicable for KQL. Sigma semantic validation is covered by repository validation, but production backend conversion is not claimed. |
| Query version / commit | Record release commit before tenant pilot. |

## Test Evidence

| Requirement | Result | Evidence Location |
| --- | --- | --- |
| Positive test | Defined, not executed. Requires replay or controlled lab generation of multiple Intune wipe, retire, or delete actions by a non-automation privileged identity. | Local tenant test evidence required before DRL-7. |
| Negative test | Defined, not executed. Requires approved device lifecycle activity by known MDM automation or service desk account. | Local tenant test evidence required before DRL-7. |
| Historical replay | Not run. | Export query results and alert volume from at least 30 days of tenant audit logs. |
| False-positive review | Not run. | SOC and endpoint-management owner review required. |

## Operations

| Field | Value |
| --- | --- |
| Expected alert volume | Low in normal environments after service-desk and automation accounts are allowlisted. Unknown until tenant replay. |
| Tuning guidance | Allowlist approved MDM lifecycle automation, approved service desk groups, break-glass test accounts, and documented maintenance windows. Keep all emergency or mass wipe actions visible to SOC. |
| SOC triage steps | Use `docs/detection-engineering/soc-triage-playbooks.md`, section `Identity-Plane Destruction`. Preserve privileged role activation, MFA, Conditional Access, Intune action, and backup-control events. |
| Owner | SOC Engineer |
| Review date | 2026-05-15 |
| Rollback plan | Disable alert rule or lower severity while preserving raw audit collection. Do not disable tenant audit logging. |

## Approval

Gate result: Not production approved.

Approver: Pending SOC and identity owner.

Remaining blockers:

- Confirm exact tenant table and field names for Intune destructive actions.
- Run positive and negative tests in a controlled tenant.
- Complete 30-day historical replay.
- Document expected alert volume and false-positive classes.
- Assign production owner and rollback plan before DRL-9.
