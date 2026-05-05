---
aliases: 
    - S1133
    
mitre-attack: https://attack.mitre.org/software/S1133
---

## S1133

[Apostle](https://attack.mitre.org/software/S1133) is malware that has functioned as both a wiper and, in more recent versions, as ransomware.  [Apostle](https://attack.mitre.org/software/S1133) is written in .NET and shares various programming and functional overlaps with [IPsec Helper](https://attack.mitre.org/software/S1132).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Apostle](https://attack.mitre.org/software/S1133) will attempt to delete all event logs on a victim machine following file wipe activity.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Apostle](https://attack.mitre.org/software/S1133) retrieves a list of all running processes on a victim host, and stops all services containing the string "sql," likely to propagate ransomware activity to database files.[^1]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Apostle](https://attack.mitre.org/software/S1133) reboots the victim machine following wiping and related activity.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Apostle](https://attack.mitre.org/software/S1133)'s ransomware variant requires that a base64-encoded argument is passed when executed, that is used as the Public Key for subsequent encryption operations. If [Apostle](https://attack.mitre.org/software/S1133) is executed without this argument, it automatically runs a self-delete function.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Apostle](https://attack.mitre.org/software/S1133) achieves persistence by creating a scheduled task, such as `MicrosoftCrashHandlerUAC`.[^1]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [Apostle](https://attack.mitre.org/software/S1133) searches for files on available drives based on a list of extensions hard-coded into the sample for follow-on wipe activity.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Apostle](https://attack.mitre.org/software/S1133) creates new, encrypted versions of files then deletes the originals, with the new filenames consisting of a random GUID and ".lock" for an extension.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Apostle](https://attack.mitre.org/software/S1133) initially masqueraded as ransomware but actual functionality is a data destruction tool, supported by an internal name linked to an early version, `wiper-action`. [Apostle](https://attack.mitre.org/software/S1133) writes random data to original files after an encrypted copy is created, along with resizing the original file to zero and changing time property metadata before finally deleting the original file.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Apostle](https://attack.mitre.org/software/S1133) writes batch scripts to disk, such as `system.bat` and `remover.bat`, that perform various anti-analysis and anti-forensic tasks, before finally deleting themselves at the end of execution. [Apostle](https://attack.mitre.org/software/S1133) attempts to delete itself after encryption or wiping operations are complete and before shutting down the victim machine.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Apostle](https://attack.mitre.org/software/S1133) compiled code is obfuscated in an unspecified fashion prior to delivery to victims.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Agrius\|G1030]] | Agrius |



## References

[^1]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


