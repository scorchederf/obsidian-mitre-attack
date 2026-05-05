---
aliases: 
    - Star Blizzard
    - SEABORGIUM
    - Callisto Group
    - TA446
    - COLDRIVER
mitre-attack: https://attack.mitre.org/groups/G1033
---

## G1033

[Star Blizzard](https://attack.mitre.org/groups/G1033) is a cyber espionage and influence group originating in Russia that has been active since at least 2019. [Star Blizzard](https://attack.mitre.org/groups/G1033) campaigns align closely with Russian state interests and have included persistent phishing and credential theft against academic, defense, government, NGO, and think tank organizations in NATO countries, particularly the US and the UK.[^2] [^8] [^6] [^5] <br>

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Impersonation\|T1684.001]] | Impersonation | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered impersonation email accounts to spoof experts in a particular field or individuals and organizations affiliated with the intended target.[^2] [^8] [^5]  |
| [[Domains\|T1583.001]] | Domains | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered domains using randomized words and with names resembling legitimate organizations.[^8] [^6]   |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Star Blizzard](https://attack.mitre.org/groups/G1033) has remotely accessed victims' email accounts to steal messages and attachments.[^8]  |
| [[Web Session Cookie\|T1550.004]] | Web Session Cookie | [Star Blizzard](https://attack.mitre.org/groups/G1033) has bypassed multi-factor authentication on victim email accounts by using session cookies stolen using EvilGinx.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Star Blizzard](https://attack.mitre.org/groups/G1033) has lured targets into opening malicious .pdf files to deliver malware.[^5]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Star Blizzard](https://attack.mitre.org/groups/G1033) has uploaded malicious payloads to cloud storage sites.[^5]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used EvilGinx to steal the session cookies of victims directed to<br> phishing domains.[^8]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [Star Blizzard](https://attack.mitre.org/groups/G1033) has identified ways to engage targets by researching potential victims' interests and social or professional contacts.[^8]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered impersonation email accounts to spoof experts in a particular field or individuals and organizations affiliated with the intended target.[^2] [^8] [^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails with malicious .pdf files to spread malware.[^5]  |
| [[Spearphishing Attachment\|T1598.002]] | Spearphishing Attachment | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails to establish rapport with targets eventually sending messages with attachments containing links to credential-stealing sites.[^2] [^8] [^6] [^5] <br> |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails to establish rapport with targets eventually sending messages with links to credential-stealing sites.[^2] [^8] [^6] [^5] <br> |
| [[Tool\|T1588.002]] | Tool | [Star Blizzard](https://attack.mitre.org/groups/G1033) has incorporated the open-source EvilGinx framework into their spearphishing activity.[^8] [^6]   |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used HubSpot and MailerLite marketing platform services to hide the true sender of phishing emails.[^6]   |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | [Star Blizzard](https://attack.mitre.org/groups/G1033) has abused email forwarding rules to monitor the activities of a victim, steal information, and maintain persistent access after compromised credentials are reset.[^2] [^8]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has established fraudulent profiles on professional networking sites to conduct reconnaissance.[^2] [^8]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used stolen credentials to sign into victim email accounts.[^2] [^8]   |
| [[Email Accounts\|T1586.002]] | Email Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used compromised email accounts to conduct spearphishing against<br> contacts of the original victim.[^8] <br> |
| [[JavaScript\|T1059.007]] | JavaScript | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used JavaScript to redirect victim traffic from an adversary controlled server to a server hosting the Evilginx phishing framework.[^6]   |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | <br>[Star Blizzard](https://attack.mitre.org/groups/G1033) has used open-source research to identify information about victims to use in targeting.[^2] [^8]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Spica\|S1140]] | Spica | [^5]  |



## References

[^1]: COLDRIVER


[^2]: [Microsoft Star Blizzard August 2022](https://www.microsoft.com/en-us/security/blog/2022/08/15/disrupting-seaborgiums-ongoing-phishing-operations/)


[^3]: TA446


[^4]: SEABORGIUM


[^5]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)


[^6]: [StarBlizzard](https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/)


[^7]: Callisto Group


[^8]: [CISA Star Blizzard Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a)


