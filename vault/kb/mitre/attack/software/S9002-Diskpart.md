---
aliases: 
    - S9002
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S9002-Diskpart
---

## Description

[[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.[^3]   <br><br>Adversaries may abuse [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] to conduct [[kb/mitre/attack/tactics/TA0007-Discovery\|Discovery]] techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can execute a disk partition script file, which attempts to mount a virtual hard disk.[^2]  [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can also assign and mount virtual disks.[^2]     |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^3]   |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | If executed with elevated privileges, [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can list all volumes, including virtual disks.[^2]     |
| [[kb/mitre/attack/techniques/T1222.001-Windows_Permissions\|T1222.001]] | Windows Permissions | [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can be used to display, set, or clear attributes of a disk or volume.[^3]    |
| [[kb/mitre/attack/techniques/T1561.002-Disk_Structure_Wipe\|T1561.002]] | Disk Structure Wipe | [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can be used to delete a partition or a volume.[^3]  [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can also be used to remove all partitions or volume formatting from the selected disk.[^1]     |





> [!info]- References
> [^1]: [Trendmicro_RansomHub_Dec2024](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomhub)

> [^2]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)

> [^3]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)


