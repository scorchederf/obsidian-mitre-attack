---
aliases: 
    - Suckfly
mitre-attack: https://attack.mitre.org/groups/G0039
---

## G0039

[Suckfly](https://attack.mitre.org/groups/G0039) is a China-based threat group that has been active since at least 2014. [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | Several tools used by [Suckfly](https://attack.mitre.org/groups/G0039) have been command-line driven.[^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Suckfly](https://attack.mitre.org/groups/G0039) used legitimate account credentials that they dumped to navigate the internal victim network as though they were the legitimate account owner.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Suckfly](https://attack.mitre.org/groups/G0039) the victim's internal network for hosts with ports 8080, 5900, and 40 open.[^1]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Suckfly](https://attack.mitre.org/groups/G0039) used a signed credential-dumping tool to obtain victim account credentials.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Suckfly](https://attack.mitre.org/groups/G0039) has used stolen certificates to sign its malware.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Nidiran\|S0118]] | Nidiran | [^3] [^1]  |



## References

[^1]: [Symantec Suckfly May 2016](http://www.symantec.com/connect/blogs/indian-organizations-targeted-suckfly-attacks)


[^2]: Suckfly


[^3]: [Symantec Suckfly March 2016](http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates)


