---
aliases: 
    - S1019
    
mitre-attack: https://attack.mitre.org/software/S1019
---

## S1019

[Shark](https://attack.mitre.org/software/S1019) is a backdoor malware written in C# and .NET that is an updated version of [Milan](https://attack.mitre.org/software/S1015); it has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least July 2021.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Shark](https://attack.mitre.org/software/S1019)  can download additional files from its C2 via HTTP or DNS.[^2] [^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Shark](https://attack.mitre.org/software/S1019) has the ability to upload files from the compromised host over a DNS or HTTP C2 channel.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Shark](https://attack.mitre.org/software/S1019) can use encrypted and encoded files for C2 configuration.[^2] [^3]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Shark](https://attack.mitre.org/software/S1019) can pause C2 communications for a specified time.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Shark](https://attack.mitre.org/software/S1019) can query `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid` to retrieve the machine GUID.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Shark](https://attack.mitre.org/software/S1019) can collect the GUID of a targeted machine.[^2] [^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Shark](https://attack.mitre.org/software/S1019) has the ability to use `CMD` to execute commands.[^2] [^3]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Shark](https://attack.mitre.org/software/S1019) can update its configuration to use a different C2 server.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Shark](https://attack.mitre.org/software/S1019) can upload files to its C2.[^2] [^3]  |
| [[System Checks\|T1497.001]] | System Checks | [Shark](https://attack.mitre.org/software/S1019) can stop execution if the screen width of the targeted machine is not over 600 pixels.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Shark](https://attack.mitre.org/software/S1019) binaries have been named `audioddg.pdb` and `Winlangdb.pdb` in order to appear legitimate.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Shark](https://attack.mitre.org/software/S1019) can delete files downloaded to the compromised host.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Shark](https://attack.mitre.org/software/S1019) can extract and decrypt downloaded .zip files.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Shark](https://attack.mitre.org/software/S1019) has the ability to use HTTP in C2 communications.[^2] [^3]  |
| [[DNS\|T1071.004]] | DNS | [Shark](https://attack.mitre.org/software/S1019) can use DNS in C2 communications.[^2] [^3]  |
| [[Data Staged\|T1074]] | Data Staged | [Shark](https://attack.mitre.org/software/S1019) has stored information in folders named `U1` and `U2` prior to exfiltration.[^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Shark](https://attack.mitre.org/software/S1019) can send DNS C2 communications using a unique domain generation algorithm.[^2] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HEXANE\|G1001]] | HEXANE |



## References

[^1]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^2]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^3]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


