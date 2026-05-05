---
aliases: 
    - S1212
    
mitre-attack: https://attack.mitre.org/software/S1212
---

## S1212

[RansomHub](https://attack.mitre.org/software/S1212) is a ransomware-as-a-service (RaaS) offering with Windows, ESXi, Linux, and FreeBSD versions that has been in use since at least 2024 to target organizations in multiple sectors globally. [RansomHub](https://attack.mitre.org/software/S1212) operators may have purchased and rebranded resources from Knight  (formerly Cyclops) Ransomware which shares infrastructure, feature, and code overlaps with [RansomHub](https://attack.mitre.org/software/S1212).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [RansomHub](https://attack.mitre.org/software/S1212) can use PowerShell to delete volume shadow copies.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to self-delete.[^1]  |
| [[Proxy\|T1090]] | Proxy | [RansomHub](https://attack.mitre.org/software/S1212) can use a proxy to connect to remote SFTP servers.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [RansomHub](https://attack.mitre.org/software/S1212) will terminate without proceeding to encryption if the infected machine is on a list of allowlisted machines specified in its configuration.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [RansomHub](https://attack.mitre.org/software/S1212) has an encrypted configuration file.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [RansomHub](https://attack.mitre.org/software/S1212) has created an autorun Registry key through the `-safeboot-instance -pass` command line argument.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RansomHub](https://attack.mitre.org/software/S1212) can use `cmd.exe` to execute multiple commands on infected hosts.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RansomHub](https://attack.mitre.org/software/S1212) can use a provided passphrase to decrypt its configuration file.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [RansomHub](https://attack.mitre.org/software/S1212) can enumerate all accessible machines from the infected system.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [RansomHub](https://attack.mitre.org/software/S1212) can use credentials provided in its configuration to move laterally from the infected machine over SMBv2.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [RansomHub](https://attack.mitre.org/software/S1212) can sleep for a set number of minutes before beginning execution.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [RansomHub](https://attack.mitre.org/software/S1212) can delete events from the Security, System, and Application logs.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [RansomHub](https://attack.mitre.org/software/S1212) has used `vssadmin.exe` to delete volume shadow copies.[^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to only encrypt specific files.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [RansomHub](https://attack.mitre.org/software/S1212) can use Elliptic Curve Encryption to encrypt files on targeted systems.[^2]  [RansomHub](https://attack.mitre.org/software/S1212) can also skip content at regular intervals (ex. encrypt 1 MB, skip 3 MB) to optomize performance and enable faster encryption for large files.[^1]   |
| [[Process Discovery\|T1057]] | Process Discovery | [RansomHub](https://attack.mitre.org/software/S1212) can stop processes associated with files currently in use to maximize the impact of encryption.[^2]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [RansomHub](https://attack.mitre.org/software/S1212) has placed a ransom note on comrpomised systems to warn victims and provide directions for how to retrieve data.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to target specific network shares for encryption.[^1]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [RansomHub](https://attack.mitre.org/software/S1212) can reboot targeted systems into Safe Mode prior to encryption.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to terminate specified services.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RansomHub](https://attack.mitre.org/software/S1212) can retrieve information about virtual machines.[^1]  |




## References

[^1]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^2]: [CISA RansomHub AUG 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)


