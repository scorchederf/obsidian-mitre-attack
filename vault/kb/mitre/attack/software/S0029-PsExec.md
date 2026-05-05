---
aliases: 
    - S0029
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0029-PsExec
---

## Description

[[kb/mitre/attack/software/S0029-PsExec\|PsExec]] is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.[^3] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|T1021.002]] | SMB／Windows Admin Shares | [[kb/mitre/attack/software/S0029-PsExec\|PsExec]], a tool that has been used by adversaries, writes programs to the `ADMIN$` network share to execute commands on remote systems.[^2]  |
| [[kb/mitre/attack/techniques/T1136.002-Domain_Account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] has the ability to remotely create accounts on target systems.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] can leverage Windows services to escalate privileges from administrator to SYSTEM with the `-s` argument.[^3]  |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | Microsoft Sysinternals [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] is a popular administration tool that can be used to execute binaries on remote systems using a temporary Windows service.[^3]  |
| [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] can be used to download or upload a file over a network share.[^2]  |





> [!info]- References
> [^1]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)

> [^2]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)

> [^3]: [Russinovich Sysinternals](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)

> [^4]: [SANS PsExec](https://www.sans.org/blog/protecting-privileged-domain-accounts-psexec-deep-dive/)


