---
aliases: 
    - S0445
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0445-ShimRatReporter
---

## Description

[[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] is a tool used by suspected Chinese adversary Mofang to automatically conduct initial discovery. The details from this discovery are used to customize follow-on payloads (such as ShimRat) as well as set up faux infrastructure which mimics the adversary's targets. [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] has been used in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1020-Automated_Exfiltration\|T1020]] | Automated Exfiltration | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] sent collected system and network information compiled into a report to an adversary-controlled C2.[^1]  |
| [[kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] encrypted gathered information with a combination of shifting and XOR using a static key.[^1]  |
| [[kb/mitre/attack/techniques/T1036.005-Match_Legitimate_Resource_Name_or_Location\|T1036.005]] | Match Legitimate Resource Name or Location | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] spoofed itself as `AlphaZawgyl_font.exe`, a specialized Unicode font.[^1]  |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] sent generated reports to the C2 via HTTP POST requests.[^1]  |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used the Windows function `GetExtendedUdpTable` to detect connected UDP endpoints.[^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] listed all running processes on the machine.[^1]  |
| [[kb/mitre/attack/techniques/T1069-Permission_Groups_Discovery\|T1069]] | Permission Groups Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the local privileges for the infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] communicated over HTTP with preconfigured C2 servers.[^1]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the operating system name and specific Windows version of an infected machine.[^1]  |
| [[kb/mitre/attack/techniques/T1087-Account_Discovery\|T1087]] | Account Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] listed all non-privileged and privileged accounts available on the machine.[^1]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] had the ability to download additional payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used several Windows API functions to gather information from the infected system.[^1]  |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.[^1]  |
| [[kb/mitre/attack/techniques/T1518-Software_Discovery\|T1518]] | Software Discovery | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered a list of installed software on the infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1560-Archive_Collected_Data\|T1560]] | Archive Collected Data | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used LZ compression to compress initial reconnaissance reports before sending to the C2.[^1] 	 |





> [!info]- References
> [^1]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


