---
aliases: 
    - S0267
    
mitre-attack: https://attack.mitre.org/software/S0267
---

## S0267

[FELIXROOT](https://attack.mitre.org/software/S0267) is a backdoor that has been used to target Ukrainian victims. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) collects a list of running processes.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [FELIXROOT](https://attack.mitre.org/software/S0267) deletes the Registry key `HKCU\Software\Classes\Applications\rundll32.exe\shell\open`.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) collects the victim’s volume serial number.[^3] [^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) checks for installed security software like antivirus and firewall.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [FELIXROOT](https://attack.mitre.org/software/S0267) encrypts strings in the backdoor using a custom XOR algorithm.[^3] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) collects the victim’s computer name, processor architecture, OS version, and system type.[^3] [^1]  |
| [[Query Registry\|T1012]] | Query Registry | [FELIXROOT](https://attack.mitre.org/software/S0267) queries the Registry for specific keys for potential privilege escalation and proxy information. [FELIXROOT](https://attack.mitre.org/software/S0267) has also used WMI to query the Windows Registry.[^3] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FELIXROOT](https://attack.mitre.org/software/S0267) uses HTTP and HTTPS to communicate with the C2 server.[^3] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) collects information about the network including the IP address and DHCP server.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FELIXROOT](https://attack.mitre.org/software/S0267) uses WMI to query the Windows Registry.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) gathers the time zone information from the victim’s machine.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [FELIXROOT](https://attack.mitre.org/software/S0267) encrypts collected data with AES and Base64 and then sends it to the C2 server.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [FELIXROOT](https://attack.mitre.org/software/S0267) uses Rundll32 for executing the dropper program.[^3] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [FELIXROOT](https://attack.mitre.org/software/S0267) collects the username from the victim’s machine.[^3] [^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [FELIXROOT](https://attack.mitre.org/software/S0267) creates a .LNK file for persistence.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FELIXROOT](https://attack.mitre.org/software/S0267) downloads and uploads files to and from the victim’s machine.[^3] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FELIXROOT](https://attack.mitre.org/software/S0267) executes batch scripts on the victim’s machine, and can launch a reverse shell for command execution.[^3] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FELIXROOT](https://attack.mitre.org/software/S0267) adds a shortcut file to the startup folder for persistence.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FELIXROOT](https://attack.mitre.org/software/S0267) deletes the .LNK file from the startup directory as well as the dropper components.[^3]  |




## References

[^1]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^2]: GreyEnergy mini


[^3]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^4]: FELIXROOT


