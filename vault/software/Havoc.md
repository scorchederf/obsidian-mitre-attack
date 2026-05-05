---
aliases: 
    - S1229
    
mitre-attack: https://attack.mitre.org/software/S1229
---

## S1229

[Havoc](https://attack.mitre.org/software/S1229) is an open-source post-exploitation command and control (C2) framework first released on GitHub in October 2022 by C5pider (Paul Ungur), who continues to maintain and develop it with community contributors. [Havoc](https://attack.mitre.org/software/S1229) provides a wide range of offensive security capabilities and has been adopted by multiple threat actors to establish and maintain control over compromised systems.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Havoc](https://attack.mitre.org/software/S1229) can trigger exection of `whoami` on the target host to display the current user.[^5] [^1]  |
| [[Proxy\|T1090]] | Proxy | [Havoc](https://attack.mitre.org/software/S1229) has the ability to route HTTP/S communications through designated proxies.[^3]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | The [Havoc](https://attack.mitre.org/software/S1229) SMB demon can use named pipes for communication through a parent demon.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Havoc](https://attack.mitre.org/software/S1229) can send an AES encrypted check-in request to the C2 server.[^5] [^1]  |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | The [Havoc](https://attack.mitre.org/software/S1229) infection chain has been initiated via ClickFix lures in phishing emails.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Havoc](https://attack.mitre.org/software/S1229) can execute commands via `cmd.exe`.[^3] [^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Havoc](https://attack.mitre.org/software/S1229) can capture screenshots.[^3] [^5] [^4]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Havoc](https://attack.mitre.org/software/S1229) has a module capable of token impersonation.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Havoc](https://attack.mitre.org/software/S1229) can use HTTP/S listeners to establish and maintain C2 communications. [^3] [^5] [^1] [^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Havoc](https://attack.mitre.org/software/S1229) can gather system information including hostname, domain, and OS details.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Havoc](https://attack.mitre.org/software/S1229) can enumerate processes on targeted hosts.[^3] [^5] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Havoc](https://attack.mitre.org/software/S1229) can facilitate the execution of PowerShell commands.[^4]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Havoc](https://attack.mitre.org/software/S1229) has itself injected into `C:\\Windows\\System32\\Werfault.exe` on targeted systems.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Havoc](https://attack.mitre.org/software/S1229) has the ability to upload files to infected systems.[^3] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | The [Havoc](https://attack.mitre.org/software/S1229) interface can display a file explorer view of the compromised host.[^3]  |
| [[DLL\|T1574.001]] | DLL | [Havoc](https://attack.mitre.org/software/S1229) has leveraged legitimate executables to side-load malicious payloads.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Havoc](https://attack.mitre.org/software/S1229) has the ability to copy files from one location to another.[^3]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | The [Havoc](https://attack.mitre.org/software/S1229) demon can check for a connection to the C2 server from the target machine.[^5]  |
| [[Account Discovery\|T1087]] | Account Discovery | [Havoc](https://attack.mitre.org/software/S1229) can identify privileged user accounts on infected systems.[^1] <br> |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Havoc](https://attack.mitre.org/software/S1229) has DLL spawn and injection modules.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Havoc](https://attack.mitre.org/software/S1229) has utilized XOR encryption with the key “01-01-1900” to obfuscate command strings.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | The [Havoc](https://attack.mitre.org/software/S1229) demon agent can be set to sleep for a specified time.[^3] [^5]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Havoc](https://attack.mitre.org/software/S1229) can use an SMB listener for C2 communication.[^3] [^5] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Havoc](https://attack.mitre.org/software/S1229) can download files from the victim's computer.[^3] [^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Havoc](https://attack.mitre.org/software/S1229) has been executed by victims through the use of targeted lures and crafted decoy documents.[^2]  |
| [[Native API\|T1106]] | Native API | [Havoc](https://attack.mitre.org/software/S1229) can use `NtAllocateVirtualMemory` and `NtCreateThreadEx` to aid process injection.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Havoc](https://attack.mitre.org/software/S1229) has a module for network enumeration including determining IP addresses.[^3]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Havoc](https://attack.mitre.org/software/S1229) has been distributed through ClickFix phishing campaigns.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Havoc](https://attack.mitre.org/software/S1229) features a module capable of host enumeration.[^3] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)


[^2]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^3]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^4]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)


[^5]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)


