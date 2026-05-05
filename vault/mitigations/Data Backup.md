---
aliases: 
    - M1053
    
mitre-attack: https://attack.mitre.org/mitigations/M1053
---

## M1053

Data Backup involves taking and securely storing backups of data from end-user systems and critical servers. It ensures that data remains available in the event of system compromise, ransomware attacks, or other disruptions. Backup processes should include hardening backup systems, implementing secure storage solutions, and keeping backups isolated from the corporate network to prevent compromise during active incidents. This mitigation can be implemented through the following measures:<br><br>Regular Backup Scheduling:<br>- Use Case: Ensure timely and consistent backups of critical data.<br>- Implementation: Schedule daily incremental backups and weekly full backups for all critical servers and systems.<br><br>Immutable Backups:<br>- Use Case: Protect backups from modification or deletion, even by attackers.<br>- Implementation: Use write-once-read-many (WORM) storage for backups, preventing ransomware from encrypting or deleting backup files.<br><br>Backup Encryption:<br>- Use Case: Protect data integrity and confidentiality during transit and storage.<br>- Implementation: Encrypt backups using strong encryption protocols (e.g., AES-256) before storing them in local, cloud, or remote locations.<br><br>Offsite Backup Storage:<br>- Use Case: Ensure data availability during physical disasters or onsite breaches.<br>- Implementation: Use cloud-based solutions like AWS S3, Azure Backup, or physical offsite storage to maintain a copy of critical data.<br><br>Backup Testing:<br>- Use Case: Validate backup integrity and ensure recoverability.<br>- Implementation: Regularly test data restoration processes to ensure that backups are not corrupted and can be recovered quickly.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Lifecycle-Triggered Deletion\|T1485.001]] | Lifecycle-Triggered Deletion | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Data Destruction\|T1485]] | Data Destruction | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Defacement\|T1491]] | Defacement | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.<br> |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Disk Wipe\|T1561]] | Disk Wipe | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[External Defacement\|T1491.002]] | External Defacement | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Consider enabling versioning in cloud environments to maintain backup copies of storage objects.[^4]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. In cloud environments, enable versioning on storage objects where possible, and copy backups to other accounts or regions to isolate them from the original copies.[^2]  On ESXi servers, ensure that disk images and snapshots of virtual machines are regularly taken, with copies stored off system.[^3]  |


## References

[^1]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^2]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^3]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^4]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


