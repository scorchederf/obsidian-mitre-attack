---
aliases: 
    - S0456
    
mitre-attack: https://attack.mitre.org/software/S0456
---

## S0456

[Aria-body](https://attack.mitre.org/software/S0456) is a custom backdoor that has been used by [Naikon](https://attack.mitre.org/groups/G0019) since approximately 2017.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Aria-body](https://attack.mitre.org/software/S0456) has used TCP in C2 communications.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to enumerate loaded modules for a process.[^1] . |
| [[Native API\|T1106]] | Native API | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to launch files using `ShellExecute`.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to use a DGA for C2 communications.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to decrypt the loader configuration and payload DLL.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to collect data from USB devices.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the location, public IP address, and domain name on a compromised host.[^1]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to execute a process using `runas`.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Aria-body](https://attack.mitre.org/software/S0456) has used HTTP in C2 communications.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to capture screenshots on compromised hosts.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the username on a compromised host.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the titles of running windows on a compromised host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the hostname, computer name, Windows version, processor speed, and machine GUID on a compromised host.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to delete files and directories on compromised hosts.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Aria-body](https://attack.mitre.org/software/S0456) has established persistence via the Startup folder or Run Registry key.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Aria-body](https://attack.mitre.org/software/S0456) has used an encrypted configuration file for its loader.[^1]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to duplicate a token from ntprint.exe.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to use a reverse SOCKS proxy module.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to download additional payloads from C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to gather metadata from a file and to search for file and directory names.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to inject itself into another process such as rundll32.exe and dllhost.exe.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify disk information on a compromised host.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Aria-body](https://attack.mitre.org/software/S0456) has used ZIP to compress data gathered on a compromised host.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to gather TCP and UDP table status listings.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^2]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


