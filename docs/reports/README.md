# Report Index

Use `data/sources.csv` as the authoritative machine-readable source register.

Use `sources/` as the analyst-facing scored source library:

- `sources/score-a-primary/` for high-reliability primary sources.
- `sources/score-b-supporting/` for supporting methodology, authored assessments, and secondary summaries.
- `sources/score-c-watchlist/` for claims and leads that require corroboration.

## Priority Report Categories

- Government advisories: CISA, FBI, NSA, INCD, CERT-IL, ENISA, NCSC.
- ATT&CK knowledge base: actor technique mappings and reference chains.
- Vendor CTI: Microsoft, Mandiant / Google Cloud, ESET, SentinelOne, Meta, Check Point Research, Palo Alto Unit 42, CrowdStrike, Recorded Future.
- Sector sources: WaterISAC, aviation, telecom, and government-sector information sharing groups.
- Authored Medium research from this project owner: [andrey-medium-articles.md](andrey-medium-articles.md).

## Collection Rules

- Reports SHOULD be stored as links unless redistribution is explicitly allowed.
- Analyst notes MAY summarize key findings, but MUST preserve original URL and publisher.
- IOC lists SHOULD be referenced by location rather than duplicated wholesale.
