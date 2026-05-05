---
aliases: 
    - T1570
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer
tactic: 
     - Lateral Movement
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|Ingress Tool Transfer]]) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.<br><br>Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|SMB/Windows Admin Shares]] to connected network shares or with authenticated connections via [[kb/mitre/attack/techniques/T1021.001-Remote_Desktop_Protocol\|Remote Desktop Protocol]].[^10] <br><br>Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [[kb/mitre/attack/software/S0095-ftp\|ftp]]. In some cases, adversaries may be able to leverage [[kb/mitre/attack/techniques/T1102-Web_Service\|Web Service]]s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.[^6] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0029-PsExec\|S0029]] | PsExec | [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] can be used to download or upload a file over a network share.[^8]  |
| [[kb/mitre/attack/software/S0095-ftp\|S0095]] | ftp | [[kb/mitre/attack/software/S0095-ftp\|ftp]] may be abused by adversaries to transfer tools or files between systems within a compromised environment.[^7] [^12]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to copy files to/from a remotely connected internal system.[^3]  |
| [[kb/mitre/attack/software/S0190-BITSAdmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to upload and/or download files from SMB file servers.[^11]  |
| [[kb/mitre/attack/software/S0357-Impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.[^1]  |
| [[kb/mitre/attack/software/S0361-Expand\|S0361]] | Expand | [[kb/mitre/attack/software/S0361-Expand\|Expand]] can be used to download or upload a file over a network share.[^5]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files to/from a remote share.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known tools and protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. [^9]  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Consider using the host firewall to restrict file sharing communications such as SMB. [^2]  |






> [!info]- References
> [^1]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)

> [^2]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)

> [^3]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)

> [^4]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)

> [^5]: [LOLBAS Expand](https://lolbas-project.github.io/lolbas/Binaries/Expand/)

> [^6]: [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)

> [^7]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)

> [^8]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)

> [^9]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^10]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)

> [^11]: [Microsoft About BITS](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)

> [^12]: [Linux FTP](https://linux.die.net/man/1/ftp)


