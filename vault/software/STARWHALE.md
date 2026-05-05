---
aliases: 
    - S1037
    
mitre-attack: https://attack.mitre.org/software/S1037
---

## S1037

[STARWHALE](https://attack.mitre.org/software/S1037) is Windows Script File (WSF) backdoor that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069), possibly since at least November 2021; there is also a [STARWHALE](https://attack.mitre.org/software/S1037) variant written in Golang with similar capabilities. Security researchers have also noted the use of [STARWHALE](https://attack.mitre.org/software/S1037) by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).[^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [STARWHALE](https://attack.mitre.org/software/S1037) can gather the computer name of an infected host.[^3] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to create the following Windows service to establish persistence on an infected host: `sc create Windowscarpstss binpath= "cmd.exe /c cscript.exe c:\\windows\\system32\\w7_1.wsf humpback_whale" start= "auto" obj= "LocalSystem"`.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [STARWHALE](https://attack.mitre.org/software/S1037) can exfiltrate collected data to its C2 servers.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [STARWHALE](https://attack.mitre.org/software/S1037) can establish persistence by installing itself in the startup folder, whereas the GO variant has created a `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\OutlookM` registry key.[^1] [^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to contact actor-controlled C2 servers via HTTP.[^3] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [STARWHALE](https://attack.mitre.org/software/S1037) can gather the username from an infected host.[^3] [^1]   |
| [[Malicious File\|T1204.002]] | Malicious File | [STARWHALE](https://attack.mitre.org/software/S1037) has relied on victims opening a malicious Excel file for execution.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [STARWHALE](https://attack.mitre.org/software/S1037) can use the VBScript function `GetRef` as part of its persistence mechanism.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to collect the IP address of an infected host.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [STARWHALE](https://attack.mitre.org/software/S1037) has been obfuscated with hex-encoded strings.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to execute commands via `cmd.exe`.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to hex-encode collected data from an infected host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [STARWHALE](https://attack.mitre.org/software/S1037) can collect data from an infected local host.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [STARWHALE](https://attack.mitre.org/software/S1037) has stored collected data in a file called `stari.txt`.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^2]: CANOPY


[^3]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


