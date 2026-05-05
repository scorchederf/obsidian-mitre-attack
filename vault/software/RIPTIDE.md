---
aliases: 
    - S0003
    
mitre-attack: https://attack.mitre.org/software/S0003
---

## S0003

[RIPTIDE](https://attack.mitre.org/software/S0003) is a proxy-aware backdoor used by [APT12](https://attack.mitre.org/groups/G0005). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT12](https://attack.mitre.org/groups/G0005) has used [RIPTIDE](https://attack.mitre.org/software/S0003), a RAT that uses HTTP to communicate.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [APT12](https://attack.mitre.org/groups/G0005) has used the [RIPTIDE](https://attack.mitre.org/software/S0003) RAT, which communicates over HTTP with a payload encrypted with RC4.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT12\|G0005]] | APT12 |



## References

[^1]: [Moran 2014](https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html)


