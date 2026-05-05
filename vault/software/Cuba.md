---
aliases: 
    - S0625
    
mitre-attack: https://attack.mitre.org/software/S0625
---

## S0625

<br>[Cuba](https://attack.mitre.org/software/S0625) is a Windows-based ransomware family that has been used against financial institutions, technology, and logistics organizations in North and South America as well as Europe since at least December 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Cuba](https://attack.mitre.org/software/S0625) can enumerate local drives, disk type, and disk free space.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Cuba](https://attack.mitre.org/software/S0625) can modify services by using the `OpenService` and `ChangeServiceConfig` functions.[^1]   |
| [[Software Packing\|T1027.002]] | Software Packing | [Cuba](https://attack.mitre.org/software/S0625) has a packed payload when delivered.[^1]   |
| [[Native API\|T1106]] | Native API | [Cuba](https://attack.mitre.org/software/S0625) has used several built-in API functions for discovery like GetIpNetTable and NetShareEnum.[^1]   |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Cuba](https://attack.mitre.org/software/S0625) can check if Russian language is installed on the infected machine by using the function `GetKeyboardLayoutList`.[^1]   |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Cuba](https://attack.mitre.org/software/S0625) has the ability to encrypt system data and add the ".cuba" extension to encrypted files.[^1]   |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Cuba](https://attack.mitre.org/software/S0625) can discover shared resources using the `NetShareEnum` API call.[^1]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cuba](https://attack.mitre.org/software/S0625) has used `cmd.exe /c` and batch files for execution.[^1]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Cuba](https://attack.mitre.org/software/S0625) can use the command `cmd.exe /c del` to delete its artifacts from the system.[^1]   |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Cuba](https://attack.mitre.org/software/S0625) loaded the payload into memory using PowerShell.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Cuba](https://attack.mitre.org/software/S0625) has been dropped onto systems and used for lateral movement via obfuscated PowerShell scripts.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cuba](https://attack.mitre.org/software/S0625) can enumerate files by using a variety of functions.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cuba](https://attack.mitre.org/software/S0625) can download files from its C2 server.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Cuba](https://attack.mitre.org/software/S0625) logs keystrokes via polling by using `GetKeyState` and `VkKeyScan` functions.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Cuba](https://attack.mitre.org/software/S0625) has used multiple layers of obfuscation to avoid analysis, including its Base64 encoded payload.[^1]   |
| [[Service Stop\|T1489]] | Service Stop | [Cuba](https://attack.mitre.org/software/S0625) has a hardcoded list of services and processes to terminate.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Cuba](https://attack.mitre.org/software/S0625) can retrieve the ARP cache from the local system by using `GetIpNetTable`.[^1]   |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Cuba](https://attack.mitre.org/software/S0625) can use the function `GetIpNetTable` to recover the last connections to the victim's machine.[^1]   |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Cuba](https://attack.mitre.org/software/S0625) can query service status using `QueryServiceStatusEx` function.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Cuba](https://attack.mitre.org/software/S0625) can enumerate processes running on a victim's machine.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Cuba](https://attack.mitre.org/software/S0625) has used `SeDebugPrivilege` and `AdjustTokenPrivileges` to elevate privileges.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Cuba](https://attack.mitre.org/software/S0625) has been disguised as legitimate 360 Total Security Antivirus and OpenVPN programs.[^1]   |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Cuba](https://attack.mitre.org/software/S0625) has executed hidden PowerShell windows.[^1]   |




## References

[^1]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^2]: Cuba


