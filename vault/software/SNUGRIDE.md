---
aliases: 
    - S0159
    
mitre-attack: https://attack.mitre.org/software/S0159
---

## S0159

[SNUGRIDE](https://attack.mitre.org/software/S0159) is a backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) as first stage malware. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SNUGRIDE](https://attack.mitre.org/software/S0159) communicates with its C2 server over HTTP.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SNUGRIDE](https://attack.mitre.org/software/S0159) establishes persistence through a Registry Run key.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SNUGRIDE](https://attack.mitre.org/software/S0159) is capable of executing commands and spawning a reverse shell.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SNUGRIDE](https://attack.mitre.org/software/S0159) encrypts C2 traffic using AES with a static key.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: SNUGRIDE


[^2]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


