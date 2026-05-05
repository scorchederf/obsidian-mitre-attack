---
aliases: 
    - EXOTIC LILY
mitre-attack: https://attack.mitre.org/groups/G1011
---

## G1011

[EXOTIC LILY](https://attack.mitre.org/groups/G1011) is a financially motivated group that has been closely linked with [Wizard Spider](https://attack.mitre.org/groups/G0102) and the deployment of ransomware including [Conti](https://attack.mitre.org/software/S0575) and [Diavol](https://attack.mitre.org/software/S0659). [EXOTIC LILY](https://attack.mitre.org/groups/G1011) may be acting as an initial access broker for other malicious actors, and has targeted a wide range of industries including IT, cybersecurity, and healthcare since at least September 2021.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used the e-mail notification features of legitimate file sharing services for spearphishing.[^2]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has established social media profiles to mimic employees of targeted companies.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) conducted an e-mail thread-hijacking campaign with malicious ISO attachments.[^2] [^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used malicious documents containing exploits for CVE-2021-40444 affecting Microsoft MSHTML.[^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has relied on victims to open malicious links in e-mails for execution.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has gained execution through victims clicking on malicious LNK files contained within ISO files, which can execute hidden DLLs within the ISO.[^2] [^1]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has created e-mail accounts to spoof targeted organizations.[^2]  |
| [[Web Service\|T1102]] | Web Service | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used file-sharing services including WeTransfer, TransferNow, and OneDrive to deliver payloads.[^2]  |
| [[Search Victim-Owned Websites\|T1594]] | Search Victim-Owned Websites | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used contact forms on victim websites to generate phishing e-mails.[^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used malicious links to lure users into executing malicious payloads.[^2]  |
| [[Search Closed Sources\|T1597]] | Search Closed Sources | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has searched for information on targeted individuals on business databases including RocketReach and CrunchBase.[^2]  |
| [[Domains\|T1583.001]] | Domains | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has registered domains to spoof targeted organizations by changing the top-level domain (TLD) to “.us”, “.co” or “.biz”.[^2]  |
| [[Social Media\|T1593.001]] | Social Media | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has copied data from social media sites to impersonate targeted individuals.[^2]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has gathered targeted individuals' e-mail addresses through open source research and website contact forms.[^2]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [EXOTIC LILY](https://attack.mitre.org/groups/G1011)  has uploaded malicious payloads to file-sharing services including TransferNow, TransferXL, WeTransfer, and OneDrive.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Bumblebee\|S1039]] | Bumblebee | [^2]  |
| [[Bazar\|S0534]] | Bazar | [^2]  |



## References

[^1]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^2]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


