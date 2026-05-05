---
aliases: 
    - admin@338
mitre-attack: https://attack.mitre.org/groups/G0018
---

## G0018

[admin@338](https://attack.mitre.org/groups/G0018) is a China-based cyber threat group. It has previously used newsworthy events as lures to deliver malware and has primarily targeted organizations involved in financial, economic, and trade policy, typically using publicly available RATs such as [PoisonIvy](https://attack.mitre.org/software/S0012), as well as some non-public backdoors. [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [admin@338](https://attack.mitre.org/groups/G0018) has sent emails with malicious Microsoft Office documents attached.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to acquire information about local networks: `ipconfig /all >> %temp%\download`[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command to rename one of their tools to a benign file name: `ren "%temp%\upload" audiodg.exe`[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following commands after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to obtain information about files and directories: `dir c:\ >> %temp%\download` `dir "c:\Documents and Settings" >> %temp%\download` `dir "c:\Program Files\" >> %temp%\download` `dir d:\ >> %temp%\download`[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command following exploitation of a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to list local groups: `net localgroup administrator >> %temp%\download`[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command following exploitation of a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to display network connections: `netstat -ano >> %temp%\download`[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following commands following exploitation of a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to enumerate user accounts: `net user >> %temp%\download` `net user /domain >> %temp%\download`[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [admin@338](https://attack.mitre.org/groups/G0018) has exploited client software vulnerabilities for execution, such as Microsoft Word CVE-2012-0158.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command following exploitation of a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to obtain information about services: `net start >> %temp%\download`[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [admin@338](https://attack.mitre.org/groups/G0018) has attempted to get victims to launch malicious Microsoft Word attachments delivered via spearphishing emails.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following commands after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to obtain information about the OS: `ver >> %temp%\download` `systeminfo >> %temp%\download`[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | Following exploitation with [LOWBALL](https://attack.mitre.org/software/S0042) malware, [admin@338](https://attack.mitre.org/groups/G0018) actors created a file containing a list of commands to be executed on the compromised computer.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^1]  |
| [[ipconfig\|S0100]] | ipconfig | [^1]  |
| [[netstat\|S0104]] | netstat | [^1]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^1]  |
| [[BUBBLEWRAP\|S0043]] | BUBBLEWRAP | [^1]  |
| [[LOWBALL\|S0042]] | LOWBALL | [^1]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^1]  |



## References

[^1]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^2]: admin@338


