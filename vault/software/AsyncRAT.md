---
aliases: 
    - S1087
    
mitre-attack: https://attack.mitre.org/software/S1087
---

## S1087

[AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.[^3] [^5] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [AsyncRAT](https://attack.mitre.org/software/S1087) can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [AsyncRAT](https://attack.mitre.org/software/S1087) can be deployed via batch script.[^2]  |
| [[Native API\|T1106]] | Native API | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.[^6]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [AsyncRAT](https://attack.mitre.org/software/S1087) can check whether the current system hour and day of the week are within operating hours defined it its configuration.[^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [AsyncRAT](https://attack.mitre.org/software/S1087) use a DGA to generate a C2 domains.[^2]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [AsyncRAT](https://attack.mitre.org/software/S1087) can proxy C2 through a [Tor](https://attack.mitre.org/software/S0183) client.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [AsyncRAT](https://attack.mitre.org/software/S1087) can check the disk size through the values obtained with `DeviceInfo.`[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [AsyncRAT](https://attack.mitre.org/software/S1087) can check if the current user of a compromised system is an administrator. [^6]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [AsyncRAT](https://attack.mitre.org/software/S1087) has been delivered via malicious email attachments.[^1]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [AsyncRAT](https://attack.mitre.org/software/S1087) can be configured to use dynamic DNS.[^8]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | <br>[AsyncRAT](https://attack.mitre.org/software/S1087) can hide the execution of scheduled tasks using `ProcessWindowStyle.Hidden`.[^6]  |
| [[System Checks\|T1497.001]] | System Checks | [AsyncRAT](https://attack.mitre.org/software/S1087) can identify strings such as Virtual, vmware, or VirtualBox to detect virtualized environments.[^6]  |
| [[Video Capture\|T1125]] | Video Capture | [AsyncRAT](https://attack.mitre.org/software/S1087) can record screen content on targeted systems.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to download files including over SFTP.[^8] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [AsyncRAT](https://attack.mitre.org/software/S1087) has been executed through victims opening malicious file attachments.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [AsyncRAT](https://attack.mitre.org/software/S1087) can examine running processes to determine if a debugger is present.[^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [AsyncRAT](https://attack.mitre.org/software/S1087) can enumerate the NetBIOS name on targeted machines.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to view the screen on compromised hosts.[^8]  |
| [[Keylogging\|T1056.001]] | Keylogging | [AsyncRAT](https://attack.mitre.org/software/S1087) can capture keystrokes on the victim’s machine.[^8]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [AsyncRAT](https://attack.mitre.org/software/S1087) can create a scheduled task to maintain persistence on system start-up.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA2541\|G1018]] | TA2541 |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)


[^2]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^3]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


[^4]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^5]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)


[^6]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^7]: [LevelBlue Blind Eagle Proton66 JUN 2025](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/)


[^8]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)


[^9]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^10]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


