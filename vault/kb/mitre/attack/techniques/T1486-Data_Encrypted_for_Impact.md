---
aliases: 
    - T1486
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact
tactic: 
     - Impact
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.[^7] [^4] [^1] [^13] <br><br>In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as [[kb/mitre/attack/techniques/T1222-File_and_Directory_Permissions_Modification\|File and Directory Permissions Modification]] or [[kb/mitre/attack/techniques/T1529-System_Shutdown_Reboot\|System Shutdown/Reboot]], in order to unlock and/or gain access to manipulate these files.[^9]  In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.[^1]  Adversaries may also encrypt virtual machines hosted on ESXi or other hypervisors.[^5]  <br><br>To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]], [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|OS Credential Dumping]], and [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|SMB/Windows Admin Shares]].[^4] [^1]  Encryption malware may also leverage [[kb/mitre/attack/techniques/T1491.001-Internal_Defacement\|Internal Defacement]], such as changing victim wallpapers or ESXi server login messages, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing").[^12] [^2] <br><br>In cloud environments, storage objects within compromised accounts may also be encrypted.[^8]  For example, in AWS environments, adversaries may leverage services such as AWS’s Server-Side Encryption with Customer Provided Keys (SSE-C) to encrypt data.[^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable cloud-delivered protection and Attack Surface Reduction (ASR) rules to block the execution of files that resemble ransomware.[^11]  In AWS environments, create an IAM policy to restrict or block the use of SSE-C on S3 buckets.[^3]  |
| [[kb/mitre/attack/mitigations/M1053-Data_Backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.[^10]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Consider enabling versioning in cloud environments to maintain backup copies of storage objects.[^6]  |






> [!info]- References
> [^1]: [US-CERT NotPetya 2017](https://www.us-cert.gov/ncas/alerts/TA17-181A)

> [^2]: [Varonis](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)

> [^3]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)

> [^4]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)

> [^5]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

> [^6]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)

> [^7]: [US-CERT Ransomware 2016](https://www.us-cert.gov/ncas/alerts/TA16-091A)

> [^8]: [Rhino S3 Ransomware Part 1](https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/)

> [^9]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)

> [^10]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)

> [^11]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^12]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)

> [^13]: [US-CERT SamSam 2018](https://www.us-cert.gov/ncas/alerts/AA18-337A)


