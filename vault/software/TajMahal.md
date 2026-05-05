---
aliases: 
    - S0467
    
mitre-attack: https://attack.mitre.org/software/S0467
---

## S0467

[TajMahal](https://attack.mitre.org/software/S0467) is a multifunctional spying framework that has been in use since at least 2014. [TajMahal](https://attack.mitre.org/software/S0467) is comprised of two separate packages, named Tokyo and Yokohama, and can deploy up to 80 plugins.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Archive via Library\|T1560.002]] | Archive via Library | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to use the open source libraries XZip/Xunzip and zlib to compress files.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to capture webcam video.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify hardware information, the computer name, and OS information on an infected host.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to take screenshots on an infected host including capturing content from windows of instant messaging applications.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to capture VoiceIP application audio on an infected host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify which anti-virus products, firewalls, and anti-spyware products are in use.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to index and compress files into a send queue for exfiltration.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to determine local time on a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to send collected files over its C2.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify running processes and associated plugins on an infected host.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify the Internet Explorer (IE) version on an infected host.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [TajMahal](https://attack.mitre.org/software/S0467) can set the `KeepPrintedJobs` attribute for configured printers in `SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\Printers` to enable document stealing.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify the MAC address on an infected host.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to manage an automated queue of egress files and commands sent to its C2.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to inject the `LoadLibrary` call template DLL into running processes.[^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to steal web session cookies from Internet Explorer, Netscape Navigator, FireFox and RealNetworks applications.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to index files from drives, user profiles, and removable drives.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to inject DLLs for malicious plugins into running processes.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to steal written CD images and files of interest from previously connected removable drives when they become available again.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to steal documents from the local system including the print spooler queue.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to capture keystrokes on an infected host.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify connected Apple devices.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to steal data from the clipboard of an infected host.[^1] <br> |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [TajMahal](https://attack.mitre.org/software/S0467) has used an encrypted Virtual File System to store plugins.[^1]  |




## References

[^1]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


