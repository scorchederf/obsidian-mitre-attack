---
aliases: 
    - Strider
    - ProjectSauron
mitre-attack: https://attack.mitre.org/groups/G0041
---

## G0041

[Strider](https://attack.mitre.org/groups/G0041) is a threat group that has been active since at least 2011 and has targeted victims in Russia, China, Sweden, Belgium, Iran, and Rwanda.[^5] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Strider](https://attack.mitre.org/groups/G0041) has used local servers with both local network and Internet access to act as internal proxy nodes to exfiltrate data from other parts of the network without direct Internet access.[^3]  |
| [[Password Filter DLL\|T1556.002]] | Password Filter DLL | [Strider](https://attack.mitre.org/groups/G0041) has registered its persistence module on domain controllers as a Windows LSA (Local System Authority) password filter to acquire credentials any time a domain, local user, or administrator logs in or changes a password.[^2]  |
| [[Hidden File System\|T1564.005]] | Hidden File System | [Strider](https://attack.mitre.org/groups/G0041) has used a hidden file system that is stored as a file on disk.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Remsec\|S0125]] | Remsec | [^5] [^3]  |



## References

[^1]: Strider


[^2]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)


[^3]: [Kaspersky ProjectSauron Blog](https://securelist.com/faq-the-projectsauron-apt/75533/)


[^4]: ProjectSauron


[^5]: [Symantec Strider Blog](http://www.symantec.com/connect/blogs/strider-cyberespionage-group-turns-eye-sauron-targets)


