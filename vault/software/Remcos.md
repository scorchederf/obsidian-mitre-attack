---
aliases: 
    - S0332
    
mitre-attack: https://attack.mitre.org/software/S0332
---

## S0332

[Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been observed being used in malware campaigns.[^3] [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [Remcos](https://attack.mitre.org/software/S0332) has the ability to modify the desktop wallpaper.[^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Remcos](https://attack.mitre.org/software/S0332) can add itself to the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Remcos](https://attack.mitre.org/software/S0332) can collect the OS version and process architecture of compromised hosts.[^8]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Remcos](https://attack.mitre.org/software/S0332) steals and modifies data from the clipboard.[^3] [^8]  |
| [[Process Injection\|T1055]] | Process Injection | [Remcos](https://attack.mitre.org/software/S0332) has a command to hide itself by injecting into another process.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Remcos](https://attack.mitre.org/software/S0332) has been spread through emails containing malicious documents.[^8]  |
| [[Python\|T1059.006]] | Python | [Remcos](https://attack.mitre.org/software/S0332) uses Python scripts.[^3]  |
| [[Proxy\|T1090]] | Proxy | [Remcos](https://attack.mitre.org/software/S0332) uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.[^3] [^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Remcos](https://attack.mitre.org/software/S0332) has full control of the Registry, including the ability to modify it.[^3] [^8]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Remcos](https://attack.mitre.org/software/S0332) can use TLS to encrypt C2 communication.[^8]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Remcos](https://attack.mitre.org/software/S0332) uses RC4 and base64 to obfuscate data, including Registry entries and file paths.[^9]  [Remcos](https://attack.mitre.org/software/S0332) can also employ control flow flattening to hinder analysis.[^6]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Remcos](https://attack.mitre.org/software/S0332) can terminate, suspend, and resume a process by PID.[^8]  |
| [[System Checks\|T1497.001]] | System Checks | [Remcos](https://attack.mitre.org/software/S0332) searches for Sandboxie and VMware on the system.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Remcos](https://attack.mitre.org/software/S0332) can launch a remote command line to execute commands on the victim’s machine.[^4] [^8]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Remcos](https://attack.mitre.org/software/S0332) can use string encryption to hinder analysis.[^8]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Remcos](https://attack.mitre.org/software/S0332) has a command for UAC bypassing.[^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Remcos](https://attack.mitre.org/software/S0332) takes automated screenshots of the infected machine.[^3] [^8]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Remcos](https://attack.mitre.org/software/S0332) can zip files and folders for upload.[^8]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Remcos](https://attack.mitre.org/software/S0332) can clean saved cookies and logins from the web browser.[^8]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Remcos](https://attack.mitre.org/software/S0332) can set `ProcessWindowStyle.Hidden` to hide windows.[^6] <br> |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Remcos](https://attack.mitre.org/software/S0332) can upload and download files to and from the victim’s machine.[^3] [^8]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Remcos](https://attack.mitre.org/software/S0332) can execute VBS remotely.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Remcos](https://attack.mitre.org/software/S0332) has been executed by luring victims into opening malicious email attachments including Excel files.[^8] <br> |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Remcos](https://attack.mitre.org/software/S0332) has used dynamic DNS domains in C2 communications.[^6]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Remcos](https://attack.mitre.org/software/S0332) has a command for keylogging.[^4] [^9]  |
| [[Video Capture\|T1125]] | Video Capture | [Remcos](https://attack.mitre.org/software/S0332) can access a system’s webcam and take pictures.[^4]  |
| [[Query Registry\|T1012]] | Query Registry | [Remcos](https://attack.mitre.org/software/S0332) can obtain Registry data from targeted systems.[^8]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [Remcos](https://attack.mitre.org/software/S0332) can modify file attributes to hide the file.[^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Remcos](https://attack.mitre.org/software/S0332) can search for files on the infected machine.[^3] [^8]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Remcos](https://attack.mitre.org/software/S0332) can capture data from the system’s microphone.[^4] [^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Remcos](https://attack.mitre.org/software/S0332) can delete files and folders from victim machines.[^8]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Remcos](https://attack.mitre.org/software/S0332) can discover running processes on compromised machines.[^8] <br> |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Remcos](https://attack.mitre.org/software/S0332) can identify the location of targeted devices.[^8]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Remcos](https://attack.mitre.org/software/S0332) can list all windows on victim systems.[^8]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Remcos](https://attack.mitre.org/software/S0332) can shutdown and restart remote devices.[^8]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Remcos](https://attack.mitre.org/software/S0332) can enumerate the username on targeted hosts.[^8]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Remcos](https://attack.mitre.org/software/S0332) has the ability to execute JavaScript remotely.[^8]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Remcos](https://attack.mitre.org/software/S0332) can serialize collected data with Protobuf.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[Gamaredon Group\|G0047]] | Gamaredon Group |
| [[APT-C-36\|G0099]] | APT-C-36 |
| [[Gorgon Group\|G0078]] | Gorgon Group |



## References

[^1]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)


[^2]: [VenereCiscoTalos_Gamaredon_Mar2025](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)


[^3]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)


[^4]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)


[^5]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


[^6]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^7]: [LevelBlue Blind Eagle Proton66 JUN 2025](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/)


[^8]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^9]: [Talos Remcos Aug 2018](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)


[^10]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^11]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^12]: Remcos


