---
aliases: 
    - T1219
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1219-Remote_Access_Tools
tactic: 
     - Command and Control
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.[^1] [^5] [^2]  Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.<br><br>Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.<br><br>Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|Windows Service]]). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).[^3] [^4] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to remote access services. |
| [[kb/mitre/attack/mitigations/M1034-Limit_Hardware_Installation\|M1034]] | Limit Hardware Installation | Block the use of IP-based KVM devices within the network if they are not required.  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access software. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1219.001-IDE_Tunneling\|T1219.001]] | IDE Tunneling |
| [[kb/mitre/attack/techniques/T1219.002-Remote_Desktop_Software\|T1219.002]] | Remote Desktop Software |
| [[kb/mitre/attack/techniques/T1219.003-Remote_Access_Hardware\|T1219.003]] | Remote Access Hardware |




> [!info]- References
> [^1]: [Symantec Living off the Land](https://www.symantec.com/content/dam/symantec/docs/security-center/white-papers/istr-living-off-the-land-and-fileless-attack-techniques-en.pdf)

> [^2]: [CrySyS Blog TeamSpy](https://blog.crysys.hu/2013/03/teamspy/)

> [^3]: [Google Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523)

> [^4]: [Chrome Remote Desktop](https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708)

> [^5]: [CrowdStrike 2015 Global Threat Report](https://go.crowdstrike.com/rs/281-OBQ-266/images/15GlobalThreatReport.pdf)


