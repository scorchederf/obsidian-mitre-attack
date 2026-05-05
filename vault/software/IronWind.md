---
aliases: 
    - S9029
    
mitre-attack: https://attack.mitre.org/software/S9029
---

## S9029

[IronWind](https://attack.mitre.org/software/S9029) is a custom loader malware that has been in use since at least 2023 by actors including [WIRTE](https://attack.mitre.org/groups/G0090) to target entities in the Middle East.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [IronWind](https://attack.mitre.org/software/S9029) can capture the OS version and computer name of the compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [IronWind](https://attack.mitre.org/software/S9029) can used HTTP to send information to C2 about the targeted system.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [IronWind](https://attack.mitre.org/software/S9029) can enumerate the username on victim's systems.[^1]  |
| [[DLL\|T1574.001]] | DLL | [IronWind](https://attack.mitre.org/software/S9029) has used DLL sideloading for execution.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [IronWind](https://attack.mitre.org/software/S9029) has used Base64 encoding and XOR encryption with the key “53” to obfuscate command strings.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [IronWind](https://attack.mitre.org/software/S9029) can deobfuscate the next stage payload using Base64 and XOR operations with the key "53".[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [IronWind](https://attack.mitre.org/software/S9029) has used the Windows command shell to execute malicious files.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [IronWind](https://attack.mitre.org/software/S9029) can list installed software on targeted hosts.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [IronWind](https://attack.mitre.org/software/S9029) has used a .NET DLL named "exit-DN4-core.dll" to terminate malicious processes running on victim's systems.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


