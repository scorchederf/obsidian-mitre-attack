---
aliases: 
    - S0211
    
mitre-attack: https://attack.mitre.org/software/S0211
---

## S0211

[Linfo](https://attack.mitre.org/software/S0211) is a rootkit trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor on compromised hosts. [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can retrieve system information.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can change C2 servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can download files onto compromised hosts.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can list contents of drives and search for files.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can delete files.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can change the frequency at which compromised hosts contact remote C2 infrastructure.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can start a remote shell.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can retrieve a list of running processes.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can obtain data from local systems.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^2]: Linfo


[^3]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


