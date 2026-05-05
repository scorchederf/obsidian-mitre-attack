---
aliases: 
    - S0612
    
mitre-attack: https://attack.mitre.org/software/S0612
---

## S0612

[WastedLocker](https://attack.mitre.org/software/S0612) is a ransomware family attributed to [Indrik Spider](https://attack.mitre.org/groups/G0119) that has been used since at least May 2020. [WastedLocker](https://attack.mitre.org/software/S0612) has been used against a broad variety of sectors, including manufacturing, information technology, and media.[^1] [^2] [^6]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [WastedLocker](https://attack.mitre.org/software/S0612) created and established a service that runs until the encryption process is complete.[^2]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [WastedLocker](https://attack.mitre.org/software/S0612) has copied a random file from the Windows System32 folder to the `%APPDATA%` location under a different hidden filename.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [WastedLocker](https://attack.mitre.org/software/S0612) can delete shadow volumes.[^1] [^2] [^6]   |
| [[Modify Registry\|T1112]] | Modify Registry | [WastedLocker](https://attack.mitre.org/software/S0612) can modify registry values within the `Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry key.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [WastedLocker](https://attack.mitre.org/software/S0612) checked if UCOMIEnumConnections and IActiveScriptParseProcedure32 Registry keys were detected as part of its anti-analysis technique.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [WastedLocker](https://attack.mitre.org/software/S0612) can encrypt data and leave a ransom note.[^1] [^2] [^6]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WastedLocker](https://attack.mitre.org/software/S0612) has used [cmd](https://attack.mitre.org/software/S0106) to execute commands on the system.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [WastedLocker](https://attack.mitre.org/software/S0612) can perform a UAC bypass if it is not executed with administrator rights or if the infected host runs Windows Vista or later.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [WastedLocker](https://attack.mitre.org/software/S0612) checks for specific registry keys related to the `UCOMIEnumConnections` and `IActiveScriptParseProcedure32` interfaces.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [WastedLocker](https://attack.mitre.org/software/S0612) contains junk code to increase its entropy and hide the actual code.[^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [WastedLocker](https://attack.mitre.org/software/S0612) can enumerate removable drives prior to the encryption process.[^6]  |
| [[Native API\|T1106]] | Native API | [WastedLocker](https://attack.mitre.org/software/S0612)'s custom crypter, CryptOne, leveraged the VirtualAlloc() API function to help execute the payload.[^2]  |
| [[DLL\|T1574.001]] | DLL |  [WastedLocker](https://attack.mitre.org/software/S0612) has performed DLL hijacking before execution.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WastedLocker](https://attack.mitre.org/software/S0612) can enumerate files and directories just prior to encryption.[^2]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [WastedLocker](https://attack.mitre.org/software/S0612) has the ability to save and execute files as an alternate data stream (ADS).[^6]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [WastedLocker](https://attack.mitre.org/software/S0612) can identify network adjacent and accessible drives.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WastedLocker](https://attack.mitre.org/software/S0612)'s custom cryptor, CryptOne, used an XOR based algorithm to decrypt the payload.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [WastedLocker](https://attack.mitre.org/software/S0612) can execute itself as a service.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [WastedLocker](https://attack.mitre.org/software/S0612) payload includes encrypted strings stored within the .bss section of the binary file.[^2]     |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [WastedLocker](https://attack.mitre.org/software/S0612) has a command to take ownership of a file and reset the ACL permissions using the `takeown.exe /F filepath` command.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Indrik Spider\|G0119]] | Indrik Spider |



## References

[^1]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


[^2]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^3]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^4]: [Crowdstrike EvilCorp March 2021](https://www.crowdstrike.com/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)


[^5]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)


[^6]: [Sentinel Labs WastedLocker July 2020](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)


[^7]: WastedLocker


