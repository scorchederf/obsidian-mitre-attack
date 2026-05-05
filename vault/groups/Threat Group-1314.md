---
aliases: 
    - Threat Group-1314
    - TG-1314
mitre-attack: https://attack.mitre.org/groups/G0028
---

## G0028

[Threat Group-1314](https://attack.mitre.org/groups/G0028) is an unattributed threat group that has used compromised credentials to log into a victim's remote access infrastructure. [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Threat Group-1314](https://attack.mitre.org/groups/G0028) actors mapped network drives using `net use`.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Threat Group-1314](https://attack.mitre.org/groups/G0028) actors spawned shells on remote systems on a victim network to execute commands.[^3]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [Threat Group-1314](https://attack.mitre.org/groups/G0028) actors used a victim's endpoint management platform, Altiris, for lateral movement.[^3]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Threat Group-1314](https://attack.mitre.org/groups/G0028) actors used compromised domain credentials for the victim's endpoint management platform, Altiris, to move laterally.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^3]  |
| [[PsExec\|S0029]] | PsExec | [^3]  |



## References

[^1]: TG-1314


[^2]: Threat Group-1314


[^3]: [Dell TG-1314](https://web.archive.org/web/20150626073312/http://www.secureworks.com/resources/blog/living-off-the-land/)


