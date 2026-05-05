---
aliases: 
    - S0210
    
mitre-attack: https://attack.mitre.org/software/S0210
---

## S0210

[Nerex](https://attack.mitre.org/software/S0210) is a Trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Nerex](https://attack.mitre.org/software/S0210) creates a backdoor through which remote attackers can download files onto a compromised host.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Nerex](https://attack.mitre.org/software/S0210) drops a signed Microsoft DLL to disk.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Nerex](https://attack.mitre.org/software/S0210) creates a Registry subkey that registers a new service.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Nerex](https://attack.mitre.org/software/S0210) creates a Registry subkey that registers a new service.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: [Symantec Nerex May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3445-99)


[^2]: [Symantec Ristol May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3909-99)


[^3]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^4]: Nerex


