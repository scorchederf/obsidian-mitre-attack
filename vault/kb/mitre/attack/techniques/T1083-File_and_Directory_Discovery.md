---
aliases: 
    - T1083
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|File and Directory Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Many command shell utilities can be used to obtain this information. Examples include `dir`, `tree`, `ls`, `find`, and `locate`.[^4]  Custom tools may also be used to gather file and directory information and interact with the [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]]. Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] on network devices to gather file and directory information (e.g. `dir`, `show flash`, and/or `nvram`).[^7] <br><br>Some files and directories may require elevated or specific user permissions to access.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to find files and directories with native functionality such as `dir` commands.[^11]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can walk through directories and recursively search for strings in files.[^13]  |
| [[kb/mitre/attack/software/S0193-Forfiles\|S0193]] | Forfiles | [[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^15]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can obtain a list of directories.[^1]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can search for files on the infected machine.[^9] [^2]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes various modules for finding files of interest on hosts and network shares.[^18]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^14]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.[^20]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover specified filetypes and log files on a targeted system.[^17]  |
| [[kb/mitre/attack/software/S0592-RemoteUtilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can enumerate files and directories on a target machine.[^6]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can enumerate files on a target system.[^16]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^10]   |
| [[kb/mitre/attack/software/S1040-Rclone\|S1040]] | Rclone | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^5]  |
| [[kb/mitre/attack/software/S9002-Diskpart\|S9002]] | Diskpart | If executed with elevated privileges, [[kb/mitre/attack/software/S9002-Diskpart\|Diskpart]] can list all volumes, including virtual disks.[^19]     |
| [[kb/mitre/attack/software/S9009-TruffleHog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-TruffleHog\|TruffleHog]] has can browse and scan individual files and directories.[^12] [^3] [^8]  |








> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^3]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)

> [^4]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)

> [^5]: [Rclone](https://rclone.org)

> [^6]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)

> [^7]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^8]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)

> [^9]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^10]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^11]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)

> [^12]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)

> [^13]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^14]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^15]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)

> [^16]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)

> [^17]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^18]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^19]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)

> [^20]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


