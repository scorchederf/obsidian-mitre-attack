---
aliases: 
    - S1146
    
mitre-attack: https://attack.mitre.org/software/S1146
---

## S1146

[MgBot](https://attack.mitre.org/software/S1146) is a modular malware framework exclusively associated with [Daggerfly](https://attack.mitre.org/groups/G1034) operations since at least 2012. [MgBot](https://attack.mitre.org/software/S1146) was developed in C++ and features a module design with multiple available plugins that have been under active development through 2024.[^1] [^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [MgBot](https://attack.mitre.org/software/S1146) includes keylogger payloads focused on the QQ chat application.[^3] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MgBot](https://attack.mitre.org/software/S1146) includes modules for identifying local users and administrators on victim machines.[^4]  |
| [[Domain Account\|T1087.002]] | Domain Account | [MgBot](https://attack.mitre.org/software/S1146) includes modules for collecting information on Active Directory domain accounts.[^4]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [MgBot](https://attack.mitre.org/software/S1146) includes modules for dumping and capturing credentials from process memory.[^4]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [MgBot](https://attack.mitre.org/software/S1146) includes modules for stealing stored credentials from Outlook and Foxmail email client software.[^3] [^4]  |
| [[Local Account\|T1087.001]] | Local Account | [MgBot](https://attack.mitre.org/software/S1146) includes modules for identifying local administrator accounts on victim systems.[^4]  |
| [[Databases\|T1213.006]] | Databases | [MgBot](https://attack.mitre.org/software/S1146) includes a module capable of stealing content from the Tencent QQ database storing user QQ message history on infected devices.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [MgBot](https://attack.mitre.org/software/S1146) includes modules for stealing credentials from various browsers and applications, including Chrome, Opera, Firefox, Foxmail, QQBrowser, FileZilla, and WinSCP.[^3] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MgBot](https://attack.mitre.org/software/S1146) includes modules for collecting files from local systems based on a given set of properties and filenames.[^3]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [MgBot](https://attack.mitre.org/software/S1146) includes modules capable of gathering information from USB thumb drives and CD-ROMs on the victim machine given a list of provided criteria.[^3]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [MgBot](https://attack.mitre.org/software/S1146) includes modules for collecting information on local domain users and permissions.[^4]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [MgBot](https://attack.mitre.org/software/S1146) can capture clipboard data.[^3] [^4]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [MgBot](https://attack.mitre.org/software/S1146) includes modules that can steal cookies from Firefox, Chrome, and Edge web browsers.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [MgBot](https://attack.mitre.org/software/S1146) includes modules for performing ARP scans of local connected systems.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MgBot](https://attack.mitre.org/software/S1146) includes a module for establishing a process watchdog for itself, identifying if the [MgBot](https://attack.mitre.org/software/S1146) process is still running.[^4]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [MgBot](https://attack.mitre.org/software/S1146) includes modules for performing HTTP and server service scans.[^4]  |
| [[Audio Capture\|T1123]] | Audio Capture | [MgBot](https://attack.mitre.org/software/S1146) can capture input and output audio streams from infected devices.[^3] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Daggerfly\|G1034]] | Daggerfly |



## References

[^1]: [Szappanos MgBot 2014](https://www.virusbulletin.com/virusbulletin/2014/02/needle-haystack)


[^2]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)


[^3]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)


[^4]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


