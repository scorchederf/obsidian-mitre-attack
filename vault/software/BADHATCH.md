---
aliases: 
    - S1081
    
mitre-attack: https://attack.mitre.org/software/S1081
---

## S1081

[BADHATCH](https://attack.mitre.org/software/S1081) is a backdoor that has been utilized by [FIN8](https://attack.mitre.org/groups/G0061) since at least 2019. [BADHATCH](https://attack.mitre.org/software/S1081) has been used to target the insurance, retail, technology, and chemical industries in the United States, Canada, South Africa, Panama, and Italy.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can check a user's access to the C$ share on a compromised machine.[^1]   |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [BADHATCH](https://attack.mitre.org/software/S1081) can copy a large byte array of 64-bit shellcode into process memory and execute it with a call to `CreateThread`.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [BADHATCH](https://attack.mitre.org/software/S1081) can utilize `powershell.exe` to execute commands on a compromised host.[^2] [^1]  |
| [[Process Injection\|T1055]] | Process Injection | [BADHATCH](https://attack.mitre.org/software/S1081) can inject itself into an existing explorer.exe process by using `RtlCreateUserThread`.[^2] [^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can use a PowerShell object such as, `System.Net.NetworkInformation.Ping` to ping a computer.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can retrieve a list of running processes from a compromised machine.[^1]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can obtain current system information from a compromised machine such as the `SHELL PID`, `PSVERSION`, `HOSTNAME`, `LOGONSERVER`, `LASTBOOTUP`, OS type/version, bitness, and hostname.[^2] [^1]   |
| [[Screen Capture\|T1113]] | Screen Capture | [BADHATCH](https://attack.mitre.org/software/S1081) can take screenshots and send them to an actor-controlled C2 server.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [BADHATCH](https://attack.mitre.org/software/S1081) has an embedded second stage DLL payload within the first stage of the malware.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can obtain the `DATETIME` and `UPTIME` from a compromised machine.[^1]    |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BADHATCH](https://attack.mitre.org/software/S1081) can use `schtasks.exe` to gain persistence.[^1]   |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [BADHATCH](https://attack.mitre.org/software/S1081) malicious PowerShell commands can be encoded with base64.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BADHATCH](https://attack.mitre.org/software/S1081) can use HTTP and HTTPS over port 443 to communicate with actor-controlled C2 servers.[^2] [^1]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can obtain logged user information from a compromised machine and can execute the command `whoami.exe`.[^1]  |
| [[Proxy\|T1090]] | Proxy | [BADHATCH](https://attack.mitre.org/software/S1081) can use SOCKS4 and SOCKS5 proxies to connect to actor-controlled C2 servers. [BADHATCH](https://attack.mitre.org/software/S1081) can also emulate a reverse proxy on a compromised machine to connect with actor-controlled C2 servers.[^1]  |
| [[Native API\|T1106]] | Native API | [BADHATCH](https://attack.mitre.org/software/S1081) can utilize Native API functions such as, `ToolHelp32` and `Rt1AdjustPrivilege` to enable `SeDebugPrivilege` on a compromised machine.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [BADHATCH](https://attack.mitre.org/software/S1081) has the ability to execute a malicious DLL by injecting into `explorer.exe` on a compromised machine.[^2]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can check for open ports on a computer by establishing a TCP connection.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BADHATCH](https://attack.mitre.org/software/S1081) has the ability to load a second stage malicious DLL file onto a compromised machine.[^2]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [BADHATCH](https://attack.mitre.org/software/S1081) can beacon to a hardcoded C2 IP address using TLS encryption every 5 minutes.[^2]  |
| [[Compression\|T1027.015]] | Compression | [BADHATCH](https://attack.mitre.org/software/S1081) can be compressed with the ApLib algorithm.[^1]  |
| [[Web Service\|T1102]] | Web Service | [BADHATCH](https://attack.mitre.org/software/S1081) can be utilized to abuse `sslip.io`, a free IP to domain mapping service, as part of actor-controlled C2 channels.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BADHATCH](https://attack.mitre.org/software/S1081) has the ability to delete PowerShell scripts from a compromised machine.[^2]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [BADHATCH](https://attack.mitre.org/software/S1081) can use WMI event subscriptions for persistence.[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [BADHATCH](https://attack.mitre.org/software/S1081) can use `net.exe group "domain admins" /domain` to identify Domain Administrators.[^1]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [BADHATCH](https://attack.mitre.org/software/S1081) can perform pass the hash on compromised machines with x64 versions.[^1]   |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can use `nltest.exe /domain_trusts` to discover domain trust relationships on a compromised machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BADHATCH](https://attack.mitre.org/software/S1081) can use `cmd.exe` to execute commands on a compromised host.[^2] [^1]   |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [BADHATCH](https://attack.mitre.org/software/S1081) can emulate an FTP server to connect to actor-controlled C2 servers.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [BADHATCH](https://attack.mitre.org/software/S1081) can utilize WMI to collect system information, create new processes, and run malicious PowerShell scripts on a compromised machine.[^2] [^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [BADHATCH](https://attack.mitre.org/software/S1081) can utilize the CMSTPLUA COM interface and the SilentCleanup task to bypass UAC.[^1]   |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [BADHATCH](https://attack.mitre.org/software/S1081) can inject itself into a new `svchost.exe -k netsvcs` process using the asynchronous procedure call (APC) queue.[^2] [^1]   |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [BADHATCH](https://attack.mitre.org/software/S1081) can impersonate a `lsass.exe` or `vmtoolsd.exe` token.[^1]   |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [BADHATCH](https://attack.mitre.org/software/S1081) can execute `netstat.exe -f` on a compromised machine.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BADHATCH](https://attack.mitre.org/software/S1081) can exfiltrate data over the C2 channel.[^2] [^1]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^2]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)


