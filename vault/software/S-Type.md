---
aliases: 
    - S0085
    
mitre-attack: https://attack.mitre.org/software/S0085
---

## S0085

[S-Type](https://attack.mitre.org/software/S0085) is a backdoor that was used in [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) since at least 2013.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [S-Type](https://attack.mitre.org/software/S0085) may save itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^2] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [S-Type](https://attack.mitre.org/software/S0085) has run tests to determine the privilege level of the compromised user.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [S-Type](https://attack.mitre.org/software/S0085) has uploaded data and files from a compromised host to its C2 servers.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [S-Type](https://attack.mitre.org/software/S0085) can download additional files onto a compromised host.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [S-Type](https://attack.mitre.org/software/S0085) primarily uses port 80 for C2, but falls back to ports 443 or 8080 if initial communication fails.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [S-Type](https://attack.mitre.org/software/S0085) uses HTTP for C2.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [S-Type](https://attack.mitre.org/software/S0085) has provided the ability to execute shell commands on a compromised host.[^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [S-Type](https://attack.mitre.org/software/S0085) has attempted to determine if a compromised system was using a Japanese keyboard via the `GetKeyboardType` API call.[^2]  |
| [[Local Account\|T1136.001]] | Local Account | [S-Type](https://attack.mitre.org/software/S0085) may create a temporary user on the system named `Lost_{Unique Identifier}` with the password `pond~!@6”{Unique Identifier}`.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [S-Type](https://attack.mitre.org/software/S0085) has deleted files it has created on a compromised host.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | The initial beacon packet for [S-Type](https://attack.mitre.org/software/S0085) contains the operating system version and file system of the victim.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [S-Type](https://attack.mitre.org/software/S0085) uses Base64 encoding for C2 traffic.[^2]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [S-Type](https://attack.mitre.org/software/S0085) may create the file `%HOMEPATH%\Start Menu\Programs\Startup\Realtek {Unique Identifier}.lnk`, which points to the malicious `msdtc.exe` file already created in the `%CommonFiles%` directory.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | Some [S-Type](https://attack.mitre.org/software/S0085) samples have been packed with UPX.[^2]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [S-Type](https://attack.mitre.org/software/S0085) has deleted accounts it has created.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [S-Type](https://attack.mitre.org/software/S0085) has used `ipconfig /all` on a compromised host.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [S-Type](https://attack.mitre.org/software/S0085) runs the command `net start` on a victim.[^2]  |
| [[Native API\|T1106]] | Native API | [S-Type](https://attack.mitre.org/software/S0085) has used Windows APIs, including `GetKeyboardType`, `NetUserAdd`, and `NetUserDel`.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [S-Type](https://attack.mitre.org/software/S0085) may create a .lnk file to itself that is saved in the Start menu folder. It may also create the Registry key `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ IMJPMIJ8.1{3 characters of Unique Identifier}`.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [S-Type](https://attack.mitre.org/software/S0085) has run the command `net user` on a victim.[^2]  |




## References

[^1]: [Microsoft DTC](https://technet.microsoft.com/en-us/library/cc759136(v=ws.10).aspx)


[^2]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


