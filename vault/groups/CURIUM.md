---
aliases: 
    - CURIUM
    - Crimson Sandstorm
    - TA456
    - Tortoise Shell
    - Yellow Liderc
mitre-attack: https://attack.mitre.org/groups/G1012
---

## G1012

[CURIUM](https://attack.mitre.org/groups/G1012) is an Iranian threat group, first reported in September 2019 and active since at least July 2018, targeting IT service providers in the Middle East.[^8]  [CURIUM](https://attack.mitre.org/groups/G1012) has since invested in building relationships with potential targets via social media over a period of months to establish trust and confidence before sending malware. Security researchers note [CURIUM](https://attack.mitre.org/groups/G1012) has demonstrated great patience and persistence by chatting with potential targets daily and sending benign files to help lower their security consciousness.[^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [CURIUM](https://attack.mitre.org/groups/G1012) has used social media to deliver malicious files to victims.[^5]  |
| [[Web Shell\|T1505.003]] | Web Shell | [CURIUM](https://attack.mitre.org/groups/G1012) has been linked to web shells following likely server compromise as an initial access vector into victim networks.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [CURIUM](https://attack.mitre.org/groups/G1012) has lured users into opening malicious files delivered via social media.[^5]  |
| [[Web Services\|T1584.006]] | Web Services | [CURIUM](https://attack.mitre.org/groups/G1012) has compromised legitimate websites to enable strategic website compromise attacks.[^4]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [CURIUM](https://attack.mitre.org/groups/G1012) created virtual private server instances to facilitate use of malicious domains and other items.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [CURIUM](https://attack.mitre.org/groups/G1012) deploys information gathering tools focused on capturing IP configuration, running application, system information, and network connectivity information.[^8]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [CURIUM](https://attack.mitre.org/groups/G1012) used strategic website compromise to fingerprint then target victims.[^4]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [CURIUM](https://attack.mitre.org/groups/G1012) has used SMTPS to exfiltrate collected data from victims.[^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CURIUM](https://attack.mitre.org/groups/G1012) has exfiltrated data from a compromised machine.[^5]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [CURIUM](https://attack.mitre.org/groups/G1012) has established a network of fictitious social media accounts, including on Facebook and LinkedIn, to establish relationships with victims, often posing as an attractive woman.[^5]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [CURIUM](https://attack.mitre.org/groups/G1012) has created dedicated email accounts for use with tools such as [IMAPLoader](https://attack.mitre.org/software/S1152).[^4]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [CURIUM](https://attack.mitre.org/groups/G1012) deployed mechanisms to check system time information following strategic website compromise attacks.[^4]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [CURIUM](https://attack.mitre.org/groups/G1012) used malicious links to adversary-controlled resources for credential harvesting.[^4]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [CURIUM](https://attack.mitre.org/groups/G1012) has used strategic website compromise to infect victims with malware such as [IMAPLoader](https://attack.mitre.org/software/S1152).[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [CURIUM](https://attack.mitre.org/groups/G1012) has used phishing with malicious attachments for initial access to victim environments.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CURIUM](https://attack.mitre.org/groups/G1012) has leveraged PowerShell scripts for initial process execution and data gathering in victim environments.[^8]  |
| [[Domains\|T1583.001]] | Domains | [CURIUM](https://attack.mitre.org/groups/G1012) created domains to facilitate strategic website compromise and credential capture activities.[^4]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [CURIUM](https://attack.mitre.org/groups/G1012) has used IMAP and SMTPS for exfiltration via tools such as [IMAPLoader](https://attack.mitre.org/software/S1152).[^4]  |
| [[Server\|T1583.004]] | Server | [CURIUM](https://attack.mitre.org/groups/G1012) has created dedicated servers for command and control and exfiltration purposes.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[IMAPLoader\|S1152]] | IMAPLoader | [IMAPLoader](https://attack.mitre.org/software/S1152) was deployed by [CURIUM](https://attack.mitre.org/groups/G1012) as a post-exploitation payload from strategic website compromise.[^4]  |



## References

[^1]: Crimson Sandstorm


[^2]: [Proofpoint TA456 Defense Contractor July 2021](https://www.proofpoint.com/us/blog/threat-insight/i-knew-you-were-trouble-ta456-targets-defense-contractor-alluring-social-media)


[^3]: TA456


[^4]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)


[^5]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^6]: Tortoise Shell


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: [Symantec Tortoiseshell 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain)


[^9]: Yellow Liderc


