---
aliases: 
    - S0693
    
mitre-attack: https://attack.mitre.org/software/S0693
---

## S0693

[CaddyWiper](https://attack.mitre.org/software/S0693) is a destructive data wiper that has been used in attacks against organizations in Ukraine since at least March 2022.[^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [CaddyWiper](https://attack.mitre.org/software/S0693) can use `DsRoleGetPrimaryDomainInformation` to determine the role of the infected machine. [CaddyWiper](https://attack.mitre.org/software/S0693) can also halt execution if the compromised host is identified as a domain controller.[^1] [^2]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [CaddyWiper](https://attack.mitre.org/software/S0693) can modify ACL entries to take ownership of files.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CaddyWiper](https://attack.mitre.org/software/S0693) can enumerate all files and directories on a compromised host.[^2]  |
| [[Data Destruction\|T1485]] | Data Destruction | [CaddyWiper](https://attack.mitre.org/software/S0693) can work alphabetically through drives on a compromised system to take ownership of and overwrite all files.[^3] [^1]  |
| [[Native API\|T1106]] | Native API | [CaddyWiper](https://attack.mitre.org/software/S0693) has the ability to dynamically resolve and use APIs, including `SeTakeOwnershipPrivilege`.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [CaddyWiper](https://attack.mitre.org/software/S0693) can obtain a list of current processes.[^2]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [CaddyWiper](https://attack.mitre.org/software/S0693) has the ability to destroy information about a physical drive's partitions including the MBR, GPT, and partition entries.[^3] [^1]  |




## References

[^1]: [Cisco CaddyWiper March 2022](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)


[^2]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)


[^3]: [ESET CaddyWiper March 2022](https://www.welivesecurity.com/2022/03/15/caddywiper-new-wiper-malware-discovered-ukraine)


