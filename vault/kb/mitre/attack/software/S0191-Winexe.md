---
aliases: 
    - S0191
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0191-Winexe
---

## Description

[[kb/mitre/attack/software/S0191-Winexe\|Winexe]] is a lightweight, open source tool similar to [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] designed to allow system administrators to execute commands on remote servers. [^1]  [[kb/mitre/attack/software/S0191-Winexe\|Winexe]] is unique in that it is a GNU/Linux based client. [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0191-Winexe\|Winexe]] installs a service on the remote system, executes the command, then uninstalls the service.[^2]  |





> [!info]- References
> [^1]: [Winexe Github Sept 2013](https://github.com/skalkoto/winexe/)

> [^2]: [Secpod Winexe June 2017](https://web.archive.org/web/20211019012628/https://www.secpod.com/blog/winexe/)

> [^3]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


