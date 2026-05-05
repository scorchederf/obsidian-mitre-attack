---
aliases: 
    - S0553
    
mitre-attack: https://attack.mitre.org/software/S0553
---

## S0553

[MoleNet](https://attack.mitre.org/software/S0553) is a downloader tool with backdoor capabilities that has been observed in use since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MoleNet](https://attack.mitre.org/software/S0553) can collect information about the about the system.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MoleNet](https://attack.mitre.org/software/S0553) can execute commands via the command line utility.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [MoleNet](https://attack.mitre.org/software/S0553) can use PowerShell to set persistence.[^1]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MoleNet](https://attack.mitre.org/software/S0553) can achieve persitence on the infected machine by setting the Registry run key.[^1]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [MoleNet](https://attack.mitre.org/software/S0553) can perform WMI commands on the system.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MoleNet](https://attack.mitre.org/software/S0553) can download additional payloads from the C2.[^1]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [MoleNet](https://attack.mitre.org/software/S0553) can use WMI commands to check the system for firewall and antivirus software.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^2]: MoleNet


