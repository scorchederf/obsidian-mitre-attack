---
aliases: 
    - S0198
    
mitre-attack: https://attack.mitre.org/software/S0198
---

## S0198

[NETWIRE](https://attack.mitre.org/software/S0198) is a publicly available, multiplatform remote administration tool (RAT) that has been used by criminal and APT groups since at least 2012.[^3] [^9] [^10] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [NETWIRE](https://attack.mitre.org/software/S0198) can implement use of proxies to pivot traffic.[^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [NETWIRE](https://attack.mitre.org/software/S0198) creates a Registry start-up entry to establish persistence.[^9] [^8] [^7] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [NETWIRE](https://attack.mitre.org/software/S0198) has used .NET packer tools to evade detection.[^8]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [NETWIRE](https://attack.mitre.org/software/S0198) can use AES encryption for C2 data transferred.[^8]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [NETWIRE](https://attack.mitre.org/software/S0198) has used a custom encryption algorithm to encrypt collected data.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [NETWIRE](https://attack.mitre.org/software/S0198) has been executed through luring victims into opening malicious documents.[^6] [^7] [^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [NETWIRE](https://attack.mitre.org/software/S0198) has been executed through convincing victims into clicking malicious links.[^6] [^7]  |
| [[Automated Collection\|T1119]] | Automated Collection | [NETWIRE](https://attack.mitre.org/software/S0198) can automatically archive collected data.[^8]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | [NETWIRE](https://attack.mitre.org/software/S0198) can use XDG Autostart Entries to establish persistence on Linux systems.[^8]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [NETWIRE](https://attack.mitre.org/software/S0198) has been executed through use of VBScripts.[^6] [^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [NETWIRE](https://attack.mitre.org/software/S0198) has used a custom obfuscation algorithm to hide strings including Registry keys, APIs, and DLL names.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | The [NETWIRE](https://attack.mitre.org/software/S0198) binary has been executed via PowerShell script.[^6]  |
| [[Process Injection\|T1055]] | Process Injection | [NETWIRE](https://attack.mitre.org/software/S0198) can inject code into system processes including notepad.exe, svchost.exe, and vbc.exe.[^8]  |
| [[Cron\|T1053.003]] | Cron | [NETWIRE](https://attack.mitre.org/software/S0198) can use crontabs to establish persistence.[^8]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [NETWIRE](https://attack.mitre.org/software/S0198) can store its configuration information in the Registry under `HKCU:\Software\Netwire`.[^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to search for files on the compromised host.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) can discover processes on compromised hosts.[^6]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to use `/bin/bash` and `/bin/sh` to execute commands.[^8] [^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) can capture session logon details from a compromised host.[^6]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to compress archived screenshots.[^8]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to steal credentials from web browsers including Internet Explorer, Opera, Yandex, and Chrome.[^6] [^8] [^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [NETWIRE](https://attack.mitre.org/software/S0198) has been spread via e-mail campaigns utilizing malicious links.[^7]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [NETWIRE](https://attack.mitre.org/software/S0198) can retrieve passwords from messaging and mail client applications.[^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [NETWIRE](https://attack.mitre.org/software/S0198) has masqueraded as legitimate software including TeamViewer and macOS Finder.[^8]  |
| [[Web Service\|T1102]] | Web Service | [NETWIRE](https://attack.mitre.org/software/S0198) has used web services including Paste.ee to host payloads.[^6]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [NETWIRE](https://attack.mitre.org/software/S0198) can copy itself to and launch itself from hidden folders.[^8]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) can discover and close windows on controlled systems.[^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [NETWIRE](https://attack.mitre.org/software/S0198) can issue commands using cmd.exe.[^8] [^1]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | The [NETWIRE](https://attack.mitre.org/software/S0198) client has been signed by fake and invalid digital certificates.[^9]  |
| [[Keylogging\|T1056.001]] | Keylogging | [NETWIRE](https://attack.mitre.org/software/S0198) can perform keylogging.[^9] [^10] [^6] [^8] [^1]  |
| [[Native API\|T1106]] | Native API | [NETWIRE](https://attack.mitre.org/software/S0198) can use Native API including `CreateProcess` `GetProcessById`, and `WriteProcessMemory`.[^6]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [NETWIRE](https://attack.mitre.org/software/S0198) can create a scheduled task to establish persistence.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [NETWIRE](https://attack.mitre.org/software/S0198) can capture the victim's screen.[^9] [^6] [^8] [^1]  |
| [[Login Items\|T1547.015]] | Login Items | [NETWIRE](https://attack.mitre.org/software/S0198) can persist via startup options for Login items.[^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) can collect the IP address of a compromised host.[^8] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to communicate over HTTP.[^8] [^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | The [NETWIRE](https://attack.mitre.org/software/S0198) payload has been injected into benign Microsoft executables via process hollowing.[^6] [^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [NETWIRE](https://attack.mitre.org/software/S0198) can modify the Registry to store its configuration information.[^8]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NETWIRE](https://attack.mitre.org/software/S0198) can discover and collect victim system information.[^9]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [NETWIRE](https://attack.mitre.org/software/S0198) has been spread via e-mail campaigns utilizing malicious attachments.[^7] [^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to write collected data to a file created in the `./LOGS` directory.[^6]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [NETWIRE](https://attack.mitre.org/software/S0198) can use TCP in C2 communications.[^8] [^7]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [NETWIRE](https://attack.mitre.org/software/S0198) can encrypt C2 communications.[^8]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [NETWIRE](https://attack.mitre.org/software/S0198) can use launch agents for persistence.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NETWIRE](https://attack.mitre.org/software/S0198) can downloaded payloads from C2 to the compromised host.[^6] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[The White Company\|G0089]] | The White Company |
| [[APT33\|G0064]] | APT33 |
| [[SilverTerrier\|G0083]] | SilverTerrier |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)


[^2]: NETWIRE


[^3]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^4]: [Unit42 SilverTerrier 2018](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)


[^5]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^6]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)


[^7]: [Unit 42 NETWIRE April 2020](https://unit42.paloaltonetworks.com/guloader-installing-netwire-rat/)


[^8]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^9]: [McAfee Netwire Mar 2015](https://securingtomorrow.mcafee.com/mcafee-labs/netwire-rat-behind-recent-targeted-attacks/)


[^10]: [FireEye APT33 Webinar Sept 2017](https://www.brighttalk.com/webcast/10703/275683)


[^11]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


