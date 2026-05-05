---
aliases: 
    - S0094
    
mitre-attack: https://attack.mitre.org/software/S0094
---

## S0094

[Trojan.Karagany](https://attack.mitre.org/software/S0094) is a modular remote access tool used for recon and linked to [Dragonfly](https://attack.mitre.org/groups/G0035). The source code for [Trojan.Karagany](https://attack.mitre.org/software/S0094) originated from Dream Loader malware which was leaked in 2010 and sold on underground forums. [^1] [^3] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can gather information about the user on a compromised host.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can take a desktop screenshot and save the file into `\ProgramData\Mail\MailAg\shot.png`.[^1] [^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can use [netstat](https://attack.mitre.org/software/S0104) to collect a list of network connections.[^3]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can monitor the titles of open windows to identify specific keywords.[^3] 	  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can base64 encode and AES-128-CBC encrypt data prior to transmission.[^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Trojan.Karagany](https://attack.mitre.org/software/S0094) samples sometimes use common binary packers such as UPX and Aspack on top of a custom Delphi binary packer.[^1] [^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can steal data and credentials from browsers.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can use [Tasklist](https://attack.mitre.org/software/S0057) to collect a list of running tasks.[^1] [^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can create a link to itself in the Startup folder to automatically start itself upon system restart.[^1] [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can capture information regarding the victim's OS, security, and hardware configuration.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Trojan.Karagany](https://attack.mitre.org/software/S0094) has used plugins with a self-delete capability.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can upload, download, and execute files on the victim.[^1] [^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can capture keystrokes on a compromised host.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can enumerate files and directories on a compromised host.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can create directories to store plugin output and stage data for exfiltration.[^1] [^3]  |
| [[Thread Execution Hijacking\|T1055.003]] | Thread Execution Hijacking | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can inject a suspended thread of its own process into a new process and initiate via the `ResumeThread` API.[^3]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can secure C2 communications with SSL and TLS.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can detect commonly used and generic virtualization platforms based primarily on drivers and file paths.[^3]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can dump passwords and save them into `\ProgramData\Mail\MailAg\pwds.txt`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can gather information on the network configuration of a compromised host.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can perform reconnaissance commands on a victim machine via a cmd.exe process.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can communicate with C2 via HTTP POST requests.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dragonfly\|G0035]] | Dragonfly |



## References

[^1]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^2]: xFrost


[^3]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^4]: Karagany


[^5]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^6]: [Dragos DYMALLOY ](https://www.dragos.com/threat/dymalloy/)


