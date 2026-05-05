---
aliases: 
    - S9002
    
mitre-attack: https://attack.mitre.org/software/S9002
---

## S9002

[Diskpart](https://attack.mitre.org/software/S9002) is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.[^2]   <br><br>Adversaries may abuse [Diskpart](https://attack.mitre.org/software/S9002) to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using [Diskpart](https://attack.mitre.org/software/S9002) to conduct [Discovery](https://attack.mitre.org/tactics/TA0007) techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [Diskpart](https://attack.mitre.org/software/S9002) can be used to delete a partition or a volume.[^2]  [Diskpart](https://attack.mitre.org/software/S9002) can also be used to remove all partitions or volume formatting from the selected disk.[^3]     |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [Diskpart](https://attack.mitre.org/software/S9002) can be used to display, set, or clear attributes of a disk or volume.[^2]    |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Diskpart](https://attack.mitre.org/software/S9002) can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^2]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Diskpart](https://attack.mitre.org/software/S9002) can execute a disk partition script file, which attempts to mount a virtual hard disk.[^1]  [Diskpart](https://attack.mitre.org/software/S9002) can also assign and mount virtual disks.[^1]     |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | If executed with elevated privileges, [Diskpart](https://attack.mitre.org/software/S9002) can list all volumes, including virtual disks.[^1]     |




## References

[^1]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)


[^2]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)


[^3]: [Trendmicro_RansomHub_Dec2024](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomhub)


