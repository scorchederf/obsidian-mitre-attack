---
aliases: 
    - Windigo
mitre-attack: https://attack.mitre.org/groups/G0124
---

## G0124

The [Windigo](https://attack.mitre.org/groups/G0124) group has been operating since at least 2011, compromising thousands of Linux and Unix servers using the [Ebury](https://attack.mitre.org/software/S0377) SSH backdoor to create a spam botnet. Despite law enforcement intervention against the creators, [Windigo](https://attack.mitre.org/groups/G0124) operators continued updating [Ebury](https://attack.mitre.org/software/S0377) through 2019.[^2] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to detect which Linux distribution and version is currently installed on the system.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to gather credentials in files left on disk by OpenSSH backdoors.[^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to detect installed software on targeted systems.[^3]  |
| [[Proxy\|T1090]] | Proxy | [Windigo](https://attack.mitre.org/groups/G0124) has delivered a generic Windows proxy Win32/Glubteta.M. [Windigo](https://attack.mitre.org/groups/G0124) has also used multiple reverse proxy chains as part of their C2 infrastructure.[^2]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Windigo](https://attack.mitre.org/groups/G0124) has used a Perl script for information gathering.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to check for the presence of files created by OpenSSH backdoors.[^3]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Windigo](https://attack.mitre.org/groups/G0124) has distributed Windows malware via drive-by downloads.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Ebury\|S0377]] | Ebury | [^1]  |



## References

[^1]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)


[^2]: [ESET Windigo Mar 2014](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)


[^3]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^4]: [CERN Windigo June 2019](https://security.web.cern.ch/advisories/windigo/windigo.shtml)


