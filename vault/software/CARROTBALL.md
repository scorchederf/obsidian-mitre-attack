---
aliases: 
    - S0465
    
mitre-attack: https://attack.mitre.org/software/S0465
---

## S0465

[CARROTBALL](https://attack.mitre.org/software/S0465) is an FTP downloader utility that has been in use since at least 2019. [CARROTBALL](https://attack.mitre.org/software/S0465) has been used as a downloader to install [SYSCON](https://attack.mitre.org/software/S0464).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to use FTP in C2 communications.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to download and install a remote payload.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [CARROTBALL](https://attack.mitre.org/software/S0465) has been executed through users being lured into opening malicious e-mail attachments.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [CARROTBALL](https://attack.mitre.org/software/S0465) has used a custom base64 alphabet to decode files.[^1]  |




## References

[^1]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


