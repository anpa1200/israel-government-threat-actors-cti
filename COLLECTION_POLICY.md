# Collection Policy

## Allowed

- Public CTI reports from reputable vendors, governments, CERTs, ISACs, and research teams.
- Public ATT&CK mappings, YARA/Sigma/KQL/Splunk detections, and defensive analytics.
- IOC references, hashes, domains, IPs, and URLs when they are already published for defensive use.
- Malware family names, tool names, behavior summaries, and reverse-engineering summaries.

## Prohibited

- Malware binaries, droppers, payloads, loaders, or weaponized scripts.
- Leaked data, credentials, session tokens, private keys, or victim PII.
- Instructions that materially enable unauthorized access or evasion.
- Unverified claims copied from social media without source reliability notes.

## Source Handling

Every source SHOULD be recorded in `data/sources.csv` with publisher, publication date, URL, reliability rating, and notes. Actor claims SHOULD be traceable to at least one source record.

