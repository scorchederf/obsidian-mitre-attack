---
aliases: 
    - S0364
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0364-RawDisk
---

## Description

[[kb/mitre/attack/software/S0364-RawDisk\|RawDisk]] is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1485-Data_Destruction\|T1485]] | Data Destruction | [[kb/mitre/attack/software/S0364-RawDisk\|RawDisk]] was used in Shamoon to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1561.001-Disk_Content_Wipe\|T1561.001]] | Disk Content Wipe | [[kb/mitre/attack/software/S0364-RawDisk\|RawDisk]] has been used to directly access the hard disk to help overwrite arbitrarily sized portions of disk content.[^1]  |
| [[kb/mitre/attack/techniques/T1561.002-Disk_Structure_Wipe\|T1561.002]] | Disk Structure Wipe | [[kb/mitre/attack/software/S0364-RawDisk\|RawDisk]] was used in Shamoon to help overwrite components of disk structure like the MBR and disk partitions.[^4] [^3]  |





> [!info]- References
> [^1]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)

> [^2]: [EldoS RawDisk ITpro](https://www.itprotoday.com/windows-78/eldos-provides-raw-disk-access-vista-and-xp)

> [^3]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)

> [^4]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


