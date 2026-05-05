---
aliases: 
    - S1065
    
mitre-attack: https://attack.mitre.org/software/S1065
---

## S1065

 [Woody RAT](https://attack.mitre.org/software/S1065) is a remote access trojan (RAT) that has been used since at least August 2021 against Russian organizations.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can list all files and their associated attributes, including filename, type, owner, creation time, last access time, last write time, size, and permissions.[^1]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve a list of user accounts and usernames from an infected machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Woody RAT](https://attack.mitre.org/software/S1065) can execute commands using `cmd.exe`.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Woody RAT](https://attack.mitre.org/software/S1065) can create a suspended notepad process and write shellcode to delete a file into the suspended process using `NtWriteVirtualMemory`.[^1]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve the following information from an infected machine: OS, architecture, computer name, OS build version, and environment variables.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Woody RAT](https://attack.mitre.org/software/S1065) can execute PowerShell commands and scripts with the use of .NET DLL, `WoodyPowerSession`.[^1]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Woody RAT](https://attack.mitre.org/software/S1065) can exfiltrate files from an infected machine to its C2 server.[^1]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can call `NtQuerySystemProcessInformation` with `SystemProcessInformation` to enumerate all running processes, including associated information such as PID, parent PID, image name, and owner.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Woody RAT](https://attack.mitre.org/software/S1065) has used Base64 encoded strings and scripts.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve information about storage drives from an infected machine.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can detect Avast Software, Doctor Web, Kaspersky, AVG, ESET, and Sophos antivirus programs.[^1]  |
| [[Account Discovery\|T1087]] | Account Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can identify administrator accounts on an infected machine.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Woody RAT](https://attack.mitre.org/software/S1065) can collect information from a compromised host.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Woody RAT](https://attack.mitre.org/software/S1065) has the ability to take a screenshot of the infected host desktop using Windows GDI+.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Woody RAT](https://attack.mitre.org/software/S1065) can deobfuscate Base64-encoded strings and scripts.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Woody RAT](https://attack.mitre.org/software/S1065) can download files from its C2 server, including the .NET DLLs, `WoodySharpExecutor` and `WoodyPowerSession`.[^1]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Woody RAT](https://attack.mitre.org/software/S1065) can use RSA-4096 to encrypt data sent to its C2 server.[^1]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Woody RAT](https://attack.mitre.org/software/S1065) has the ability to delete itself from disk by creating a suspended notepad process and writing shellcode to delete a file into the suspended process using `NtWriteVirtualMemory`.[^1]   |
| [[Process Injection\|T1055]] | Process Injection | [Woody RAT](https://attack.mitre.org/software/S1065) can inject code into a targeted process by writing to the remote memory of an infected system and then create a remote thread.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Woody RAT](https://attack.mitre.org/software/S1065) can communicate with its C2 server using HTTP requests.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Woody RAT](https://attack.mitre.org/software/S1065) has been delivered via malicious Word documents and archive files.[^1]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can make `Ping` GET HTTP requests to its C2 server at regular intervals for network connectivity checks.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Woody RAT](https://attack.mitre.org/software/S1065) has relied on users opening a malicious email attachment for execution.[^1]  |
| [[Native API\|T1106]] | Native API | [Woody RAT](https://attack.mitre.org/software/S1065) can use multiple native APIs, including `WriteProcessMemory`, `CreateProcess`, and `CreateRemoteThread` for process injection.[^1]    |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Woody RAT](https://attack.mitre.org/software/S1065) has suppressed all error reporting by calling `SetErrorMode` with 0x8007 as a parameter.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve network interface and proxy information.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Woody RAT](https://attack.mitre.org/software/S1065) has relied on CVE-2022-30190 (Follina) for execution during delivery.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Woody RAT](https://attack.mitre.org/software/S1065) can search registry keys to identify antivirus programs on an compromised host.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Woody RAT](https://attack.mitre.org/software/S1065) can collect .NET, PowerShell, and Python information from an infected host.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Woody RAT](https://attack.mitre.org/software/S1065) can use AES-CBC to encrypt data sent to its C2 server.[^1]   |




## References

[^1]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


