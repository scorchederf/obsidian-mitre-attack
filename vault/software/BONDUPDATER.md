---
aliases: 
    - S0360
    
mitre-attack: https://attack.mitre.org/software/S0360
---

## S0360

[BONDUPDATER](https://attack.mitre.org/software/S0360) is a PowerShell backdoor used by [OilRig](https://attack.mitre.org/groups/G0049). It was first observed in November 2017 during targeting of a Middle Eastern government organization, and an updated version was observed in August 2018 being used to target a government organization with spearphishing emails.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BONDUPDATER](https://attack.mitre.org/software/S0360) can read batch commands in a file sent from its C2 server and execute them with cmd.exe.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [BONDUPDATER](https://attack.mitre.org/software/S0360) uses `-windowstyle hidden` to conceal a [PowerShell](https://attack.mitre.org/techniques/T1059/001) window that downloads a payload.[^1]  |
| [[DNS\|T1071.004]] | DNS | [BONDUPDATER](https://attack.mitre.org/software/S0360) can use DNS and TXT records within its DNS tunneling protocol for command and control.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BONDUPDATER](https://attack.mitre.org/software/S0360) persists using a scheduled task that executes every minute.[^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [BONDUPDATER](https://attack.mitre.org/software/S0360) uses a DGA to communicate with command and control servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BONDUPDATER](https://attack.mitre.org/software/S0360) can download or upload files from its C2 server.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [BONDUPDATER](https://attack.mitre.org/software/S0360) is written in PowerShell.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^2]: [Palo Alto OilRig Sep 2018](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)


