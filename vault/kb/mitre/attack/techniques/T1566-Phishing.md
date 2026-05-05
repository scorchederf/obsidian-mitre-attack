---
aliases: 
    - T1566
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1566-Phishing
tactic: 
     - Initial Access
platforms:
     - Identity Provider - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.<br><br>Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [[kb/mitre/attack/techniques/T1564.008-Email_Hiding_Rules\|Email Hiding Rules]]).[^2] [^8]  Another way to accomplish this is by [[kb/mitre/attack/techniques/T1684.002-Email_Spoofing\|Email Spoofing]][^4]  the identity of the sender, which can be used to fool both the human recipient as well as automated security tools,[^1]  or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking").[^3] <br><br>Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware,[^10] [^6]  or install adversary-accessible remote management tools onto their computer (i.e., [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]]).[^9] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Users can be trained to identify social engineering techniques and phishing emails. |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Determine if certain websites or attachment types (ex: .scr, .exe, .pif, .cpl, etc.) that can be used for phishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion prevention systems and systems designed to scan and remove malicious email attachments or links can be used to block activity. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can automatically quarantine suspicious files. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^5] [^7]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1566.001-Spearphishing_Attachment\|T1566.001]] | Spearphishing Attachment |
| [[kb/mitre/attack/techniques/T1566.002-Spearphishing_Link\|T1566.002]] | Spearphishing Link |
| [[kb/mitre/attack/techniques/T1566.003-Spearphishing_via_Service\|T1566.003]] | Spearphishing via Service |
| [[kb/mitre/attack/techniques/T1566.004-Spearphishing_Voice\|T1566.004]] | Spearphishing Voice |




> [!info]- References
> [^1]: [cyberproof-double-bounce](https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends)

> [^2]: [Microsoft OAuth Spam 2022](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/)

> [^3]: [phishing-krebs](https://krebsonsecurity.com/2024/03/thread-hijacking-phishes-that-prey-on-your-curiosity/)

> [^4]: [Proofpoint-spoof](https://www.proofpoint.com/us/threat-reference/email-spoofing)

> [^5]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)

> [^6]: [CISA Remote Monitoring and Management Software](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a)

> [^7]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

> [^8]: [Palo Alto Unit 42 VBA Infostealer 2014](https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/)

> [^9]: [Unit42 Luna Moth](https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/)

> [^10]: [sygnia Luna Month](https://blog.sygnia.co/luna-moth-false-subscription-scams)


