---
aliases: 
    - T1125
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1125-Video_Capture
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.<br><br>Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [[kb/mitre/attack/techniques/T1113-Screen_Capture\|Screen Capture]] due to use of specific devices or applications for video recording rather than capturing the victim's screen.<br><br>In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. [^3] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can access a connected webcam and capture pictures.[^11]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can perform webcam viewing.[^7] [^2]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can access a system’s webcam and take pictures.[^4]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can capture webcam data on Windows and macOS systems.[^6]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has a remote webcam monitoring capability.[^1] [^8]  |
| [[kb/mitre/attack/software/S0591-ConnectWise\|S0591]] | ConnectWise | [[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] can record video on remote hosts.[^12]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can capture camera video as part of its collection process.[^5]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can record screen content on targeted systems.[^9]  |
| [[kb/mitre/attack/software/S1209-Quick_Assist\|S1209]] | Quick Assist | [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] allows for the remote administrator to view the interactive session of the running machine, including full screen activity.[^10] [^13]  |








> [!info]- References
> [^1]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)

> [^2]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)

> [^3]: [objective-see 2017 review](https://objective-see.com/blog/blog_0x25.html)

> [^4]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)

> [^5]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^6]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^7]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^8]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)

> [^9]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)

> [^10]: [Microsoft Quick Assist 2024](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)

> [^11]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^12]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)

> [^13]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


