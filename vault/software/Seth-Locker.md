---
aliases: 
    - S0639
    
mitre-attack: https://attack.mitre.org/software/S0639
---

## S0639

[Seth-Locker](https://attack.mitre.org/software/S0639) is a ransomware with some remote control capabilities that has been in use since at least 2021.<br>[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Seth-Locker](https://attack.mitre.org/software/S0639) can execute commands via the command line shell.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Seth-Locker](https://attack.mitre.org/software/S0639) has the ability to download and execute files on a compromised host.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Seth-Locker](https://attack.mitre.org/software/S0639) can encrypt files on a targeted system, appending them with the suffix .seth.[^1]  |




## References

[^1]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


