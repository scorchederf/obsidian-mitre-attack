---
aliases: 
    - S1178
    
mitre-attack: https://attack.mitre.org/software/S1178
---

## S1178

[ShrinkLocker](https://attack.mitre.org/software/S1178) is a VBS-based malicious script that leverages the legitimate Bitlocker application to encrypt files on victim systems for ransom. [ShrinkLocker](https://attack.mitre.org/software/S1178) functions by using Bitlocker to encrypt files, then renames impacted drives to the adversary’s contact email address to facilitate communication for the ransom payment.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Time Discovery\|T1124]] | System Time Discovery | [ShrinkLocker](https://attack.mitre.org/software/S1178) retrieves a system timestamp that is used in generating an encryption key.[^2]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [ShrinkLocker](https://attack.mitre.org/software/S1178) renames disk labels on victim hosts to the threat actor's email address to enable the victim to contact the threat actor for ransom negotiation.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses WMI queries to gather various information about the victim machine and operating system.[^1] [^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [ShrinkLocker](https://attack.mitre.org/software/S1178) is a VisualBasic script (VBS) object that calls multiple other operating system functions during execution.[^1] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses PowerShell to disable protectors used to secure the BitLocker encryption key on victim machines and then delete the key from the system.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [ShrinkLocker](https://attack.mitre.org/software/S1178) modifies various registry keys associated with system logon and BitLocker functionality to effectively lock-out users following disk encryption.[^1] [^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [ShrinkLocker](https://attack.mitre.org/software/S1178) calls [Wevtutil](https://attack.mitre.org/software/S0645) to clear the Windows PowerShell and Microsoft-Windows-Powershell/Operational logs.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses WMI to query information about the victim operating system.[^1]  |
| [[Web Service\|T1102]] | Web Service | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses a subdomain on the legitimate Cloudflare resource "trycloudflare[.]com" to obfuscate the threat actor's actual address and to tunnel information sent from victim systems.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses the legitimate BitLocker application to encrypt victim files for ransom.[^1] [^2]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [ShrinkLocker](https://attack.mitre.org/software/S1178) has used [Diskpart](https://attack.mitre.org/software/S9002) to format newly-created partitions.[^2]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ShrinkLocker](https://attack.mitre.org/software/S1178) will exfiltrate victim system information along with the encryption key via an HTTP POST.[^1] [^2]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [ShrinkLocker](https://attack.mitre.org/software/S1178) can restart the victim system if it encounters an error during execution, and will forcibly shutdown the system following encryption to lock out victim users.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [ShrinkLocker](https://attack.mitre.org/software/S1178) disables protectors used to secure the BitLocker encryption key on victim systems.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [ShrinkLocker](https://attack.mitre.org/software/S1178) captures the IP address of the victim system and sends this to the attacker following encryption.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [ShrinkLocker](https://attack.mitre.org/software/S1178) turns on the system firewall and deletes all of its rules during execution.[^1] [^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [ShrinkLocker](https://attack.mitre.org/software/S1178) will exit its "main" function if the victim domain name does not match provided criteria.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ShrinkLocker](https://attack.mitre.org/software/S1178) can delete itself depending on various checks performed during execution.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [ShrinkLocker](https://attack.mitre.org/software/S1178) can initiate a destructive payload depending on the operating system check through resizing and reformatting portions of the victim machine's disk, leading to system instability and potential data corruption.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ShrinkLocker](https://attack.mitre.org/software/S1178) checks whether the Bitlocker Drive Encryption Tools service is running.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses HTTP POST requests to communicate victim information back to the threat actor.[^1]  |




## References

[^1]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)


[^2]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)


