---
aliases: 
    - S0192
    
mitre-attack: https://attack.mitre.org/software/S0192
---

## S0192

[Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. [^2]  It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). [^2]  [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Execution\|T1569.002]] | Service Execution | [Pupy](https://attack.mitre.org/software/S0192) uses [PsExec](https://attack.mitre.org/software/S0029) to execute a payload or commands on a remote host.[^2]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Pupy](https://attack.mitre.org/software/S0192) has a built-in module for port scanning.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Pupy](https://attack.mitre.org/software/S0192) can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.[^2]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pupy](https://attack.mitre.org/software/S0192) can upload and download to/from a victim machine.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Pupy](https://attack.mitre.org/software/S0192) can list local and remote shared drives and folders over SMB.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Pupy](https://attack.mitre.org/software/S0192)'s default encryption for its C2 communication channel is SSL, but it also has transport options for RSA and AES.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Pupy](https://attack.mitre.org/software/S0192) can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Pupy](https://attack.mitre.org/software/S0192) has a module for loading and executing PowerShell scripts.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Pupy](https://attack.mitre.org/software/S0192) can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^2]  |
| [[Domain Account\|T1136.002]] | Domain Account | [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create domain accounts.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Pupy](https://attack.mitre.org/software/S0192) can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.[^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Pupy](https://attack.mitre.org/software/S0192) can record sound with the microphone.[^2]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Pupy](https://attack.mitre.org/software/S0192) can migrate into another process using reflective DLL injection.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Pupy](https://attack.mitre.org/software/S0192) has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^2]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Pupy](https://attack.mitre.org/software/S0192) can interact with a victim’s Outlook session and look through folders and emails.[^2]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Pupy](https://attack.mitre.org/software/S0192) can be used to establish persistence using a systemd service.[^2]  |
| [[Local Account\|T1136.001]] | Local Account | [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create local system accounts.[^2]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | [Pupy](https://attack.mitre.org/software/S0192) can use an XDG Autostart to establish persistence.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Pupy](https://attack.mitre.org/software/S0192) can walk through directories and recursively search for strings in files.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pupy](https://attack.mitre.org/software/S0192) can grab a system’s information including the OS version, architecture, etc.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Pupy](https://attack.mitre.org/software/S0192) can execute Lazagne as well as [Mimikatz](https://attack.mitre.org/software/S0002) using PowerShell.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Pupy](https://attack.mitre.org/software/S0192) uses a keylogger to capture keystrokes it then sends back to the server after it is stopped.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Pupy](https://attack.mitre.org/software/S0192) can communicate over HTTP for C2.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Pupy](https://attack.mitre.org/software/S0192) has a module that checks a number of indicators on the system to determine if its running on a virtual machine.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Pupy](https://attack.mitre.org/software/S0192) can enable/disable RDP connection and can start a remote desktop session using a browser web socket client.[^2]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | [Pupy](https://attack.mitre.org/software/S0192) can also perform pass-the-ticket.[^2]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Pupy](https://attack.mitre.org/software/S0192) can sniff plaintext network credentials and use NBNS Spoofing to poison name services.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Pupy](https://attack.mitre.org/software/S0192) uses PowerView and Pywerview to perform discovery commands such as net user, net group, net local group, etc.[^2]  |
| [[Python\|T1059.006]] | Python | [Pupy](https://attack.mitre.org/software/S0192) can use an add on feature when creating payloads that allows you to create custom Python scripts (“scriptlets”) to perform tasks offline (without requiring a session) such as sandbox detection, adding persistence, etc.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [Pupy](https://attack.mitre.org/software/S0192) can access a connected webcam and capture pictures.[^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Pupy](https://attack.mitre.org/software/S0192) has a module to clear event logs with PowerShell.[^2]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Pupy](https://attack.mitre.org/software/S0192) can obtain a list of SIDs and provide the option for selecting process tokens to impersonate.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Pupy](https://attack.mitre.org/software/S0192) can compress data with Zip before sending it over C2.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Pupy](https://attack.mitre.org/software/S0192) adds itself to the startup folder or adds itself to the Registry key `SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run` for persistence.[^2]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.[^2]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Pupy](https://attack.mitre.org/software/S0192) has a built-in utility command for `netstat`, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.[^2]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Pupy](https://attack.mitre.org/software/S0192) can list the running processes and get the process ID and parent process’s ID.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[APT33\|G0064]] | APT33 |



## References

[^1]: [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^2]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^3]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^4]: [Secureworks Cobalt Gypsy Feb 2017](https://www.secureworks.com/blog/iranian-pupyrat-bites-middle-eastern-organizations)


[^5]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^6]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


