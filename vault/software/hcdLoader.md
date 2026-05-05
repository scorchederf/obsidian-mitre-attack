---
aliases: 
    - S0071
    
mitre-attack: https://attack.mitre.org/software/S0071
---

## S0071

[hcdLoader](https://attack.mitre.org/software/S0071) is a remote access tool (RAT) that has been used by [APT18](https://attack.mitre.org/groups/G0026). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [hcdLoader](https://attack.mitre.org/software/S0071) provides command-line access to the compromised system.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [hcdLoader](https://attack.mitre.org/software/S0071) installs itself as a service for persistence.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT18\|G0026]] | APT18 |



## References

[^1]: [Dell Lateral Movement](http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/)


[^2]: [ThreatStream Evasion Analysis](https://www.threatstream.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


