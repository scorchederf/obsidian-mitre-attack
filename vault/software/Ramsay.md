---
aliases: 
    - S0458
    
mitre-attack: https://attack.mitre.org/software/S0458
---

## S0458

[Ramsay](https://attack.mitre.org/software/S0458) is an information stealing malware framework designed to collect and exfiltrate sensitive documents, including from air-gapped systems. Researchers have identified overlaps between [Ramsay](https://attack.mitre.org/software/S0458) and the [Darkhotel](https://attack.mitre.org/groups/G0012)-associated Retro malware.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can scan for network drives which may contain documents for collection.[^1] [^2] 	 |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Ramsay](https://attack.mitre.org/software/S0458) has been delivered using OLE objects in malicious documents.[^1] 	 |
| [[Screen Capture\|T1113]] | Screen Capture | [Ramsay](https://attack.mitre.org/software/S0458) can take screenshots every 30 seconds as well as when an external removable storage device is connected.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can use [ipconfig](https://attack.mitre.org/software/S0100) and [Arp](https://attack.mitre.org/software/S0099) to collect network configuration information, including routing information and ARP tables.[^2]  |
| [[Native API\|T1106]] | Native API | [Ramsay](https://attack.mitre.org/software/S0458) can use Windows API functions such as `WriteFile`, `CloseHandle`, and `GetCurrentHwProfile` during its collection and file storage operations. [Ramsay](https://attack.mitre.org/software/S0458) can execute its embedded components via `CreateProcessA` and `ShellExecute`.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Ramsay](https://attack.mitre.org/software/S0458) has included a rootkit to evade defenses.[^1] 	 |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can scan for systems that are vulnerable to the EternalBlue exploit.[^1] [^2] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Ramsay](https://attack.mitre.org/software/S0458) has used HTTP for C2.[^2]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Ramsay](https://attack.mitre.org/software/S0458) can spread itself by infecting other portable executable files on networks shared drives.[^1] 	 |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Ramsay](https://attack.mitre.org/software/S0458) has been distributed through spearphishing emails with malicious attachments.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Ramsay](https://attack.mitre.org/software/S0458) can collect Microsoft Word documents from the target's file system, as well as `.txt`, `.doc`, and `.xls` files from the Internet Explorer cache.[^1] [^2] 	 |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Ramsay](https://attack.mitre.org/software/S0458) can schedule tasks via the Windows COM API to maintain persistence.[^1] 	 |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Ramsay](https://attack.mitre.org/software/S0458) can stage data prior to exfiltration in `%APPDATA%\Microsoft\UserSetting` and `%APPDATA%\Microsoft\UserSetting\MediaCache`.[^1] [^2] 	 |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can scan for removable media which may contain documents for collection.[^1] [^2] 	 |
| [[DLL\|T1574.001]] | DLL | [Ramsay](https://attack.mitre.org/software/S0458) can hijack outdated Windows application dependencies with malicious versions of its own DLL payload.[^1] 	 |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Ramsay](https://attack.mitre.org/software/S0458) can collect data from network drives and stage it for exfiltration.[^1] 	 |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Ramsay](https://attack.mitre.org/software/S0458) can store collected documents in a custom container after encrypting and compressing them using RC4 and WinRAR.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Ramsay](https://attack.mitre.org/software/S0458) can compress and archive collected files using WinRAR.[^1] [^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Ramsay](https://attack.mitre.org/software/S0458) has been embedded in documents exploiting CVE-2017-0199, CVE-2017-11882, and CVE-2017-8570.[^1] [^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can detect system information--including disk names, total space, and remaining space--to create a hardware profile GUID which acts as a system identifier for operators.[^1] [^2] 	 |
| [[Steganography\|T1027.003]] | Steganography | [Ramsay](https://attack.mitre.org/software/S0458) has PE data embedded within JPEG files contained within Word documents.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ramsay](https://attack.mitre.org/software/S0458) has masqueraded as a 7zip installer.[^1] [^2] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can gather a list of running processes by using [Tasklist](https://attack.mitre.org/software/S0057).[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Ramsay](https://attack.mitre.org/software/S0458) has created Registry Run keys to establish persistence.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Ramsay](https://attack.mitre.org/software/S0458) can use [UACMe](https://attack.mitre.org/software/S0116) for privilege escalation.[^1] [^2] 	 |
| [[Masquerading\|T1036]] | Masquerading | [Ramsay](https://attack.mitre.org/software/S0458) has masqueraded as a JPG image file.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Ramsay](https://attack.mitre.org/software/S0458) can conduct an initial scan for Microsoft Word documents on the local system, removable media, and connected network drives, before tagging and collecting them. It can continue tagging documents to collect with follow up scans.[^1] 	 |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Ramsay](https://attack.mitre.org/software/S0458) can spread itself by infecting other portable executable files on removable drives.[^1] 	 |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can collect directory and file lists.[^1] [^2] 	 |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Ramsay](https://attack.mitre.org/software/S0458) can use `ImprovedReflectiveDLLInjection` to deploy components.[^1]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Ramsay](https://attack.mitre.org/software/S0458) has been executed through malicious e-mail attachments.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Ramsay](https://attack.mitre.org/software/S0458) has included embedded Visual Basic scripts in malicious documents.[^1] [^2] 	 |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Ramsay](https://attack.mitre.org/software/S0458) has base64-encoded its portable executable and hidden itself under a JPG header. [Ramsay](https://attack.mitre.org/software/S0458) can also embed information within document footers.[^1] 	 |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Ramsay](https://attack.mitre.org/software/S0458) can use `netstat` to enumerate network connections.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Ramsay](https://attack.mitre.org/software/S0458) can extract its agent from the body of a malicious document.[^1] 	 |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Ramsay](https://attack.mitre.org/software/S0458) has used base64 to encode its C2 traffic.[^2]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Ramsay](https://attack.mitre.org/software/S0458) can use the Windows COM API to schedule tasks and maintain persistence.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Ramsay](https://attack.mitre.org/software/S0458) can collect data from removable media and stage it for exfiltration.[^1] 	 |
| [[AppInit DLLs\|T1546.010]] | AppInit DLLs | [Ramsay](https://attack.mitre.org/software/S0458) can insert itself into the address space of other applications using the AppInit DLL Registry key.[^1] 	 |




## References

[^1]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^2]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^3]: Ramsay


