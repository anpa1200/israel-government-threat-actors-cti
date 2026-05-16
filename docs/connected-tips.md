---
title: Connected TIPs And CTI Feeds
sidebar_label: Connected TIPs
---

# Connected TIPs And CTI Feeds

This framework now has a feed-intake layer for open-source/free CTI updates.
The connectors create review candidates, not finished intelligence records.

## Connected Without API Keys

| Feed | Type | What It Adds | How To Use |
| --- | --- | --- | --- |
| MITRE ATT&CK Enterprise STIX | STIX bundle | Actor taxonomy, aliases, ATT&CK group modified dates, and drift signals. | Review actor alias and technique changes before updating `data/actors.csv` or `data/ttps.csv`. |
| CISA Known Exploited Vulnerabilities | JSON catalog | Exposure-prioritization leads for edge, identity, remote-access, and OT products. | Route to the [Surface And Capability Matrix](navigation/surface-capability-matrix.md); do not infer actor attribution from KEV alone. |
| CISA Cybersecurity Advisories RSS | RSS | New government advisory leads for ICS, edge, cloud, and critical-infrastructure surfaces. | Add a normal source/evidence record before promoting an advisory into actor, hunt, or detection content. |

## Optional TIP Connectors

| Platform | Status | Required Secret | Notes |
| --- | --- | --- | --- |
| AlienVault OTX | Implemented for subscribed pulses | `OTX_API_KEY` | Pulls matching subscribed pulses when configured. Commit reviewed summaries only, not raw private pulse dumps. |
| VirusTotal | Implemented for hash enrichment candidates | `VT_API_KEY` | Enriches reviewed hash seeds in `data/virustotal-hash-seeds.csv`. Commit only summary rows in `data/virustotal-enrichment-candidates.csv`; never commit API keys, raw JSON, private telemetry, downloaded samples, or VT-only attribution. |
| MISP | Connector target documented | `MISP_API_KEY` plus trusted instance URL | Requires a trusted MISP instance and local policy for event tags, distribution, and confidence handling. |
| OpenCTI | Connector target documented | `OPENCTI_TOKEN` plus trusted instance URL | Requires a trusted OpenCTI instance and local policy for marking definitions and source reliability. |

## Commands

Run a local feed pull:

```bash
npm run intel:update
```

Run a local VirusTotal enrichment pass:

```bash
VT_API_KEY=... npm run intel:vt
```

The command updates:

- `data/intel-update-candidates.csv`
- `docs/intelligence-updates.md`

The VirusTotal command updates:

- `data/virustotal-enrichment-candidates.csv`
- [VirusTotal Malware Enrichment](virustotal-enrichment.md)

## GitHub Actions

The `Intel Update Check` workflow runs on a weekday schedule and can be started
manually. It uploads the generated update queue as an artifact. It does not
auto-commit or auto-promote feed data.

## Promotion Workflow

1. Review the candidate in [Intelligence Update Queue](intelligence-updates.md).
2. Open the source URL and verify the claim.
3. Decide whether the item is actor-specific, surface-specific, or only context.
4. Add or update `data/sources.csv` if the source should become a repository source.
5. Add or update `examples/registers/evidence-register.csv` for claim-backed content.
6. Update actor pages, TTP mappings, hunts, detections, or surface routes only after source/evidence review.
7. Regenerate navigation with `npm run validate`.

## Guardrails

- Feed hits are leads, not confirmed incidents.
- KEV entries prove known exploitation in the wild, not use by a specific actor.
- OTX/MISP/OpenCTI enrichment can be noisy and must be source-rated.
- VirusTotal verdicts are enrichment only. They do not prove actor attribution, and a not-found result is not a benign verdict.
- Do not commit API keys, private feeds, restricted reports, raw malware, leaked data, or victim telemetry.
- Keep the repo boundary: public-source, defensive, `TLP:CLEAR`.
