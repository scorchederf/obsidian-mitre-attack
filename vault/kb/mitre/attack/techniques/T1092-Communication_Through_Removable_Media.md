---
aliases: 
    - T1092
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1092-Communication_Through_Removable_Media
tactic: 
     - Command and Control
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.[^1]  Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [[kb/mitre/attack/techniques/T1091-Replication_Through_Removable_Media\|Replication Through Removable Media]]. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Disallow or restrict removable media at an organizational policy level if they are not required for business operations.[^2]  |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable Autoruns if it is unnecessary.[^3]  |






> [!info]- References
> [^1]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)

> [^2]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

> [^3]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


