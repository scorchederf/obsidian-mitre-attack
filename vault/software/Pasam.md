---
aliases: 
    - S0208
    
mitre-attack: https://attack.mitre.org/software/S0208
---

## S0208

[Pasam](https://attack.mitre.org/software/S0208) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^2]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve lists of running processes.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve information like free disk space.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can upload files.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve lists of files.[^3]  |
| [[LSASS Driver\|T1547.008]] | LSASS Driver | [Pasam](https://attack.mitre.org/software/S0208) establishes by infecting the Security Accounts Manager (SAM) DLL to load a malicious DLL dropped to disk.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve information like hostname.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can delete files.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve files.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: Pasam


[^2]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^3]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


