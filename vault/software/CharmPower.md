---
aliases: 
    - S0674
    
mitre-attack: https://attack.mitre.org/software/S0674
---

## S0674

[CharmPower](https://attack.mitre.org/software/S0674) is a PowerShell-based, modular backdoor that has been used by [Magic Hound](https://attack.mitre.org/groups/G0059) since at least 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [CharmPower](https://attack.mitre.org/software/S0674) can remove persistence-related artifacts from the Registry.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [CharmPower](https://attack.mitre.org/software/S0674) can enumerate the OS version and computer name on a targeted system.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [CharmPower](https://attack.mitre.org/software/S0674) can list the installed applications on a compromised host.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [CharmPower](https://attack.mitre.org/software/S0674) can send victim data via FTP with credentials hardcoded in the script.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [CharmPower](https://attack.mitre.org/software/S0674) can send additional modules over C2 encrypted with a simple substitution cipher.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CharmPower](https://attack.mitre.org/software/S0674) can decrypt downloaded modules prior to execution.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [CharmPower](https://attack.mitre.org/software/S0674) can exfiltrate gathered data to a hardcoded C2 URL via HTTP POST.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [CharmPower](https://attack.mitre.org/software/S0674) can retrieve C2 domain information from actor-controlled S3 buckets.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CharmPower](https://attack.mitre.org/software/S0674) can enumerate drives and list the contents of the C: drive on a victim's computer.[^1]  |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [CharmPower](https://attack.mitre.org/software/S0674) can use `netsh wlan show profiles` to list specific Wi-Fi profile details.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CharmPower](https://attack.mitre.org/software/S0674) can use PowerShell for payload execution and C2 communication.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [CharmPower](https://attack.mitre.org/software/S0674) can delete created files from a compromised system.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CharmPower](https://attack.mitre.org/software/S0674) can use HTTP to communicate with C2.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [CharmPower](https://attack.mitre.org/software/S0674) can change its C2 channel once every 360 loops by retrieving a new domain from the actors’ S3 bucket.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to list running processes through the use of `tasklist`.[^1]  |
| [[Web Service\|T1102]] | Web Service | [CharmPower](https://attack.mitre.org/software/S0674) can download additional modules from actor-controlled Amazon S3 buckets.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CharmPower](https://attack.mitre.org/software/S0674) can collect data and files from a compromised host.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | The C# implementation of  the [CharmPower](https://attack.mitre.org/software/S0674) command execution module can use `cmd`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to use `ipconfig` to enumerate system network settings.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to capture screenshots.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to download additional modules to a compromised host.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [CharmPower](https://attack.mitre.org/software/S0674) can send additional modules over C2 encoded with base64.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [CharmPower](https://attack.mitre.org/software/S0674) can use `wmic` to gather information from a system.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to enumerate `Uninstall` registry values.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Magic Hound\|G0059]] | Magic Hound |



## References

[^1]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


