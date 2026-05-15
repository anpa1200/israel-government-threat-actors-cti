---
title: Backend Conversion Results
sidebar_label: Backend Conversion Results
---

# Backend Conversion Results

Sigma conversion was run locally with temporary `sigma-cli` backends for Splunk
and Elasticsearch.

Run date: 2026-05-15

Commands:

```bash
sigma check detections/sigma/*.yml
sigma convert -t splunk -p splunk_windows detections/sigma/*.yml > detections/splunk/sigma-converted-splunk.spl
sigma convert -t lucene -p ecs_windows detections/sigma/*.yml > detections/elastic/sigma-converted-lucene.txt
```

Results:

| Backend | Output | Result | Notes |
| --- | --- | --- | --- |
| Sigma semantic check | `docs/detection-engineering/sigma-validation-results.md` | 0 errors, 0 condition errors, 0 issues | Validates Sigma syntax and metadata after tag cleanup. |
| Splunk SPL | `detections/splunk/sigma-converted-splunk.spl` | Generated | Requires local index, sourcetype, CIM, and field mapping before deployment. |
| Elastic Lucene / ECS Windows | `detections/elastic/sigma-converted-lucene.txt` | Generated | Requires ECS pipeline validation and index mapping before deployment. |

Interpretation:

- Conversion artifacts prove the portable Sigma rules can be rendered to target
  backend query languages.
- Conversion does not prove field correctness in a real SIEM.
- Converted queries are release artifacts for review and pilot design, not
  production analytics.
