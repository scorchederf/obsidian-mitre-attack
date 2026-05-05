---
aliases: 
    - S0156
    
mitre-attack: https://attack.mitre.org/software/S0156
---

## S0156

[KOMPROGO](https://attack.mitre.org/software/S0156) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050) that is capable of process, file, and registry management. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [KOMPROGO](https://attack.mitre.org/software/S0156) is capable of retrieving information about the infected system.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [KOMPROGO](https://attack.mitre.org/software/S0156) is capable of running WMI queries.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [KOMPROGO](https://attack.mitre.org/software/S0156) is capable of creating a reverse shell.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^2]: KOMPROGO


