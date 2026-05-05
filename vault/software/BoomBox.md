---
aliases: 
    - S0635
    
mitre-attack: https://attack.mitre.org/software/S0635
---

## S0635

[BoomBox](https://attack.mitre.org/software/S0635) is a downloader responsible for executing next stage components that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Rundll32\|T1218.011]] | Rundll32 | [BoomBox](https://attack.mitre.org/software/S0635) can use RunDLL32 for execution.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BoomBox](https://attack.mitre.org/software/S0635) has the ability to download next stage malware components to a compromised system.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BoomBox](https://attack.mitre.org/software/S0635) can decrypt AES-encrypted files downloaded from C2.[^1]  |
| [[Web Service\|T1102]] | Web Service | [BoomBox](https://attack.mitre.org/software/S0635) can download files from Dropbox using a hardcoded access token.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [BoomBox](https://attack.mitre.org/software/S0635) has the ability to execute an LDAP query to enumerate the distinguished name, SAM account name, and display name for all domain users.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BoomBox](https://attack.mitre.org/software/S0635) has used HTTP POST requests for C2.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BoomBox](https://attack.mitre.org/software/S0635) has gained execution through user interaction with a malicious file.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BoomBox](https://attack.mitre.org/software/S0635) can enumerate the hostname, domain, and IP of a compromised host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BoomBox](https://attack.mitre.org/software/S0635) can search for specific files and directories on a machine.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [BoomBox](https://attack.mitre.org/software/S0635) has the ability to mask malicious data strings as PDF files.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BoomBox](https://attack.mitre.org/software/S0635) can check its current working directory and for the presence of a specific file and terminate if specific values are not found.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BoomBox](https://attack.mitre.org/software/S0635) can establish persistence by writing the Registry value `MicroNativeCacheSvc` to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BoomBox](https://attack.mitre.org/software/S0635) can enumerate the username on a compromised host.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [BoomBox](https://attack.mitre.org/software/S0635) can upload data to dedicated per-victim folders in Dropbox.[^1]  |
| [[Email Account\|T1087.003]] | Email Account | [BoomBox](https://attack.mitre.org/software/S0635) can execute an LDAP query to discover e-mail accounts for domain users.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BoomBox](https://attack.mitre.org/software/S0635) can encrypt data using AES prior to exfiltration.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


