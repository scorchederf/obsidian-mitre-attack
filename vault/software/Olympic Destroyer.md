---
aliases: 
    - S0365
    
mitre-attack: https://attack.mitre.org/software/S0365
---

## S0365

[Olympic Destroyer](https://attack.mitre.org/software/S0365) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) against the 2018 Winter Olympics, held in Pyeongchang, South Korea. The main purpose of the malware was to render infected computer systems inoperable. The malware leverages various native Windows utilities and API calls to carry out its destructive tasks. [Olympic Destroyer](https://attack.mitre.org/software/S0365) has worm-like features to spread itself across a computer network in order to maximize its destructive impact.[^2] [^4]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses API calls to enumerate the infected system's ARP table.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Olympic Destroyer](https://attack.mitre.org/software/S0365) contains a module that tries to obtain stored credentials from web browsers.[^2]  |
| [[Service Stop\|T1489]] | Service Stop | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses the API call `ChangeServiceConfigW` to disable all services on the affected system.[^2]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Olympic Destroyer](https://attack.mitre.org/software/S0365) will shut down the compromised system after it is done modifying system configuration settings.[^2] [^4]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Olympic Destroyer](https://attack.mitre.org/software/S0365) will attempt to clear the System and Security event logs using `wevtutil`.[^2]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Olympic Destroyer](https://attack.mitre.org/software/S0365) overwrites files locally and on remote shares.[^2] [^4]   |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Olympic Destroyer](https://attack.mitre.org/software/S0365) attempts to copy itself to remote machines on the network.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses WMI to help propagate itself across a network.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) to enumerate all systems in the network.[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Olympic Destroyer](https://attack.mitre.org/software/S0365) will attempt to enumerate mapped network shares to later attempt to wipe all files on those shares.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Olympic Destroyer](https://attack.mitre.org/software/S0365) utilizes [PsExec](https://attack.mitre.org/software/S0029) to help propagate itself across a network.[^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses [PsExec](https://attack.mitre.org/software/S0029) to interact with the `ADMIN$` network share to execute commands on remote systems.[^2] [^3]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses the native Windows utilities `vssadmin`, `wbadmin`, and `bcdedit` to delete and disable operating system recovery features such as the Windows backup catalog and Windows Automatic Repair.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Olympic Destroyer](https://attack.mitre.org/software/S0365) contains a module that tries to obtain credentials from LSASS, similar to [Mimikatz](https://attack.mitre.org/software/S0002). These credentials are used with [PsExec](https://attack.mitre.org/software/S0029) and [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) to help the malware propagate itself across a network.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^2]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)


[^3]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)


[^4]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^5]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^6]: [CrowdStrike GTR 2019](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2019GlobalThreatReport.pdf)


[^7]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^8]: [UK NCSC Olympic Attacks October 2020](https://www.gov.uk/government/news/uk-exposes-series-of-russian-cyber-attacks-against-olympic-and-paralympic-games)


