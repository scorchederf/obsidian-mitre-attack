---
aliases: 
    - S0667
    
mitre-attack: https://attack.mitre.org/software/S0667
---

## S0667

[Chrommme](https://attack.mitre.org/software/S0667) is a backdoor tool written using the Microsoft Foundation Class (MFC) framework that was first reported in June 2021; security researchers noted infrastructure overlaps with [Gelsemium](https://attack.mitre.org/software/S0666) malware.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Chrommme](https://attack.mitre.org/software/S0667) can enumerate the IP address of a compromised host.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Chrommme](https://attack.mitre.org/software/S0667) can encrypt and store on disk collected data before exfiltration.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Chrommme](https://attack.mitre.org/software/S0667) can download its code from C2.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Chrommme](https://attack.mitre.org/software/S0667) has the ability to list drives.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Chrommme](https://attack.mitre.org/software/S0667) has the ability to obtain the computer name of a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Chrommme](https://attack.mitre.org/software/S0667) can decrypt its encrypted internal code.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Chrommme](https://attack.mitre.org/software/S0667) can store captured system information locally prior to exfiltration.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Chrommme](https://attack.mitre.org/software/S0667) can encrypt sections of its code to evade detection.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Chrommme](https://attack.mitre.org/software/S0667) has the ability to capture screenshots.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Chrommme](https://attack.mitre.org/software/S0667) can exfiltrate collected data via C2.[^1]  |
| [[Native API\|T1106]] | Native API | [Chrommme](https://attack.mitre.org/software/S0667) can use Windows API including `WinExec` for execution.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Chrommme](https://attack.mitre.org/software/S0667) can set itself to sleep before requesting a new command from C2.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Chrommme](https://attack.mitre.org/software/S0667) can collect data from a local system.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Chrommme](https://attack.mitre.org/software/S0667) can retrieve the username from a targeted system.[^1]  |




## References

[^1]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


