---
aliases: 
    - S0476
    
mitre-attack: https://attack.mitre.org/software/S0476
---

## S0476

[Valak](https://attack.mitre.org/software/S0476) is a multi-stage modular malware that can function as a standalone information stealer or downloader, first observed in 2019 targeting enterprises in the US and Germany.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [Valak](https://attack.mitre.org/software/S0476) has the ability to modify the Registry key `HKCU\Software\ApplicationContainer\Appsw64` to store information regarding the C2 server and downloads.[^2] [^1] [^5]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Valak](https://attack.mitre.org/software/S0476) can use a .NET compiled module named exchgrabber to enumerate credentials from the Credential Manager.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Valak](https://attack.mitre.org/software/S0476) has the ability to enumerate running processes on a compromised host.[^2]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Valak](https://attack.mitre.org/software/S0476) has the ability save and execute files as alternate data streams (ADS).[^2] [^1] [^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Valak](https://attack.mitre.org/software/S0476) has the ability to base64 encode and XOR encrypt strings.[^2] [^1] [^5]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Valak](https://attack.mitre.org/software/S0476) has used `regsvr32.exe` to launch malicious DLLs.[^2] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Valak](https://attack.mitre.org/software/S0476) has used HTTP in communications with C2.[^2] [^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [Valak](https://attack.mitre.org/software/S0476) can download additional modules and malware capable of using separate C2 channels.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Valak](https://attack.mitre.org/software/S0476) can communicate over multiple C2 hosts.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Valak](https://attack.mitre.org/software/S0476) can determine if a compromised host has security products installed.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Valak](https://attack.mitre.org/software/S0476) has been executed via Microsoft Word documents containing malicious macros.[^2] [^1] [^5]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Valak](https://attack.mitre.org/software/S0476) has the ability to take screenshots on a compromised host.[^2] 	  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Valak](https://attack.mitre.org/software/S0476) can gather information regarding the user.[^2]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Valak](https://attack.mitre.org/software/S0476) can execute tasks via OLE.[^5]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Valak](https://attack.mitre.org/software/S0476) can execute JavaScript containing configuration data for establishing persistence.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Valak](https://attack.mitre.org/software/S0476) can determine the Windows version and computer name on a compromised host.[^2] [^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Valak](https://attack.mitre.org/software/S0476) has been delivered via spearphishing e-mails with password protected ZIP files.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Valak](https://attack.mitre.org/software/S0476) can download a module to search for and build a report of harvested credential data.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Valak](https://attack.mitre.org/software/S0476) has downloaded a variety of modules and payloads to the compromised host, including [IcedID](https://attack.mitre.org/software/S0483) and NetSupport Manager RAT-based malware.[^1] [^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Valak](https://attack.mitre.org/software/S0476) has the ability to exfiltrate data over the C2 channel.[^2] [^1] [^5]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [Valak](https://attack.mitre.org/software/S0476) can use the clientgrabber module to steal e-mail credentials from the Registry.[^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Valak](https://attack.mitre.org/software/S0476) has the ability to identify the domain and the MAC and IP addresses of an infected machine.[^2]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Valak](https://attack.mitre.org/software/S0476) can collect sensitive mailing information from Exchange servers, including credentials and the domain certificate of an enterprise.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Valak](https://attack.mitre.org/software/S0476) has used packed DLL payloads.[^5]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Valak](https://attack.mitre.org/software/S0476) has the ability to store information regarding the C2 server and downloads in the Registry key `HKCU\Software\ApplicationContainer\Appsw64`.[^2] [^1] [^5]  |
| [[Query Registry\|T1012]] | Query Registry | [Valak](https://attack.mitre.org/software/S0476) can use the Registry for code updates and to collect credentials.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Valak](https://attack.mitre.org/software/S0476) has used scheduled tasks to execute additional payloads and to gain persistence on a compromised host.[^2] [^1] [^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Valak](https://attack.mitre.org/software/S0476) has the ability to decode and decrypt downloaded files.[^2] [^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Valak](https://attack.mitre.org/software/S0476) has returned C2 data as encoded ASCII.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Valak](https://attack.mitre.org/software/S0476) has the ability to enumerate domain admin accounts.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Valak](https://attack.mitre.org/software/S0476) has the ability to enumerate local admin accounts.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Valak](https://attack.mitre.org/software/S0476) has used PowerShell to download additional modules.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Valak](https://attack.mitre.org/software/S0476) can use `wmic process call create` in a scheduled task to launch plugins and for execution.[^5]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Valak](https://attack.mitre.org/software/S0476) has been delivered via malicious links in e-mail.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA551\|G0127]] | TA551 |



## References

[^1]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^2]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^3]: [Secureworks GOLD CABIN](https://www.secureworks.com/research/threat-profiles/gold-cabin)


[^4]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^5]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)


