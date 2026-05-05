---
aliases: 
    - S0262
    
mitre-attack: https://attack.mitre.org/software/S0262
---

## S0262

[QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.[^6] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [QuasarRAT](https://attack.mitre.org/software/S0262) has a module for performing remote desktop access.[^6] [^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [QuasarRAT](https://attack.mitre.org/software/S0262) has a built-in keylogger.[^6] [^3] [^15]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [QuasarRAT](https://attack.mitre.org/software/S0262) uses AES with a hardcoded pre-shared key to encrypt network communication.[^6] [^3] [^9]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common web browsers.[^6] [^3] [^15] <br> |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | If the [QuasarRAT](https://attack.mitre.org/software/S0262) client process does not have administrator privileges it will add a registry key to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^6] [^9]   |
| [[Hidden Window\|T1564.003]] | Hidden Window | [QuasarRAT](https://attack.mitre.org/software/S0262) can hide process windows and make web requests invisible to the compromised user. Requests marked as invisible have been sent with user-agent string `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A` though [QuasarRAT](https://attack.mitre.org/software/S0262) can only be run on Windows systems.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [QuasarRAT](https://attack.mitre.org/software/S0262) can gather system information from the victim’s machine including the OS type.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [QuasarRAT](https://attack.mitre.org/software/S0262) can download files to the victim’s machine and execute them.[^6] [^3]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [QuasarRAT](https://attack.mitre.org/software/S0262) can determine the country a victim host is located in.[^9]  |
| [[Modify Registry\|T1112]] | Modify Registry | [QuasarRAT](https://attack.mitre.org/software/S0262) has a command to edit the Registry on the victim’s machine.[^6] [^9]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | <br>[QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to set file attributes to "hidden" to hide files from the compromised user's view in Windows File Explorer.[^9]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [QuasarRAT](https://attack.mitre.org/software/S0262) can enumerate the username and account type.[^9]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | <br>[QuasarRAT](https://attack.mitre.org/software/S0262) can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.[^9]  |
| [[Data from Local System\|T1005]] | Data from Local System | [QuasarRAT](https://attack.mitre.org/software/S0262) can retrieve files from compromised client machines.[^9]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [QuasarRAT](https://attack.mitre.org/software/S0262) can use TCP for C2 communication.[^9]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^9]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common FTP clients.[^6] [^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from FTP clients.[^6] [^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [QuasarRAT](https://attack.mitre.org/software/S0262) can launch a remote shell to execute commands on the victim’s machine.[^6] [^9]  |
| [[Proxy\|T1090]] | Proxy | [QuasarRAT](https://attack.mitre.org/software/S0262) can communicate over a reverse proxy using SOCKS5.[^6] [^3]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [QuasarRAT](https://attack.mitre.org/software/S0262) can use port 4782 on the compromised host for TCP callbacks.[^9]  |
| [[Code Signing\|T1553.002]] | Code Signing | A [QuasarRAT](https://attack.mitre.org/software/S0262) .dll file is digitally signed by a certificate from AirVPN.[^3]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [APT-C-36](https://attack.mitre.org/groups/G0099) used a customized version of [QuasarRAT](https://attack.mitre.org/software/S0262) to monitor browser windows for strings relating to specific Colombian financial institutions.[^15] <br> |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [QuasarRAT](https://attack.mitre.org/software/S0262) contains a .NET wrapper DLL for creating and managing scheduled tasks for maintaining persistence upon reboot.[^3] [^9]  |
| [[Video Capture\|T1125]] | Video Capture | [QuasarRAT](https://attack.mitre.org/software/S0262) can perform webcam viewing.[^6] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[Gorgon Group\|G0078]] | Gorgon Group |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[menuPass\|G0045]] | menuPass |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^2]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^3]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^4]: [DOJ APT10 Dec 2018](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)


[^5]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)


[^6]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^7]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^8]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^9]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^10]: xRAT


[^11]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^12]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^13]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^14]: QuasarRAT


[^15]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


