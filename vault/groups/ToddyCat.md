---
aliases: 
    - ToddyCat
mitre-attack: https://attack.mitre.org/groups/G1022
---

## G1022

[ToddyCat](https://attack.mitre.org/groups/G1022) is a sophisticated threat group that has been active since at least 2020 using custom loaders and malware in multi-stage infection chains against government and military targets across Europe and Asia.[^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | Prior to executing a backdoor [ToddyCat](https://attack.mitre.org/groups/G1022)  has run `cmd /c start /b netsh advfirewall firewall add rule name="SGAccessInboundRule" dir=in protocol=udp action=allow localport=49683` to allow the targeted system to receive UDP packets on port 49683.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to collect documents from targeted hosts.[^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [ToddyCat](https://attack.mitre.org/groups/G1022) has executed `net group "domain admins" /dom` for discovery on compromised machines.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ToddyCat](https://attack.mitre.org/groups/G1022) has used scheduled tasks to execute discovery commands and scripts for collection.[^2]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [ToddyCat](https://attack.mitre.org/groups/G1022) has sent loaders configured to run [Ninja](https://attack.mitre.org/software/S1100) as zip archives via Telegram.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [ToddyCat](https://attack.mitre.org/groups/G1022) has run `net user %USER% /dom` for account discovery.[^2] <br> |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [ToddyCat](https://attack.mitre.org/groups/G1022) has used a passive backdoor that receives commands with UDP packets.[^2]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [ToddyCat](https://attack.mitre.org/groups/G1022) has used compromised domain admin credentials to mount local network shares.[^2]  |
| [[Native API\|T1106]] | Native API | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `WinExec` to execute commands received from C2 on compromised hosts.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has run `cmd /c start /b tasklist` to enumerate processes.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `ping %REMOTE_HOST%` for post exploit discovery.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has used `netstat -anop tcp` to discover TCP connections to compromised hosts.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [ToddyCat](https://attack.mitre.org/groups/G1022) has used locally mounted network shares for lateral movement through targated environments.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ToddyCat](https://attack.mitre.org/groups/G1022) has used .bat scripts and `cmd` for execution on compromised hosts.[^2]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [ToddyCat](https://attack.mitre.org/groups/G1022) has exploited the ProxyLogon vulnerability (CVE-2021-26855) to compromise Exchange Servers at multiple organizations.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [ToddyCat](https://attack.mitre.org/groups/G1022) has used a DropBox uploader to exfiltrate stolen files.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) can determine is Kaspersky software is running on an endpoint by running `cmd /c wmic process where name="avp.exe"`.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ToddyCat](https://attack.mitre.org/groups/G1022) has used Powershell scripts to perform post exploit collection.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [ToddyCat](https://attack.mitre.org/groups/G1022) has hidden malicious scripts using `powershell.exe -windowstyle hidden`. [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to enumerate recently modified documents having either a .pdf, .doc, .docx, .xls or .xlsx extension.[^2]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [ToddyCat](https://attack.mitre.org/groups/G1022) manually transferred collected files to an exfiltration host using xcopy.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [ToddyCat](https://attack.mitre.org/groups/G1022) has used WMI to execute scripts for post exploit document collection.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [ToddyCat](https://attack.mitre.org/groups/G1022) has used the name `debug.exe` for malware components.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [ToddyCat](https://attack.mitre.org/groups/G1022) has collected information on bootable drives including model, vendor, and serial numbers.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [ToddyCat](https://attack.mitre.org/groups/G1022) has leveraged  xcopy, 7zip, and RAR to stage and compress collected documents prior to exfiltration.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^2]  |
| [[netstat\|S0104]] | netstat | [^2]  |
| [[Ping\|S0097]] | Ping | [^2]  |
| [[Ninja\|S1100]] | Ninja | [^1]  |
| [[LoFiSe\|S1101]] | LoFiSe | [^2]  |
| [[China Chopper\|S0020]] | China Chopper | [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^2]  |
| [[Samurai\|S1099]] | Samurai | [^1]  |
| [[Pcexter\|S1102]] | Pcexter | [^2]  |



## References

[^1]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^2]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


