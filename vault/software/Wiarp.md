---
aliases: 
    - S0206
    
mitre-attack: https://attack.mitre.org/software/S0206
---

## S0206

[Wiarp](https://attack.mitre.org/software/S0206) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can download files.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can open a command line interface.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can inject files into running processes.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can create a service.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)


[^2]: Wiarp


[^3]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


