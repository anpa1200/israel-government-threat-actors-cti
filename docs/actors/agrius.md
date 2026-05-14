# Agrius

Aliases: Pink Sandstorm, AMERICIUM, Agonizing Serpens, BlackShadow.

Assessed sponsor: Iran-aligned (assessed by some sources as MOIS-linked; firm MOIS attribution not established in primary reporting). SentinelLabs, Unit 42, and Microsoft use "Iran-aligned" or "Iran-nexus" language without confirming a specific Iranian intelligence service. Use evidence label `Assessed-by-source` rather than `Source-reported` for any MOIS claim.

## Relevance

Agrius is high priority because public reporting links the actor to ransomware and wiper operations in the Middle East with emphasis on Israeli targets.

## Defensive Focus

- Destructive staging and wiper-like activity.
- Backup deletion or backup access abuse.
- Security tool tampering.
- Ransomware-style encryption and extortion cover stories.

## Detection Ideas

- Privileged account deleting or modifying backup policies.
- Endpoint protection service tampering followed by mass file operations.
- Unexpected use of tunneling or admin tools from non-admin workstations.

Sources: `SRC-MITRE-G1030`, `SRC-S1-AGRIUS-WIPER`, `SRC-S1-APOSTLE`, `SRC-UNIT42-AGRIUS`.
