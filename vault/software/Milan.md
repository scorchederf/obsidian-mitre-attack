---
aliases: 
    - S1015
    
mitre-attack: https://attack.mitre.org/software/S1015
---

## S1015

[Milan](https://attack.mitre.org/software/S1015) is a backdoor implant based on [DanBot](https://attack.mitre.org/software/S1014) that was written in Visual C++ and .NET. [Milan](https://attack.mitre.org/software/S1015) has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2020.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Milan](https://attack.mitre.org/software/S1015) can establish persistence on a targeted host with scheduled tasks.[^3] [^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Milan](https://attack.mitre.org/software/S1015) has saved files prior to upload from a compromised host to folders beginning with the characters `a9850d2f`.[^3]  |
| [[DNS\|T1071.004]] | DNS | [Milan](https://attack.mitre.org/software/S1015) has the ability to use DNS for C2 communications.[^3] [^2] [^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Milan](https://attack.mitre.org/software/S1015) can enumerate the targeted machine's name and GUID.[^3] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Milan](https://attack.mitre.org/software/S1015) can run `C:\Windows\system32\cmd.exe /c cmd /c ipconfig /all 2>&1` to discover network settings.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Milan](https://attack.mitre.org/software/S1015) can identify users registered to a targeted machine.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Milan](https://attack.mitre.org/software/S1015) can encode files containing information about the targeted system.[^3] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Milan](https://attack.mitre.org/software/S1015) has received files from C2 and stored them in log folders beginning with the character sequence `a9850d2f`.[^3]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Milan](https://attack.mitre.org/software/S1015) can use a COM component to generate scheduled tasks.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Milan](https://attack.mitre.org/software/S1015) can use HTTPS for communication with C2.[^3] [^2] [^4]  |
| [[Query Registry\|T1012]] | Query Registry | [Milan](https://attack.mitre.org/software/S1015) can query `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid` to retrieve the machine GUID.[^4]  |
| [[Masquerading\|T1036]] | Masquerading | [Milan](https://attack.mitre.org/software/S1015) has used an executable named `companycatalogue` to appear benign.[^3]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Milan](https://attack.mitre.org/software/S1015) can use a custom protocol tunneled through DNS or HTTP.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Milan](https://attack.mitre.org/software/S1015) can use `cmd.exe` for discovery actions on a targeted system.[^3]  |
| [[Native API\|T1106]] | Native API | [Milan](https://attack.mitre.org/software/S1015) can use the API `DnsQuery_A` for DNS resolution.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Milan](https://attack.mitre.org/software/S1015) can upload files from a compromised host.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [Milan](https://attack.mitre.org/software/S1015) has run `C:\Windows\system32\cmd.exe /c cmd /c dir c:\users\ /s 2>&1` to discover local accounts.[^3]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Milan](https://attack.mitre.org/software/S1015) can use hardcoded domains as an input for domain generation algorithms.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Milan](https://attack.mitre.org/software/S1015) can delete files via `C:\Windows\system32\cmd.exe /c ping 1.1.1.1 -n 1 -w 3000 > Nul & rmdir /s /q`.[^3]  |
| [[Double File Extension\|T1036.007]] | Double File Extension | [Milan](https://attack.mitre.org/software/S1015) has used an executable named `companycatalog.exe.config` to appear benign.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HEXANE\|G1001]] | HEXANE |



## References

[^1]: James


[^2]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^3]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^4]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


