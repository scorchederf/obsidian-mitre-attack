---
aliases: 
    - Cinnamon Tempest
    - DEV-0401
    - Emperor Dragonfly
    - BRONZE STARLIGHT
mitre-attack: https://attack.mitre.org/groups/G1021
---

## G1021

[Cinnamon Tempest](https://attack.mitre.org/groups/G1021) is a China-based threat group that has been active since at least 2021 deploying multiple strains of ransomware based on the leaked [Babuk](https://attack.mitre.org/software/S0638) source code. [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) does not operate their ransomware on an affiliate model or purchase access but appears to act independently in all stages of the attack lifecycle. Based on victimology, the short lifespan of each ransomware variant, and use of malware attributed to government-sponsored threat groups, [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) may be motivated by intellectual property theft or cyberespionage rather than financial gain.[^7] [^8] [^10] [^9] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used [Impacket](https://attack.mitre.org/software/S0357) for lateral movement via WMI.[^7] [^2]  |
| [[DLL\|T1574.001]] | DLL | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used search order hijacking to launch [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacons.[^7] [^9]  [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has also abused legitimate executables to side-load weaponized DLLs.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has downloaded files, including [Cobalt Strike](https://attack.mitre.org/software/S0154), to compromised hosts.[^2]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used Group Policy to deploy batch scripts for ransomware deployment.[^7]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has uploaded captured keystroke logs to the Alibaba Cloud Object Storage Service, Aliyun OSS.[^2]  |
| [[Tool\|T1588.002]] | Tool | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used open-source tools including customized versions of the Iox proxy tool, NPS tunneling tool, Meterpreter, and a keylogger that uploads data to Alibaba cloud storage.[^2] [^9]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used compromised user accounts to deploy payloads and create system services.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has maintained leak sites for exfiltrated data in attempt to extort victims into paying a ransom.[^7]  |
| [[Proxy\|T1090]] | Proxy | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used a customized version of the Iox port-forwarding and proxy tool.[^2]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has obtained highly privileged credentials such as domain administrator in order to deploy malware.[^7]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has exploited multiple unpatched vulnerabilities for initial access including vulnerabilities in Microsoft Exchange, Manage Engine AdSelfService Plus, Confluence, and Log4j.[^7] [^4] [^2] [^9]  |
| [[Python\|T1059.006]] | Python | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used a customized version of the [Impacket](https://attack.mitre.org/software/S0357) wmiexec.py module to create renamed output files.[^7]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used weaponized DLLs to load and decrypt payloads.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used SMBexec for lateral movement.[^2]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used the Iox and NPS proxy and tunneling tools in combination  create multiple connections through a single tunnel.[^2]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has deployed ransomware from a batch file in a network share.[^7]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has created system services to establish persistence for deployed tooling.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has used PowerShell to communicate with C2, download files, and execute reconnaissance commands.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has executed ransomware using batch scripts deployed via GPO.[^7]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Sliver\|S0633]] | Sliver |  [^7]  |
| [[Impacket\|S0357]] | Impacket | [^7] [^2]  |
| [[Rclone\|S1040]] | Rclone | [^2] <br> |
| [[HUI Loader\|S1097]] | HUI Loader | [^9] [^1]  |
| [[Cheerscrypt\|S1096]] | Cheerscrypt | [^2] [^10]  |
| [[PlugX\|S0013]] | PlugX | [^1]  |
| [[Pandora\|S0664]] | Pandora |  [^7] [^9] [^2] [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^7] [^1]  |



## References

[^1]: [Dell SecureWorks BRONZE STARLIGHT Profile](https://www.secureworks.com/research/threat-profiles/bronze-starlight)


[^2]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^3]: BRONZE STARLIGHT


[^4]: [Microsoft Log4j Vulnerability Exploitation December 2021](https://www.microsoft.com/en-us/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/)


[^5]: Emperor Dragonfly


[^6]: DEV-0401


[^7]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)


[^10]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)


