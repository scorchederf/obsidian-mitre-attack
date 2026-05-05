---
aliases: 
    - S0192
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0192-Pupy
---

## Description

[[kb/mitre/attack/software/S0192-Pupy\|Pupy]] is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. [^1]  It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). [^1]  [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] is publicly available on GitHub. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can execute Lazagne as well as [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] using PowerShell.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1003.005-Cached_Domain_Credentials\|T1003.005]] | Cached Domain Credentials | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^1]  |
| [[kb/mitre/attack/techniques/T1021.001-Remote_Desktop_Protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can enable/disable RDP connection and can start a remote desktop session using a browser web socket client.[^1]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^1]  |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a built-in module for port scanning.[^1]  |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a built-in utility command for `netstat`, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.[^1]  |
| [[kb/mitre/attack/techniques/T1055.001-Dynamic-link_Library_Injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can migrate into another process using reflective DLL injection.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] uses a keylogger to capture keystrokes it then sends back to the server after it is stopped.[^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can list the running processes and get the process ID and parent process’s ID.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a module for loading and executing PowerShell scripts.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use an add on feature when creating payloads that allows you to create custom Python scripts (“scriptlets”) to perform tasks offline (without requiring a session) such as sandbox detection, adding persistence, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can communicate over HTTP for C2.[^1]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can grab a system’s information including the OS version, architecture, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can walk through directories and recursively search for strings in files.[^1]  |
| [[kb/mitre/attack/techniques/T1087.001-Local_Account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] uses PowerView and Pywerview to perform discovery commands such as net user, net group, net local group, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can upload and download to/from a victim machine.[^1]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.[^1]  |
| [[kb/mitre/attack/techniques/T1114.001-Local_Email_Collection\|T1114.001]] | Local Email Collection | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can interact with a victim’s Outlook session and look through folders and emails.[^1]  |
| [[kb/mitre/attack/techniques/T1123-Audio_Capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can record sound with the microphone.[^1]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can access a connected webcam and capture pictures.[^1]  |
| [[kb/mitre/attack/techniques/T1134.001-Token_Impersonation_Theft\|T1134.001]] | Token Impersonation／Theft | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can obtain a list of SIDs and provide the option for selecting process tokens to impersonate.[^1]  |
| [[kb/mitre/attack/techniques/T1135-Network_Share_Discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can list local and remote shared drives and folders over SMB.[^1]  |
| [[kb/mitre/attack/techniques/T1136.001-Local_Account\|T1136.001]] | Local Account | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can user PowerView to execute “net user” commands and create local system accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1136.002-Domain_Account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can user PowerView to execute “net user” commands and create domain accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1497.001-System_Checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a module that checks a number of indicators on the system to determine if its running on a virtual machine.[^1]  |
| [[kb/mitre/attack/techniques/T1543.002-Systemd_Service\|T1543.002]] | Systemd Service | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can be used to establish persistence using a systemd service.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] adds itself to the startup folder or adds itself to the Registry key `SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run` for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1547.013-XDG_Autostart_Entries\|T1547.013]] | XDG Autostart Entries | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use an XDG Autostart to establish persistence.[^2]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.[^1]  |
| [[kb/mitre/attack/techniques/T1550.003-Pass_the_Ticket\|T1550.003]] | Pass the Ticket | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can also perform pass-the-ticket.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1555-Credentials_from_Password_Stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can sniff plaintext network credentials and use NBNS Spoofing to poison name services.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can compress data with Zip before sending it over C2.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] uses [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] to execute a payload or commands on a remote host.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]]'s default encryption for its C2 communication channel is SSL, but it also has transport options for RSA and AES.[^1]  |
| [[kb/mitre/attack/techniques/T1685.005-Clear_Windows_Event_Logs\|T1685.005]] | Clear Windows Event Logs | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a module to clear event logs with PowerShell.[^1]  |





> [!info]- References
> [^1]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^2]: [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


