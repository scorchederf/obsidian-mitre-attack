---
aliases: 
    - S0250
    
mitre-attack: https://attack.mitre.org/software/S0250
---

## S0250

[Koadic](https://attack.mitre.org/software/S0250) is a Windows post-exploitation framework and penetration testing tool that is publicly available on GitHub. [Koadic](https://attack.mitre.org/software/S0250) has several options for staging payloads and creating implants, and performs most of its operations using Windows Script Host.[^1] [^6] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the contents of the IP routing table as well as information about the Windows domain.[^1] [^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Koadic](https://attack.mitre.org/software/S0250) can obtain the OS version and build, computer name, and processor architecture from a compromised host.[^7]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (VBScript) and runs arbitrary shellcode .[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [Koadic](https://attack.mitre.org/software/S0250) can use mshta to serve additional payloads and to help schedule tasks for persistence.[^1] [^7]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Koadic](https://attack.mitre.org/software/S0250) can perform process injection by using a reflective DLL.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Koadic](https://attack.mitre.org/software/S0250) can use Regsvr32 to execute additional payloads.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Koadic](https://attack.mitre.org/software/S0250) can identify logged in users across the domain and views user sessions.[^1] [^7]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Koadic](https://attack.mitre.org/software/S0250) has used the command `Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden` to hide its window.[^7]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by dumping SAM/SECURITY hive.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Koadic](https://attack.mitre.org/software/S0250) can download additional files and tools.[^1] [^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Koadic](https://attack.mitre.org/software/S0250) has used HTTP for C2 communications.[^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Koadic](https://attack.mitre.org/software/S0250) can use WMI to execute commands.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Koadic](https://attack.mitre.org/software/S0250) has used PowerShell to establish persistence.[^7]   |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the current content of the user clipboard.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Koadic](https://attack.mitre.org/software/S0250) has 2 methods for elevating integrity. It can bypass UAC through `eventvwr.exe` and `sdclt.exe`.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Koadic](https://attack.mitre.org/software/S0250) can scan for open TCP ports on the target network.[^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Koadic](https://attack.mitre.org/software/S0250) can enable remote desktop on the victim's machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Koadic](https://attack.mitre.org/software/S0250) can open an interactive command-shell to perform command line functions on victim machines. [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (Jscript) and to run arbitrary shellcode.[^1] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Koadic](https://attack.mitre.org/software/S0250) can obtain a list of directories.[^7]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Koadic](https://attack.mitre.org/software/S0250) has added persistence to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` Registry key.[^7]  |
| [[NTDS\|T1003.003]] | NTDS | [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by gathering domain controller hashes from NTDS.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Koadic](https://attack.mitre.org/software/S0250) can run a command on another machine using [PsExec](https://attack.mitre.org/software/S0029).[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Koadic](https://attack.mitre.org/software/S0250) can download files off the target system to send back to the server.[^1] [^7]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Koadic](https://attack.mitre.org/software/S0250) can use SSL and TLS for communications.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Koadic](https://attack.mitre.org/software/S0250) can scan local network for open SMB.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Koadic](https://attack.mitre.org/software/S0250) can use Rundll32 to execute additional payloads.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Koadic](https://attack.mitre.org/software/S0250) has used scheduled tasks to add persistence.[^7]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[Sidewinder\|G0121]] | Sidewinder |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [Github Koadic](https://github.com/offsecginger/koadic)


[^2]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^3]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^4]: [Reaqta MuddyWater November 2017](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)


[^5]: Koadic


[^6]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^7]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


