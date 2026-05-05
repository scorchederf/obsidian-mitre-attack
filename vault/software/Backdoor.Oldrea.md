---
aliases: 
    - S0093
    
mitre-attack: https://attack.mitre.org/software/S0093
---

## S0093

[Backdoor.Oldrea](https://attack.mitre.org/software/S0093) is a modular backdoor that used by [Dragonfly](https://attack.mitre.org/groups/G0035) against energy companies since at least 2013. [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) was distributed via supply chain compromise, and included specialized modules to enumerate and map ICS-specific systems, processes, and protocols.[^1] [^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) adds Registry Run keys to achieve persistence.[^1] [^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can use a network scanning module to identify ICS-related ports.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) contains a cleanup module that removes traces of itself from the victim.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about the Internet adapter configuration.[^1] [^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can use rundll32 for execution on compromised hosts.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) injects itself into explorer.exe.[^1] [^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | Some [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) samples use standard Base64 + bzip2, and some use standard Base64 + reverse XOR + RSA-2048 to decrypt data received from C2 servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can download additional modules from C2.[^3]  |
| [[Email Account\|T1087.003]] | Email Account | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects address book information from Outlook.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) writes collected data to a temporary file in an encrypted form before exfiltration to a C2 server.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | Some [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) samples contain a publicly available Web browser password recovery tool.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about running processes.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about available drives, default browser, desktop file list, My Documents, Internet history, program files, and root of available drives. It also searches for ICS-related software files.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects the current username from the victim.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can enumerate and map ICS-specific systems in victim environments.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about the OS and computer name.[^1] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dragonfly\|G0035]] | Dragonfly |



## References

[^1]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^2]: [Symantec Dragonfly Sept 2017](https://docs.broadcom.com/doc/dragonfly_threat_against_western_energy_suppliers)


[^3]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


