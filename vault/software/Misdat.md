---
aliases: 
    - S0083
    
mitre-attack: https://attack.mitre.org/software/S0083
---

## S0083

[Misdat](https://attack.mitre.org/software/S0083) is a backdoor that was used in [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) from 2010 to 2011.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Misdat](https://attack.mitre.org/software/S0083) saves itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Misdat](https://attack.mitre.org/software/S0083) is capable of running commands to obtain a list of files and directories, as well as enumerating logical drives.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Misdat](https://attack.mitre.org/software/S0083) has uploaded files and data to its C2 servers.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Misdat](https://attack.mitre.org/software/S0083) network traffic communicates over a raw socket.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Misdat](https://attack.mitre.org/software/S0083) has collected files and data from a compromised host.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Misdat](https://attack.mitre.org/software/S0083) is capable of deleting the backdoor file.[^2]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [Misdat](https://attack.mitre.org/software/S0083) is capable of deleting Registry keys used for persistence.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | The initial beacon packet for [Misdat](https://attack.mitre.org/software/S0083) contains the operating system version of the victim.[^2]  |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [Misdat](https://attack.mitre.org/software/S0083) has created registry keys for persistence, including `HKCU\Software\dnimtsoleht\StubPath`, `HKCU\Software\snimtsOleht\StubPath`, `HKCU\Software\Backtsaleht\StubPath`, `HKLM\SOFTWARE\Microsoft\Active Setup\Installed. Components\{3bf41072-b2b1-21c8-b5c1-bd56d32fbda7}`, and `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3ef41072-a2f1-21c8-c5c1-70c2c3bc7905}`.[^2]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Misdat](https://attack.mitre.org/software/S0083) network traffic is Base64-encoded plaintext.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Misdat](https://attack.mitre.org/software/S0083) is capable of downloading files from the C2.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Misdat](https://attack.mitre.org/software/S0083) is capable of providing shell functionality to the attacker to execute commands.[^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Misdat](https://attack.mitre.org/software/S0083) has attempted to detect if a compromised host had a Japanese keyboard via the Windows API call `GetKeyboardType`.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Misdat](https://attack.mitre.org/software/S0083) was typically packed using UPX.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | Many [Misdat](https://attack.mitre.org/software/S0083) samples were programmed using Borland Delphi, which will mangle the default PE compile timestamp of a file.[^2]  |
| [[Native API\|T1106]] | Native API | [Misdat](https://attack.mitre.org/software/S0083) has used Windows APIs, including `ExitWindowsEx` and `GetKeyboardType`.[^2]   |




## References

[^1]: [Microsoft DTC](https://technet.microsoft.com/en-us/library/cc759136(v=ws.10).aspx)


[^2]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


