---
aliases: 
    - S0207
    
mitre-attack: https://attack.mitre.org/software/S0207
---

## S0207

[Vasport](https://attack.mitre.org/software/S0207) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Vasport](https://attack.mitre.org/software/S0207) creates a backdoor by making a connection using a HTTP POST.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Vasport](https://attack.mitre.org/software/S0207) can download files.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Vasport](https://attack.mitre.org/software/S0207) copies itself to disk and creates an associated run key Registry entry to establish.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Vasport](https://attack.mitre.org/software/S0207) is capable of tunneling though a proxy.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: [Symantec Vasport May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-5938-99)


[^2]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^3]: Vasport


