---
aliases: 
    - S1068
    
mitre-attack: https://attack.mitre.org/software/S1068
---

## S1068

[BlackCat](https://attack.mitre.org/software/S1068) is ransomware written in Rust that has been offered via the Ransomware-as-a-Service (RaaS) model. First observed November 2021, [BlackCat](https://attack.mitre.org/software/S1068) has been used to target multiple sectors and organizations in various countries and regions in Africa, the Americas, Asia, Australia, and Europe.[^1] [^5] [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [BlackCat](https://attack.mitre.org/software/S1068) can replicate itself across connected servers via `psexec`.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [BlackCat](https://attack.mitre.org/software/S1068) can clear Windows event logs using `wevtutil.exe`.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BlackCat](https://attack.mitre.org/software/S1068) can broadcasts NetBIOS Name Service (NBNC) messages to search for servers connected to compromised networks.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to encrypt Windows devices, Linux devices, and VMWare instances.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to stop VM services on compromised networks.[^1] [^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BlackCat](https://attack.mitre.org/software/S1068) can obtain the computer name and UUID.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [BlackCat](https://attack.mitre.org/software/S1068) can bypass UAC to escalate privileges.[^1]   |
| [[Domain Account\|T1087.002]] | Domain Account | [BlackCat](https://attack.mitre.org/software/S1068) can utilize `net use` commands to identify domain users.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to add the following registry key on compromised networks to maintain persistence: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services \LanmanServer\Paramenters`[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [BlackCat](https://attack.mitre.org/software/S1068) can determine if a user on a compromised host has domain admin privileges.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [BlackCat](https://attack.mitre.org/software/S1068) can use `wmic.exe` to delete shadow copies on compromised networks.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [BlackCat](https://attack.mitre.org/software/S1068) can enumerate local drives.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to discover network shares on compromised networks.[^1] [^5]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [BlackCat](https://attack.mitre.org/software/S1068) can use Windows commands such as `fsutil behavior set SymLinkEvaluation R2L:1` to redirect file system access to a different location after gaining access into compromised networks.[^1]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [BlackCat](https://attack.mitre.org/software/S1068) can change the desktop wallpaper on compromised hosts.[^1] [^5]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to wipe VM snapshots on compromised networks.[^1] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BlackCat](https://attack.mitre.org/software/S1068) can execute commands on a compromised network with the use of `cmd.exe`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BlackCat](https://attack.mitre.org/software/S1068) can enumerate files for encryption.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BlackCat](https://attack.mitre.org/software/S1068) can utilize `net use` commands to discover the user name on a compromised host.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BlackCat](https://attack.mitre.org/software/S1068) can delete shadow copies using `vssadmin.exe delete shadows /all /quiet` and `wmic.exe Shadowcopy Delete`; it can also modify the boot loader using `bcdedit /set {default} recoveryenabled No`.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [BlackCat](https://attack.mitre.org/software/S1068) has the ability modify access tokens.[^1] [^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Scattered Spider\|G1015]] | Scattered Spider |



## References

[^1]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^2]: [MSTIC Octo Tempest Operations October 2023](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)


[^3]: ALPHV


[^4]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^5]: [Sophos BlackCat Jul 2022](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)


[^6]: Noberus


[^7]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^8]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


[^9]: [ACSC BlackCat Apr 2022](https://www.cyber.gov.au/about-us/advisories/2022-004-acsc-ransomware-profile-alphv-aka-blackcat)


