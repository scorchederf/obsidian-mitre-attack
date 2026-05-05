---
aliases: 
    - S0343
    
mitre-attack: https://attack.mitre.org/software/S0343
---

## S0343

[Exaramel for Windows](https://attack.mitre.org/software/S0343) is a backdoor used for targeting Windows systems. The Linux version is tracked separately under [Exaramel for Linux](https://attack.mitre.org/software/S0401).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Exaramel for Windows](https://attack.mitre.org/software/S0343) automatically encrypts files before sending them to the C2 server.[^2]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Exaramel for Windows](https://attack.mitre.org/software/S0343) has a command to execute VBS scripts on the victim’s machine.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Exaramel for Windows](https://attack.mitre.org/software/S0343) stores the backdoor's configuration in the Registry in XML format.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | The [Exaramel for Windows](https://attack.mitre.org/software/S0343) dropper creates and starts a Windows service named wsmprovav with the description “Windows Check AV.”[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Exaramel for Windows](https://attack.mitre.org/software/S0343) adds the configuration to the Registry in XML format.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Exaramel for Windows](https://attack.mitre.org/software/S0343) has a command to launch a remote shell and executes commands on the victim’s machine.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | The [Exaramel for Windows](https://attack.mitre.org/software/S0343) dropper creates and starts a Windows service named wsmprovav with the description “Windows Check AV” in an apparent attempt to masquerade as a legitimate service.[^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Exaramel for Windows](https://attack.mitre.org/software/S0343) specifies a path to store files scheduled for exfiltration.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: Exaramel for Windows


[^2]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


