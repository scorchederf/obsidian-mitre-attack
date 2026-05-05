---
aliases: 
    - S0335
    
mitre-attack: https://attack.mitre.org/software/S0335
---

## S0335

[Carbon](https://attack.mitre.org/software/S0335) is a sophisticated, second-stage backdoor and framework that can be used to steal sensitive information from victims. [Carbon](https://attack.mitre.org/software/S0335) has been selectively used by [Turla](https://attack.mitre.org/groups/G0010) to target government and foreign affairs-related organizations in Central Asia.[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Carbon](https://attack.mitre.org/software/S0335) creates several tasks for later execution to continue persistence on the victim’s machine.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Carbon](https://attack.mitre.org/software/S0335) can use Pastebin to receive C2 commands.[^4]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Carbon](https://attack.mitre.org/software/S0335) uses the `netstat -r` and `netstat -an` commands.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Carbon](https://attack.mitre.org/software/S0335) enumerates values in the Registry.[^1]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [Carbon](https://attack.mitre.org/software/S0335) uses the `net group` command.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Carbon](https://attack.mitre.org/software/S0335) uses the command `net time \\127.0.0.1` to get information the system’s time.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Carbon](https://attack.mitre.org/software/S0335) can collect the IP address of the victims and other computers on the network using the commands: `ipconfig -all` `nbtstat -n`, and `nbtstat -s`.[^1] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Carbon](https://attack.mitre.org/software/S0335) creates a base directory that contains the files and folders that are collected.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Carbon](https://attack.mitre.org/software/S0335) establishes persistence by creating a service and naming it based off the operating system version running on the current machine.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Carbon](https://attack.mitre.org/software/S0335) has used RSA encryption for C2 communications.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Carbon](https://attack.mitre.org/software/S0335) decrypts task and configuration files for execution.[^1] [^4]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Carbon](https://attack.mitre.org/software/S0335) uses HTTP to send data to the C2 server.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Carbon](https://attack.mitre.org/software/S0335) uses the `net view` command.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Carbon](https://attack.mitre.org/software/S0335) can use HTTP in C2 communications.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Carbon](https://attack.mitre.org/software/S0335) encrypts configuration files and tasks for the malware to complete using CAST-128 algorithm.[^1] [^4]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Carbon](https://attack.mitre.org/software/S0335) uses TCP and UDP for C2.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Carbon](https://attack.mitre.org/software/S0335) has a command to inject code into a process.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Carbon](https://attack.mitre.org/software/S0335) can list the processes on the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)


[^2]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)


[^3]: [Securelist Turla Oct 2018](https://securelist.com/shedding-skin-turlas-fresh-faces/88069/)


[^4]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


[^5]: Carbon


[^6]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


