---
title: Source Freshness
sidebar_label: Source Freshness
---

# Source Freshness

Source freshness keeps public CTI from silently aging into stale assumptions.

## Source Date Fields

`data/sources.csv` separates:

- `publication_date`: when the publisher released the source.
- `accessed_date`: when this repository last accessed the source.
- `source_last_updated`: when the publisher indicates the source changed, if
  known.
- `record_last_reviewed`: when this repository last reviewed the row.
- `archived_date`: when a local ignored archive copy was captured, if any.
- `archive_hash`: SHA-256 of the local ignored archive copy, if any.

## Review Cadence

| Source Type | Review Cadence | Reason |
| --- | --- | --- |
| Government advisory | 90 days | Advisories can be updated with new IOCs, mitigations, or attribution language. |
| MITRE ATT&CK page | 90 days | Group pages and technique references change over time. |
| Vendor CTI report | 180 days | Most technical details are stable, but links and IOCs age. |
| News or secondary synthesis | 90 days | Corrections and superseding primary reports are common. |
| Watchlist/persona claim | 30 days | Public claims decay quickly and require corroboration. |

## Promotion Rules

- A source MAY be Score A and still have individual low-confidence claims.
- A stale source SHOULD NOT be used for current operational blocking without
  freshness review.
- Local archive hashes support reproducibility, but the original publisher URL
  remains the citation target unless redistribution is explicitly permitted.
- If a primary source becomes available, replace secondary-only claims or
  downgrade the secondary source to context.
