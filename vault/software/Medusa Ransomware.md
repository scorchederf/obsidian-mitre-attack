---
aliases: 
    - S1244
    
mitre-attack: https://attack.mitre.org/software/S1244
---

## S1244

[Medusa Ransomware](https://attack.mitre.org/software/S1244) has been utilized in attacks since at least 2021. [Medusa Ransomware](https://attack.mitre.org/software/S1244) has been known to be utilized in conjunction with living off the land techniques and remote management software. [Medusa Ransomware](https://attack.mitre.org/software/S1244) has been used in campaigns associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. [Medusa Ransomware](https://attack.mitre.org/software/S1244) software was initially a closed ransomware variant which later evolved to a Ransomware as a Service (RaaS). [Medusa Ransomware](https://attack.mitre.org/software/S1244) has impacted victims from a diverse range of sectors within a multitude of countries, and it is assessed [Medusa Ransomware](https://attack.mitre.org/software/S1244) is used in an opportunistic manner.[^4] [^2] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has identified networked drives.[^3] [^1] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has the capability to detect security solutions for termination or deletion within the victim device using hard-coded lists of strings containing security product executables.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has utilized XOR encrypted strings.[^3] [^2]  |
| [[Selective Exclusion\|T1679]] | Selective Exclusion | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has avoided specified files, file extensions and folders to ensure successful execution of the payload and continued operations of the impacted device.[^3] [^1] [^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has leveraged an encoded list of services that it designates for termination.[^3] [^1] [^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has deleted recovery files such as shadow copies using `vssadmin.exe`.[^3] [^4] [^1] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has created a new PowerShell process using the `CreateProcessA` API.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has utilized an encoded list of the processes that it detects and terminates.[^3] [^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has the ability to delete itself after execution.[^1]  [Medusa Ransomware](https://attack.mitre.org/software/S1244) also has the ability to delete itself after execution through the command `cmd /c ping localhost -n 3 > nul & del`.[^3] [^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has enumerated logical drives on infected hosts.[^2]  |
| [[Service Stop\|T1489]] | Service Stop | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has the capability to terminate services related to backups, security, databases, communication, filesharing and websites.[^4] [^1] [^2]  [Medusa Ransomware](https://attack.mitre.org/software/S1244) has also utilized the `taskkill /F /IM <process> /T` command to stop targeted processes and `net stop <process>` command to stop designated services.[^1] [^2]  |
| [[Native API\|T1106]] | Native API | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has leveraged Windows Native API functions to execute payloads.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has decoded XOR encrypted strings prior to execution in memory.[^3] [^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has utilized the `ShowWindow` function to hide current window.[^2]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has leveraged the `CreatePipe` API to enable inter-process communication.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has searched for files within the victim environment for encryption and exfiltration.[^3] [^4] [^2]   [Medusa Ransomware](https://attack.mitre.org/software/S1244) has also identified files associated with remote management services.[^3] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has used `cmd.exe` to execute command on an infected host.[^3] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has collected data from the SMBIOS firmware table using `GetSystemFirmwareTable`.[^2]    |
| [[PowerShell\|T1059.001]] | PowerShell | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has launched PowerShell scripts for execution and defense evasion.[^3] [^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has discovered device uptime through `GetTickCount()`.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has terminated antivirus services utilizing the gaze.exe executable.[^3]  [Medusa Ransomware](https://attack.mitre.org/software/S1244) has also terminated antivirus services utilizing PowerShell scripts.[^3] [^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has encrypted files using AES-256 encryption, which then appends the file extension “.medusa” to encrypted files and leaves a ransomware note named “!READ_ME_MEDUSA!!!.txt.”[^3] [^4] [^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Medusa Group\|G1051]] | Medusa Group |



## References

[^1]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^2]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^3]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^4]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


