---
aliases: 
    - S0662
    
mitre-attack: https://attack.mitre.org/software/S0662
---

## S0662

[RCSession](https://attack.mitre.org/software/S0662) is a backdoor written in C++ that has been in use since at least 2018 by [Mustang Panda](https://attack.mitre.org/groups/G0129) and by [Threat Group-3390](https://attack.mitre.org/groups/G0027) (Type II Backdoor).[^1] [^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [RCSession](https://attack.mitre.org/software/S0662) can use an encrypted beacon to check in with C2.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [RCSession](https://attack.mitre.org/software/S0662) can launch itself from a hollowed svchost.exe process.[^1] [^2] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RCSession](https://attack.mitre.org/software/S0662) can identify processes based on PID.[^4]  |
| [[Msiexec\|T1218.007]] | Msiexec | [RCSession](https://attack.mitre.org/software/S0662) has the ability to execute inside the msiexec.exe process.[^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RCSession](https://attack.mitre.org/software/S0662) can capture screenshots from a compromised host.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [RCSession](https://attack.mitre.org/software/S0662) has the ability to capture keystrokes on a compromised host.[^2] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RCSession](https://attack.mitre.org/software/S0662) has the ability to drop additional files to an infected machine.[^4]  |
| [[Native API\|T1106]] | Native API | [RCSession](https://attack.mitre.org/software/S0662) can use WinSock API for communication including `WSASend` and `WSARecv`.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RCSession](https://attack.mitre.org/software/S0662) can use HTTP in C2 communications.[^2] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RCSession](https://attack.mitre.org/software/S0662) can gather system owner information, including user and administrator privileges.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RCSession](https://attack.mitre.org/software/S0662) can remove files from a targeted system.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RCSession](https://attack.mitre.org/software/S0662) has the ability to modify a Registry Run key to establish persistence.[^2] [^4]  |
| [[Compression\|T1027.015]] | Compression | [RCSession](https://attack.mitre.org/software/S0662) can compress and obfuscate its strings to evade detection on a compromised host.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [RCSession](https://attack.mitre.org/software/S0662) can collect data from a compromised host.[^4] [^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [RCSession](https://attack.mitre.org/software/S0662) has the ability to use TCP and UDP in C2 communications.[^2] [^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RCSession](https://attack.mitre.org/software/S0662) can gather system information from a compromised host.[^4]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [RCSession](https://attack.mitre.org/software/S0662) can store its obfuscated configuration file in the Registry under `HKLM\SOFTWARE\Plus` or `HKCU\SOFTWARE\Plus`.[^2] [^4]  |
| [[Masquerading\|T1036]] | Masquerading | [RCSession](https://attack.mitre.org/software/S0662) has used a file named English.rtf to appear benign on victim hosts.[^1] [^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [RCSession](https://attack.mitre.org/software/S0662) can write its configuration file to the Registry.[^2] [^4]  |
| [[DLL\|T1574.001]] | DLL | [RCSession](https://attack.mitre.org/software/S0662) can be installed via DLL side-loading.[^1] [^2] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RCSession](https://attack.mitre.org/software/S0662) can use `cmd.exe` for execution on compromised hosts.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [RCSession](https://attack.mitre.org/software/S0662) can bypass UAC to escalate privileges.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)


[^2]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^3]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^4]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


