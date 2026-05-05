---
aliases: 
    - S1209
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1209-Quick_Assist
---

## Description

[[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] is a remote assistance tool primarily for Microsoft Windows, although a macOS version also exists. [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] allows for remote screen sharing and, with end user approval, remote control and command execution on the enabling device.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] communicates over TCP 443 via HTTPS to a remote session server, under which RDP traffic is transferred.[^1]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] allows for the remote administrator to take screenshots of the running system.[^1]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] allows for the remote administrator to view the interactive session of the running machine, including full screen activity.[^1] [^2]  |





> [!info]- References
> [^1]: [Microsoft Quick Assist 2024](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)

> [^2]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


