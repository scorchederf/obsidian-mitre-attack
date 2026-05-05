---
aliases: 
    - S0592
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0592-RemoteUtilities
---

## Description

[[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] is a legitimate remote administration tool that has been used by MuddyWater since at least 2021 for execution on target machines.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can enumerate files and directories on a target machine.[^1]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can upload and download files to and from a target machine.[^1]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can take screenshots on a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1218.007-Msiexec\|T1218.007]] | Msiexec | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can use Msiexec to install a service.[^1]  |





> [!info]- References
> [^1]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


