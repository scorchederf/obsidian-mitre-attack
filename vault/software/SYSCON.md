---
aliases: 
    - S0464
    
mitre-attack: https://attack.mitre.org/software/S0464
---

## S0464

[SYSCON](https://attack.mitre.org/software/S0464) is a backdoor that has been in use since at least 2017 and has been associated with campaigns involving North Korean themes. [SYSCON](https://attack.mitre.org/software/S0464) has been delivered by the [CARROTBALL](https://attack.mitre.org/software/S0465) and [CARROTBAT](https://attack.mitre.org/software/S0462) droppers.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to use [Systeminfo](https://attack.mitre.org/software/S0096) to identify system information.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to execute commands through [cmd](https://attack.mitre.org/software/S0106) on a compromised host.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [SYSCON](https://attack.mitre.org/software/S0464) has been executed by luring victims to open malicious e-mail attachments.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to use [Tasklist](https://attack.mitre.org/software/S0057) to list running processes.[^2]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to use FTP in C2 communications.[^1] [^2]  |




## References

[^1]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^2]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


