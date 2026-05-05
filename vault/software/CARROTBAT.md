---
aliases: 
    - S0462
    
mitre-attack: https://attack.mitre.org/software/S0462
---

## S0462

[CARROTBAT](https://attack.mitre.org/software/S0462) is a customized dropper that has been in use since at least 2017. [CARROTBAT](https://attack.mitre.org/software/S0462) has been used to install [SYSCON](https://attack.mitre.org/software/S0464) and has infrastructure overlap with [KONNI](https://attack.mitre.org/software/S0356).[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to determine the operating system of the compromised host and whether Windows is being run with x86 or x64 architecture.[^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to execute command line arguments on a compromised host.[^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to execute obfuscated commands on the infected host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to download and execute a remote file via [certutil](https://attack.mitre.org/software/S0160).[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to delete downloaded files from a compromised host.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to download a base64 encoded payload.[^1]  |




## References

[^1]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^2]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


