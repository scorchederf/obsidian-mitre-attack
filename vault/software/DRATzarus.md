---
aliases: 
    - S0694
    
mitre-attack: https://attack.mitre.org/software/S0694
---

## S0694

[DRATzarus](https://attack.mitre.org/software/S0694) is a remote access tool (RAT) that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) to target the defense and aerospace organizations globally since at least summer 2020. [DRATzarus](https://attack.mitre.org/software/S0694) shares similarities with [Bankshot](https://attack.mitre.org/software/S0239), which was used by [Lazarus Group](https://attack.mitre.org/groups/G0032) in 2017 to target the Turkish financial sector.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [DRATzarus](https://attack.mitre.org/software/S0694) can obtain a list of users from an infected machine.[^1]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [DRATzarus](https://attack.mitre.org/software/S0694) can use `IsDebuggerPresent` to detect whether a debugger is present on a victim.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [DRATzarus](https://attack.mitre.org/software/S0694) can use the `GetTickCount` and `GetSystemTimeAsFileTime` API calls to inspect system time.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [DRATzarus](https://attack.mitre.org/software/S0694) can collect information from a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DRATzarus](https://attack.mitre.org/software/S0694) can deploy additional tools onto an infected machine.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [DRATzarus](https://attack.mitre.org/software/S0694) has been named `Flash.exe`, and its dropper has been named `IExplorer`.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [DRATzarus](https://attack.mitre.org/software/S0694) can search for other machines connected to compromised host and attempt to map the network.[^1]  |
| [[Native API\|T1106]] | Native API | [DRATzarus](https://attack.mitre.org/software/S0694) can use various API calls to see if it is running in a sandbox.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [DRATzarus](https://attack.mitre.org/software/S0694)'s dropper can be packed with UPX.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [DRATzarus](https://attack.mitre.org/software/S0694) can enumerate and examine running processes to determine if a debugger is present.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DRATzarus](https://attack.mitre.org/software/S0694) can use HTTP or HTTPS for C2 communications.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [DRATzarus](https://attack.mitre.org/software/S0694) can use the `GetTickCount` and `GetSystemTimeAsFileTime` API calls to measure function timing.[^1]  [DRATzarus](https://attack.mitre.org/software/S0694) can also remotely shut down into sleep mode under specific conditions to evade <br>detection.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [DRATzarus](https://attack.mitre.org/software/S0694) can be partly encrypted with XOR.[^1]  |




## References

[^1]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


