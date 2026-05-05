---
aliases: 
    - S0590
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0590-NBTscan
---

## Description

[[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.[^1] [^3] [^2] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can be used to collect MAC addresses.[^1] [^3] 	 |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can list NetBIOS computer names.[^1] [^3] 	 |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can list active users on the system.[^1] [^3] 	 |
| [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can dump and print whole packet content.[^1] [^3] 	 |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can be used to scan IP networks.[^1] [^3]  |





> [!info]- References
> [^1]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^2]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)

> [^3]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^4]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


