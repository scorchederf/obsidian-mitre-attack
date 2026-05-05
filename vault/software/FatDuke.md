---
aliases: 
    - S0512
    
mitre-attack: https://attack.mitre.org/software/S0512
---

## S0512

[FatDuke](https://attack.mitre.org/software/S0512) is a backdoor used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2016.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [FatDuke](https://attack.mitre.org/software/S0512) can get user agent strings for the default browser from `HKCU\Software\Classes\http\shell\open\command`.[^2]  |
| [[Browser Fingerprint\|T1036.012]] | Browser Fingerprint | [FatDuke](https://attack.mitre.org/software/S0512) has attempted to mimic a compromised user's traffic by using the same user agent as the installed browser.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FatDuke](https://attack.mitre.org/software/S0512) can be controlled via a custom C2 protocol over HTTP.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [FatDuke](https://attack.mitre.org/software/S0512) can turn itself on or off at random intervals.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [FatDuke](https://attack.mitre.org/software/S0512) can identify the MAC address on the target computer.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [FatDuke](https://attack.mitre.org/software/S0512) has used several C2 servers per targeted organization.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FatDuke](https://attack.mitre.org/software/S0512) can collect the user name, Windows version, computer name, and available space on discs from a compromised host.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FatDuke](https://attack.mitre.org/software/S0512) has used `HKLM\SOFTWARE\Microsoft\CurrentVersion\Run` to establish persistence.[^2]  |
| [[Native API\|T1106]] | Native API | [FatDuke](https://attack.mitre.org/software/S0512) can call `ShellExecuteW` to open the default browser on the URL localhost.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [FatDuke](https://attack.mitre.org/software/S0512) has been regularly repacked by its operators to create large binaries and evade detection.[^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [FatDuke](https://attack.mitre.org/software/S0512) can used pipes to connect machines with restricted internet access to remote machines via other infected hosts.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [FatDuke](https://attack.mitre.org/software/S0512) can list running processes on the localhost.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [FatDuke](https://attack.mitre.org/software/S0512) can use base64 encoding, string stacking, and opaque predicates for obfuscation.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FatDuke](https://attack.mitre.org/software/S0512) can secure delete its DLL.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FatDuke](https://attack.mitre.org/software/S0512) can copy files and directories from a compromised host.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [FatDuke](https://attack.mitre.org/software/S0512) can execute via rundll32.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [FatDuke](https://attack.mitre.org/software/S0512) has the ability to execute PowerShell scripts.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [FatDuke](https://attack.mitre.org/software/S0512) can AES encrypt C2 communications.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FatDuke](https://attack.mitre.org/software/S0512) can enumerate directories on target machines.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [FatDuke](https://attack.mitre.org/software/S0512) has been packed with junk code and strings.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FatDuke](https://attack.mitre.org/software/S0512) can decrypt AES encrypted C2 communications.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


