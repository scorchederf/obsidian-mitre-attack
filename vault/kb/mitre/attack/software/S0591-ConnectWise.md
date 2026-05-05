---
aliases: 
    - S0591
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0591-ConnectWise
---

## Description

[[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] is a legitimate remote administration tool that has been used since at least 2016 by threat actors including MuddyWater and GOLD SOUTHFIELD to connect to and conduct lateral movement in target environments.[^1] [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] can be used to execute PowerShell commands on target machines.[^1]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] can take screenshots on remote hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] can record video on remote hosts.[^1]  |





> [!info]- References
> [^1]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)

> [^2]: ScreenConnect

> [^3]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


