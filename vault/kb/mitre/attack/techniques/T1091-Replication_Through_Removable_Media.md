---
aliases: 
    - T1091
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1091-Replication_Through_Removable_Media
tactic: 
     - Lateral Movement - Initial Access
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.<br><br>Mobile devices may also be used to infect PCs with malware if connected via USB.[^1]  This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables.[^4] [^5]  For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1034-Limit_Hardware_Installation\|M1034]] | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block unsigned/untrusted executable files (such as .exe, .dll, or .scr) from running from USB removable drives. [^6]  |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable Autorun if it is unnecessary. [^3]  Disallow or restrict removable media at an organizational policy level if it is not required for business operations. [^2]  |






> [!info]- References
> [^1]: [Exploiting Smartphone USB ](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.226.3427&rep=rep1&type=pdf)

> [^2]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

> [^3]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)

> [^4]: [Windows Malware Infecting Android](https://www.computerworld.com/article/2486903/windows-malware-tries-to-infect-android-devices-connected-to-pcs.html)

> [^5]: [iPhone Charging Cable Hack](https://techcrunch.com/2019/08/12/iphone-charging-cable-hack-computer-def-con/)

> [^6]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


