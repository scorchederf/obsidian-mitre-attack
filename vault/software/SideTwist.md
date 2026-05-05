---
aliases: 
    - S0610
    
mitre-attack: https://attack.mitre.org/software/S0610
---

## S0610

[SideTwist](https://attack.mitre.org/software/S0610) is a C-based backdoor that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [SideTwist](https://attack.mitre.org/software/S0610) can use `GetUserNameW`, `GetComputerNameW`, and `GetComputerNameExW` to gather information.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SideTwist](https://attack.mitre.org/software/S0610) has used Base64 for encoded C2 traffic.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SideTwist](https://attack.mitre.org/software/S0610) can collect the username on a targeted system.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SideTwist](https://attack.mitre.org/software/S0610) can encrypt C2 communications with a randomly generated key.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to search for specific files.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SideTwist](https://attack.mitre.org/software/S0610) can execute shell commands on a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to download additional files.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SideTwist](https://attack.mitre.org/software/S0610) has used HTTP GET and POST requests over port 443 for C2.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to collect the domain name on a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SideTwist](https://attack.mitre.org/software/S0610) can decode and decrypt messages received from C2.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to upload files from a compromised host.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [SideTwist](https://attack.mitre.org/software/S0610) has primarily used port 443 for C2 but can use port 80 as a fallback.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SideTwist](https://attack.mitre.org/software/S0610) has exfiltrated data over its C2 channel.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SideTwist](https://attack.mitre.org/software/S0610) can collect the computer name of a targeted system.[^1]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [SideTwist](https://attack.mitre.org/software/S0610) can embed C2 responses in the source code of a fake Flickr webpage.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


