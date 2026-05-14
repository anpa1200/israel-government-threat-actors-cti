# Sample Registers

These CSV files operationalize the CTI-to-detection workflow:

- `pir-register.csv`
- `sir-register.csv`
- `evidence-register.csv`
- `persona-claims-register.csv`
- `threat-scenario-register.csv`
- `hunt-backlog.csv`
- `detection-backlog.csv`
- `detection-health-register.csv`
- `metrics.csv`

Use them as starter templates for real engagements. Replace sample owners, due dates, and assumptions with environment-specific values before operational use.

`persona-claims-register.csv` is specifically for public hacktivist or persona
claims. It MUST NOT be treated as a confirmed-compromise register. Use it to
separate claim capture, local telemetry review, third-party corroboration,
confidence, communications action, and legal/comms ownership.

`metrics.csv` tracks whether the repository is improving as an engineering
system, not only growing as a source collection.
