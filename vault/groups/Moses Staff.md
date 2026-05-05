---
aliases: 
    - Moses Staff
    - DEV-0500
    - Marigold Sandstorm
mitre-attack: https://attack.mitre.org/groups/G1009
---

## G1009

[Moses Staff](https://attack.mitre.org/groups/G1009) is a suspected Iranian threat group that has primarily targeted Israeli companies since at least September 2021. [Moses Staff](https://attack.mitre.org/groups/G1009) openly stated their motivation in attacking Israeli companies is to cause damage by leaking stolen sensitive data and encrypting the victim's networks without a ransom demand.[^3]  <br><br>Security researchers assess [Moses Staff](https://attack.mitre.org/groups/G1009) is politically motivated, and has targeted government, finance, travel, energy, manufacturing, and utility companies outside of Israel as well, including those in Italy, India, Germany, Chile, Turkey, the UAE, and the US.[^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Moses Staff](https://attack.mitre.org/groups/G1009) has used batch scripts that can enable SMB on a compromised host.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Moses Staff](https://attack.mitre.org/groups/G1009) has collected the domain name of a compromised network.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [Moses Staff](https://attack.mitre.org/groups/G1009) has collected the administrator username from a compromised host.[^3]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [Moses Staff](https://attack.mitre.org/groups/G1009) has used batch scripts that can disable the Windows firewall on specific remote machines.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Moses Staff](https://attack.mitre.org/groups/G1009) collected information about the infected host, including the machine names and OS architecture.[^3] <br> |
| [[Tool\|T1588.002]] | Tool | [Moses Staff](https://attack.mitre.org/groups/G1009) has used the commercial tool DiskCryptor.[^3]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Moses Staff](https://attack.mitre.org/groups/G1009) has dropped a web shell onto a compromised system.[^3]  |
| [[Malware\|T1587.001]] | Malware | [Moses Staff](https://attack.mitre.org/groups/G1009) has built malware, such as [DCSrv](https://attack.mitre.org/software/S1033) and [PyDCrypt](https://attack.mitre.org/software/S1032), for targeting victims' machines.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Moses Staff](https://attack.mitre.org/groups/G1009) has used signed drivers from an open source tool called DiskCryptor to evade detection.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Moses Staff](https://attack.mitre.org/groups/G1009) has used obfuscated web shells in their operations.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Moses Staff](https://attack.mitre.org/groups/G1009) has downloaded and installed web shells to following path `C:\inetpub\wwwroot\aspnet_client\system_web\IISpool.aspx`.[^3]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Moses Staff](https://attack.mitre.org/groups/G1009) has exploited known vulnerabilities in public-facing infrastructure such as Microsoft Exchange Servers.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PsExec\|S0029]] | PsExec | [^3]  |
| [[PyDCrypt\|S1032]] | PyDCrypt | [^3]  |
| [[DCSrv\|S1033]] | DCSrv | [^3]  |
| [[StrifeWater\|S1034]] | StrifeWater | [^5]  |



## References

[^1]: Marigold Sandstorm


[^2]: DEV-0500


[^3]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


