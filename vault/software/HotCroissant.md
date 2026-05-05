---
aliases: 
    - S0431
    
mitre-attack: https://attack.mitre.org/software/S0431
---

## S0431

[HotCroissant](https://attack.mitre.org/software/S0431) is a remote access trojan (RAT) attributed by U.S. government entities to malicious North Korean government cyber activity, tracked collectively as HIDDEN COBRA.[^2]  [HotCroissant](https://attack.mitre.org/software/S0431) shares numerous code similarities with [Rifdoor](https://attack.mitre.org/software/S0433).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to download files from the infected host to the command and control (C2) server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [HotCroissant](https://attack.mitre.org/software/S0431) has compressed network communications and encrypted them with a custom stream cipher.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to clean up installed files, delete files, and delete itself from the victim’s machine.[^1]  |
| [[Native API\|T1106]] | Native API | [HotCroissant](https://attack.mitre.org/software/S0431) can perform dynamic DLL importing and API lookups using `LoadLibrary` and `GetProcAddress` on obfuscated strings.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [HotCroissant](https://attack.mitre.org/software/S0431) has used the open source UPX executable packer.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to retrieve a list of files in a given directory as well as drives and drive types.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to stop services on the infected host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to upload a file from the command and control (C2) server to the victim machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HotCroissant](https://attack.mitre.org/software/S0431) can remotely open applications on the infected host with the `ShellExecuteA` command.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to list running processes on the infected host.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to retrieve a list of services on the infected host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to collect the username on the infected host.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HotCroissant](https://attack.mitre.org/software/S0431) has encrypted strings with single-byte XOR and base64 encoded RC4.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to list the names of all open windows on the infected host.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) can retrieve a list of applications from the `SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` registry key.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to determine if the current user is an administrator, Windows product name, processor name, screen resolution, and physical RAM of the infected host.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to do real time screen viewing on an infected host.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to identify the IP address of the compromised machine.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [HotCroissant](https://attack.mitre.org/software/S0431) has attempted to install a scheduled task named “Java Maintenance64” on startup to establish persistence.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to hide the window for operations performed on a given file.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^2]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)


