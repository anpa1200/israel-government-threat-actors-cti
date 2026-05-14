# Gate D: Detection Design Approval Evidence Pack

Result: Sample / Partially ready.

## Scope

DET-001 through DET-004 in `examples/registers/detection-backlog.csv`.

## Required Evidence

| Requirement | Evidence |
| --- | --- |
| Scenario link | `scenario_id` is populated for every detection. |
| ATT&CK mapping | `attack_id` is populated for every detection. |
| Data source | `data_source` is populated for every detection. |
| Rule path | Sigma or KQL path is populated. |
| SOC action | `soc_action` field is populated. |

## Blockers

- DET-001 requires tenant replay testing before pilot.
- DET-003 requires local OT logsource mapping.
- DET-004 requires Defender XDR table validation.

