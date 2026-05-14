---
title: Artifact Contracts
sidebar_label: Artifact Contracts
---

# Artifact Contracts

Artifact contracts define the minimum fields required for reusable CTI, hunting, and detection-engineering outputs.

## PIR Register

A PIR row MUST include:

- `pir_id`
- `decision_owner`
- `decision`
- `question`
- `time_horizon`
- `status`
- `confidence_threshold`

## SIR Register

A SIR row MUST include:

- `sir_id`
- `pir_id`
- `question`
- `data_source`
- `evidence_type`
- `owner`
- `due_date`
- `status`

## Evidence Register

An evidence row MUST include:

- `evidence_id`
- `claim_id`
- `actor_id`
- `source_id`
- `claim`
- `source_quote_or_summary`
- `evidence_label`
- `source_reliability`
- `information_credibility`
- `analyst_confidence`
- `confidence_reason`
- `contradiction_or_gap`
- `notes`

## Persona Claims Register

A persona claim row MUST include:

- `claim_id`
- `persona`
- `claim_date`
- `claimed_victim`
- `claimed_sector`
- `claim_channel`
- `evidence_captured`
- `local_telemetry_match`
- `third_party_corroboration`
- `confidence`
- `recommended_comms_action`
- `legal_comms_owner`
- `status`
- `notes`

Persona claims MUST remain separate from evidence-backed intrusion claims. A
Telegram post, leak-site post, or public claim MAY trigger preservation and
triage, but it MUST NOT be promoted to confirmed compromise without telemetry,
victim statement, government advisory, or credible third-party technical
corroboration.

## Threat Scenario Register

A threat scenario row MUST include:

- `scenario_id`
- `pir_id`
- `actor_or_pattern`
- `asset_or_sector`
- `attack_path`
- `likelihood`
- `impact`
- `exposure`
- `detection_gap`
- `time_sensitivity`
- `priority_score`
- `status`

## Hunt Backlog

A hunt row MUST include:

- `hunt_id`
- `scenario_id`
- `hypothesis`
- `required_telemetry`
- `query_path`
- `expected_observable`
- `status`
- `owner`

## Detection Backlog

A detection row MUST include:

- `detection_id`
- `title`
- `scenario_id`
- `attack_id`
- `data_source`
- `drl`
- `rule_path`
- `test_status`
- `soc_action`
- `owner`
- `priority`
- `platform_field_mapping`
- `drl_evidence_pack`

## Gate Evidence Pack

A gate evidence pack MUST include:

- Gate result.
- Scope.
- Required evidence table.
- Blockers or explicit statement that no blockers remain.
- Approver or owner.
- Review date.

## Metrics Register

A metrics row MUST include:

- `metric_id`
- `metric_name`
- `scope`
- `value`
- `unit`
- `measurement_date`
- `owner`
- `notes`
