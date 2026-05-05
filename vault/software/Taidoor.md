---
aliases: 
    - S0011
    
mitre-attack: https://attack.mitre.org/software/S0011
---

## S0011

[Taidoor](https://attack.mitre.org/software/S0011) is a remote access trojan (RAT) that has been used by Chinese government cyber actors to maintain access on victim networks.[^1]  [Taidoor](https://attack.mitre.org/software/S0011) has primarily been used against Taiwanese government organizations since at least 2010.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Taidoor](https://attack.mitre.org/software/S0011) can use `GetLocalTime` and `GetSystemTime` to collect system time.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Taidoor](https://attack.mitre.org/software/S0011) can copy cmd.exe into the system temp folder.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Taidoor](https://attack.mitre.org/software/S0011) has the ability to modify the Registry on compromised hosts using `RegDeleteValueA` and `RegCreateKeyExA`.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Taidoor](https://attack.mitre.org/software/S0011) has used HTTP GET and POST requests for C2.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Taidoor](https://attack.mitre.org/software/S0011) uses RC4 to encrypt the message body of HTTP content.[^2] [^1]  |
| [[Native API\|T1106]] | Native API | [Taidoor](https://attack.mitre.org/software/S0011) has the ability to use native APIs for execution including `GetProcessHeap`, `GetProcAddress`, and `LoadLibrary`.[^2] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Taidoor](https://attack.mitre.org/software/S0011) can use `DeleteFileA` to remove files from infected hosts.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Taidoor](https://attack.mitre.org/software/S0011) has been delivered through spearphishing emails.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Taidoor](https://attack.mitre.org/software/S0011) has collected the MAC address of a compromised host; it can also use `GetAdaptersInfo` to identify network adapters.[^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Taidoor](https://attack.mitre.org/software/S0011) can use a stream cipher to decrypt stings used by the malware.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Taidoor](https://attack.mitre.org/software/S0011) can query the Registry on compromised hosts using `RegQueryValueExA`.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Taidoor](https://attack.mitre.org/software/S0011) can perform DLL loading.[^2] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Taidoor](https://attack.mitre.org/software/S0011) has downloaded additional files onto a compromised host.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Taidoor](https://attack.mitre.org/software/S0011) can upload data and files from a victim's machine.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Taidoor](https://attack.mitre.org/software/S0011) can search for specific files.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Taidoor](https://attack.mitre.org/software/S0011) can use `GetCurrentProcessId` for process discovery.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Taidoor](https://attack.mitre.org/software/S0011) can use encrypted string blocks for obfuscation.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Taidoor](https://attack.mitre.org/software/S0011) has relied upon a victim to click on a malicious email attachment.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Taidoor](https://attack.mitre.org/software/S0011) has modified the `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` key for persistence.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Taidoor](https://attack.mitre.org/software/S0011) can use TCP for C2 communications.[^1]  |




## References

[^1]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^2]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)


