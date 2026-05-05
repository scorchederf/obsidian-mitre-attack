---
aliases: 
    - S0685
    
mitre-attack: https://attack.mitre.org/software/S0685
---

## S0685

[PowerPunch](https://attack.mitre.org/software/S0685) is a lightweight downloader that has been used by [Gamaredon Group](https://attack.mitre.org/groups/G0047) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [PowerPunch](https://attack.mitre.org/software/S0685) can use Base64-encoded scripts.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerPunch](https://attack.mitre.org/software/S0685) has the ability to execute through PowerShell.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PowerPunch](https://attack.mitre.org/software/S0685) can download payloads from adversary infrastructure.[^1]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [PowerPunch](https://attack.mitre.org/software/S0685) can use the volume serial number from a target host to generate a unique XOR key for the next stage payload.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Gamaredon Group\|G0047]] | Gamaredon Group |



## References

[^1]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


