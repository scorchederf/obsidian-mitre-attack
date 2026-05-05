---
aliases: 
    - S0678
    
mitre-attack: https://attack.mitre.org/software/S0678
---

## S0678

[Torisma](https://attack.mitre.org/software/S0678) is a second stage implant designed for specialized monitoring that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032). [Torisma](https://attack.mitre.org/software/S0678) was discovered during an investigation into the 2020 Operation North Star campaign that targeted the defense sector.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Torisma](https://attack.mitre.org/software/S0678) has been Base64 encoded and AES encrypted.[^1]  |
| [[Native API\|T1106]] | Native API | [Torisma](https://attack.mitre.org/software/S0678) has used various Windows API calls.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Torisma](https://attack.mitre.org/software/S0678) can use `GetlogicalDrives` to get a bitmask of all drives available on a compromised system. It can also use `GetDriveType` to determine if a new drive is a CD-ROM drive.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Torisma](https://attack.mitre.org/software/S0678) can collect the current time on a victim machine.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Torisma](https://attack.mitre.org/software/S0678) can send victim data to an actor-controlled C2 server.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Torisma](https://attack.mitre.org/software/S0678) has encoded C2 communications with Base64.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Torisma](https://attack.mitre.org/software/S0678) is only delivered to a compromised host if the victim's IP address is on an allow-list.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Torisma](https://attack.mitre.org/software/S0678) can use `WTSEnumerateSessionsW` to monitor remote desktop connections.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Torisma](https://attack.mitre.org/software/S0678) has used XOR and Base64 to decode C2 data.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Torisma](https://attack.mitre.org/software/S0678) has been packed with Iz4 compression.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Torisma](https://attack.mitre.org/software/S0678) has encrypted its C2 communications using XOR and VEST-32.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Torisma](https://attack.mitre.org/software/S0678) can use HTTP and HTTPS for C2 communications.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Torisma](https://attack.mitre.org/software/S0678) can collect the local MAC address using `GetAdaptersInfo` as well as the system's IP address.[^1]  |




## References

[^1]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)


