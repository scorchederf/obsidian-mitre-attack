---
aliases: 
    - S0283
    
mitre-attack: https://attack.mitre.org/software/S0283
---

## S0283

[jRAT](https://attack.mitre.org/software/S0283) is a cross-platform, Java-based backdoor originally available for purchase in 2012. Variants of [jRAT](https://attack.mitre.org/software/S0283) have been distributed via a software-as-a-service platform, similar to an online subscription model.[^6]  [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [jRAT](https://attack.mitre.org/software/S0283) has the capability to log keystrokes from the victim’s machine, both offline and online.[^9] [^6]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [jRAT](https://attack.mitre.org/software/S0283) can map UPnP ports.[^6]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [jRAT](https://attack.mitre.org/software/S0283) can be configured to reconnect at certain intervals.[^6]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [jRAT](https://attack.mitre.org/software/S0283) uses WMIC to identify anti-virus products installed on the victim’s machine and to obtain firewall details.[^9]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [jRAT](https://attack.mitre.org/software/S0283) has been distributed as HTA files with VBScript.[^6] 	 |
| [[Video Capture\|T1125]] | Video Capture | [jRAT](https://attack.mitre.org/software/S0283) has the capability to capture video from a webcam.[^9] [^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [jRAT](https://attack.mitre.org/software/S0283) has command line access.[^6]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [jRAT](https://attack.mitre.org/software/S0283) can list local services.[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [jRAT](https://attack.mitre.org/software/S0283) has a function to delete files from the victim’s machine.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [jRAT](https://attack.mitre.org/software/S0283) collects information about the OS (version, build type, install date) as well as system up-time upon receiving a connection from a backdoor.[^13]  |
| [[Startup Items\|T1037.005]] | Startup Items | [jRAT](https://attack.mitre.org/software/S0283) can list and manage startup entries.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [jRAT](https://attack.mitre.org/software/S0283) can download and execute files.[^9] [^6] [^13]  |
| [[Process Discovery\|T1057]] | Process Discovery | [jRAT](https://attack.mitre.org/software/S0283) can query and kill system processes.[^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [jRAT](https://attack.mitre.org/software/S0283) can browse file systems.[^6] [^13]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [jRAT](https://attack.mitre.org/software/S0283) can support RDP control.[^6]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [jRAT](https://attack.mitre.org/software/S0283) can capture passwords from common web browsers such as Internet Explorer, Google Chrome, and Firefox.[^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | [jRAT](https://attack.mitre.org/software/S0283) payloads have been packed.[^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [jRAT](https://attack.mitre.org/software/S0283) can list security software, such as by using WMIC to identify anti-virus products installed on the victim’s machine and to obtain firewall details.[^9] [^6]  |
| [[Proxy\|T1090]] | Proxy | [jRAT](https://attack.mitre.org/software/S0283) can serve as a SOCKS proxy server.[^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [jRAT](https://attack.mitre.org/software/S0283) has been distributed as HTA files with JScript.[^6] 	 |
| [[Clipboard Data\|T1115]] | Clipboard Data | [jRAT](https://attack.mitre.org/software/S0283) can capture clipboard data.[^6]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [jRAT](https://attack.mitre.org/software/S0283) can capture passwords from common chat applications such as MSN Messenger, AOL, Instant Messenger, and and Google Talk.[^6]  |
| [[Audio Capture\|T1123]] | Audio Capture | [jRAT](https://attack.mitre.org/software/S0283) can capture microphone recordings.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [jRAT](https://attack.mitre.org/software/S0283) has the capability to take screenshots of the victim’s machine.[^9] [^6]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [jRAT](https://attack.mitre.org/software/S0283) can list network connections.[^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [jRAT](https://attack.mitre.org/software/S0283)’s Java payload is encrypted with AES.[^9]  Additionally, backdoor files are encrypted using DES as a stream cipher. Later variants of [jRAT](https://attack.mitre.org/software/S0283) also incorporated AV evasion methods such as Java bytecode obfuscation via the commercial Allatori obfuscation tool.[^13]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [jRAT](https://attack.mitre.org/software/S0283) can gather victim internal and external IPs.[^6]  |
| [[Private Keys\|T1552.004]] | Private Keys | [jRAT](https://attack.mitre.org/software/S0283) can steal keys for VPNs and cryptocurrency wallets.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: JSocket


[^2]: Frutas


[^3]: Sockrat


[^4]: jBiFrost


[^5]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^6]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^7]: Trojan.Maljava


[^8]: jRAT


[^9]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)


[^10]: Adwind


[^11]: AlienSpy


[^12]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


[^13]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)


[^14]: jFrutas


[^15]: Unrecom


