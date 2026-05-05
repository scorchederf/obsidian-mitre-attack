---
aliases: 
    - S1138
    
mitre-attack: https://attack.mitre.org/software/S1138
---

## S1138

[Gootloader](https://attack.mitre.org/software/S1138) is a Javascript-based infection framework that has been used since at least 2020 as a delivery method for the Gootkit banking trojan, [Cobalt Strike](https://attack.mitre.org/software/S0154), [REvil](https://attack.mitre.org/software/S0496), and others. [Gootloader](https://attack.mitre.org/software/S1138) operates on an "Initial Access as a Service" model and has leveraged [SEO Poisoning](https://attack.mitre.org/techniques/T1608/006) to provide access to entities in multiple sectors worldwide including financial, military, automotive, pharmaceutical, and energy.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Gootloader](https://attack.mitre.org/software/S1138)  can use IP geolocation to determine if the person browsing to a compromised site is within a targeted territory such as the US, Canada, Germany, and South Korea.[^2]  |
| [[Domains\|T1584.001]] | Domains | [Gootloader](https://attack.mitre.org/software/S1138) has used compromised legitimate domains to as a delivery network for malicious payloads.[^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Gootloader](https://attack.mitre.org/software/S1138) can determine if a targeted system is part of an Active Directory domain by  expanding the %USERDNSDOMAIN%  environment variable.[^2]  |
| [[Web Services\|T1584.006]] | Web Services | [Gootloader](https://attack.mitre.org/software/S1138) can insert malicious scripts to compromise vulnerable content management systems (CMS).[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gootloader](https://attack.mitre.org/software/S1138) can create an autorun entry for a PowerShell script to run at reboot.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Gootloader](https://attack.mitre.org/software/S1138) can use an encoded PowerShell stager to write to the Registry for persistence.[^1] [^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Gootloader](https://attack.mitre.org/software/S1138) can designate a sleep period of more than 22 seconds between stages of infection.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Gootloader](https://attack.mitre.org/software/S1138) can determine if a victim's computer is running an operating system with specific language preferences.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Gootloader](https://attack.mitre.org/software/S1138) has been executed through malicious links presented to users as internet search results.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Gootloader](https://attack.mitre.org/software/S1138) can inspect the User-Agent string in GET request header information to determine the operating system of targeted systems.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Gootloader](https://attack.mitre.org/software/S1138) has the ability to decode and decrypt malicious payloads prior to execution.[^1] [^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Gootloader](https://attack.mitre.org/software/S1138) can execute a Javascript file for initial infection.[^1] [^2]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | <br>[Gootloader](https://attack.mitre.org/software/S1138) can use its own PE loader to execute payloads in memory.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Gootloader](https://attack.mitre.org/software/S1138) can inject its Delphi executable into ImagingDevices.exe using a process hollowing technique.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Gootloader](https://attack.mitre.org/software/S1138) can use an embedded script to check the IP address of potential victims visiting compromised websites.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Gootloader](https://attack.mitre.org/software/S1138) can retrieve a Base64 encoded stager from C2.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gootloader](https://attack.mitre.org/software/S1138) can fetch second stage code from hardcoded web domains.[^1] [^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | <br>The [Gootloader](https://attack.mitre.org/software/S1138) first stage script is obfuscated using random alpha numeric strings.[^1] [^2]  |




## References

[^1]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^2]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)


