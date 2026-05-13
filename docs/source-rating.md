# Source Rating

The repository uses a compact source reliability model.

| Rating | Meaning | Examples |
| --- | --- | --- |
| A | Highly reliable source with strong technical or institutional credibility | Government advisories, MITRE ATT&CK, primary vendor CTI reports |
| B | Usually reliable, but may summarize another primary source | Security news, secondary technical summaries |
| C | Mixed reliability or limited detail | Blog summaries, conference slides without appendix |
| D | Unverified public claim | Social media posts, Telegram claims, unattributed leak claims |

Information credibility is tracked in free text as `High`, `Medium`, `Low`, or combined values such as `Medium-High`.

## Required Practice

- Public claims by hacktivist personas MUST be corroborated before being treated as confirmed compromise.
- Vendor actor names SHOULD be mapped carefully because naming taxonomies differ.
- Source publication date MUST be considered when using IOCs.

