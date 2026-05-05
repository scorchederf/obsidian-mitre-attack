---
aliases: 
    - S0666
    
mitre-attack: https://attack.mitre.org/software/S0666
---

## S0666

[Gelsemium](https://attack.mitre.org/software/S0666) is a modular malware comprised of a dropper (Gelsemine), a loader (Gelsenicine), and main (Gelsevirine) plug-ins written using the Microsoft Foundation Class (MFC) framework. [Gelsemium](https://attack.mitre.org/software/S0666) has been used by the Gelsemium group since at least 2014.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Gelsemium](https://attack.mitre.org/software/S0666) can use dynamic DNS domain names in C2.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Gelsemium](https://attack.mitre.org/software/S0666) can decompress and decrypt DLLs and shellcode.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Gelsemium](https://attack.mitre.org/software/S0666) can bypass UAC to elevate process privileges on a compromised host.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to use TCP and UDP in C2 communications.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Gelsemium](https://attack.mitre.org/software/S0666) can drop itself in `C:\Windows\System32\spool\prtprocs\x64\winprint.dll` as an alternative Print Processor to be loaded automatically when the spoolsv Windows service starts.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Gelsemium](https://attack.mitre.org/software/S0666) can delete its dropper component from the targeted system.[^2]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Gelsemium](https://attack.mitre.org/software/S0666) can use custom shellcode to map embedded DLLs into memory.[^2]  |
| [[Print Processors\|T1547.012]] | Print Processors | [Gelsemium](https://attack.mitre.org/software/S0666) can drop itself in `C:\Windows\System32\spool\prtprocs\x64\winprint.dll` to be loaded automatically by the spoolsv Windows service.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gelsemium](https://attack.mitre.org/software/S0666) can set persistence with a Registry run key.[^2]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Gelsemium](https://attack.mitre.org/software/S0666) can use junk code to generate random activity to obscure malware behavior.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Gelsemium](https://attack.mitre.org/software/S0666) can store its components in the Registry.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Gelsemium](https://attack.mitre.org/software/S0666) can modify the Registry to store its components.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Gelsemium](https://attack.mitre.org/software/S0666) can enumerate running processes.[^2]  |
| [[DNS\|T1071.004]] | DNS | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to use DNS in communication with C2.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Gelsemium](https://attack.mitre.org/software/S0666) can retrieve data from specific Windows directories, as well as open random files as part of [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497).[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Gelsemium](https://attack.mitre.org/software/S0666) can determine the operating system and whether a targeted machine has a 32 or 64 bit architecture.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Gelsemium](https://attack.mitre.org/software/S0666) can check for the presence of specific security products.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gelsemium](https://attack.mitre.org/software/S0666) can download additional plug-ins to a compromised host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to distinguish between a standard user and an administrator on a compromised host.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Gelsemium](https://attack.mitre.org/software/S0666) can use multiple domains and protocols in C2.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Gelsemium](https://attack.mitre.org/software/S0666) can collect data from a compromised host.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to inject DLLs into specific processes.[^2]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Gelsemium](https://attack.mitre.org/software/S0666) can use token manipulation to bypass UAC on Windows7 systems.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to perform timestomping of files on targeted systems.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Gelsemium](https://attack.mitre.org/software/S0666) can open random files and Registry keys to obscure malware behavior from sandbox analysis.[^2]  |
| [[Native API\|T1106]] | Native API | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to use various Windows API functions to perform tasks.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Gelsemium](https://attack.mitre.org/software/S0666) can use HTTP/S in C2 communications.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Gelsemium](https://attack.mitre.org/software/S0666) can use a batch script to delete itself.[^2]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [Gelsemium](https://attack.mitre.org/software/S0666) has used unverified signatures on malicious DLLs.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Gelsemium](https://attack.mitre.org/software/S0666) can use junk code to hide functions and evade detection.[^2]  |
| [[Compression\|T1027.015]] | Compression | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to compress its components.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Gelsemium](https://attack.mitre.org/software/S0666) has named malicious binaries `serv.exe`, `winprint.dll`, and `chrome_elf.dll` and has set its persistence in the Registry with the key value `Chrome Update` to appear legitimate.[^2]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Gelsemium](https://attack.mitre.org/software/S0666) can use the `IARPUinstallerStringLauncher` COM interface are part of its UAC bypass process.[^2]  |




## References

[^1]: Gelsemine


[^2]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^3]: Gelsevirine


[^4]: Gelsenicine


