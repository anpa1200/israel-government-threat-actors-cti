# Review guide: Public-source CTI and detection evidence

Andrey Pautov organizes public-source actor/tool research into source registers, confidence notes, ATT&CK mappings, worked cases and defensive detection examples. Attribution claims originate in cited reporting and require source review; they are not independent proof of state sponsorship.

## Architecture and contribution

Source registers → actor/TTP/tool mappings → hunt and detection candidates → synthetic evidence packs and quality gates → documentation site.

Role relevance: CTI research, source evaluation, hypothesis design, detection evidence and stakeholder delivery.

## Safe reproducible quickstart

Run from the repository root. Python 3; no extra packages or service credentials required.

```bash
python3 scripts/validate_repo.py
python3 scripts/run_detection_fixture_tests.py
```

Expected result:

```text
Repository validator completes successfully; DET-001 through DET-004 report fixture comparisons with no mismatches. See validation.md for the exact retained output.
```

These commands use committed or generated benign/synthetic input. They do not execute malware, invoke a hosted provider, scan a target or require credentials.

## Evidence to inspect

[Worked cases](docs/reports/worked-cases.md) · [Known limitations](docs/known-limitations.md)



## Validation and limitations

The fixture runner exercises Python approximations of detection conditions, not the actual KQL/Sigma rules in a SIEM. Its synthetic_30d_replay line copies expected aggregate values from JSON and is not an executed 30-day replay. Public reporting may become stale; review cited sources before relying on attribution.

See [validation.md](validation.md) for checks performed on the exact source snapshot, verified results and capabilities not run. Existing release/CI claims remain historical repository statements, not fresh certification.

Preserve the full [README](README.md) and original technical documentation for installation, deployment and capability details.
