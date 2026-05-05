---
aliases: 
    - T1082
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1082-System_Information_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [[kb/mitre/attack/techniques/T1680-Local_Storage_Discovery\|Local Storage Discovery]] which is an adversary's discovery of local drive, disks and/or volumes.<br><br>Tools such as [[kb/mitre/attack/software/S0096-Systeminfo\|Systeminfo]] can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] on network devices to gather detailed system information (e.g. `show version`).[^10]  On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.[^6] [^2] <br><br>Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.[^12] [^11] [^18] <br><br>[[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|System Information Discovery]] combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.[^20] [^8]  


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0096-Systeminfo\|S0096]] | Systeminfo | [[kb/mitre/attack/software/S0096-Systeminfo\|Systeminfo]] can be used to gather information about the operating system.[^21]  |
| [[kb/mitre/attack/software/S0105-dsquery\|S0105]] | dsquery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.[^3]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to find information about the operating system.[^15]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can grab a system’s information including the OS version, architecture, etc.[^16]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can obtain the OS version and build, computer name, and processor architecture from a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can gather system information from the victim’s machine including the OS type.[^9]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can collect the OS version and process architecture of compromised hosts.[^5]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^22] [^4]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^17]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the operating system name and specific Windows version of an infected machine.[^7]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect information related to a compromised host, including OS version.[^14]  |
| [[kb/mitre/attack/software/S1155-Covenant\|S1155]] | Covenant | [[kb/mitre/attack/software/S1155-Covenant\|Covenant]] implants can gather basic information on infected systems.[^13]  |
| [[kb/mitre/attack/software/S9002-Diskpart\|S9002]] | Diskpart | [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^19]   |








> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [Varonis](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)

> [^3]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)

> [^4]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^5]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^6]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

> [^7]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^8]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)

> [^9]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^10]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^11]: [Google Instances Resource](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

> [^12]: [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)

> [^13]: [Github Covenant](https://github.com/cobbr/Covenant)

> [^14]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^15]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)

> [^16]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^17]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^18]: [Microsoft Virutal Machine API](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)

> [^19]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)

> [^20]: [OSX.FairyTale](https://www.sentinelone.com/blog/trail-osx-fairytale-adware-playing-malware/)

> [^21]: [TechNet Systeminfo](https://technet.microsoft.com/en-us/library/bb491007.aspx)

> [^22]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


