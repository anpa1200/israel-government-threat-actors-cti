# DRL Evidence Pack: DET-004

Detection ID: DET-004

Detection title: Mail Click To Execution Correlation

Target platform: Microsoft Defender XDR / Sentinel email, identity, and endpoint telemetry

Current DRL: DRL-4

Target DRL: DRL-6 after Defender XDR table validation; DRL-7 after VIP pilot.

## Source And Claim Traceability

| Field | Value |
| --- | --- |
| Source IDs | `SRC-GOOGLE-APT42-PHISHING`, `SRC-INCD-MUDDYWATER-PHISHING` |
| Evidence IDs | `EVD-003`, `EVD-004` |
| Scenario ID | `SCN-004` |
| Hunt ID | `HUNT-004` |
| ATT&CK technique | `T1566` Phishing |
| Mapping quality | M3 candidate. Query links click activity to endpoint or identity follow-on behavior; M4 requires test evidence. |

## Rule Artifact

| Field | Value |
| --- | --- |
| Rule path | `detections/kql/mail-click-to-exec-correlation.kql` |
| Backend conversion result | Not applicable for KQL. Target Defender XDR table validation is pending. |
| Query version / commit | Record release commit before VIP pilot. |

## Test Evidence

| Requirement | Result | Evidence Location |
| --- | --- | --- |
| Positive test | Synthetic fixture test completed for security-themed mail click followed by executable launch from Downloads within 30 minutes. | `examples/detection-test-results/synthetic-test-summary.md` |
| Negative test | Synthetic fixture test completed for approved SaaS click with no endpoint execution. | `examples/detection-test-results/synthetic-test-summary.md` |
| Historical replay | Not run. | Run against 14 days of VIP click, sign-in, and endpoint telemetry. |
| False-positive review | Synthetic false-positive rate is 0.00% over one benign fixture; no Defender XDR environment false-positive rate measured. | `examples/detection-test-results/synthetic-test-summary.md`; SOC review required for business SaaS links, training simulations, and partner portals. |

## Operations

| Field | Value |
| --- | --- |
| Expected alert volume | Medium before exclusions in high-click VIP populations; low to medium after phishing simulation and sanctioned SaaS exclusions. |
| Tuning guidance | Exclude approved phishing simulations, sanctioned SaaS portals, partner portals, and normal browser-only sign-ins. Keep click-to-script, click-to-archive, click-to-new-country-sign-in, and click-to-AitM indicators visible. |
| SOC triage steps | Preserve message headers, URL click chain, sign-in logs, endpoint process tree, downloaded files, and target-user role context. Disable malicious URLs and revoke suspicious sessions when identity evidence is present. |
| Owner | SOC Analyst |
| Review date | 2026-05-15 |
| Rollback plan | Run as scheduled hunt instead of alert if baseline noise is high; keep click and endpoint telemetry enabled. |

## Approval

Gate result: Hunt starter only.

Approver: Pending SOC lead.

Remaining blockers:

- Validate table names and joins in Defender XDR.
- Run positive and negative tests in Defender XDR or Sentinel.
- Complete 14-day VIP historical replay.
- Document alert volume and false-positive exclusions.
