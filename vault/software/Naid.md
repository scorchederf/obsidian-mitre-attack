---
aliases: 
    - S0205
    
mitre-attack: https://attack.mitre.org/software/S0205
---

## S0205

[Naid](https://attack.mitre.org/software/S0205) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^3]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Naid](https://attack.mitre.org/software/S0205) collects the domain name from a compromised host.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Naid](https://attack.mitre.org/software/S0205) collects a unique identifier (UID) from a compromised host.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Naid](https://attack.mitre.org/software/S0205) creates Registry entries that store information about a created service and point to a malicious DLL dropped to disk.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Naid](https://attack.mitre.org/software/S0205) creates a new service to establish.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: Naid


[^2]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)


[^3]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


