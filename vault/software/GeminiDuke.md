---
aliases: 
    - S0049
    
mitre-attack: https://attack.mitre.org/software/S0049
---

## S0049

[GeminiDuke](https://attack.mitre.org/software/S0049) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2009 to 2012. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information from the victim, including installed drivers, programs previously executed by users, programs and services configured to automatically run at startup, files and folders present in any user's home folder, files and folders present in any user's My Documents, programs installed to the Program Files folder, and recently accessed files, folders, and programs.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on local user accounts from the victim.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on running processes and environment variables from the victim.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on network settings and Internet proxy settings from the victim.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on programs and services on the victim that are configured to automatically run at startup.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GeminiDuke](https://attack.mitre.org/software/S0049) uses HTTP and HTTPS for command and control.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


