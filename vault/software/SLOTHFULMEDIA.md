---
aliases: 
    - S0533
    
mitre-attack: https://attack.mitre.org/software/S0533
---

## S0533

[SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) is a remote access Trojan written in C++ that has been used by an unidentified "sophisticated cyber actor" since at least January 2017.[^7] [^1]  It has been used to target government organizations, defense contractors, universities, and energy companies in Russia, India, Kazakhstan, Kyrgyzstan, Malaysia, Ukraine, and Eastern Europe.[^6] [^2]   <br><br>In October 2020, Kaspersky Labs assessed [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) is part of an activity cluster it refers to as "IAmTheKing".[^2]  ESET also noted code similarity between [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) and droppers used by a group it refers to as "PowerPool".[^5]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has collected disk information from a victim machine.[^7]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has sent system information to a C2 server via HTTP and HTTPS POST requests.[^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has mimicked the names of known executables, such as mediaplayer.exe.[^7]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can add, modify, and/or delete registry keys. It has changed the proxy configuration of a victim system by modifying the `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry.[^7]  |
| [[Process Injection\|T1055]] | Process Injection | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can inject into running processes on a compromised host.[^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has used HTTP and HTTPS for C2 communications.[^7]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has the capability to enumerate services.[^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has a keylogging capability.[^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can open a command line to execute commands.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has collected the username from a victim machine.[^7]  |
| [[Windows Service\|T1543.003]] | Windows Service | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has created a service on victim machines named "TaskFrame" to establish persistence.[^7]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has named a service it establishes on victim machines as "TaskFrame" to hide its malicious purpose.[^7]   |
| [[Service Execution\|T1569.002]] | Service Execution | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has the capability to start services.[^7]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has uploaded files and information from victim machines.[^7]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has hashed a string containing system information prior to exfiltration via POST requests.[^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can enumerate files and directories.[^7]  |
| [[Service Stop\|T1489]] | Service Stop | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has the capability to stop processes and services.[^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has deleted itself and the 'index.dat' file on a compromised machine to remove recent Internet history from the system.[^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has downloaded files onto a victim machine.[^7]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can enumerate open ports on a victim machine.[^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has enumerated processes by ID, name, or privileges.[^7]   |
| [[Screen Capture\|T1113]] | Screen Capture | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has taken a screenshot of a victim's desktop, named it "Filter3.jpg", and stored it in the local directory.[^7]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has been created with a hidden attribute to insure it's not visible to the victim.[^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has collected system name, OS version, adapter information, and memory usage from a victim machine.[^7]  |




## References

[^1]: [Costin Raiu IAmTheKing October 2020](https://x.com/craiu/status/1311920398259367942)


[^2]: [Kaspersky IAmTheKing October 2020](https://securelist.com/iamtheking-and-the-slothfulmedia-malware-family/99000/)


[^3]: QueenOfClubs


[^4]: JackOfHearts


[^5]: [ESET PowerPool Code October 2020](https://x.com/ESETresearch/status/1311762215490461696)


[^6]: [USCYBERCOM SLOTHFULMEDIA October 2020](https://x.com/CNMF_CyberAlert/status/1311743710997159953)


[^7]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


