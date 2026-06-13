---
description: "APT42 is an IRGC-IO-attributed surveillance cluster targeting journalists, civil society, government officials, and foreign policy researchers via persona-based social engineering and credential theft."
head:
  - tag: script
    attributes:
      type: application/ld+json
    innerHTML: '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is APT42?","acceptedAnswer":{"@type":"Answer","text":"APT42 is an IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) attributed surveillance cluster formally separated from APT35 by Mandiant in 2022. The group targets journalists, civil society activists, dual nationals, foreign government officials, and academics with interest to the IRGC. APT42 is known for cloud-focused credential theft via fake Google and Microsoft login portals, trojanized software packages, and long-duration persona-based social engineering. Also known as UNC788 (Mandiant), CharmingCypress (Volexity), and Yellow Garuda (Recorded Future)."}},{"@type":"Question","name":"How to detect APT42 credential theft campaigns?","acceptedAnswer":{"@type":"Answer","text":"Key APT42 detection approaches: detect risky sign-in events (impossible travel, new device, anonymizing IP) followed by immediate cloud file access bursts in M365 or Google Workspace; monitor for new OAuth application consent grants following sign-in events; watch for inbox rule creation immediately after first credential use; detect MFA device registration from a new device following suspicious authentication; monitor for browser credential store access from non-browser processes."}},{"@type":"Question","name":"What tools and techniques does APT42 use?","acceptedAnswer":{"@type":"Answer","text":"APT42's primary techniques are persona-based social engineering and credential theft via fake login portals. When malware is needed, the group uses POWERPOST, NICECURL, and TAMECAT (documented in Mandiant's 2022 APT42 report). Google TAG documented APT42 deploying trojanized legitimate software packages including NordVPN and Cisco AnyConnect installers. The group also abuses legitimate cloud services (Google Drive, OneDrive, Dropbox) for data exfiltration after credential theft."}}]}'
---

# APT42

<!-- ACTOR-NAVIGATION:START -->
## Repository Navigation

- Actor workbench: [APT42](../navigation/actor-workbench.md#apt42)
- TTP-to-detection matrix: [all mapped techniques](../navigation/ttp-detection-matrix.md)
- Surface and capability routes: [Identity, MDM, And Cloud Administration](../navigation/surface-capability-matrix.md#identity-mdm); [Endpoint RMM, Scripting, And User-Path Execution](../navigation/surface-capability-matrix.md#endpoint-rmm); [Email, Cloud-Service, IMAP, And DNS C2](../navigation/surface-capability-matrix.md#email-c2-dns)
- Detection status: [dashboard](../detection-engineering/detection-status-dashboard.md)
- Hunt workflow: [hunt workflow](../threat-hunting/hunt-workflow.md)
- ATT&CK mappings: [T1530](../navigation/ttp-detection-matrix.md#t1530) Data from Cloud Storage (M1); [T1102](../navigation/ttp-detection-matrix.md#t1102) Web Service (M1); [T1566.002](../navigation/ttp-detection-matrix.md#t1566002) Spearphishing Link (M3)
- Mapped detections: [DET-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) Mail Click To Execution Correlation (Hunt, DRL-4)
- Mapped hunts: [HUNT-004](https://github.com/anpa1200/israel-government-threat-actors-cti/blob/main/detections/kql/mail-click-to-exec-correlation.kql) If VIP phishing is active then mail click events will correlate to risky sign-in or execution
- IOC reference sources: `SRC-MANDIANT-APT42` Domains; malware hashes; infrastructure; `SRC-PROOFPOINT-IRAN-CONFLICT-2026` Phishing infrastructure; lure domains; campaign indicators
- Tool detail pages: [`POWERPOST`](../tools/powerpost.md); [`NICECURL`](../tools/nicecurl.md); [`TAMECAT`](../tools/tamecat.md)
- Tool matrix: [all actor-linked tools](../malware-tool-intelligence.md#apt42) (3 mapped tool row(s))
- Evidence records: `EVD-003` / `CLM-APT42-001`; `EVD-016` / `CLM-APT42-002`
- Imported research intakes: None currently mapped.
- Intel update candidates: [1 current candidate(s)](../intelligence-updates.md#actor-update-candidates)
- Source IDs in structured data: `SRC-GOOGLE-APT42-PHISHING`, `SRC-MANDIANT-APT42`, `SRC-MITRE-G1044`, `SRC-PROOFPOINT-IRAN-CONFLICT-2026`

<!-- ACTOR-NAVIGATION:END -->

## Background

APT42 was designated as a distinct cluster by Mandiant in 2022, formally separating it from the broader APT35/Magic Hound ecosystem it overlaps with. Like APT35, the group is attributed to the IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) by Mandiant, Proofpoint, and U.S. Treasury OFAC. APT42's primary mandate is domestic and international surveillance — targeting Iranian civil society, dual nationals, journalists, opposition figures, and foreign governments with interest to the IRGC.

The group's technical signature is cloud-focused credential theft and collection. Rather than heavy custom malware deployment, APT42 typically builds elaborate social engineering relationships, delivers spearphishing links to fake Google/Microsoft/OneDrive login portals, and then immediately harvests cloud-service credentials for persistent access. Once inside M365 or Google Workspace, the group focuses on email exfiltration and SharePoint/Drive data collection. Mandiant's 2022 comprehensive APT42 report documented tools including POWERPOST, NICECURL, and TAMECAT, used in campaigns where credential theft alone was insufficient.

Google's Threat Analysis Group documented APT42 extensively through the "Uncharmed" 2023 report and a 2024 blog post on targeting of US presidential campaigns — both Google-authenticated sources that establish the group's scale and methodology. Notably, Google TAG observed APT42 using trojanized legitimate software packages (NordVPN, Cisco AnyConnect) to deliver malware while maintaining plausible deniability.

In an Israel-specific context, Check Point's "Educated Manticore" reporting describes campaigns targeting Israeli academic and policy research environments with credential-phishing lures themed around regional conferences and public policy events — a pattern consistent with APT42's mandate to surveil individuals with access to strategic information.

Aliases: UNC788 (Mandiant), Yellow Garuda (Recorded Future), Damselfly (Symantec), CharmingCypress (Volexity), Educated Manticore (Check Point), ITG18 (IBM, overlapping with APT35).

Assessed sponsor: IRGC-IO (Islamic Revolutionary Guard Corps Intelligence Organisation) per Mandiant, Proofpoint, and U.S. Treasury designations.

**Vendor naming caveat — TA453 and Charming Kitten:** Proofpoint (2023) and Volexity (2024) map TA453 as roughly equivalent to APT42, while MITRE ATT&CK G0059 retains TA453 under Magic Hound / APT35. "Charming Kitten" is used by some vendors for APT35 and others for APT42. Analysts MUST note which vendor taxonomy their source uses before attributing TA453 or Charming Kitten activity to either profile. See the [APT35 profile](./apt35.md) for the related cluster.

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

## Public Reports

**MITRE ATT&CK:**

- [MITRE ATT&CK G1044 — APT42](https://attack.mitre.org/groups/G1044/) — Technique mappings, software associations (POWERPOST, NICECURL, TAMECAT), and alias registry. Note that TA453 / Charming Kitten vendor naming caveats apply; check the vendor taxonomy used by each source before attributing.

**Primary vendor reporting:**

- Mandiant, "APT42: Crooked Charms, Cons, and Compromises" — 2022. Foundational profile documenting IRGC-IO attribution, targeting scope, tools, and operational patterns. Source ID `SRC-MANDIANT-APT42`.
- Google Threat Analysis Group, "Spear-Phishing Campaign Targets Gmail Users Affiliated with US Government" — Documents APT42 targeting US government-affiliated targets including presidential campaign staff. Source ID `SRC-GOOGLE-APT42-PHISHING`.
- Google Threat Analysis Group, "Uncharmed: Untangling Iran's APT42 Operations" — 2023. Analysis of trojanized VPN and security software packages used for initial access. Source ID `SRC-GOOGLE-APT42-UNCHARMED`.
- Check Point Research, "Educated Manticore" — Israel-targeted campaigns using regional conference and policy research lures. Source IDs `SRC-CP-EDUCATED-2023`, `SRC-CP-EDUCATED-2025`.
- Proofpoint, Iran Conflict reporting — Campaign-level phishing infrastructure and lure analysis including Israel-facing operations. Source ID `SRC-PROOFPOINT-IRAN-CONFLICT-2026`.
- Volexity, "CharmingCypress" — Documents TA453-mapped activity using multi-persona phishing and malicious NPM packages. Note vendor taxonomy caveat.
