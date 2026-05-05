---
aliases: 
    - S0416
    
mitre-attack: https://attack.mitre.org/software/S0416
---

## S0416

[RDFSNIFFER](https://attack.mitre.org/software/S0416) is a module loaded by [BOOSTWRITE](https://attack.mitre.org/software/S0415) which allows an attacker to monitor and tamper with legitimate connections made via an application designed to provide visibility and system management capabilities to remote IT techs.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [RDFSNIFFER](https://attack.mitre.org/software/S0416) hooks several Win32 API functions to hijack elements of the remote system management user-interface.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RDFSNIFFER](https://attack.mitre.org/software/S0416) has the capability of deleting local files.[^1]  |
| [[Native API\|T1106]] | Native API | [RDFSNIFFER](https://attack.mitre.org/software/S0416) has used several Win32 API functions to interact with the victim machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)


