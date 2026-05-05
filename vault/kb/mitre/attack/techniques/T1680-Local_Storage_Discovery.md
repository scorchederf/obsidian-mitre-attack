---
aliases: 
    - T1680
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1680-Local_Storage_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement, or as a precursor to [[kb/mitre/attack/techniques/T1006-Direct_Volume_Access\|Direct Volume Access]]. <br><br>On ESXi systems, adversaries may use [[kb/mitre/attack/techniques/T1059.012-Hypervisor_CLI\|Hypervisor CLI]] commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files.[^4] [^3] <br><br>On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`.[^2] [^9] <br><br>Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. <br><br>Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.[^1] [^6] [^10] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can enumerate the system drives and associated system name.[^8]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect information related to a compromised host, including a list of drives.[^7]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check the disk size through the values obtained with `DeviceInfo.`[^5]  |








> [!info]- References
> [^1]: [AWS docs describe volumes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html)

> [^2]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)

> [^3]: [TrendMicro ESXI Ransomware](https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html)

> [^4]: [TrendMicro](https://www.trendmicro.com/en_us/research/21/e/darkside-linux-vms-targeted.html)

> [^5]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^6]: [GCP gcloud compute disks list](https://cloud.google.com/sdk/gcloud/reference/compute/disks/list)

> [^7]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^8]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^9]: [Volexity](https://www.volexity.com/blog/2023/06/28/charming-kitten-updates-powerstar-with-an-interplanetary-twist/)

> [^10]: [azure az disk](https://learn.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest)


