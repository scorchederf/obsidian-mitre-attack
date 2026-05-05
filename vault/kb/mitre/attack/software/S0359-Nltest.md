---
aliases: 
    - S0359
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0359-Nltest
---

## Description

[[kb/mitre/attack/software/S0359-Nltest\|Nltest]] is a Windows command-line utility used to list domain controllers and enumerate domain trusts.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^2]  |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate remote domain controllers using options such as `/dclist` and `/dsgetdc`.[^2]  |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate trusted domains by using commands such as `nltest /domain_trusts`.[^2] [^1]  |





> [!info]- References
> [^1]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)

> [^2]: [Nltest Manual](https://ss64.com/nt/nltest.html)


