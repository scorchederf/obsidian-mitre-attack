---
aliases: 
    - S0350
    
mitre-attack: https://attack.mitre.org/software/S0350
---

## S0350

[zwShell](https://attack.mitre.org/software/S0350) is a remote access tool (RAT) written in Delphi that has been seen in the wild since the spring of 2010 and used by threat actors during [Night Dragon](https://attack.mitre.org/campaigns/C0002).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [zwShell](https://attack.mitre.org/software/S0350) has used RDP for lateral movement.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [zwShell](https://attack.mitre.org/software/S0350) has been copied over network shares to move laterally.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [zwShell](https://attack.mitre.org/software/S0350) has used SchTasks for execution.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [zwShell](https://attack.mitre.org/software/S0350) has established persistence by adding itself as a new service.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [zwShell](https://attack.mitre.org/software/S0350) can browse the file system.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [zwShell](https://attack.mitre.org/software/S0350) has deleted itself after creating a service as well as deleted a temporary file when the system reboots.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [zwShell](https://attack.mitre.org/software/S0350) can obtain the victim PC name and OS version.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [zwShell](https://attack.mitre.org/software/S0350) can obtain the victim IP address.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [zwShell](https://attack.mitre.org/software/S0350) can modify the Registry.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [zwShell](https://attack.mitre.org/software/S0350) can obtain the name of the logged-in user on the victim.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [zwShell](https://attack.mitre.org/software/S0350) can launch command-line shells.[^2]  |




## References

[^1]: zwShell


[^2]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


