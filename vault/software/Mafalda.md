---
aliases: 
    - S1060
    
mitre-attack: https://attack.mitre.org/software/S1060
---

## S1060

[Mafalda](https://attack.mitre.org/software/S1060) is a flexible interactive implant that has been used by [Metador](https://attack.mitre.org/groups/G1013). Security researchers assess the [Mafalda](https://attack.mitre.org/software/S1060) name may be inspired by an Argentinian cartoon character that has been popular as a means of political commentary since the 1960s. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Port Knocking\|T1205.001]] | Port Knocking | [Mafalda](https://attack.mitre.org/software/S1060) can use port-knocking to authenticate itself to another implant called Cryshell to establish an indirect connection to the C2 server.[^1] [^2]  |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | [Mafalda](https://attack.mitre.org/software/S1060) can create a token for a different user.[^2]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Mafalda](https://attack.mitre.org/software/S1060) can establish an SSH connection from a compromised host to a server.[^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Mafalda](https://attack.mitre.org/software/S1060) can delete Windows Event logs by invoking the `OpenEventLogW` and `ClearEventLogW` functions.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Mafalda](https://attack.mitre.org/software/S1060) can encode data using Base64 prior to exfiltration.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Mafalda](https://attack.mitre.org/software/S1060) can execute shell commands using `cmd.exe`.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Mafalda](https://attack.mitre.org/software/S1060) can manipulate the system registry on a compromised host.[^2]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Mafalda](https://attack.mitre.org/software/S1060) can collect a Chrome encryption key used to protect browser cookies.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Mafalda](https://attack.mitre.org/software/S1060) can create a remote service, let it run once, and then delete it.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Mafalda](https://attack.mitre.org/software/S1060) can use raw TCP for C2.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Mafalda](https://attack.mitre.org/software/S1060) can place retrieved files into a destination directory.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Mafalda](https://attack.mitre.org/software/S1060) can collect files and information from a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Mafalda](https://attack.mitre.org/software/S1060) can decrypt files and data.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Mafalda](https://attack.mitre.org/software/S1060) can execute PowerShell commands on a compromised machine.[^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Mafalda](https://attack.mitre.org/software/S1060) can create a named pipe to listen for and send data to a named pipe-based C2 server.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can enumerate running processes on a machine.[^1]  |
| [[Input Capture\|T1056]] | Input Capture | [Mafalda](https://attack.mitre.org/software/S1060) can conduct mouse event logging.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mafalda](https://attack.mitre.org/software/S1060) can use HTTP for C2.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can use the `GetExtendedTcpTable` function to retrieve information about established TCP connections.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Mafalda](https://attack.mitre.org/software/S1060) can enumerate Registry keys with all subkeys and values.[^2]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can collect the contents of the `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\LocalState` file.[^1]   |
| [[Screen Capture\|T1113]] | Screen Capture | [Mafalda](https://attack.mitre.org/software/S1060) can take a screenshot of the target machine and save it to a file.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mafalda](https://attack.mitre.org/software/S1060) can send network system data and files to its C2 server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Mafalda](https://attack.mitre.org/software/S1060) can encrypt its C2 traffic with RC4.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can collect the computer name of a compromised host.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mafalda](https://attack.mitre.org/software/S1060) can download additional files onto the compromised host.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can use the `GetAdaptersInfo` function to retrieve information about network adapters and the `GetIpNetTable` function to retrieve the IPv4 to physical network address mapping table.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can collect the username from a compromised host.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can enumerate all drives on a compromised host.[^1] [^2]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Mafalda](https://attack.mitre.org/software/S1060) can use `AdjustTokenPrivileges()` to elevate privileges.[^2]  |
| [[Native API\|T1106]] | Native API | [Mafalda](https://attack.mitre.org/software/S1060) can use a variety of API calls.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can search for files and directories.[^1]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Mafalda](https://attack.mitre.org/software/S1060) can search for debugging tools on a compromised host.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Mafalda](https://attack.mitre.org/software/S1060) can search for a variety of security software programs, EDR systems, and malware analysis tools.[^1] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Mafalda](https://attack.mitre.org/software/S1060) has been obfuscated and contains encrypted functions.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Mafalda](https://attack.mitre.org/software/S1060) can dump password hashes from `LSASS.exe`.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Metador\|G1013]] | Metador |



## References

[^1]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^2]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


