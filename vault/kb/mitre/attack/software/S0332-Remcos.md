---
aliases: 
    - S0332
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0332-Remcos
---

## Description

[[kb/mitre/attack/software/S0332-Remcos\|Remcos]] is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has been observed being used in malware campaigns.[^3] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1010-Application_Window_Discovery\|T1010]] | Application Window Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can list all windows on victim systems.[^4]  |
| [[kb/mitre/attack/techniques/T1012-Query_Registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can obtain Registry data from targeted systems.[^4]  |
| [[kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] uses RC4 and base64 to obfuscate data, including Registry entries and file paths.[^1]  [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can also employ control flow flattening to hinder analysis.[^6]  |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can use string encryption to hinder analysis.[^4]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can enumerate the username on targeted hosts.[^4]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has a command to hide itself by injecting into another process.[^2]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has a command for keylogging.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can discover running processes on compromised machines.[^4] <br> |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can launch a remote command line to execute commands on the victim’s machine.[^2] [^4]  |
| [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|T1059.005]] | Visual Basic | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can execute VBS remotely.[^4]  |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] uses Python scripts.[^3]  |
| [[kb/mitre/attack/techniques/T1059.007-JavaScript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has the ability to execute JavaScript remotely.[^4]  |
| [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can clean saved cookies and logins from the web browser.[^4]  |
| [[kb/mitre/attack/techniques/T1070.004-File_Deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can delete files and folders from victim machines.[^4]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can collect the OS version and process architecture of compromised hosts.[^4]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can search for files on the infected machine.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can upload and download files to and from the victim’s machine.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has full control of the Registry, including the ability to modify it.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] takes automated screenshots of the infected machine.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1115-Clipboard_Data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] steals and modifies data from the clipboard.[^3] [^4]  |
| [[kb/mitre/attack/techniques/T1123-Audio_Capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can capture data from the system’s microphone.[^2] [^4]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can access a system’s webcam and take pictures.[^2]  |
| [[kb/mitre/attack/techniques/T1132.001-Standard_Encoding\|T1132.001]] | Standard Encoding | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can serialize collected data with Protobuf.[^6]  |
| [[kb/mitre/attack/techniques/T1204.002-Malicious_File\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has been executed by luring victims into opening malicious email attachments including Excel files.[^4] <br> |
| [[kb/mitre/attack/techniques/T1491.001-Internal_Defacement\|T1491.001]] | Internal Defacement | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has the ability to modify the desktop wallpaper.[^4]  |
| [[kb/mitre/attack/techniques/T1497.001-System_Checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] searches for Sandboxie and VMware on the system.[^1]  |
| [[kb/mitre/attack/techniques/T1529-System_Shutdown_Reboot\|T1529]] | System Shutdown／Reboot | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can shutdown and restart remote devices.[^4]  |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can terminate, suspend, and resume a process by PID.[^4]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can add itself to the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^2]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has a command for UAC bypassing.[^2]  |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can zip files and folders for upload.[^4]  |
| [[kb/mitre/attack/techniques/T1564-Hide_Artifacts\|T1564]] | Hide Artifacts | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can modify file attributes to hide the file.[^4]  |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can set `ProcessWindowStyle.Hidden` to hide windows.[^6] <br> |
| [[kb/mitre/attack/techniques/T1566.001-Spearphishing_Attachment\|T1566.001]] | Spearphishing Attachment | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has been spread through emails containing malicious documents.[^4]  |
| [[kb/mitre/attack/techniques/T1568-Dynamic_Resolution\|T1568]] | Dynamic Resolution | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has used dynamic DNS domains in C2 communications.[^6]  |
| [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can use TLS to encrypt C2 communication.[^4]  |
| [[kb/mitre/attack/techniques/T1614-System_Location_Discovery\|T1614]] | System Location Discovery | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can identify the location of targeted devices.[^4]  |





> [!info]- References
> [^1]: [Talos Remcos Aug 2018](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)

> [^2]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)

> [^3]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^4]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^5]: Remcos

> [^6]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


