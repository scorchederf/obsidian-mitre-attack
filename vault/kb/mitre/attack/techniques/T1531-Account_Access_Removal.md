---
aliases: 
    - T1531
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1531-Account_Access_Removal
tactic: 
     - Impact
platforms:
     - Linux - macOS - Windows - SaaS - IaaS - Office Suite - ESXi
permissions required:
     - none
---

## Description

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS platforms such as Sharepoint) to remove access to accounts.[^3]  Adversaries may also subsequently log off and/or perform a [[kb/mitre/attack/techniques/T1529-System_Shutdown_Reboot\|System Shutdown/Reboot]] to set malicious changes into place.[^1] [^2] <br><br>In Windows, [[kb/mitre/attack/software/S0039-Net\|Net]] utility, `Set-LocalUser` and `Set-ADAccountPassword` [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] cmdlets may be used by adversaries to modify user accounts. Accounts could also be disabled by Group Policy. In Linux, the `passwd` utility may be used to change passwords. On ESXi servers, accounts can be removed or modified via esxcli (`system account set`, `system account remove`).<br><br>Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as [[kb/mitre/attack/techniques/T1485-Data_Destruction\|Data Destruction]] and [[kb/mitre/attack/techniques/T1491-Defacement\|Defacement]], in order to impede incident response/recovery before completing the [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]] objective. 








> [!info]- References
> [^1]: [CarbonBlack LockerGoga 2019](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)

> [^2]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)

> [^3]: [Obsidian Security SaaS Ransomware June 2023](https://web.archive.org/web/20230608061141/https://www.obsidiansecurity.com/blog/saas-ransomware-observed-sharepoint-microsoft-365/)


