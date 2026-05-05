---
aliases: 
    - S0262
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0262-QuasarRAT
---

## Description

[[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] is developed in the C# language.[^4] [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can retrieve files from compromised client machines.[^6]  |
| [[kb/mitre/attack/techniques/T1010-Application_Window_Discovery\|T1010]] | Application Window Discovery | APT-C-36 used a customized version of [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] to monitor browser windows for strings relating to specific Colombian financial institutions.[^7] <br> |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^6]  |
| [[kb/mitre/attack/techniques/T1021.001-Remote_Desktop_Protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has a module for performing remote desktop access.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can enumerate the username and account type.[^6]  |
| [[kb/mitre/attack/techniques/T1053.005-Scheduled_Task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] contains a .NET wrapper DLL for creating and managing scheduled tasks for maintaining persistence upon reboot.[^3] [^6]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has a built-in keylogger.[^4] [^3] [^7]  |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can launch a remote shell to execute commands on the victim’s machine.[^4] [^6]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can gather system information from the victim’s machine including the OS type.[^4]  |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can communicate over a reverse proxy using SOCKS5.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1095-Non-Application_Layer_Protocol\|T1095]] | Non-Application Layer Protocol | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can use TCP for C2 communication.[^6]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can download files to the victim’s machine and execute them.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has a command to edit the Registry on the victim’s machine.[^4] [^6]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can perform webcam viewing.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | If the [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] client process does not have administrator privileges it will add a registry key to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^4] [^6]   |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | <br>[[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.[^6]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can obtain passwords from FTP clients.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1553.002-Code_Signing\|T1553.002]] | Code Signing | A [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] .dll file is digitally signed by a certificate from AirVPN.[^3]  |
| [[kb/mitre/attack/techniques/T1555-Credentials_from_Password_Stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can obtain passwords from common FTP clients.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can obtain passwords from common web browsers.[^4] [^3] [^7] <br> |
| [[kb/mitre/attack/techniques/T1564.001-Hidden_Files_and_Directories\|T1564.001]] | Hidden Files and Directories | <br>[[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has the ability to set file attributes to "hidden" to hide files from the compromised user's view in Windows File Explorer.[^6]  |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can hide process windows and make web requests invisible to the compromised user. Requests marked as invisible have been sent with user-agent string `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A` though [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can only be run on Windows systems.[^6]  |
| [[kb/mitre/attack/techniques/T1571-Non-Standard_Port\|T1571]] | Non-Standard Port | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can use port 4782 on the compromised host for TCP callbacks.[^6]  |
| [[kb/mitre/attack/techniques/T1573.001-Symmetric_Cryptography\|T1573.001]] | Symmetric Cryptography | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] uses AES with a hardcoded pre-shared key to encrypt network communication.[^4] [^3] [^6]  |
| [[kb/mitre/attack/techniques/T1614-System_Location_Discovery\|T1614]] | System Location Discovery | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can determine the country a victim host is located in.[^6]  |





> [!info]- References
> [^1]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)

> [^2]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)

> [^3]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)

> [^4]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)

> [^5]: QuasarRAT

> [^6]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^7]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)

> [^8]: xRAT


