---
aliases: 
    - S0057
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0057-Tasklist
---

## Description

The [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1007-System_Service_Discovery\|T1007]] | System Service Discovery | [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] can be used to discover services running on a system.[^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] can be used to discover processes running on a system.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] can be used to enumerate security software currently running on a system by process name of known products.[^1]  |





> [!info]- References
> [^1]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)


