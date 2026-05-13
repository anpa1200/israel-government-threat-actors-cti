# Israel Government Threat Model

## Protected Mission

Israeli government and public-sector networks support citizen services, national security coordination, regulatory functions, public communications, and emergency response. Attackers may pursue espionage, disruption, psychological effect, credential theft, destructive operations, or public embarrassment.

## Priority Adversary Objectives

| Objective | Defensive Interpretation |
| --- | --- |
| Credential access | Protect identity providers, email, VPN, remote access, and privileged accounts. |
| Public-sector espionage | Monitor phishing, mailbox access, endpoint scripting, and data staging. |
| Disruption and wipers | Monitor backup deletion, privilege escalation, mass file operations, and endpoint tampering. |
| Influence operations | Separate public claims from verified technical evidence; preserve evidence for communications teams. |
| OT/ICS pressure | Eliminate internet-exposed management interfaces and default credentials. |
| Supplier compromise | Monitor government-adjacent vendors, MSPs, hosting, and software providers. |

## Priority Asset Classes

- Identity: Entra ID, Active Directory, privileged access management, VPN, SSO, and MFA systems.
- Email and collaboration: Microsoft 365, Exchange, Google Workspace, file sharing, and Teams/Slack-like platforms.
- Public web: portals, citizen services, CMS platforms, API gateways, and externally exposed web servers.
- Endpoint: administrator workstations, analyst systems, developer workstations, and finance systems.
- OT/ICS: municipal water, emergency services, building systems, traffic control, and remote HMI access.
- Suppliers: MSPs, cloud tenants, SaaS platforms, telecom providers, and critical infrastructure vendors.

## Detection Priorities

1. Phishing-to-cloud-account compromise.
2. RMM abuse and remote access persistence.
3. PowerShell, certutil, mshta, rundll32, and script-host execution chains.
4. Webshell post-exploitation from IIS, Exchange, SharePoint, and public web applications.
5. MFA method changes, impossible travel, risky sign-ins, and privileged cloud changes.
6. Backup deletion, endpoint protection tampering, mass encryption, and destructive staging.
7. OT remote web interface exposure and unexpected HMI authentication.

## Attribution Caution

Attribution MUST NOT rely only on an IOC, malware family, or claimed persona. Analysts SHOULD combine victimology, infrastructure, TTPs, timing, language, tooling, and source credibility before assigning actor confidence.

