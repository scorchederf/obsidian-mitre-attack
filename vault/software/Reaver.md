---
aliases: 
    - S0172
    
mitre-attack: https://attack.mitre.org/software/S0172
---

## S0172

[Reaver](https://attack.mitre.org/software/S0172) is a malware family that has been in the wild since at least late 2016. Reporting indicates victims have primarily been associated with the "Five Poisons," which are movements the Chinese government considers dangerous. The type of malware is rare due to its final payload being in the form of [Control Panel](https://attack.mitre.org/techniques/T1218/002) items.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Reaver](https://attack.mitre.org/software/S0172) creates a shortcut file and saves it in a Startup folder to establish persistence.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Reaver](https://attack.mitre.org/software/S0172) deletes the original dropped file from the victim.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Reaver](https://attack.mitre.org/software/S0172) creates a shortcut file and saves it in a Startup folder to establish persistence.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Reaver](https://attack.mitre.org/software/S0172) encrypts some of its files with XOR.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | Some [Reaver](https://attack.mitre.org/software/S0172) variants use raw TCP for C2.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | Some [Reaver](https://attack.mitre.org/software/S0172) variants use HTTP for C2.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Reaver](https://attack.mitre.org/software/S0172) encrypts collected data with an incremental XOR key prior to exfiltration.[^2]  |
| [[Control Panel\|T1218.002]] | Control Panel | [Reaver](https://attack.mitre.org/software/S0172) drops and executes a malicious CPL file as its payload.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Reaver](https://attack.mitre.org/software/S0172) collects volume serial number from the victim.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Reaver](https://attack.mitre.org/software/S0172) collects the victim's username.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Reaver](https://attack.mitre.org/software/S0172) installs itself as a new service.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Reaver](https://attack.mitre.org/software/S0172) collects system information from the victim, including CPU speed, computer name, ANSI code page, OEM code page identifier for the OS, Microsoft Windows version, and memory information.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Reaver](https://attack.mitre.org/software/S0172) queries the Registry to determine the correct Startup path to use for persistence.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Reaver](https://attack.mitre.org/software/S0172) collects the victim's IP address.[^2]  |




## References

[^1]: Reaver


[^2]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


