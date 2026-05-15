# Detection Test Results

This directory stores committed detection test evidence that is safe for public
release. Test records here are synthetic or lab-derived unless explicitly stated
otherwise.

Do not store customer telemetry, victim data, credentials, malware, exploit
artifacts, or sensitive operational logs.

Current coverage:

| Detection | Evidence | Scope |
| --- | --- | --- |
| `DET-001` | `synthetic-fixtures.json`, `synthetic-test-summary.md` | Synthetic positive and negative tests for Intune bulk wipe threshold logic. |
| `DET-002` | `DET-002-rmm-user-path-lab.md` | Synthetic positive and negative test cases for RMM execution path logic. |
| `DET-002` | `synthetic-fixtures.json`, `synthetic-test-summary.md` | Synthetic 30-day replay substitute and false-positive measurement. |
| `DET-003` | `synthetic-fixtures.json`, `synthetic-test-summary.md` | Synthetic positive and negative tests for Unitronics web path and user-agent matching. |
| `DET-004` | `synthetic-fixtures.json`, `synthetic-test-summary.md` | Synthetic positive and negative tests for mail-click-to-execution correlation. |
