---
aliases: 
    - Leafminer
    - Raspite
mitre-attack: https://attack.mitre.org/groups/G0077
---

## G0077

[Leafminer](https://attack.mitre.org/groups/G0077) is an Iranian threat group that has targeted government organizations and business entities in the Middle East since at least early 2017. [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Leafminer](https://attack.mitre.org/groups/G0077) obfuscated scripts that were used on victim machines.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Leafminer](https://attack.mitre.org/groups/G0077) has obtained and used tools such as [LaZagne](https://attack.mitre.org/software/S0349), [Mimikatz](https://attack.mitre.org/software/S0002), [PsExec](https://attack.mitre.org/software/S0029), and [MailSniper](https://attack.mitre.org/software/S0413).[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne and Mimikatz.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Leafminer](https://attack.mitre.org/groups/G0077) scanned network services to search for vulnerabilities in the victim system.[^1]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne.[^1]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne.[^1]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Leafminer](https://attack.mitre.org/groups/G0077) used several tools for retrieving login and password information, including LaZagne.[^1]  |
| [[Process Doppelgänging\|T1055.013]] | Process Doppelgänging | [Leafminer](https://attack.mitre.org/groups/G0077) has used [Process Doppelgänging](https://attack.mitre.org/techniques/T1055/013) to evade security software while deploying tools on compromised systems.[^1] 	 |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Leafminer](https://attack.mitre.org/groups/G0077) has infected victims using watering holes.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Leafminer](https://attack.mitre.org/groups/G0077) used Microsoft’s Sysinternals tools to gather detailed information about remote systems.[^1]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Leafminer](https://attack.mitre.org/groups/G0077) used a tool called Total SMB BruteForcer to perform internal password spraying.[^1]  |
| [[Local Account\|T1136.001]] | Local Account | [Leafminer](https://attack.mitre.org/groups/G0077) used a tool called Imecab to set up a persistent remote access account on the victim machine.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Leafminer](https://attack.mitre.org/groups/G0077) infected victims using JavaScript code.[^1]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Leafminer](https://attack.mitre.org/groups/G0077) used a tool called MailSniper to search through the Exchange server mailboxes for keywords.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Leafminer](https://attack.mitre.org/groups/G0077) used a tool called MailSniper to search for files on the desktop and another utility called Sobolsoft to extract attachments from EML files.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[MailSniper\|S0413]] | MailSniper | [^1]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |
| [[LaZagne\|S0349]] | LaZagne | [^1]  |
| [[PsExec\|S0029]] | PsExec | [^1]  |



## References

[^1]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^2]: Raspite


[^3]: [Dragos Raspite Aug 2018](https://www.dragos.com/blog/20180802Raspite.html)


[^4]: Leafminer


