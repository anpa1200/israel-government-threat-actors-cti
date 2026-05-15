# Replay Datasets

These datasets are synthetic, lab-realistic samples for safe replay and parser
testing. They are not customer telemetry and must not be treated as production
false-positive evidence.

The datasets are intentionally small enough for review in Git and contain no
malware, credentials, victim data, or live infrastructure.

| Dataset | Detection | Purpose |
| --- | --- | --- |
| `det-001-intune-auditlogs.csv` | `DET-001` | Intune destructive action threshold testing. |
| `det-002-windows-process-events.csv` | `DET-002` | RMM execution from user-controlled path testing. |
| `det-003-ot-web-access.csv` | `DET-003` | Unitronics PLC/HMI path and user-agent testing. |
| `det-004-mail-click-exec.csv` | `DET-004` | Mail-click-to-execution correlation testing. |
