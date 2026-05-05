---
aliases: 
    - S0269
    
mitre-attack: https://attack.mitre.org/software/S0269
---

## S0269

[QUADAGENT](https://attack.mitre.org/software/S0269) is a PowerShell backdoor used by [OilRig](https://attack.mitre.org/groups/G0049). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | [QUADAGENT](https://attack.mitre.org/software/S0269) uses DNS for C2 communications.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [QUADAGENT](https://attack.mitre.org/software/S0269) uses HTTPS and HTTP for C2 communications.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [QUADAGENT](https://attack.mitre.org/software/S0269) uses AES and a preshared key to decrypt the custom Base64 routine used to encode strings and scripts.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [QUADAGENT](https://attack.mitre.org/software/S0269) encodes C2 communications with base64.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [QUADAGENT](https://attack.mitre.org/software/S0269) uses VBScripts.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [QUADAGENT](https://attack.mitre.org/software/S0269) gathers the current domain the victim system belongs to.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [QUADAGENT](https://attack.mitre.org/software/S0269) was likely obfuscated using `Invoke-Obfuscation`.[^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [QUADAGENT](https://attack.mitre.org/software/S0269) uses cmd.exe to execute scripts and commands on the victim’s machine.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [QUADAGENT](https://attack.mitre.org/software/S0269) used the PowerShell filenames `Office365DCOMCheck.ps1` and `SystemDiskClean.ps1`.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [QUADAGENT](https://attack.mitre.org/software/S0269) stores a session identifier unique to the compromised system as well as a pre-shared key used for encrypting and decrypting C2 communications within a Registry key (such as `HKCU\Office365DCOMCheck`) in the `HKCU` hive.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [QUADAGENT](https://attack.mitre.org/software/S0269) has a command to delete its Registry key and scheduled task.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [QUADAGENT](https://attack.mitre.org/software/S0269) checks if a value exists within a Registry key in the HKCU hive whose name is the same as the scheduled task it has created.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [QUADAGENT](https://attack.mitre.org/software/S0269) uses PowerShell scripts for execution.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [QUADAGENT](https://attack.mitre.org/software/S0269) uses multiple protocols (HTTPS, HTTP, DNS) for its C2 server as fallback channels if communication with one is unsuccessful.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [QUADAGENT](https://attack.mitre.org/software/S0269) modifies an HKCU Registry key to store a session identifier unique to the compromised system as well as a pre-shared key used for encrypting and decrypting C2 communications.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [QUADAGENT](https://attack.mitre.org/software/S0269) gathers the victim username.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [QUADAGENT](https://attack.mitre.org/software/S0269) creates a scheduled task to maintain persistence on the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^2]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^3]: QUADAGENT


