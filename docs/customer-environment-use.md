---
title: Customer Environment Use
sidebar_label: Customer Environment Use
---

# Customer Environment Use

This page explains how to use the repository in a real SOC or consulting
engagement without overpromoting public research into production analytics.

## 1. Scope The Environment

Collect the minimum context before using any detection:

- protected sectors and assets;
- identity provider and endpoint platforms;
- SIEM backend and field names;
- approved remote-management tooling;
- OT/ICS ownership and remote-access paths;
- legal/comms owner for public persona claims.

## 2. Select A Scenario

Start from `examples/registers/threat-scenario-register.csv` and choose one
scenario. Do not deploy all detections at once.

For each scenario, record:

- decision owner;
- asset scope;
- expected telemetry;
- evidence IDs;
- current detection status;
- acceptance criteria for pilot.

## 3. Validate Telemetry

Before running a detection as an alert, verify:

- required tables exist;
- required fields are populated;
- time zone and ingestion delay are understood;
- service accounts and approved admin paths are known;
- benign baseline is available.

Use `docs/detection-engineering/platform-field-mapping.md` as the checklist.

## 4. Run As Hunt First

Run each detection as a hunt query first:

- review 14 to 30 days of historical data;
- capture true positives, false positives, and unknowns;
- document exclusions;
- preserve raw query output in the customer environment, not in this public repo;
- update the DRL evidence pack with non-sensitive summary metrics.

## 5. Pilot With SOC

Move to pilot only when:

- positive and negative tests are complete;
- false-positive classes are understood;
- SOC triage steps are written;
- owner and rollback procedure are assigned.

Pilot scope should be narrow: one tenant, one business unit, or one OT segment.

## 6. Promote Or Retire

Promote to production only at DRL-9. If the detection cannot be tuned to an
acceptable signal rate, keep it as a hunt or retire it.

Production evidence must include:

- backend-specific query;
- field mapping;
- positive test;
- negative test;
- historical replay;
- false-positive review;
- expected alert volume;
- SOC triage;
- owner;
- rollback plan.

## 7. Handle Persona Claims Separately

For Handala, Cyber Toufan, Karma, Homeland Justice, and similar personas, use
`examples/registers/persona-claims-register.csv`.

Do not confirm compromise from a public post alone. Corroborate with telemetry,
victim statement, or trusted third-party reporting.
