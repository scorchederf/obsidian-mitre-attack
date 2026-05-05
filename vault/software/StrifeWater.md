---
aliases: 
    - S1034
    
mitre-attack: https://attack.mitre.org/software/S1034
---

## S1034

[StrifeWater](https://attack.mitre.org/software/S1034) is a remote-access tool that has been used by [Moses Staff](https://attack.mitre.org/groups/G1009) in the initial stages of their attacks since at least November 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [StrifeWater](https://attack.mitre.org/software/S1034) can collect the user name from the victim's machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [StrifeWater](https://attack.mitre.org/software/S1034) can execute shell commands using `cmd.exe`.[^1]  |
| [[Native API\|T1106]] | Native API | [StrifeWater](https://attack.mitre.org/software/S1034) can use a variety of APIs for execution.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [StrifeWater](https://attack.mitre.org/software/S1034) can encrypt C2 traffic using XOR with a hard coded key.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [StrifeWater](https://attack.mitre.org/software/S1034) has create a scheduled task named `Mozilla\Firefox Default Browser Agent 409046Z0FF4A39CB` for persistence.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [StrifeWater](https://attack.mitre.org/software/S1034) has the ability to take screen captures.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [StrifeWater](https://attack.mitre.org/software/S1034) has been named `calc.exe` to appear as a legitimate calculator program.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [StrifeWater](https://attack.mitre.org/software/S1034) can modify its sleep time responses from the default of 20-22 seconds.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [StrifeWater](https://attack.mitre.org/software/S1034) can send data and files from a compromised host to its C2 server.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [StrifeWater](https://attack.mitre.org/software/S1034) can collect the time zone from the victim's machine.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [StrifeWater](https://attack.mitre.org/software/S1034) can collect the OS version, architecture, and machine name to create a unique token for the infected host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [StrifeWater](https://attack.mitre.org/software/S1034) can enumerate files on a compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [StrifeWater](https://attack.mitre.org/software/S1034) can collect data from a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [StrifeWater](https://attack.mitre.org/software/S1034) can download updates and auxiliary modules.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [StrifeWater](https://attack.mitre.org/software/S1034) can self delete to cover its tracks.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Moses Staff\|G1009]] | Moses Staff |



## References

[^1]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


