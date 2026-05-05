---
aliases: 
    - S0019
    
mitre-attack: https://attack.mitre.org/software/S0019
---

## S0019

[Regin](https://attack.mitre.org/software/S0019) is a malware platform that has targeted victims in a range of industries, including telecom, government, and financial institutions. Some [Regin](https://attack.mitre.org/software/S0019) timestamps date back to 2003. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | The [Regin](https://attack.mitre.org/software/S0019) malware platform uses Extended Attributes to store encrypted executables.[^1]  |
| [[Hidden File System\|T1564.005]] | Hidden File System | [Regin](https://attack.mitre.org/software/S0019) has used a hidden file system to store some of its components.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | The [Regin](https://attack.mitre.org/software/S0019) malware platform supports many standard protocols, including HTTP and HTTPS.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Regin](https://attack.mitre.org/software/S0019) contains a keylogger.[^1]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [Regin](https://attack.mitre.org/software/S0019) stage 1 modules for 64-bit systems have been found to be signed with fake certificates masquerading as originating from Microsoft Corporation and Broadcom Corporation.[^1]  |
| [[External Proxy\|T1090.002]] | External Proxy | [Regin](https://attack.mitre.org/software/S0019) leveraged several compromised universities as proxies to obscure its origin.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | The [Regin](https://attack.mitre.org/software/S0019) malware platform supports many standard protocols, including SMB.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | The [Regin](https://attack.mitre.org/software/S0019) malware platform can use Windows admin shares to move laterally.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | The [Regin](https://attack.mitre.org/software/S0019) malware platform can use ICMP to communicate between infected computers.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Regin](https://attack.mitre.org/software/S0019) appears to have functionality to sniff for credentials passed over HTTP, SMTP, and SMB.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Regin](https://attack.mitre.org/software/S0019) appears to have functionality to modify remote Registry information.[^1]  |




## References

[^1]: [Kaspersky Regin](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)


