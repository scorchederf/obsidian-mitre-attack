---
aliases: 
    - S0385
    
mitre-attack: https://attack.mitre.org/software/S0385
---

## S0385

[njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.[^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [njRAT](https://attack.mitre.org/software/S0385) enumerates the victim operating system and computer name during the initial infection.[^9]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [njRAT](https://attack.mitre.org/software/S0385) has a module that steals passwords saved in victim web browsers.[^9] [^10] [^12]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [njRAT](https://attack.mitre.org/software/S0385) gathers information about opened windows during the initial infection.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [njRAT](https://attack.mitre.org/software/S0385) can download files to the victim’s machine.[^9] [^10]  [APT-C-36](https://attack.mitre.org/groups/G0099) has used modified versions of [njRAT](https://attack.mitre.org/software/S0385) to enable the download of .NET assemblies.[^16]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [njRAT](https://attack.mitre.org/software/S0385) can browse file systems using a file manager module.[^9]  |
| [[Query Registry\|T1012]] | Query Registry | [njRAT](https://attack.mitre.org/software/S0385) can read specific registry values.[^10]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [njRAT](https://attack.mitre.org/software/S0385) will attempt to detect if the victim system has a camera during the initial infection. [njRAT](https://attack.mitre.org/software/S0385) can also detect any removable drives connected to the system.[^9] [^10]  |
| [[Video Capture\|T1125]] | Video Capture | [njRAT](https://attack.mitre.org/software/S0385) can access the victim's webcam.[^9] [^12]  |
| [[Screen Capture\|T1113]] | Screen Capture | [njRAT](https://attack.mitre.org/software/S0385) can capture screenshots of the victim’s machines.[^10] [^16]  |
| [[Native API\|T1106]] | Native API | [njRAT](https://attack.mitre.org/software/S0385) has used the ShellExecute() function within a script.[^10]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [njRAT](https://attack.mitre.org/software/S0385) can identify remote hosts on connected networks.[^9]  |
| [[File Deletion\|T1070.004]] | File Deletion | [njRAT](https://attack.mitre.org/software/S0385) is capable of deleting files.[^9] [^10]  |
| [[PowerShell\|T1059.001]] | PowerShell | [njRAT](https://attack.mitre.org/software/S0385) has executed PowerShell commands via auto-run registry key persistence.[^10]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [njRAT](https://attack.mitre.org/software/S0385) has included a base64 encoded executable.[^10]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [njRAT](https://attack.mitre.org/software/S0385) uses Base64 encoding for C2 traffic.[^9]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [njRAT](https://attack.mitre.org/software/S0385) has used AutoIt to compile the payload and main script into a single executable after delivery.[^10]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [njRAT](https://attack.mitre.org/software/S0385) has used port 1177 for HTTP C2 communications.[^10]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [njRAT](https://attack.mitre.org/software/S0385) can be configured to spread via removable drives.[^9] [^10]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [njRAT](https://attack.mitre.org/software/S0385) enumerates the current user during the initial infection.[^9]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [njRAT](https://attack.mitre.org/software/S0385) has added persistence via the Registry key `HKCU\Software\Microsoft\CurrentVersion\Run\` and dropped a shortcut in `%STARTUP%`.[^9] [^10]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [njRAT](https://attack.mitre.org/software/S0385) has a module for performing remote desktop access.[^9] [^16]  |
| [[Keylogging\|T1056.001]] | Keylogging | [njRAT](https://attack.mitre.org/software/S0385) is capable of logging keystrokes.[^9] [^10] [^12] [^16]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [njRAT](https://attack.mitre.org/software/S0385) has used HTTP for C2 communications.[^10]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [njRAT](https://attack.mitre.org/software/S0385) has modified the Windows firewall to allow itself to communicate through the firewall.[^9] [^10]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [njRAT](https://attack.mitre.org/software/S0385) is capable of manipulating and deleting registry keys, including those used for persistence.[^10]  |
| [[Modify Registry\|T1112]] | Modify Registry | [njRAT](https://attack.mitre.org/software/S0385) can create, delete, or modify a specified Registry key or value.[^9] [^10]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [njRAT](https://attack.mitre.org/software/S0385) has used C2 infrastructure to receive stolen information from the infected machine including screenshots and other system information.[^10] [^16] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [njRAT](https://attack.mitre.org/software/S0385) can search a list of running processes for Tr.exe.[^10]  |
| [[Fast Flux DNS\|T1568.001]] | Fast Flux DNS | [njRAT](https://attack.mitre.org/software/S0385) has used a fast flux DNS for C2 IP resolution.[^10]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [njRAT](https://attack.mitre.org/software/S0385) can launch a command shell interface for executing commands.[^9]  |
| [[Data from Local System\|T1005]] | Data from Local System | [njRAT](https://attack.mitre.org/software/S0385) can collect data from a local system.[^9]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |
| [[Transparent Tribe\|G0134]] | Transparent Tribe |
| [[Group5\|G0043]] | Group5 |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |
| [[APT41\|G0096]] | APT41 |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[Gorgon Group\|G0078]] | Gorgon Group |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: Njw0rm


[^2]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)


[^3]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^4]: [FireEye Njw0rm Aug 2013](https://web.archive.org/web/20200302085808/https://www.fireeye.com/blog/threat-research/2013/08/njw0rm-brother-from-the-same-mother.html)


[^5]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^6]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)


[^7]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^8]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^9]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^10]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^11]: Bladabindi


[^12]: [Citizen Lab Group5](https://citizenlab.ca/2016/08/group5-syria/)


[^13]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^14]: LV


[^15]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^16]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^17]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


