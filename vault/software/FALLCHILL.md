---
aliases: 
    - S0181
    
mitre-attack: https://attack.mitre.org/software/S0181
---

## S0181

[FALLCHILL](https://attack.mitre.org/software/S0181) is a RAT that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) since at least 2016 to target the aerospace, telecommunications, and finance industries. It is usually dropped by other [Lazarus Group](https://attack.mitre.org/groups/G0032) malware or delivered when a victim unknowingly visits a compromised website. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FALLCHILL](https://attack.mitre.org/software/S0181) can search files on a victim.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [FALLCHILL](https://attack.mitre.org/software/S0181) can modify file or directory timestamps.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [FALLCHILL](https://attack.mitre.org/software/S0181) encrypts C2 data with RC4 encryption.[^2] [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FALLCHILL](https://attack.mitre.org/software/S0181) can delete malware and associated artifacts from the victim.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FALLCHILL](https://attack.mitre.org/software/S0181) can collect operating system (OS) version information, processor information, and system name from the victim.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [FALLCHILL](https://attack.mitre.org/software/S0181) collects MAC address and local IP address information from the victim.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [FALLCHILL](https://attack.mitre.org/software/S0181) can collect information about installed disks from the victim.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [FALLCHILL](https://attack.mitre.org/software/S0181) has been installed as a Windows service.[^3]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [FALLCHILL](https://attack.mitre.org/software/S0181) uses fake Transport Layer Security (TLS) to communicate with its C2 server.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: FALLCHILL


[^2]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^3]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


