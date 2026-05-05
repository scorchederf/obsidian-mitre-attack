---
aliases: 
    - S0158
    
mitre-attack: https://attack.mitre.org/software/S0158
---

## S0158

[PHOREAL](https://attack.mitre.org/software/S0158) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [PHOREAL](https://attack.mitre.org/software/S0158) is capable of manipulating the Registry.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PHOREAL](https://attack.mitre.org/software/S0158) is capable of creating reverse shell.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [PHOREAL](https://attack.mitre.org/software/S0158) communicates via ICMP for C2.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: PHOREAL


[^2]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


