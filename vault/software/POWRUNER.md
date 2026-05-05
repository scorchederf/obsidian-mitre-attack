---
aliases: 
    - S0184
    
mitre-attack: https://attack.mitre.org/software/S0184
---

## S0184

[POWRUNER](https://attack.mitre.org/software/S0184) is a PowerShell script that sends and receives commands to and from the C2 server. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect network configuration data by running `ipconfig /all` on a victim.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [POWRUNER](https://attack.mitre.org/software/S0184) can use HTTP for C2 communications.[^2] [^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [POWRUNER](https://attack.mitre.org/software/S0184) may use WMI when collecting information about a victim.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect process information by running `tasklist` on a victim.[^2]  |
| [[DNS\|T1071.004]] | DNS | [POWRUNER](https://attack.mitre.org/software/S0184) can use DNS for C2 communications.[^2] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect information about the currently logged in user by running `whoami` on a victim.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect information on the victim's anti-virus software.[^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [POWRUNER](https://attack.mitre.org/software/S0184) may collect domain group information by running `net group /domain` or a series of other commands on a victim.[^2]  |
| [[Local Groups\|T1069.001]] | Local Groups | [POWRUNER](https://attack.mitre.org/software/S0184) may collect local group information by running `net localgroup administrators` or a series of other commands on a victim.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [POWRUNER](https://attack.mitre.org/software/S0184) may collect user account information by running `net user /domain` or a series of other commands on a victim.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may enumerate user directories on a victim.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect information about the system by running `hostname` and `systeminfo` on a victim.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [POWRUNER](https://attack.mitre.org/software/S0184) can execute commands from its C2 server.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [POWRUNER](https://attack.mitre.org/software/S0184) is written in PowerShell.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [POWRUNER](https://attack.mitre.org/software/S0184) can use base64 encoded C2 communications.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [POWRUNER](https://attack.mitre.org/software/S0184) can download or upload files from its C2 server.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [POWRUNER](https://attack.mitre.org/software/S0184) may query the Registry by running `reg query` on a victim.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [POWRUNER](https://attack.mitre.org/software/S0184) may collect active network connections by running `netstat -an` on a victim.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [POWRUNER](https://attack.mitre.org/software/S0184) persists through a scheduled task that executes it every minute.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [POWRUNER](https://attack.mitre.org/software/S0184) can capture a screenshot from a victim.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^2]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^3]: POWRUNER


