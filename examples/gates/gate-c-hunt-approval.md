# Gate C: Hunt Approval Evidence Pack

Gate result: sample / hunt-ready only after local telemetry confirmation.

Scope: Identity-plane destructive activity and Intune remote wipe abuse.

Required evidence:

| Requirement | Evidence |
| --- | --- |
| Falsifiable hypothesis | Bulk destructive device action should appear in Intune/M365 audit logs from a privileged actor |
| Telemetry and fields identified | Entra ID AuditLogs, PIM, Intune device actions, M365 unified audit logs |
| Query scoped | `detections/kql/intune-bulk-device-wipe-anomaly.kql` |
| Closure criteria defined | No anomalous wipe/retire/delete actions or all actions mapped to approved change tickets |

Blockers:

- Needs tenant-specific privileged actor inventory.
- Needs normal administrative baseline for device lifecycle actions.

Owner: SOC Engineer.

Review date: 2026-05-14.
