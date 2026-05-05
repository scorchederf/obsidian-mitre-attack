---
aliases: 
    - S0074
    
mitre-attack: https://attack.mitre.org/software/S0074
---

## S0074

[Sakula](https://attack.mitre.org/software/S0074) is a remote access tool (RAT) that first surfaced in 2012 and was used in intrusions throughout 2015. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Sakula](https://attack.mitre.org/software/S0074) uses single-byte XOR obfuscation to obfuscate many of its files.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Sakula](https://attack.mitre.org/software/S0074) has the capability to download files.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | Most [Sakula](https://attack.mitre.org/software/S0074) samples maintain persistence by setting the Registry Run key `SOFTWARE\Microsoft\Windows\CurrentVersion\Run\` in the HKLM or HKCU hive, with the Registry value and file name varying by sample.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sakula](https://attack.mitre.org/software/S0074) uses HTTP for C2.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Sakula](https://attack.mitre.org/software/S0074) contains UAC bypass code for both 32- and 64-bit systems.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Sakula](https://attack.mitre.org/software/S0074) encodes C2 traffic with single-byte XOR keys.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Sakula](https://attack.mitre.org/software/S0074) uses DLL side-loading, typically using a digitally signed sample of Kaspersky Anti-Virus (AV) 6.0 for Windows Workstations or McAfee's Outlook Scan About Box to load malicious DLL files.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Sakula](https://attack.mitre.org/software/S0074) calls cmd.exe to run various DLL files via rundll32 and also to perform file cleanup. [Sakula](https://attack.mitre.org/software/S0074) also has the capability to invoke a reverse shell.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Sakula](https://attack.mitre.org/software/S0074) calls cmd.exe to run various DLL files via rundll32.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | Some [Sakula](https://attack.mitre.org/software/S0074) samples install themselves as services for persistence by calling WinExec with the `net start` argument.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | Some [Sakula](https://attack.mitre.org/software/S0074) samples use cmd.exe to delete temporary files.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Deep Panda\|G0009]] | Deep Panda |



## References

[^1]: [ThreatConnect Anthem](https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/)


[^2]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


