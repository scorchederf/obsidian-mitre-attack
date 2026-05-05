---
aliases: 
    - T1485
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1485-Data_Destruction
tactic: 
     - Impact
platforms:
     - Containers - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.[^9] [^5] [^8] [^6] [^4] [^1]  Common operating system file deletion commands such as `del` and `rm` often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [[kb/mitre/attack/techniques/T1561.001-Disk_Content_Wipe\|Disk Content Wipe]] and [[kb/mitre/attack/techniques/T1561.002-Disk_Structure_Wipe\|Disk Structure Wipe]] because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.<br><br>Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.[^6] [^4]  In some cases politically oriented image files have been used to overwrite data.[^5] [^8] [^6] <br><br>To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]], [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|OS Credential Dumping]], and [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|SMB/Windows Admin Shares]].[^9] [^5] [^8] [^6] [^1] .<br><br>In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.[^2] [^10]  Similarly, they may delete virtual machines from on-prem virtualized environments.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0195-SDelete\|S0195]] | SDelete | [[kb/mitre/attack/software/S0195-SDelete\|SDelete]] deletes data in a way that makes it unrecoverable.[^3]  |
| [[kb/mitre/attack/software/S0364-RawDisk\|S0364]] | RawDisk | [[kb/mitre/attack/software/S0364-RawDisk\|RawDisk]] was used in Shamoon to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.[^8] [^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | In cloud environments, limit permissions to modify cloud bucket lifecycle policies (e.g., `PutLifecycleConfiguration` in AWS) to only those accounts that require it. In AWS environments, consider using Service Control policies to limit the use of the `PutBucketLifecycle` API call.  |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Implement multi-factor authentication (MFA) delete for cloud storage resources, such as AWS S3 buckets, to prevent unauthorized deletion of critical data and infrastructure. MFA delete requires additional authentication steps, making it significantly more difficult for adversaries to destroy data without proper credentials. This additional security layer helps protect against the impact of data destruction in cloud environments by ensuring that only authenticated actions can irreversibly delete storage or machine images. |
| [[kb/mitre/attack/mitigations/M1053-Data_Backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^7]  Ensure backups are stored off system and protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1485.001-Lifecycle-Triggered_Deletion\|T1485.001]] | Lifecycle-Triggered Deletion |




> [!info]- References
> [^1]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)

> [^2]: [Data Destruction - Threat Post](https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/)

> [^3]: [Microsoft SDelete July 2016](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete)

> [^4]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)

> [^5]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)

> [^6]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)

> [^7]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)

> [^8]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)

> [^9]: [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)

> [^10]: [DOJ  - Cisco Insider](https://www.justice.gov/usao-ndca/pr/san-jose-man-pleads-guilty-damaging-cisco-s-network)


