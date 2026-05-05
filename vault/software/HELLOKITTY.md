---
aliases: 
    - S0617
    
mitre-attack: https://attack.mitre.org/software/S0617
---

## S0617

[HELLOKITTY](https://attack.mitre.org/software/S0617) is a ransomware written in C++  that shares similar code structure and functionality with [DEATHRANSOM](https://attack.mitre.org/software/S0616) and [FIVEHANDS](https://attack.mitre.org/software/S0618). [HELLOKITTY](https://attack.mitre.org/software/S0617) has been used since at least 2020, targets have included a Polish video game developer and a Brazilian electric power company.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [HELLOKITTY](https://attack.mitre.org/software/S0617) can use an embedded RSA-2048 public key to encrypt victim data for ransom.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [HELLOKITTY](https://attack.mitre.org/software/S0617) can delete volume shadow copies on compromised hosts.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [HELLOKITTY](https://attack.mitre.org/software/S0617) has the ability to enumerate network resources.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [HELLOKITTY](https://attack.mitre.org/software/S0617) can use WMI to delete volume shadow copies.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [HELLOKITTY](https://attack.mitre.org/software/S0617) can enumerate logical drives on a target system.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HELLOKITTY](https://attack.mitre.org/software/S0617) can search for specific processes to terminate.[^1]  |




## References

[^1]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


