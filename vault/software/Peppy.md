---
aliases: 
    - S0643
    
mitre-attack: https://attack.mitre.org/software/S0643
---

## S0643

[Peppy](https://attack.mitre.org/software/S0643) is a Python-based remote access Trojan, active since at least 2012, with similarities to [Crimson](https://attack.mitre.org/software/S0115).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [Peppy](https://attack.mitre.org/software/S0643) can log keystrokes on compromised hosts.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Peppy](https://attack.mitre.org/software/S0643) can download and execute remote files.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Peppy](https://attack.mitre.org/software/S0643) can use HTTP to communicate with C2.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Peppy](https://attack.mitre.org/software/S0643) has the ability to execute shell commands.[^2]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Peppy](https://attack.mitre.org/software/S0643) has the ability to automatically exfiltrate files and keylogs.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Peppy](https://attack.mitre.org/software/S0643) can take screenshots on targeted systems.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Peppy](https://attack.mitre.org/software/S0643) can identify specific files for exfiltration.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Transparent Tribe\|G0134]] | Transparent Tribe |



## References

[^1]: [Unit 42 ProjectM March 2016](https://unit42.paloaltonetworks.com/unit42-projectm-link-found-between-pakistani-actor-and-operation-transparent-tribe/)


[^2]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


