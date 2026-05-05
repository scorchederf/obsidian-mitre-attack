---
aliases: 
    - S0616
    
mitre-attack: https://attack.mitre.org/software/S0616
---

## S0616

[DEATHRANSOM](https://attack.mitre.org/software/S0616) is ransomware written in C that has been used since at least 2020, and has potential overlap with [FIVEHANDS](https://attack.mitre.org/software/S0618) and [HELLOKITTY](https://attack.mitre.org/software/S0617).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can use public and private key pair encryption to encrypt files for ransom payment.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can use HTTPS to download files.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can delete volume shadow copies on compromised hosts.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can use loop operations to enumerate directories on a compromised host.[^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | Some versions of [DEATHRANSOM](https://attack.mitre.org/software/S0616) have performed language ID and keyboard layout checks; if either of these matched Russian, Kazakh, Belarusian, Ukrainian or Tatar [DEATHRANSOM](https://attack.mitre.org/software/S0616) would exit.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can download files to a compromised host.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [DEATHRANSOM](https://attack.mitre.org/software/S0616) has the ability to use WMI to delete volume shadow copies.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can enumerate logical drives on a target system.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [DEATHRANSOM](https://attack.mitre.org/software/S0616) has the ability to use loop operations to enumerate network resources.[^1]  |




## References

[^1]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


