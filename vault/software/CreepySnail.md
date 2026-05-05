---
aliases: 
    - S1024
    
mitre-attack: https://attack.mitre.org/software/S1024
---

## S1024

[CreepySnail](https://attack.mitre.org/software/S1024) is a custom PowerShell implant that has been used by [POLONIUM](https://attack.mitre.org/groups/G1005) since at least 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [CreepySnail](https://attack.mitre.org/software/S1024) can use stolen credentials to authenticate on target networks.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CreepySnail](https://attack.mitre.org/software/S1024) can use HTTP for C2.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [CreepySnail](https://attack.mitre.org/software/S1024) can use `getmac` and `Get-NetIPAddress` to enumerate network settings.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [CreepySnail](https://attack.mitre.org/software/S1024) can use Base64 to encode its C2 traffic.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CreepySnail](https://attack.mitre.org/software/S1024) can use PowerShell for execution, including the cmdlets `Invoke-WebRequst` and `Invoke-Expression`.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [CreepySnail](https://attack.mitre.org/software/S1024) can connect to C2 for data exfiltration.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [CreepySnail](https://attack.mitre.org/software/S1024) can execute `getUsername` on compromised systems.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[POLONIUM\|G1005]] | POLONIUM |



## References

[^1]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


