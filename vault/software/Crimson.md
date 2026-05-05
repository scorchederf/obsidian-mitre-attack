---
aliases: 
    - S0115
    
mitre-attack: https://attack.mitre.org/software/S0115
---

## S0115

[Crimson](https://attack.mitre.org/software/S0115) is a remote access Trojan that has been used by [Transparent Tribe](https://attack.mitre.org/groups/G0134) since at least 2016.[^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains commands to list files and directories, as well as search for files matching certain extensions from a defined list.[^3] [^1] [^2]  |
| [[Video Capture\|T1125]] | Video Capture | [Crimson](https://attack.mitre.org/software/S0115) can capture webcam video on targeted systems.[^3] [^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect information about anti-virus software on the victim.[^3] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Crimson](https://attack.mitre.org/software/S0115) can add Registry run keys for persistence.[^3] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Crimson](https://attack.mitre.org/software/S0115) has the ability to delete files from a compromised host.[^3] [^1] [^2] 	  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Crimson](https://attack.mitre.org/software/S0115) has the ability to determine the date and time on a compromised host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect the victim PC name and operating system.[^3] [^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Crimson](https://attack.mitre.org/software/S0115) can decode its encoded PE file prior to execution.[^3]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Crimson](https://attack.mitre.org/software/S0115) can determine when it has been installed on a host for at least 15 days before downloading the final payload.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Crimson](https://attack.mitre.org/software/S0115) can use a module to perform keylogging on compromised hosts.[^3] [^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Crimson](https://attack.mitre.org/software/S0115) can use a HTTP GET request to download its final payload.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Crimson](https://attack.mitre.org/software/S0115) can collect information from a compromised host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Crimson](https://attack.mitre.org/software/S0115) can identify the user on a targeted system.[^3] [^1] [^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Crimson](https://attack.mitre.org/software/S0115) contains a command to perform screen captures.[^3] [^1] [^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Crimson](https://attack.mitre.org/software/S0115) can perform audio surveillance using microphones.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Crimson](https://attack.mitre.org/software/S0115) can exfiltrate stolen information over its C2.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains a command to list processes.[^3] [^1] [^2] 	  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect and exfiltrate emails from Outlook.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Crimson](https://attack.mitre.org/software/S0115) can set a Registry key to determine how long it has been installed and possibly to indicate the version number.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect the victim MAC address and LAN IP.[^3] [^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Crimson](https://attack.mitre.org/software/S0115) has the ability to discover pluggable/removable drives to extract files from.[^3] [^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Crimson](https://attack.mitre.org/software/S0115) contains a module to collect data from removable drives.[^3] [^1]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Crimson](https://attack.mitre.org/software/S0115) can spread across systems by infecting removable media.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Crimson](https://attack.mitre.org/software/S0115) can identify the geographical location of a victim host.[^1] 	  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Crimson](https://attack.mitre.org/software/S0115) contains a command to retrieve files from its C2 server.[^3] [^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Crimson](https://attack.mitre.org/software/S0115) has the ability to execute commands with the COMSPEC environment variable.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Crimson](https://attack.mitre.org/software/S0115) uses a custom TCP protocol for C2.[^3] [^1] 	  |
| [[Query Registry\|T1012]] | Query Registry | [Crimson](https://attack.mitre.org/software/S0115) can check the Registry for the presence of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\last_edate` to determine how long it has been installed on a host.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Crimson](https://attack.mitre.org/software/S0115) contains a module to steal credentials from Web browsers on the victim machine.[^3] [^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect disk drive information.[^3] [^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Transparent Tribe\|G0134]] | Transparent Tribe |



## References

[^1]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^2]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^3]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^4]: MSIL/Crimson


