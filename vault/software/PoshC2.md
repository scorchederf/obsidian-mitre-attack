---
aliases: 
    - S0378
    
mitre-attack: https://attack.mitre.org/software/S0378
---

## S0378

[PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.[^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate network adapter information.[^5]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [PoshC2](https://attack.mitre.org/software/S0378) contains modules for searching for passwords in local and remote files.[^5]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [PoshC2](https://attack.mitre.org/software/S0378) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PoshC2](https://attack.mitre.org/software/S0378) can use protocols like HTTP/HTTPS for command and control traffic.[^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that use WMI to execute tasks.[^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [netstat](https://attack.mitre.org/software/S0104) to enumerate TCP and UDP connections.[^5]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [PoshC2](https://attack.mitre.org/software/S0378) contains modules for local privilege escalation exploits such as CVE-2016-9192 and CVE-2016-0099.[^5]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate service and service permission information.[^5]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-RunAs to make tokens.[^5]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [PoshC2](https://attack.mitre.org/software/S0378) can utilize multiple methods to bypass UAC.[^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [PsExec](https://attack.mitre.org/software/S0029) for remote execution.[^5]  |
| [[Local Account\|T1087.001]] | Local Account | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.[^5]  |
| [[Automated Collection\|T1119]] | Automated Collection | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for recursively parsing through files and directories to gather valid credit card numbers.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^5]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PoshC2](https://attack.mitre.org/software/S0378) has modules for keystroke logging and capturing credentials from spoofed Outlook authentication messages.[^5]  |
| [[Domain Account\|T1087.002]] | Domain Account | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.[^5]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for compressing data using ZIP.[^5]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that leverage pass the hash for lateral movement.[^5]  |
| [[Local Groups\|T1069.001]] | Local Groups | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as `Get-LocAdm` for enumerating permission groups.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^5]  |
| [[Proxy\|T1090]] | Proxy | [PoshC2](https://attack.mitre.org/software/S0378) contains modules that allow for use of proxies in command and control.[^5]  |
| [[Brute Force\|T1110]] | Brute Force | [PoshC2](https://attack.mitre.org/software/S0378) has modules for brute forcing local administrator and AD user accounts.[^5]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.[^5]  |
| [[Process Injection\|T1055]] | Process Injection | [PoshC2](https://attack.mitre.org/software/S0378) contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^5]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for exploiting SMB via EternalBlue.[^5]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [PoshC2](https://attack.mitre.org/software/S0378) has modules for enumerating domain trusts.[^5]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-TokenManipulation for manipulating tokens.[^5]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [PoshC2](https://attack.mitre.org/software/S0378) can perform port scans from an infected host.[^5]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [PoshC2](https://attack.mitre.org/software/S0378) can decrypt passwords stored in the RDCMan configuration file.[^2]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for taking packet captures on compromised hosts.[^5]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [PoshC2](https://attack.mitre.org/software/S0378) has the ability to persist on a system using WMI events.[^5]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [PoshC2](https://attack.mitre.org/software/S0378) can use `Get-PassPol` to enumerate the domain password policy.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[HEXANE\|G1001]] | HEXANE |



## References

[^1]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^2]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^3]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^4]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^5]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


