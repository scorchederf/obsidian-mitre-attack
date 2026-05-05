---
aliases: 
    - S0084
    
mitre-attack: https://attack.mitre.org/software/S0084
---

## S0084

[Mis-Type](https://attack.mitre.org/software/S0084) is a backdoor hybrid that was used in [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) by 2012.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [Mis-Type](https://attack.mitre.org/software/S0084) has used Windows API calls, including `NetUserAdd` and `NetUserDel`.[^2]  |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [Mis-Type](https://attack.mitre.org/software/S0084) has created registry keys for persistence, including `HKCU\Software\bkfouerioyou`, `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{6afa8072-b2b1-31a8-b5c1-{Unique Identifier}`, and `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3BF41072-B2B1-31A8-B5C1-{Unique Identifier}`.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Mis-Type](https://attack.mitre.org/software/S0084) may create a file containing the results of the command `cmd.exe /c ipconfig /all`.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Mis-Type](https://attack.mitre.org/software/S0084) has used `cmd.exe` to run commands on a compromised host.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mis-Type](https://attack.mitre.org/software/S0084) has downloaded additional malware and files onto a compromised host.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Mis-Type](https://attack.mitre.org/software/S0084) saves itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^2] [^1]  |
| [[Local Account\|T1136.001]] | Local Account | [Mis-Type](https://attack.mitre.org/software/S0084) may create a temporary user on the system named `Lost_{Unique Identifier}`.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Mis-Type](https://attack.mitre.org/software/S0084) uses Base64 encoding for C2 traffic.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mis-Type](https://attack.mitre.org/software/S0084) network traffic can communicate over HTTP.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Mis-Type](https://attack.mitre.org/software/S0084) runs tests to determine the privilege level of the compromised user.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Mis-Type](https://attack.mitre.org/software/S0084) may create a file containing the results of the command `cmd.exe /c net user {Username}`.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Mis-Type](https://attack.mitre.org/software/S0084) first attempts to use a Base64-encoded network protocol over a raw TCP socket for C2, and if that method fails, falls back to a secondary HTTP-based protocol to communicate to an alternate C2 server.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Mis-Type](https://attack.mitre.org/software/S0084) has collected files and data from a compromised host.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | The initial beacon packet for [Mis-Type](https://attack.mitre.org/software/S0084) contains the operating system version and file system of the victim.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mis-Type](https://attack.mitre.org/software/S0084) has transmitted collected files and data to its C2 server.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Mis-Type](https://attack.mitre.org/software/S0084) network traffic can communicate over a raw socket.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [Mis-Type](https://attack.mitre.org/software/S0084) has been injected directly into a running process, including `explorer.exe`.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Mis-Type](https://attack.mitre.org/software/S0084) has temporarily stored collected information to the files `“%AppData%\{Unique Identifier}\HOSTRURKLSR”` and `“%AppData%\{Unique Identifier}\NEWERSSEMP”`.[^2]  |




## References

[^1]: [Microsoft DTC](https://technet.microsoft.com/en-us/library/cc759136(v=ws.10).aspx)


[^2]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


