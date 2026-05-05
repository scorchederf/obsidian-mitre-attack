---
aliases: 
    - S0130
    
mitre-attack: https://attack.mitre.org/software/S0130
---

## S0130

[Unknown Logger](https://attack.mitre.org/software/S0130) is a publicly released, free backdoor. Version 1.5 of the backdoor has been used by the actors responsible for the MONSOON campaign. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim computer name, physical memory, country, and date.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim usernames.[^1]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Unknown Logger](https://attack.mitre.org/software/S0130) is capable of spreading to USB devices.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Unknown Logger](https://attack.mitre.org/software/S0130) is capable of downloading remote files.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Unknown Logger](https://attack.mitre.org/software/S0130) has functionality to disable security tools, including Kaspersky, BitDefender, and MalwareBytes.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim's IP address.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Unknown Logger](https://attack.mitre.org/software/S0130) is capable of stealing usernames and passwords from browsers on the victim machine.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Unknown Logger](https://attack.mitre.org/software/S0130) is capable of recording keystrokes.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


