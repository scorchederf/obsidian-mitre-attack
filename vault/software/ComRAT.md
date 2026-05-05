---
aliases: 
    - S0126
    
mitre-attack: https://attack.mitre.org/software/S0126
---

## S0126

[ComRAT](https://attack.mitre.org/software/S0126) is a second stage implant suspected of being a descendant of [Agent.btz](https://attack.mitre.org/software/S0092) and used by [Turla](https://attack.mitre.org/groups/G0010). The first version of [ComRAT](https://attack.mitre.org/software/S0126) was identified in 2007, but the tool has undergone substantial development for many years since.[^1] [^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [ComRAT](https://attack.mitre.org/software/S0126) can use email attachments for command and control.[^3]  |
| [[Hidden File System\|T1564.005]] | Hidden File System | [ComRAT](https://attack.mitre.org/software/S0126) has used a portable FAT16 partition image placed in %TEMP% as a hidden file system.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ComRAT](https://attack.mitre.org/software/S0126) has used HTTP requests for command and control.[^4] [^3] [^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [ComRAT](https://attack.mitre.org/software/S0126) has used a scheduled task to launch its PowerShell loader.[^3] [^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [ComRAT](https://attack.mitre.org/software/S0126) can use SSL/TLS encryption for its HTTP-based C2 channel. [ComRAT](https://attack.mitre.org/software/S0126) has used public key cryptography with RSA and AES encrypted email attachments for its Gmail C2 channel.[^3] [^5]   |
| [[Software Discovery\|T1518]] | Software Discovery | [ComRAT](https://attack.mitre.org/software/S0126) can check the victim's default browser to determine which process to inject its communications module into.[^3]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [ComRAT](https://attack.mitre.org/software/S0126) has injected its orchestrator DLL into explorer.exe. [ComRAT](https://attack.mitre.org/software/S0126) has also injected its communications module into the victim's default browser to make C2 connections appear less suspicious as all network connections will be initiated by the browser process.[^3] [^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ComRAT](https://attack.mitre.org/software/S0126) has encrypted its virtual file system using AES-256 in XTS mode.[^3] [^5]   |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [ComRAT](https://attack.mitre.org/software/S0126) has stored encrypted orchestrator code and payloads in the Registry.[^3] [^5]   |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [ComRAT](https://attack.mitre.org/software/S0126) has used encryption and base64 to obfuscate its orchestrator code in the Registry. [ComRAT](https://attack.mitre.org/software/S0126) has also used encoded PowerShell scripts.[^3] [^5]   |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [ComRAT](https://attack.mitre.org/software/S0126) has been programmed to sleep outside local business hours (9 to 5, Monday to Friday).[^3]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [ComRAT](https://attack.mitre.org/software/S0126) samples have been seen which hijack COM objects for persistence by replacing the path to shell32.dll in registry location `HKCU\Software\Classes\CLSID\{42aedc87-2188-41fd-b9a3-0c966feabec1}\InprocServer32`.[^4]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [ComRAT](https://attack.mitre.org/software/S0126) has the ability to use the Gmail web UI to receive commands and exfiltrate information.[^3] [^5]  |
| [[Native API\|T1106]] | Native API | [ComRAT](https://attack.mitre.org/software/S0126) can load a PE file from memory or the file system and execute it with `CreateProcessW`.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ComRAT](https://attack.mitre.org/software/S0126) has used `cmd.exe` to execute commands.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ComRAT](https://attack.mitre.org/software/S0126) has used unique per machine passwords to decrypt the orchestrator payload and a hardcoded XOR key to decrypt its communications module. [ComRAT](https://attack.mitre.org/software/S0126) has also used a unique password to decrypt the file used for its hidden file system.[^3] [^5]  |
| [[Query Registry\|T1012]] | Query Registry | [ComRAT](https://attack.mitre.org/software/S0126) can check the default browser by querying `HKCR\http\shell\open\command`.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ComRAT](https://attack.mitre.org/software/S0126) has used PowerShell to load itself every time a user logs in to the system. [ComRAT](https://attack.mitre.org/software/S0126) can execute PowerShell scripts loaded into memory or from the file system.[^3] [^5]  |
| [[Modify Registry\|T1112]] | Modify Registry | [ComRAT](https://attack.mitre.org/software/S0126) has modified Registry values to store encrypted orchestrator code and payloads.[^3] [^5]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [ComRAT](https://attack.mitre.org/software/S0126) has checked the victim system's date and time to perform tasks during business hours (9 to 5, Monday to Friday).[^5]   |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [ComRAT](https://attack.mitre.org/software/S0126) has embedded a XOR encrypted communications module inside the orchestrator module.[^3] [^5]   |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [ComRAT](https://attack.mitre.org/software/S0126) has used a task name associated with Windows SQM Consolidator.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Symantec Waterbug](https://www.threatminer.org/report.php?q=waterbug-attack-group.pdf&y=2015#gsc.tab=0&gsc.q=waterbug-attack-group.pdf&gsc.page=1)


[^2]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


[^3]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^4]: [NorthSec 2015 GData Uroburos Tools](https://docplayer.net/101655589-Tools-used-by-the-uroburos-actors.html)


[^5]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)


[^6]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


