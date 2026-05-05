---
aliases: 
    - S0107
    
mitre-attack: https://attack.mitre.org/software/S0107
---

## S0107

[Cherry Picker](https://attack.mitre.org/software/S0107) is a point of sale (PoS) memory scraper. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | Recent versions of [Cherry Picker](https://attack.mitre.org/software/S0107) delete files and registry keys created by the malware.[^1]  |
| [[AppInit DLLs\|T1546.010]] | AppInit DLLs | Some variants of [Cherry Picker](https://attack.mitre.org/software/S0107) use AppInit_DLLs to achieve persistence by creating the following Registry key: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows "AppInit_DLLs"="pserver32.dll"`[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Cherry Picker](https://attack.mitre.org/software/S0107) exfiltrates files over FTP.[^1]  |




## References

[^1]: [Trustwave Cherry Picker](https://www.trustwave.com/Resources/SpiderLabs-Blog/Shining-the-Spotlight-on-Cherry-Picker-PoS-Malware/)


