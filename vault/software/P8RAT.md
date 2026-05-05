---
aliases: 
    - S0626
    
mitre-attack: https://attack.mitre.org/software/S0626
---

## S0626

[P8RAT](https://attack.mitre.org/software/S0626) is a fileless malware used by [menuPass](https://attack.mitre.org/groups/G0045) to download and execute payloads since at least 2020.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [P8RAT](https://attack.mitre.org/software/S0626) has the ability to "sleep" for a specified time to evade detection.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [P8RAT](https://attack.mitre.org/software/S0626) can check for specific processes associated with virtual environments.[^3]  |
| [[Junk Data\|T1001.001]] | Junk Data | [P8RAT](https://attack.mitre.org/software/S0626) can send randomly-generated data as part of its C2 communication.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [P8RAT](https://attack.mitre.org/software/S0626) can check the compromised host for processes associated with VMware or VirtualBox environments.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [P8RAT](https://attack.mitre.org/software/S0626) can download additional payloads to a target system.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: GreetCake


[^2]: HEAVYPOT


[^3]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


