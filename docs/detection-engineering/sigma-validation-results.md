---
title: Sigma Validation Results
sidebar_label: Sigma Validation Results
---

# Sigma Validation Results

Sigma semantic validation was run locally with `sigma-cli` against all rules in
`detections/sigma/`.

Run date: 2026-05-15

Command:

```bash
sigma check detections/sigma/*.yml
```

Result:

```text
Parsing Sigma rules
Checking Sigma rules

=== Summary ===
Found 0 errors, 0 condition errors and 0 issues.
No rule errors found.
No condition errors found.
No validation issues found.
```

Interpretation:

- The public Sigma rules parse and pass Sigma CLI semantic checks.
- This is not the same as backend conversion or production deployment.
- Backend-specific conversion and field mapping are still required before
  deployment to Splunk, Elastic, Sentinel, or another SIEM.

Known remaining work:

- Add committed conversion output for target backends.
- Add backend-specific field mappings for each production candidate.
- Add real benign replay and false-positive measurements per backend.
