---
aliases: 
    - S0162
    
mitre-attack: https://attack.mitre.org/software/S0162
---

## S0162

[Komplex](https://attack.mitre.org/software/S0162) is a backdoor that has been used by [APT28](https://attack.mitre.org/groups/G0007) on OS X and appears to be developed in a similar manner to [XAgentOSX](https://attack.mitre.org/software/S0161) [^1]  [^2] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | The [Komplex](https://attack.mitre.org/software/S0162) trojan supports file deletion.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | The OsInfo function in [Komplex](https://attack.mitre.org/software/S0162) collects the current running username.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | The OsInfo function in [Komplex](https://attack.mitre.org/software/S0162) collects a running process list.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | The [Komplex](https://attack.mitre.org/software/S0162) C2 channel uses an 11-byte XOR algorithm to hide data.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | The [Komplex](https://attack.mitre.org/software/S0162) C2 channel uses HTTP POST requests.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent |  The [Komplex](https://attack.mitre.org/software/S0162) trojan creates a persistent launch agent called with `$HOME/Library/LaunchAgents/com.apple.updates.plist` with `launchctl load -w ~/Library/LaunchAgents/com.apple.updates.plist`.[^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | The [Komplex](https://attack.mitre.org/software/S0162) payload is stored in a hidden directory at `/Users/Shared/.local/kextd`.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^2]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)


[^3]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


