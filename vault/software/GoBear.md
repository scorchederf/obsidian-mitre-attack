---
aliases: 
    - S1197
    
mitre-attack: https://attack.mitre.org/software/S1197
---

## S1197

[GoBear](https://attack.mitre.org/software/S1197) is a Go-based backdoor that abuses legitimate, stolen certificates for defense evasion purposes. [GoBear](https://attack.mitre.org/software/S1197) is exclusively linked to [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [GoBear](https://attack.mitre.org/software/S1197) implements SOCKS5 proxy functionality.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [GoBear](https://attack.mitre.org/software/S1197) is installed through droppers masquerading as legitimate, signed software installers.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [GoBear](https://attack.mitre.org/software/S1197) uses stolen legitimate code signing certificates for defense evasion.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^2]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


