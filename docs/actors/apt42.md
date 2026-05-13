# APT42

Aliases: APT42; some reporting discusses overlap with Charming Kitten / Magic Hound taxonomies.

Assessed sponsor: Iran-sponsored in public reporting.

## Relevance

APT42 is high priority because MITRE and Mandiant describe cyber espionage and surveillance operations focused on the Middle East, including spearphishing, cloud collection, and custom tooling.

## Defensive Focus

- Spearphishing and cloud-hosted lure delivery.
- Credential theft from browsers and cloud services.
- Microsoft 365 data collection.
- HTTPS-based command and control using custom tools.

## Detection Ideas

- Risky sign-in followed by cloud file access burst.
- Browser credential store access from unusual processes.
- New OAuth grants or suspicious cloud application consent.

Sources: `SRC-MITRE-G1044`, `SRC-MANDIANT-APT42`, `SRC-GOOGLE-APT42-UNCHARMED`, `SRC-GOOGLE-APT42-PHISHING`, `SRC-GOOGLE-AI-MISUSE`, `SRC-GOOGLE-AI-TRACKER`.
