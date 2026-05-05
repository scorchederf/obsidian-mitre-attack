---
aliases: 
    - S0668
    
mitre-attack: https://attack.mitre.org/software/S0668
---

## S0668

[TinyTurla](https://attack.mitre.org/software/S0668) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) against targets in the US, Germany, and Afghanistan since at least 2020.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [TinyTurla](https://attack.mitre.org/software/S0668) has the ability to encrypt C2 traffic with SSL/TLS.[^1]  |
| [[Native API\|T1106]] | Native API | [TinyTurla](https://attack.mitre.org/software/S0668) has used `WinHTTP`, `CreateProcess`, and other APIs for C2 communications and other functions.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [TinyTurla](https://attack.mitre.org/software/S0668) has been deployed as `w64time.dll` to appear legitimate.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [TinyTurla](https://attack.mitre.org/software/S0668) can install itself as a service on compromised machines.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [TinyTurla](https://attack.mitre.org/software/S0668) can set its configuration parameters in the Registry.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TinyTurla](https://attack.mitre.org/software/S0668) has been installed using a .bat file.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TinyTurla](https://attack.mitre.org/software/S0668) has the ability to act as a second-stage dropper used to infect the system with additional malware.[^1]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [TinyTurla](https://attack.mitre.org/software/S0668) can save its configuration parameters in the Registry.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [TinyTurla](https://attack.mitre.org/software/S0668) has mimicked an existing Windows service by being installed as `Windows Time Service`.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [TinyTurla](https://attack.mitre.org/software/S0668) contacts its C2 based on a scheduled timing set in its configuration.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [TinyTurla](https://attack.mitre.org/software/S0668) can query the Registry for its configuration information.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [TinyTurla](https://attack.mitre.org/software/S0668) can go through a list of C2 server IPs and will try to register with each until one responds.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [TinyTurla](https://attack.mitre.org/software/S0668) can upload files from a compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TinyTurla](https://attack.mitre.org/software/S0668) can use HTTPS in C2 communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


