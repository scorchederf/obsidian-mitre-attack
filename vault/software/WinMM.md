---
aliases: 
    - S0059
    
mitre-attack: https://attack.mitre.org/software/S0059
---

## S0059

[WinMM](https://attack.mitre.org/software/S0059) is a full-featured, simple backdoor used by [Naikon](https://attack.mitre.org/groups/G0019). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [WinMM](https://attack.mitre.org/software/S0059) sets a WH_CBT Windows hook to collect information on process creation.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WinMM](https://attack.mitre.org/software/S0059) sets a WH_CBT Windows hook to search for and capture files on the victim.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [WinMM](https://attack.mitre.org/software/S0059) collects the system name, OS version including service pack, and system install date and sends the information to the C2 server.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [WinMM](https://attack.mitre.org/software/S0059) is usually configured with primary and backup domains for C2 communications.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WinMM](https://attack.mitre.org/software/S0059) uses HTTP for C2.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [WinMM](https://attack.mitre.org/software/S0059) uses NetUser-GetInfo to identify that it is running under an “Admin” account on the local system.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^2]: [CameraShy](http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf)


