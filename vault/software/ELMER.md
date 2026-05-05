---
aliases: 
    - S0064
    
mitre-attack: https://attack.mitre.org/software/S0064
---

## S0064

[ELMER](https://attack.mitre.org/software/S0064) is a non-persistent, proxy-aware HTTP backdoor written in Delphi that has been used by [APT16](https://attack.mitre.org/groups/G0023). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ELMER](https://attack.mitre.org/software/S0064) is capable of performing directory listings.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ELMER](https://attack.mitre.org/software/S0064) uses HTTP for command and control.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ELMER](https://attack.mitre.org/software/S0064) is capable of performing process listings.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT16\|G0023]] | APT16 |



## References

[^1]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)


