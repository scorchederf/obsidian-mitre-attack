---
aliases: 
    - S0337
    
mitre-attack: https://attack.mitre.org/software/S0337
---

## S0337

[BadPatch](https://attack.mitre.org/software/S0337) is a Windows Trojan that was used in a Gaza Hackers-linked campaign.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BadPatch](https://attack.mitre.org/software/S0337) establishes a foothold by adding a link to the malware executable in the startup folder.[^2]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [BadPatch](https://attack.mitre.org/software/S0337) uses SMTP for C2.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [BadPatch](https://attack.mitre.org/software/S0337) stores collected data in log files before exfiltration.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BadPatch](https://attack.mitre.org/software/S0337) uses HTTP for C2.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BadPatch](https://attack.mitre.org/software/S0337) collects the OS system, OS version, MAC address, and the computer name from the victim’s machine.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [BadPatch](https://attack.mitre.org/software/S0337) captures screenshots in .jpg format and then exfiltrates them.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BadPatch](https://attack.mitre.org/software/S0337) searches for files with specific file extensions.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [BadPatch](https://attack.mitre.org/software/S0337) attempts to detect if it is being run in a Virtual Machine (VM) using a WMI query for disk drive name, BIOS, and motherboard information. [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [BadPatch](https://attack.mitre.org/software/S0337) has a keylogging capability.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BadPatch](https://attack.mitre.org/software/S0337) can download and execute or update malware.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [BadPatch](https://attack.mitre.org/software/S0337) uses WMI to enumerate installed security products in the victim’s environment.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BadPatch](https://attack.mitre.org/software/S0337) collects files from the local system that have the following extensions, then prepares them for exfiltration: .xls, .xlsx, .pdf, .mdb, .rar, .zip, .doc, .docx.[^2]  |




## References

[^1]: BadPatch


[^2]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)


