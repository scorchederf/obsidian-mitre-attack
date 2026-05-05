---
aliases: 
    - S0344
    
mitre-attack: https://attack.mitre.org/software/S0344
---

## S0344

[Azorult](https://attack.mitre.org/software/S0344) is a commercial Trojan that is used to steal information from compromised hosts. [Azorult](https://attack.mitre.org/software/S0344) has been observed in the wild as early as 2016.<br>In July 2018, [Azorult](https://attack.mitre.org/software/S0344) was seen used in a spearphishing campaign against targets in North America. [Azorult](https://attack.mitre.org/software/S0344) has been seen used for cryptocurrency theft. [^2] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Azorult](https://attack.mitre.org/software/S0344) can call WTSQueryUserToken and CreateProcessAsUser to start a new process with local system privileges.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Azorult](https://attack.mitre.org/software/S0344) can delete files from victim machines.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Azorult](https://attack.mitre.org/software/S0344) can encrypt C2 traffic using XOR.[^2] [^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Azorult](https://attack.mitre.org/software/S0344) can collect the username from the victim’s machine.[^2]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Azorult](https://attack.mitre.org/software/S0344) can decrypt the payload into memory, create a new suspended process of itself, then inject a decrypted payload to the new process and resume new process execution.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Azorult](https://attack.mitre.org/software/S0344) can check for installed software on the system under the Registry key `Software\Microsoft\Windows\CurrentVersion\Uninstall`.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Azorult](https://attack.mitre.org/software/S0344) uses an XOR key to decrypt content and uses Base64 to decode the C2 address.[^2] [^4]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Azorult](https://attack.mitre.org/software/S0344) can steal credentials in files belonging to common software such as Skype, Telegram, and Steam.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Azorult](https://attack.mitre.org/software/S0344) can steal credentials from the victim's browser.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Azorult](https://attack.mitre.org/software/S0344) can download and execute additional files. [Azorult](https://attack.mitre.org/software/S0344) has also downloaded a ransomware payload called Hermes.[^2] [^4]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Azorult](https://attack.mitre.org/software/S0344) can collect the time zone information from the system.[^2] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Azorult](https://attack.mitre.org/software/S0344) can collect host IP information from the victim’s machine.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Azorult](https://attack.mitre.org/software/S0344) can recursively search for files in folders and collects files from the desktop with certain extensions.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Azorult](https://attack.mitre.org/software/S0344) can collect the machine information, system architecture, the OS version, computer name, Windows product name, the number of CPU cores, video card information, and the system language.[^2] [^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Azorult](https://attack.mitre.org/software/S0344) can capture screenshots of the victim’s machines.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Azorult](https://attack.mitre.org/software/S0344) can collect a list of running processes by calling CreateToolhelp32Snapshot.[^2] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^2]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^3]: Azorult


[^4]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)


