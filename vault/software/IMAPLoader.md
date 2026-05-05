---
aliases: 
    - S1152
    
mitre-attack: https://attack.mitre.org/software/S1152
---

## S1152

[IMAPLoader](https://attack.mitre.org/software/S1152) is a .NET-based loader malware exclusively associated with [CURIUM](https://attack.mitre.org/groups/G1012) operations since at least 2022. [IMAPLoader](https://attack.mitre.org/software/S1152) leverages email protocols for command and control and payload delivery.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | [IMAPLoader](https://attack.mitre.org/software/S1152) modifies Windows tasks on the victim machine to reference a retrieved PE file through a path modification.[^1]  |
| [[Native API\|T1106]] | Native API | [IMAPLoader](https://attack.mitre.org/software/S1152) imports native Windows APIs such as `GetConsoleWindow` and `ShowWindow`.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [IMAPLoader](https://attack.mitre.org/software/S1152) uses WMI queries to query system information on victim hosts.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [IMAPLoader](https://attack.mitre.org/software/S1152) uses WMI queries to gather information about the victim machine.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [IMAPLoader](https://attack.mitre.org/software/S1152) hides the Windows Console window created by its execution by directly importing the `kernel32.dll` and `user32.dll` libraries `GetConsoleWindow` and `ShowWindow` APIs.[^1]  |
| [[AppDomainManager\|T1574.014]] | AppDomainManager | [IMAPLoader](https://attack.mitre.org/software/S1152) is executed via the AppDomainManager injection technique.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [IMAPLoader](https://attack.mitre.org/software/S1152) uses the IMAP email protocol for command and control purposes.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [IMAPLoader](https://attack.mitre.org/software/S1152) is a loader used to retrieve follow-on payload encoded in email messages for execution on victim systems.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [IMAPLoader](https://attack.mitre.org/software/S1152) creates scheduled tasks for persistence based on the operating system version of the victim machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[CURIUM\|G1012]] | CURIUM |



## References

[^1]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)


