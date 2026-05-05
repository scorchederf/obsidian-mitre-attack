---
aliases: 
    - T1598
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1598-Phishing_for_Information
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]] in that the objective is gathering data from the victim rather than executing malicious code.<br><br>All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass credential harvesting campaigns.<br><br>Adversaries may also try to obtain information directly through the exchange of emails, instant messages, or other electronic conversation means.[^8] [^11] [^2] [^6] [^3]  Victims may also receive phishing messages that direct them to call a phone number where the adversary attempts to collect confidential information.[^5] <br><br>Phishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [[kb/mitre/attack/techniques/T1585-Establish_Accounts\|Establish Accounts]] or [[kb/mitre/attack/techniques/T1586-Compromise_Accounts\|Compromise Accounts]]) and/or sending multiple, seemingly urgent messages. Another way to accomplish this is by [[kb/mitre/attack/techniques/T1684.002-Email_Spoofing\|Email Spoofing]][^7]  the identity of the sender, which can be used to fool both the human recipient as well as automated security tools.[^1]  <br><br>Phishing for information may also involve evasive techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., [[kb/mitre/attack/techniques/T1564.008-Email_Hiding_Rules\|Email Hiding Rules]]).[^4] [^10] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Users can be trained to identify social engineering techniques and spearphishing attempts. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation.[^12] [^9]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1598.001-Spearphishing_Service\|T1598.001]] | Spearphishing Service |
| [[kb/mitre/attack/techniques/T1598.002-Spearphishing_Attachment\|T1598.002]] | Spearphishing Attachment |
| [[kb/mitre/attack/techniques/T1598.003-Spearphishing_Link\|T1598.003]] | Spearphishing Link |
| [[kb/mitre/attack/techniques/T1598.004-Spearphishing_Voice\|T1598.004]] | Spearphishing Voice |




> [!info]- References
> [^1]: [cyberproof-double-bounce](https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends)

> [^2]: [PCMag FakeLogin](https://www.pcmag.com/news/hackers-try-to-phish-united-nations-staffers-with-fake-login-pages)

> [^3]: [GitHub Phishery](https://github.com/ryhanson/phishery)

> [^4]: [Microsoft OAuth Spam 2022](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/)

> [^5]: [Avertium callback phishing](https://www.avertium.com/resources/threat-reports/everything-you-need-to-know-about-callback-phishing)

> [^6]: [Sophos Attachment](https://nakedsecurity.sophos.com/2020/10/02/serious-security-phishing-without-links-when-phishers-bring-along-their-own-web-pages/)

> [^7]: [Proofpoint-spoof](https://www.proofpoint.com/us/threat-reference/email-spoofing)

> [^8]: [ThreatPost Social Media Phishing](https://threatpost.com/facebook-launching-pad-phishing-attacks/160351/)

> [^9]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

> [^10]: [Palo Alto Unit 42 VBA Infostealer 2014](https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/)

> [^11]: [TrendMictro Phishing](https://www.trendmicro.com/en_us/research/20/i/tricky-forms-of-phishing.html)

> [^12]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


