---
aliases: 
    - S0615
    
mitre-attack: https://attack.mitre.org/software/S0615
---

## S0615

[SombRAT](https://attack.mitre.org/software/S0615) is a modular backdoor written in C++ that has been used since at least 2019 to download and execute malicious payloads, including [FIVEHANDS](https://attack.mitre.org/software/S0618) ransomware.[^1] [^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [SombRAT](https://attack.mitre.org/software/S0615) can SSL encrypt C2 traffic.[^1] [^2] [^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can execute `getinfo`  to discover the current time on a compromised host.[^1] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can use the `getprocesslist` command to enumerate processes on a compromised host.[^1] [^2] [^3]  |
| [[Proxy\|T1090]] | Proxy | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to use an embedded SOCKS proxy in C2 communications.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SombRAT](https://attack.mitre.org/software/S0615) can run `upload` to decrypt and upload files from storage.[^1] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SombRAT](https://attack.mitre.org/software/S0615) has collected data and files from a compromised host.[^1] [^3]  |
| [[Native API\|T1106]] | Native API | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to respawn itself using `ShellExecuteW` and `CreateProcessW`.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SombRAT](https://attack.mitre.org/software/S0615) can encrypt strings with XOR-based routines and use a custom AES storage format for plugins, configuration, C2 domains, and harvested data.[^1] [^2] [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion |  [SombRAT](https://attack.mitre.org/software/S0615) has the ability to run `cancel` or `closeanddeletestorage` to remove all files from storage and delete the storage temp file on a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to download and execute additional payloads.[^1] [^2] [^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to use TCP sockets to send data and ICMP to ping the C2 server.[^1] [^2]  |
| [[Process Argument Spoofing\|T1564.010]] | Process Argument Spoofing | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to modify its process memory to hide process command-line arguments.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can execute `getinfo`  to identify the username on a compromised host.[^1] [^3]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [SombRAT](https://attack.mitre.org/software/S0615) has encrypted collected data with AES-256 using a hardcoded key.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SombRAT](https://attack.mitre.org/software/S0615) has encrypted its C2 communications with AES.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SombRAT](https://attack.mitre.org/software/S0615) has uploaded collected data and files from a compromised host to its C2 server.[^1]  |
| [[DNS\|T1071.004]] | DNS | [SombRAT](https://attack.mitre.org/software/S0615) can communicate over DNS with the C2 server.[^1] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SombRAT](https://attack.mitre.org/software/S0615) can store harvested data in a custom database under the %TEMP% directory.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [SombRAT](https://attack.mitre.org/software/S0615) can use a custom DGA to generate a subdomain for C2.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can enumerate services on a victim machine.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [SombRAT](https://attack.mitre.org/software/S0615) can execute `loadfromfile`, `loadfromstorage`, and `loadfrommem` to inject a DLL  from disk, storage, or memory respectively.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can execute `enum` to enumerate files in storage on a compromised system.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [SombRAT](https://attack.mitre.org/software/S0615) can use a legitimate process name to hide itself.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SombRAT](https://attack.mitre.org/software/S0615) can execute `getinfo` to enumerate the computer name and OS version of a compromised system.[^1]  |




## References

[^1]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^2]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^3]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


