# Scored Source Library

This folder organizes source material by reliability score so analysts can quickly decide which references are suitable for executive claims, detection logic, attribution notes, or watchlist monitoring.

## Score Model

| Folder | Score | Use |
| --- | --- | --- |
| `score-a-primary/` | A | Government advisories, MITRE ATT&CK, and primary vendor CTI reports. Suitable for control decisions and detection engineering after local validation. |
| `score-b-supporting/` | B | Author analysis, reputable secondary reporting, think tank reports, and vendor summaries. Suitable for context and hypothesis building. |
| `score-c-watchlist/` | C | Monitoring leads, persona claims, and lower-confidence items that require corroboration before operational use. |

## Required Practice

- A source score rates source reliability, not whether every analytic judgment in the source is true.
- Actor attribution MUST still be evaluated at the claim level.
- IOCs from any score SHOULD be tested for recency and local relevance before blocking.

