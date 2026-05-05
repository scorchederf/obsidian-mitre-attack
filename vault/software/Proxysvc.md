---
aliases: 
    - S0238
    
mitre-attack: https://attack.mitre.org/software/S0238
---

## S0238

[Proxysvc](https://attack.mitre.org/software/S0238) is a malicious DLL used by [Lazarus Group](https://attack.mitre.org/groups/G0032) in a campaign known as Operation GhostSecret. It has appeared to be operating undetected since 2017 and was mostly observed in higher education organizations. The goal of [Proxysvc](https://attack.mitre.org/software/S0238) is to deliver additional payloads to the target and to maintain control for the attacker. It is in the form of a DLL that can also be executed as a standalone process. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [Proxysvc](https://attack.mitre.org/software/S0238) searches the local system and gathers data.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Proxysvc](https://attack.mitre.org/software/S0238) uses HTTP over SSL to communicate commands with the control server.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Proxysvc](https://attack.mitre.org/software/S0238) can delete files indicated by the attacker and remove itself from disk using a batch file.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Proxysvc](https://attack.mitre.org/software/S0238) automatically collects data about the victim and sends it to the control server.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Proxysvc](https://attack.mitre.org/software/S0238) registers itself as a service on the victim’s machine to run as a standalone process.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Proxysvc](https://attack.mitre.org/software/S0238) collects volume information for all drives on the system.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Proxysvc](https://attack.mitre.org/software/S0238) lists files in directories.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Proxysvc](https://attack.mitre.org/software/S0238) collects the OS version, country name, MAC address, computer name, and physical memory statistics.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Proxysvc](https://attack.mitre.org/software/S0238) lists processes running on the system.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Proxysvc](https://attack.mitre.org/software/S0238) performs data exfiltration over the control server channel using a custom protocol.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Proxysvc](https://attack.mitre.org/software/S0238) gathers product names from the Registry key: `HKLM\Software\Microsoft\Windows NT\CurrentVersion ProductName` and the processor description from the Registry key `HKLM\HARDWARE\DESCRIPTION\System\CentralProcessor\0 ProcessorNameString`.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Proxysvc](https://attack.mitre.org/software/S0238) collects the network adapter information and domain/username information based on current remote sessions.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | As part of the data reconnaissance phase, [Proxysvc](https://attack.mitre.org/software/S0238) grabs the system time to send back to the control server.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Proxysvc](https://attack.mitre.org/software/S0238) executes a binary on the system and logs the results into a temp file by using: `cmd.exe /c "<file_path> > %temp%\PM* .tmp 2>&1"`.[^2]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Proxysvc](https://attack.mitre.org/software/S0238) can overwrite files indicated by the attacker before deleting them.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: Proxysvc


[^2]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


