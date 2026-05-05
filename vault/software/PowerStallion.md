---
aliases: 
    - S0393
    
mitre-attack: https://attack.mitre.org/software/S0393
---

## S0393

[PowerStallion](https://attack.mitre.org/software/S0393) is a lightweight [PowerShell](https://attack.mitre.org/techniques/T1059/001) backdoor used by [Turla](https://attack.mitre.org/groups/G0010), possibly as a recovery access tool to install other backdoors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [PowerStallion](https://attack.mitre.org/software/S0393) uses Microsoft OneDrive as a C2 server via a network drive mapped with `net use`.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PowerStallion](https://attack.mitre.org/software/S0393) uses a XOR cipher to encrypt command output written to its OneDrive C2 server.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerStallion](https://attack.mitre.org/software/S0393) uses PowerShell loops to iteratively check for available commands in its OneDrive C2 server.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [PowerStallion](https://attack.mitre.org/software/S0393) modifies the MAC times of its local log files to match that of the victim's desktop.ini file.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PowerStallion](https://attack.mitre.org/software/S0393) has been used to monitor process lists.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


