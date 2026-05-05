---
aliases: 
    - S1087
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1087-AsyncRAT
---

## Description

[[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.[^6] [^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can enumerate the NetBIOS name on targeted machines.[^3]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check if the current user of a compromised system is an administrator. [^2]  |
| [[kb/mitre/attack/techniques/T1053.005-Scheduled_Task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can create a scheduled task to maintain persistence on system start-up.[^2]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can capture keystrokes on the victim’s machine.[^4]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can examine running processes to determine if a debugger is present.[^2]  |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can be deployed via batch script.[^3]  |
| [[kb/mitre/attack/techniques/T1090.003-Multi-hop_Proxy\|T1090.003]] | Multi-hop Proxy | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can proxy C2 through a [[kb/mitre/attack/software/S0183-Tor\|Tor]] client.[^3]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to download files including over SFTP.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.[^2]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to view the screen on compromised hosts.[^4]  |
| [[kb/mitre/attack/techniques/T1124-System_Time_Discovery\|T1124]] | System Time Discovery | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check whether the current system hour and day of the week are within operating hours defined it its configuration.[^3]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can record screen content on targeted systems.[^4]  |
| [[kb/mitre/attack/techniques/T1204.002-Malicious_File\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has been executed through victims opening malicious file attachments.[^5]  |
| [[kb/mitre/attack/techniques/T1497.001-System_Checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can identify strings such as Virtual, vmware, or VirtualBox to detect virtualized environments.[^2]  |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window | <br>[[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can hide the execution of scheduled tasks using `ProcessWindowStyle.Hidden`.[^2]  |
| [[kb/mitre/attack/techniques/T1566.001-Spearphishing_Attachment\|T1566.001]] | Spearphishing Attachment | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has been delivered via malicious email attachments.[^5]  |
| [[kb/mitre/attack/techniques/T1568-Dynamic_Resolution\|T1568]] | Dynamic Resolution | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can be configured to use dynamic DNS.[^4]  |
| [[kb/mitre/attack/techniques/T1568.002-Domain_Generation_Algorithms\|T1568.002]] | Domain Generation Algorithms | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] use a DGA to generate a C2 domains.[^3]  |
| [[kb/mitre/attack/techniques/T1622-Debugger_Evasion\|T1622]] | Debugger Evasion | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.[^2]  |
| [[kb/mitre/attack/techniques/T1680-Local_Storage_Discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check the disk size through the values obtained with `DeviceInfo.`[^2]  |





> [!info]- References
> [^1]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)

> [^2]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^3]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)

> [^4]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)

> [^5]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)

> [^6]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


