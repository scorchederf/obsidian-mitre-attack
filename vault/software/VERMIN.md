---
aliases: 
    - S0257
    
mitre-attack: https://attack.mitre.org/software/S0257
---

## S0257

[VERMIN](https://attack.mitre.org/software/S0257) is a remote access tool written in the Microsoft .NET framework. It is mostly composed of original code, but also has some open source code. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [VERMIN](https://attack.mitre.org/software/S0257) gathers the local IP address.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [VERMIN](https://attack.mitre.org/software/S0257) is initially packed.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [VERMIN](https://attack.mitre.org/software/S0257) uses HTTP for C2 communications.[^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [VERMIN](https://attack.mitre.org/software/S0257) can perform audio capture.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [VERMIN](https://attack.mitre.org/software/S0257) can delete files on the victim’s machine.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [VERMIN](https://attack.mitre.org/software/S0257) collects keystrokes from the victim machine.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [VERMIN](https://attack.mitre.org/software/S0257) uses WMI to check for anti-virus software installed on the system.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [VERMIN](https://attack.mitre.org/software/S0257) collects data stored in the clipboard.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [VERMIN](https://attack.mitre.org/software/S0257) decrypts code, strings, and commands to use once it's on the victim's machine.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [VERMIN](https://attack.mitre.org/software/S0257) saves each collected file with the automatically generated format {0:dd-MM-yyyy}.txt .[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [VERMIN](https://attack.mitre.org/software/S0257) encrypts the collected files using 3-DES.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [VERMIN](https://attack.mitre.org/software/S0257) can perform screen captures of the victim’s machine.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [VERMIN](https://attack.mitre.org/software/S0257) is obfuscated using the obfuscation tool called ConfuserEx.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [VERMIN](https://attack.mitre.org/software/S0257) can download and upload files to the victim's machine.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [VERMIN](https://attack.mitre.org/software/S0257) gathers the username from the victim’s machine.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [VERMIN](https://attack.mitre.org/software/S0257) collects the OS name, machine name, and architecture information.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [VERMIN](https://attack.mitre.org/software/S0257) can get a list of the processes and running tasks on the system.[^2]  |




## References

[^1]: VERMIN


[^2]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


