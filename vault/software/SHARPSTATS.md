---
aliases: 
    - S0450
    
mitre-attack: https://attack.mitre.org/software/S0450
---

## S0450

[SHARPSTATS](https://attack.mitre.org/software/S0450) is a .NET backdoor used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the domain of the compromised host.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to employ a custom PowerShell script.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to upload and download files.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [SHARPSTATS](https://attack.mitre.org/software/S0450) has used base64 encoding and XOR to obfuscate PowerShell scripts.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the IP address, machine name, and OS of the compromised host.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the current date and time on the compromised host.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the username on the compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


