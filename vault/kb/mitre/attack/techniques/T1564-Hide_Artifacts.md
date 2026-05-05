---
aliases: 
    - T1564
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1564-Hide_Artifacts
tactic: 
     - Stealth
platforms:
     - ESXi - Linux - macOS - Office Suite - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.[^4] [^5] [^3] <br><br>Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.[^6] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can modify file attributes to hide the file.[^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Application developers should consider limiting the requirements for custom or otherwise difficult to manage file/folder exclusions. Where possible, install applications to trusted system folder paths that are already protected by restricted file and directory permissions. |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Periodically audit virtual machines for abnormalities. |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Review and audit file/folder exclusions, and limit scope of exclusions to only what is required where possible.[^1]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1564.001-Hidden_Files_and_Directories\|T1564.001]] | Hidden Files and Directories |
| [[kb/mitre/attack/techniques/T1564.002-Hidden_Users\|T1564.002]] | Hidden Users |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window |
| [[kb/mitre/attack/techniques/T1564.004-NTFS_File_Attributes\|T1564.004]] | NTFS File Attributes |
| [[kb/mitre/attack/techniques/T1564.005-Hidden_File_System\|T1564.005]] | Hidden File System |
| [[kb/mitre/attack/techniques/T1564.006-Run_Virtual_Instance\|T1564.006]] | Run Virtual Instance |
| [[kb/mitre/attack/techniques/T1564.007-VBA_Stomping\|T1564.007]] | VBA Stomping |
| [[kb/mitre/attack/techniques/T1564.008-Email_Hiding_Rules\|T1564.008]] | Email Hiding Rules |
| [[kb/mitre/attack/techniques/T1564.009-Resource_Forking\|T1564.009]] | Resource Forking |
| [[kb/mitre/attack/techniques/T1564.010-Process_Argument_Spoofing\|T1564.010]] | Process Argument Spoofing |
| [[kb/mitre/attack/techniques/T1564.011-Ignore_Process_Interrupts\|T1564.011]] | Ignore Process Interrupts |
| [[kb/mitre/attack/techniques/T1564.012-File_Path_Exclusions\|T1564.012]] | File／Path Exclusions |
| [[kb/mitre/attack/techniques/T1564.013-Bind_Mounts\|T1564.013]] | Bind Mounts |
| [[kb/mitre/attack/techniques/T1564.014-Extended_Attributes\|T1564.014]] | Extended Attributes |




> [!info]- References
> [^1]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)

> [^2]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^3]: [MalwareBytes ADS July 2015](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)

> [^4]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)

> [^5]: [Cybereason OSX Pirrit](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)

> [^6]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


