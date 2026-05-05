---
aliases: 
    - T1490
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1490-Inhibit_System_Recovery
tactic: 
     - Impact
platforms:
     - Containers - ESXi - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.[^1] [^8]  This may deny access to available backups and recovery options.<br><br>Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [[kb/mitre/attack/techniques/T1485-Data_Destruction\|Data Destruction]] and [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]].[^1] [^8]  Furthermore, adversaries may disable recovery notifications, then corrupt backups.[^5] <br><br>A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:<br><br>* `vssadmin.exe` can be used to delete all volume shadow copies on a system - `vssadmin.exe delete shadows /all /quiet`<br>* [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|Windows Management Instrumentation]] can be used to delete volume shadow copies - `wmic shadowcopy delete`<br>* `wbadmin.exe` can be used to delete the Windows Backup Catalog - `wbadmin.exe delete catalog -quiet`<br>* `bcdedit.exe` can be used to disable automatic Windows recovery features by modifying boot configuration data - `bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no`<br>* `REAgentC.exe` can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system<br>* `diskshadow.exe` can be used to delete all volume shadow copies on a system - `diskshadow delete shadows all` [^2]  [^3] <br><br>On network devices, adversaries may leverage [[kb/mitre/attack/techniques/T1561-Disk_Wipe\|Disk Wipe]] to delete backup firmware images and reformat the file system, then [[kb/mitre/attack/techniques/T1529-System_Shutdown_Reboot\|System Shutdown/Reboot]] to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.<br><br>On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]], preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`).[^13] <br><br>Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services.[^10]  In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.[^12] [^7] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images.  |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: `reagentc /enable`.[^6]  |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries.  |
| [[kb/mitre/attack/mitigations/M1053-Data_Backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^11]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. In cloud environments, enable versioning on storage objects where possible, and copy backups to other accounts or regions to isolate them from the original copies.[^4]  On ESXi servers, ensure that disk images and snapshots of virtual machines are regularly taken, with copies stored off system.[^9]  |






> [!info]- References
> [^1]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)

> [^2]: [Diskshadow](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow)

> [^3]: [Crytox Ransomware](https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware)

> [^4]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)

> [^5]: [disable_notif_synology_ransom](https://x.com/TheDFIRReport/status/1498657590259109894)

> [^6]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)

> [^7]: [Rhino Security Labs AWS S3 Ransomware](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)

> [^8]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)

> [^9]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

> [^10]: [ZDNet Ransomware Backups 2020](https://www.zdnet.com/article/ransomware-victims-thought-their-backups-were-safe-they-were-wrong/)

> [^11]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)

> [^12]: [Dark Reading Code Spaces Cyber Attack](https://www.darkreading.com/attacks-breaches/code-hosting-service-shuts-down-after-cyber-attack)

> [^13]: [Cybereason](https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware)


