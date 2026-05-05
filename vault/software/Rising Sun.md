---
aliases: 
    - S0448
    
mitre-attack: https://attack.mitre.org/software/S0448
---

## S0448

[Rising Sun](https://attack.mitre.org/software/S0448) is a modular backdoor that was used extensively in [Operation Sharpshooter](https://attack.mitre.org/campaigns/C0013) between 2017 and 2019. [Rising Sun](https://attack.mitre.org/software/S0448) infected at least 87 organizations around the world, including nuclear, defense, energy, and financial service companies. Security researchers assessed [Rising Sun](https://attack.mitre.org/software/S0448) included some source code from [Lazarus Group](https://attack.mitre.org/groups/G0032)'s Trojan Duuzer.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [Rising Sun](https://attack.mitre.org/software/S0448) can delete files and artifacts it creates.[^2] 	 |
| [[Data from Local System\|T1005]] | Data from Local System | [Rising Sun](https://attack.mitre.org/software/S0448) has collected data and files from a compromised host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can detect the username of the infected host.[^2] 	 |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Rising Sun](https://attack.mitre.org/software/S0448) can archive data using RC4 encryption and Base64 encoding prior to exfiltration.[^2] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Rising Sun](https://attack.mitre.org/software/S0448) has decrypted itself using a single-byte XOR scheme. Additionally, [Rising Sun](https://attack.mitre.org/software/S0448) can decrypt its configuration data at runtime.[^2] 	 |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can detect the computer name and operating system.[^2] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Configuration data used by [Rising Sun](https://attack.mitre.org/software/S0448) has been encrypted using an RC4 stream algorithm.[^2] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Rising Sun](https://attack.mitre.org/software/S0448) has used HTTP and HTTPS for command and control.[^2]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Rising Sun](https://attack.mitre.org/software/S0448) can clear a memory blog in the process by overwriting it with junk bytes.[^2] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate all running processes and process information on an infected machine.[^2] 	 |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Rising Sun](https://attack.mitre.org/software/S0448) variants can use SSL for encrypting C2 communications.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Rising Sun](https://attack.mitre.org/software/S0448) can send data gathered from the infected machine via HTTP POST request to the C2.[^2] 	 |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can test a connection to a specified network IP address over a specified port number.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Rising Sun](https://attack.mitre.org/software/S0448) has executed commands using `cmd.exe /c “<command> > <%temp%>\AM<random>. tmp” 2>&1`.[^2]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate information about files from the infected system, including file size, attributes, creation time, last access time, and write time. [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate the compilation timestamp of Windows executable files.[^2] 	 |
| [[Query Registry\|T1012]] | Query Registry | [Rising Sun](https://attack.mitre.org/software/S0448) has identified the OS product name from a compromised host by searching the registry for `SOFTWARE\MICROSOFT\Windows NT\ CurrentVersion | ProductName`.[^2]  |
| [[Native API\|T1106]] | Native API | [Rising Sun](https://attack.mitre.org/software/S0448) used dynamic API resolutions to various Windows APIs by leveraging `LoadLibrary()` and `GetProcAddress()`.[^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Rising Sun](https://attack.mitre.org/software/S0448) can modify file attributes to hide files.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can detect drive information, including drive type, total number of bytes on disk, total number of free bytes on disk, and name of a specified volume.[^2] 	 |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Rising Sun](https://attack.mitre.org/software/S0448) can detect network adapter and IP address information.[^2] 	 |




## References

[^1]: [Bleeping Computer Op Sharpshooter March 2019](https://www.bleepingcomputer.com/news/security/op-sharpshooter-connected-to-north-koreas-lazarus-group/)


[^2]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


