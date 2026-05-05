---
aliases: 
    - T1052
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1052-Exfiltration_Over_Physical_Medium
tactic: 
     - Exfiltration
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1034-Limit_Hardware_Installation\|M1034]] | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable Autorun if it is unnecessary. [^2]  Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [^1]  |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can detect and block sensitive data being copied to physical mediums. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1052.001-Exfiltration_over_USB\|T1052.001]] | Exfiltration over USB |




> [!info]- References
> [^1]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

> [^2]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


