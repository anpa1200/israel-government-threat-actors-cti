# APT42

Aliases: UNC788 (Mandiant), Yellow Garuda (Recorded Future), Damselfly (Symantec), CharmingCypress (Volexity), Educated Manticore (Check Point), ITG18 (IBM, overlapping with APT35).

Assessed sponsor: IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) per Mandiant, Proofpoint, and U.S. Treasury designations.

**Vendor naming caveat — TA453 and Charming Kitten:** Proofpoint (2023) and Volexity (2024) map TA453 as roughly equivalent to APT42, while MITRE ATT&CK G0059 retains TA453 under Magic Hound / APT35. "Charming Kitten" is used by some vendors for APT35 and others for APT42. Analysts MUST note which vendor taxonomy their source uses before attributing TA453 or Charming Kitten activity to either profile.

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

Sources: `SRC-MITRE-G1044`, `SRC-MANDIANT-APT42`, `SRC-GOOGLE-APT42-UNCHARMED`, `SRC-GOOGLE-APT42-PHISHING`, `SRC-GOOGLE-AI-MISUSE`, `SRC-GOOGLE-AI-TRACKER`, `SRC-PROOFPOINT-IRAN-CONFLICT-2026`.
