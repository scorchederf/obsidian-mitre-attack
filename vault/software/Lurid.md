---
aliases: 
    - S0010
    
mitre-attack: https://attack.mitre.org/software/S0010
---

## S0010

[Lurid](https://attack.mitre.org/software/S0010) is a malware family that has been used by several groups, including [PittyTiger](https://attack.mitre.org/groups/G0011), in targeted attacks as far back as 2006. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Lurid](https://attack.mitre.org/software/S0010) performs XOR encryption.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Lurid](https://attack.mitre.org/software/S0010) can compress data before sending it.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PittyTiger\|G0011]] | PittyTiger |



## References

[^1]: [Villeneuve 2011](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_dissecting-lurid-apt.pdf)


[^2]: [Villeneuve 2014](https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html)


