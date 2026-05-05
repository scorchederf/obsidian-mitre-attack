---
aliases: 
    - S0214
    
mitre-attack: https://attack.mitre.org/software/S0214
---

## S0214

[HAPPYWORK](https://attack.mitre.org/software/S0214) is a downloader used by [APT37](https://attack.mitre.org/groups/G0067) to target South Korean government and financial victims in November 2016. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | can collect system information, including computer name, system manufacturer, IsDebuggerPresent state, and execution path.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | can collect the victim user name.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | can download and execute a second-stage payload.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


