---
aliases: 
    - S1173
    
mitre-attack: https://attack.mitre.org/software/S1173
---

## S1173

[PowerExchange](https://attack.mitre.org/software/S1173) is a PowerShell backdoor that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2023 including against government targets in the Middle East.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PowerExchange](https://attack.mitre.org/software/S1173) can decode Base64-encoded files and call `WriteAllBytes` to write the files to compromised hosts.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PowerExchange](https://attack.mitre.org/software/S1173) can exfiltrate files via its email C2 channel.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [PowerExchange](https://attack.mitre.org/software/S1173) can receive and send back the results of executed C2 commands through email.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PowerExchange](https://attack.mitre.org/software/S1173) can decode and decrypt C2 commands received via email.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerExchange](https://attack.mitre.org/software/S1173) can use PowerShell to execute commands received from C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


