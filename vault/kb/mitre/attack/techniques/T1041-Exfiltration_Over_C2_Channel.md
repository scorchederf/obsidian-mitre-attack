---
aliases: 
    - T1041
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel
tactic: 
     - Exfiltration
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^9]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can send data gathered from a target through the command and control channel.[^5] [^1]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has uploaded a file containing debugger logs, network information and system information to the C2.[^8]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] sent generated reports to the C2 via HTTP POST requests.[^6]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can exfiltrate files from the victim using the `download` command.[^2]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can transfer files from an infected host to the C2 server.[^3]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can upload files and information from a compromised host to its C2 servers.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [^7]  |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |






> [!info]- References
> [^1]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^2]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)

> [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^4]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^5]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^6]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^7]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^8]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)

> [^9]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


