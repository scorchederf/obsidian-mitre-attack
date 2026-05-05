---
aliases: 
    - S1160
    
mitre-attack: https://attack.mitre.org/software/S1160
---

## S1160

[Latrodectus](https://attack.mitre.org/software/S1160) is a Windows malware downloader that has been used since at least 2023 to download and execute additional payloads and modules. [Latrodectus](https://attack.mitre.org/software/S1160) has most often been distributed through email campaigns, primarily by [TA577](https://attack.mitre.org/groups/G1037) and [TA578](https://attack.mitre.org/groups/G1038), and has infrastructure overlaps with historic [IcedID](https://attack.mitre.org/software/S0483) operations.[^2] [^5] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Service\|T1102]] | Web Service | [Latrodectus](https://attack.mitre.org/software/S1160) has used Google Firebase to download malicious installation scripts.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Latrodectus](https://attack.mitre.org/software/S1160) can use rundll32.exe to execute downloaded DLLs.[^3] [^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Latrodectus](https://attack.mitre.org/software/S1160) has Base64-encoded the message body of a HTTP request sent to C2.[^2] [^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | The [Latrodectus](https://attack.mitre.org/software/S1160) command handler can use `cmdexe` to run multiple discovery commands.[^3] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Latrodectus](https://attack.mitre.org/software/S1160) can discover the IP and MAC address of a targeted host.[^3] [^6]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Latrodectus](https://attack.mitre.org/software/S1160) has called `msiexec` to install remotely-hosted MSI files.[^2] [^5]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can run `C:\Windows\System32\cmd.exe /c net view /all` to discover network shares.[^3] [^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can enumerate running processes including process grandchildren on targeted hosts.[^2] [^3] [^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Latrodectus](https://attack.mitre.org/software/S1160) can discover the username of an infected host.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can create scheduled tasks for persistence.[^2] [^3] [^6]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Latrodectus](https://attack.mitre.org/software/S1160) has been executed through malicious links distributed in email campaigns.[^2] [^5]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can resolve Windows APIs dynamically by hash.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Latrodectus](https://attack.mitre.org/software/S1160) can collect data from a compromised host using a stealer module.[^6]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Latrodectus](https://attack.mitre.org/software/S1160) has been distributed through reply-chain phishing emails with malicious attachments.[^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Latrodectus](https://attack.mitre.org/software/S1160) has the ability to deobfuscate encrypted strings.[^2] [^3] [^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Latrodectus](https://attack.mitre.org/software/S1160) has the ability to delete itself.[^3] [^6] <br> |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Latrodectus](https://attack.mitre.org/software/S1160) can collect desktop filenames.[^2] [^6] [^3]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Latrodectus](https://attack.mitre.org/software/S1160) can use the Windows Component Object Model (COM) to set scheduled tasks.[^3] [^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | The [Latrodectus](https://attack.mitre.org/software/S1160) payload has been packed for obfuscation.[^3]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Latrodectus](https://attack.mitre.org/software/S1160) has used JavaScript files as part its infection chain during malicious spam <br> email campaigns.[^3] [^6] [^1] <br> |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Latrodectus](https://attack.mitre.org/software/S1160) can download and execute PEs, DLLs, and shellcode from C2.[^2] [^3] [^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Latrodectus](https://attack.mitre.org/software/S1160) can send registration information to C2 via HTTP `POST`.[^2] [^3] [^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can exfiltrate encrypted system information to the C2 server.[^2] [^6]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Latrodectus](https://attack.mitre.org/software/S1160) has been packed to appear as a component to Bitdefender’s kernel-mode driver, TRUFOS.SYS.[^3]  |
| [[Native API\|T1106]] | Native API | [Latrodectus](https://attack.mitre.org/software/S1160) has used multiple Windows API post exploitation including `GetAdaptersInfo`, `CreateToolhelp32Snapshot`, and `CreateProcessW`.[^3] [^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Latrodectus](https://attack.mitre.org/software/S1160) has lured users into opening malicious email attachments for execution.[^5]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | <br>[Latrodectus](https://attack.mitre.org/software/S1160) has used a two-tiered C2 configuration with tier one nodes connecting to the victim and tier two nodes connecting to backend infrastructure.[^2]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Latrodectus](https://attack.mitre.org/software/S1160) can run `C:\Windows\System32\cmd.exe /c nltest /domain_trusts` to discover domain trusts.[^3] [^6]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Latrodectus](https://attack.mitre.org/software/S1160) has been obfuscated with a 129 byte sequence of junk data prepended to the file.[^3]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | <br>[Latrodectus](https://attack.mitre.org/software/S1160) has the ability to restart compromised hosts.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can gather operating system information.[^2] [^3] [^3] [^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Latrodectus](https://attack.mitre.org/software/S1160) has the ability to identify installed antivirus products.[^3] [^6] <br> |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Latrodectus](https://attack.mitre.org/software/S1160) can send RC4 encrypted data over C2 channels.[^2] [^3] [^6]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Latrodectus](https://attack.mitre.org/software/S1160) can delete itself while its process is still running through the use of an alternate data stream.[^3]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Latrodectus](https://attack.mitre.org/software/S1160) can identify domain groups through `cmd.exe /c net group "Domain Admins" /domain`.[^6] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Latrodectus](https://attack.mitre.org/software/S1160) has used a pseudo random number generator (PRNG) algorithm and a rolling XOR key to obfuscate strings.[^2] [^3] [^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can set an AutoRun key to establish persistence.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Latrodectus](https://attack.mitre.org/software/S1160) can determine if it is running in a virtualized environment by checking the OS version, checking the number of running processes, ensuring a 64-bit application is running on a 64-bit host, and checking if the host has a valid MAC address.[^2] [^3] [^6]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Latrodectus](https://attack.mitre.org/software/S1160) has been distributed to victims through emails containing malicious links.[^2] [^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Latrodectus](https://attack.mitre.org/software/S1160) has used WMI in malicious email infection chains to facilitate the installation of remotely-hosted files.[^3] [^6]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | <br>[Latrodectus](https://attack.mitre.org/software/S1160) has the ability to check for the presence of debuggers.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Latrodectus](https://attack.mitre.org/software/S1160) can run `C:\Windows\System32\cmd.exe /c net group "Domain Admins" /domain` to identify domain administrator accounts.[^3]  |
| [[VNC\|T1021.005]] | VNC | <br>[Latrodectus](https://attack.mitre.org/software/S1160) has routed C2 traffic using Keyhole VNC.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA577\|G1037]] | TA577 |
| [[TA578\|G1038]] | TA578 |



## References

[^1]: [Palo Alto Latrodectus Activity June 2024](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-06-25-IOCs-from-Latrodectus-activity.txt)


[^2]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^3]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^4]: Unidentified 111


[^5]: [Bleeping Computer Latrodectus April 2024](https://www.bleepingcomputer.com/news/security/new-latrodectus-malware-attacks-use-microsoft-cloudflare-themes/)


[^6]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^7]: IceNova


