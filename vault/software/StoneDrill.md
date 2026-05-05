---
aliases: 
    - S0380
    
mitre-attack: https://attack.mitre.org/software/S0380
---

## S0380

[StoneDrill](https://attack.mitre.org/software/S0380) is wiper malware discovered in destructive campaigns against both Middle Eastern and European targets in association with [APT33](https://attack.mitre.org/groups/G0064).[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [StoneDrill](https://attack.mitre.org/software/S0380) has used several anti-emulation techniques to prevent automated analysis by emulators or sandboxes.[^2] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [StoneDrill](https://attack.mitre.org/software/S0380) has downloaded and dropped temporary files containing scripts; it additionally has a function to upload files from the victims machine.[^2] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [StoneDrill](https://attack.mitre.org/software/S0380) has been observed deleting the temporary files once they fulfill their task.[^2] 	 |
| [[System Time Discovery\|T1124]] | System Time Discovery | [StoneDrill](https://attack.mitre.org/software/S0380) can obtain the current date and time of the victim machine.[^2] 	 |
| [[Process Injection\|T1055]] | Process Injection | [StoneDrill](https://attack.mitre.org/software/S0380) has relied on injecting its payload directly into the process memory of the victim's preferred browser.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [StoneDrill](https://attack.mitre.org/software/S0380) can check for antivirus and antimalware programs.[^2] 	 |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [StoneDrill](https://attack.mitre.org/software/S0380) has used the WMI command-line (WMIC) utility to run tasks.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [StoneDrill](https://attack.mitre.org/software/S0380) has obfuscated its module with an alphabet-based table or XOR encryption.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [StoneDrill](https://attack.mitre.org/software/S0380) has the capability to discover the system OS, Windows version, architecture and environment.[^2] 	 |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [StoneDrill](https://attack.mitre.org/software/S0380) can wipe the master boot record of an infected computer.[^5]  |
| [[Query Registry\|T1012]] | Query Registry | [StoneDrill](https://attack.mitre.org/software/S0380) has looked in the registry to find the default browser path.[^2]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [StoneDrill](https://attack.mitre.org/software/S0380) can wipe the accessible physical or logical drives of the infected machine.[^5] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [StoneDrill](https://attack.mitre.org/software/S0380) has several VBS scripts used throughout the malware's lifecycle.[^2] 	 |
| [[Screen Capture\|T1113]] | Screen Capture | [StoneDrill](https://attack.mitre.org/software/S0380) can take screenshots.[^2] 	 |
| [[Data Destruction\|T1485]] | Data Destruction | [StoneDrill](https://attack.mitre.org/software/S0380) has a disk wiper module that targets files other than those in the Windows directory.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |



## References

[^1]: DROPSHOT


[^2]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)


[^3]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^4]: StoneDrill


[^5]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


