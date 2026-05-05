---
aliases: 
    - S0640
    
mitre-attack: https://attack.mitre.org/software/S0640
---

## S0640

[Avaddon](https://attack.mitre.org/software/S0640) is ransomware written in C++ that has been offered as Ransomware-as-a-Service (RaaS) since at least June 2020.[^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Avaddon](https://attack.mitre.org/software/S0640) checks for specific keyboard layouts and OS languages to avoid targeting Commonwealth of Independent States (CIS) entities.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Avaddon](https://attack.mitre.org/software/S0640) has decrypted encrypted strings.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Avaddon](https://attack.mitre.org/software/S0640) looks for and attempts to stop database processes.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Avaddon](https://attack.mitre.org/software/S0640) has been executed through a malicious JScript downloader.[^2] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Avaddon](https://attack.mitre.org/software/S0640) has searched for specific files prior to encryption.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Avaddon](https://attack.mitre.org/software/S0640) looks for and attempts to stop anti-malware solutions.[^1]  |
| [[Native API\|T1106]] | Native API | [Avaddon](https://attack.mitre.org/software/S0640) has used the Windows Crypto API to generate an AES key.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Avaddon](https://attack.mitre.org/software/S0640) has collected information about running processes.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Avaddon](https://attack.mitre.org/software/S0640) deletes backups and shadow copies using native system tools.[^2] [^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Avaddon](https://attack.mitre.org/software/S0640) bypasses UAC using the CMSTPLUA COM interface.[^1]   |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Avaddon](https://attack.mitre.org/software/S0640) has enumerated shared folders and mapped volumes.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Avaddon](https://attack.mitre.org/software/S0640) uses wmic.exe to delete shadow copies.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Avaddon](https://attack.mitre.org/software/S0640) encrypts the victim system using a combination of AES256 and RSA encryption schemes.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Avaddon](https://attack.mitre.org/software/S0640) modifies several registry keys for persistence and UAC bypass.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Avaddon](https://attack.mitre.org/software/S0640) has used encrypted strings.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Avaddon](https://attack.mitre.org/software/S0640) uses registry run keys for persistence.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Avaddon](https://attack.mitre.org/software/S0640) can collect the external IP address of the victim.[^3]  |




## References

[^1]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^2]: [Hornet Security Avaddon June 2020](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)


[^3]: [Awake Security Avaddon](https://awakesecurity.com/blog/threat-hunting-for-avaddon-ransomware/)


