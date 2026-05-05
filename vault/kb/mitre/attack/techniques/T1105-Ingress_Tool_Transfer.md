---
aliases: 
    - T1105
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [[kb/mitre/attack/software/S0095-ftp\|ftp]]. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|Lateral Tool Transfer]]). <br><br>On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [[kb/mitre/attack/software/S0160-certutil\|certutil]], and [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] commands such as `IEX(New-Object Net.WebClient).downloadString()` and `Invoke-WebRequest`. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.[^21]   A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).[^34] <br><br>Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]] (typically after interacting with [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]] lures).[^8] <br><br>Files can also be transferred using various [[kb/mitre/attack/techniques/T1102-Web_Service\|Web Service]]s as well as native or otherwise present tools on the victim system.[^27]  In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.[^29] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0095-ftp\|S0095]] | ftp | [[kb/mitre/attack/software/S0095-ftp\|ftp]] may be abused by adversaries to transfer tools or files from an external system into a compromised environment.[^3] [^9]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to copy files to/from a remotely connected external system.[^18]  |
| [[kb/mitre/attack/software/S0160-certutil\|S0160]] | certutil | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to download files from a given URL.[^12] [^6]  |
| [[kb/mitre/attack/software/S0190-BITSAdmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-BITSAdmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-BITS_Jobs\|BITS Jobs]] to upload and/or download files.[^10]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can upload and download to/from a victim machine.[^24]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can download additional files and tools.[^17] [^1]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can download files to the victim’s machine and execute them.[^14] [^2]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can upload and download files to and from the victim’s machine.[^20] [^4]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can upload and download to and from a victim machine.[^31]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to copy files from a given URL.[^11]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] had the ability to download additional payloads.[^5]  |
| [[kb/mitre/attack/software/S0465-CARROTBALL\|S0465]] | CARROTBALL | [[kb/mitre/attack/software/S0465-CARROTBALL\|CARROTBALL]] has the ability to download and install a remote payload.[^23]  |
| [[kb/mitre/attack/software/S0500-MCMD\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-MCMD\|MCMD]] can upload additional files to a compromised host.[^19]  |
| [[kb/mitre/attack/software/S0527-CSPY_Downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-CSPY_Downloader\|CSPY Downloader]] can download additional tools to a compromised host.[^25]  |
| [[kb/mitre/attack/software/S0592-RemoteUtilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can upload and download files to and from a target machine.[^16]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can download additional content and files from the [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] server to the client residing on the victim machine using the `upload` command.[^28] [^32]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can load additional files and tools, including [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]].[^22]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can download and execute previously staged shellcode payloads.[^26]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | <br>[[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can download files to compromised hosts.[^13] [^30]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to download files including over SFTP.[^7] [^15]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools.[^33]  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Use network filtering to block outbound traffic from compromised systems to unapproved external destinations. Restricting access to known, trusted IP addresses and protocols can prevent attackers from downloading malicious tools or payloads onto compromised servers after gaining initial access. |






> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)

> [^3]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)

> [^4]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^5]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^6]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)

> [^7]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)

> [^8]: [T1105: Trellix_search-ms](https://www.trellix.com/blogs/research/beyond-file-search-a-novel-method/)

> [^9]: [Linux FTP](https://linux.die.net/man/1/ftp)

> [^10]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)

> [^11]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)

> [^12]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)

> [^13]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^14]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^15]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)

> [^16]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)

> [^17]: [Github Koadic](https://github.com/offsecginger/koadic)

> [^18]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)

> [^19]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)

> [^20]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^21]: [t1105_lolbas](https://lolbas-project.github.io/#t1105)

> [^22]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^23]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)

> [^24]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^25]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)

> [^26]: [Donut Github](https://github.com/TheWover/donut)

> [^27]: [PTSecurity Cobalt Dec 2016](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)

> [^28]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)

> [^29]: [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)

> [^30]: [Rapid7 Fake W2 July 2024](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)

> [^31]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^32]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)

> [^33]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^34]: [Google Cloud Threat Intelligence COSCMICENERGY 2023](https://cloud.google.com/blog/topics/threat-intelligence/cosmicenergy-ot-malware-russian-response/)


