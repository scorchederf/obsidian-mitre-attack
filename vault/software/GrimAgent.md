---
aliases: 
    - S0632
    
mitre-attack: https://attack.mitre.org/software/S0632
---

## S0632

[GrimAgent](https://attack.mitre.org/software/S0632) is a backdoor that has been used before the deployment of [Ryuk](https://attack.mitre.org/software/S0446) ransomware since at least 2020; it is likely used by [FIN6](https://attack.mitre.org/groups/G0037) and [Wizard Spider](https://attack.mitre.org/groups/G0102).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [GrimAgent](https://attack.mitre.org/software/S0632) can set persistence with a Registry run key.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GrimAgent](https://attack.mitre.org/software/S0632) can use the Windows Command Shell to execute commands, including its own removal.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to set persistence using the Task Scheduler.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [GrimAgent](https://attack.mitre.org/software/S0632) can collect data and files from a compromised host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) can identify the user id on a target machine.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [GrimAgent](https://attack.mitre.org/software/S0632) can use a hardcoded server public RSA key to encrypt the first request to C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to enumerate files and directories on a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to download and execute additional payloads.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) can enumerate the IP and domain of a target system.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [GrimAgent](https://attack.mitre.org/software/S0632) can base64 encode C2 replies.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [GrimAgent](https://attack.mitre.org/software/S0632) can use an AES key to encrypt C2 communications.[^1]  |
| [[Native API\|T1106]] | Native API | [GrimAgent](https://attack.mitre.org/software/S0632) can use Native API including `GetProcAddress` and `ShellExecuteW`.[^1]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [GrimAgent](https://attack.mitre.org/software/S0632) uses the last 64 bytes of the binary to compute a mutex name. If the generated name is invalid, it will default to the generic `mymutex`.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) has used `Accept-Language` to identify hosts in the United Kingdom, United States, France, and Spain.[^1]   |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [GrimAgent](https://attack.mitre.org/software/S0632) can sleep for 195 - 205 seconds after payload execution and before deleting its task.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) can identify the country code on a compromised host.[^1]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [GrimAgent](https://attack.mitre.org/software/S0632) can delete previously created tasks on a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [GrimAgent](https://attack.mitre.org/software/S0632) can use a decryption algorithm for strings based on Rotate on Right (RoR) and Rotate on Left (RoL) functionality.[^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [GrimAgent](https://attack.mitre.org/software/S0632)  can pad C2 messages with random generated values.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [GrimAgent](https://attack.mitre.org/software/S0632) can delete old binaries on a compromised host.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [GrimAgent](https://attack.mitre.org/software/S0632) has used Rotate on Right (RoR) and Rotate on Left (RoL) functionality to encrypt strings.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to use HTTP for C2 communications.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [GrimAgent](https://attack.mitre.org/software/S0632) can collect the OS, and build version on a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [GrimAgent](https://attack.mitre.org/software/S0632) has sent data related to a compromise host over its C2 channel.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to add bytes to change the file hash.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN6\|G0037]] | FIN6 |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


