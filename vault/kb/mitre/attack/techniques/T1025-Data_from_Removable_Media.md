---
aliases: 
    - T1025
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1025-Data_from_Removable_Media
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[kb/mitre/attack/software/S0106-cmd\|cmd]] may be used to gather information. <br><br>Some adversaries may also use [[kb/mitre/attack/techniques/T1119-Automated_Collection\|Automated Collection]] on removable media.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |





