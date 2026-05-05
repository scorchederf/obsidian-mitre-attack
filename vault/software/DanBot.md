---
aliases: 
    - S1014
    
mitre-attack: https://attack.mitre.org/software/S1014
---

## S1014

[DanBot](https://attack.mitre.org/software/S1014) is a first-stage remote access Trojan written in C# that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least 2018.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [DanBot](https://attack.mitre.org/software/S1014) can use a scheduled task for installation.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [DanBot](https://attack.mitre.org/software/S1014) files have been named `UltraVNC.exe` and `WINVNC.exe` to appear as legitimate VNC tools.[^1]  |
| [[VNC\|T1021.005]] | VNC | [DanBot](https://attack.mitre.org/software/S1014) can use VNC for remote access to targeted systems.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DanBot](https://attack.mitre.org/software/S1014) can Base64 encode its payload.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [DanBot](https://attack.mitre.org/software/S1014) can delete its configuration file after installation.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [DanBot](https://attack.mitre.org/software/S1014) has relied on victims' opening a malicious file for initial execution.[^2] [^1]  |
| [[DNS\|T1071.004]] | DNS | [DanBot](https://attack.mitre.org/software/S1014) can use use IPv4 A records and IPv6 AAAA DNS records in C2 communications.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [DanBot](https://attack.mitre.org/software/S1014) can upload files from compromised hosts.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DanBot](https://attack.mitre.org/software/S1014) can download additional files to a targeted system.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [DanBot](https://attack.mitre.org/software/S1014) has been distributed within a malicious Excel attachment via spearphishing emails.[^2]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DanBot](https://attack.mitre.org/software/S1014) can use HTTP in C2 communication.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [DanBot](https://attack.mitre.org/software/S1014) can use a VBA macro embedded in an Excel file to drop the payload.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DanBot](https://attack.mitre.org/software/S1014) has the ability to execute arbitrary commands via `cmd.exe`.[^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DanBot](https://attack.mitre.org/software/S1014) can use a VBA macro to decode its payload prior to installation and execution.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[HEXANE\|G1001]] | HEXANE |



## References

[^1]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^2]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


