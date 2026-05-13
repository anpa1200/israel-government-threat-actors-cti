# Magic Hound / APT35

Aliases: Charming Kitten, TA453, COBALT ILLUSION, Phosphorus, Newscaster, Mint Sandstorm.

Assessed sponsor: Iran state-linked in public reporting.

## Relevance

APT35-related reporting is highly relevant to Israeli government because the actor family is associated with credential phishing, persona-based social engineering, and targeting of policy, defense, academia, media, and regional entities.

## Defensive Focus

- Fake login portals and domain impersonation.
- Spearphishing links and long-running social engineering.
- Mailbox access after credential theft.
- OAuth consent and MFA reset attempts.

## Detection Ideas

- New inbox rules after risky sign-in.
- MFA method registration after impossible travel or new device sign-in.
- Lookalike domains targeting ministries, public agencies, or suppliers.

Source: `SRC-MITRE-G0059`.

