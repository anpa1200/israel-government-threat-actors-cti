# Synthetic Detection Test Summary

Generated from `scripts/run_detection_fixture_tests.py` using
`examples/detection-test-results/synthetic-fixtures.json`.

Run date: 2026-05-15

Scope: deterministic synthetic fixture tests. These are not customer telemetry,
not production replay, and not DRL-9 evidence.

```text
DET-001: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-002: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-003: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-004: TP=2 FP=0 TN=4 FN=0 synthetic_fp_rate=0.00%
DET-002 synthetic_30d_replay: benign_events=240 malicious_seeded_events=2 alerts=2 false_positives=0 synthetic_fp_rate=0.00%
```

Interpretation:

- The committed rule logic boundaries behave as expected against synthetic
  positive and negative fixtures.
- `DET-002` has a synthetic 30-day replay substitute with 240 benign events and
  two seeded malicious events.
- These results support lab/replay confidence only. They do not measure a real
  customer false-positive rate.

Remaining validation required:

- tenant or customer historical replay;
- backend-specific query conversion and execution;
- SOC pilot review;
- measured production-like alert volume;
- owner approval and rollback plan.
