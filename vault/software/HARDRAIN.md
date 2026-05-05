---
aliases: 
    - S0246
    
mitre-attack: https://attack.mitre.org/software/S0246
---

## S0246

[HARDRAIN](https://attack.mitre.org/software/S0246) is a Trojan malware variant reportedly used by the North Korean government. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [HARDRAIN](https://attack.mitre.org/software/S0246) binds and listens on port 443 with a FakeTLS method.[^2]  |
| [[Proxy\|T1090]] | Proxy | [HARDRAIN](https://attack.mitre.org/software/S0246) uses the command `cmd.exe /c netsh firewall add portopening TCP 443 "adp"` and makes the victim machine function as a proxy server.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HARDRAIN](https://attack.mitre.org/software/S0246) uses cmd.exe to execute `netsh`commands.[^2]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [HARDRAIN](https://attack.mitre.org/software/S0246) uses FakeTLS to communicate with its C2 server.[^1]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [HARDRAIN](https://attack.mitre.org/software/S0246) opens the Windows Firewall to modify incoming connections.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [MAR10135536-F](https://web.archive.org/web/20210709132313/https://us-cert.cisa.gov/sites/default/files/publications/MAR-10135536-F.pdf)


[^2]: [US-CERT HARDRAIN March 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)


[^3]: HARDRAIN


