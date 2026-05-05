---
aliases: 
    - S0459
    
mitre-attack: https://attack.mitre.org/software/S0459
---

## S0459

[MechaFlounder](https://attack.mitre.org/software/S0459) is a python-based remote access tool (RAT) that has been used by [APT39](https://attack.mitre.org/groups/G0087). The payload uses a combination of actor developed code and code snippets freely available online in development communities.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to send the compromised user's account name and hostname within a URL to C2.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [MechaFlounder](https://attack.mitre.org/software/S0459) has been downloaded as a file named lsass.exe, which matches the legitimate Windows file.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to identify the username and hostname on a compromised host.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to use base16 encoded strings in C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to use HTTP in communication with C2.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to run commands on a compromised host.[^1]  |
| [[Python\|T1059.006]] | Python | [MechaFlounder](https://attack.mitre.org/software/S0459) uses a python-based payload.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to upload and download files to and from a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT39\|G0087]] | APT39 |



## References

[^1]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


