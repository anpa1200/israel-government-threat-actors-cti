# Local validation evidence

Date: 2026-10-01. The reviewed changes were applied to public `main` at `705cfb6fc46892182c9c4507e13bf6c386f3b6ef` in an isolated clone. Checks below distinguish local editorial evidence from broader application and release validation.

| Check | Status | Scope |
|---|---|---|
| `python3 scripts/validate_repo.py` | Verified: exit 0 | Offline benign/synthetic or help check only |
| `python3 scripts/run_detection_fixture_tests.py` | Verified: exit 0 | Offline benign/synthetic or help check only |
| Broader capabilities | Not run | SIEM queries, Sigma translation, feed fetching, live attribution/source verification and website build not run. Printed 30-day aggregate is expected fixture metadata, not measured event processing. |

## Retained output

```text
$ python3 scripts/validate_repo.py
Repository validation passed
```

```text
$ python3 scripts/run_detection_fixture_tests.py
DET-001: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-002: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-003: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-004: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-002 synthetic_30d_replay: benign_events=240 malicious_seeded_events=2 alerts=2 false_positives=0 synthetic_fp_rate=0.00%
```

The four detector rows compare 24 synthetic cases (2 positive and 4 negative cases per detector). The zero synthetic false-positive rate applies only to those tiny fixtures. The final `synthetic_30d_replay` line is read from expected JSON values; no 30-day events are replayed. The Python predicates do not validate deployed KQL/Sigma semantics.
