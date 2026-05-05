---
aliases: 
    - S0199
    
mitre-attack: https://attack.mitre.org/software/S0199
---

## S0199

[TURNEDUP](https://attack.mitre.org/software/S0199) is a non-public backdoor. It has been dropped by [APT33](https://attack.mitre.org/groups/G0064)'s [StoneDrill](https://attack.mitre.org/software/S0380) malware. [^3]  [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of injecting code into the APC queue of a created [Rundll32](https://attack.mitre.org/techniques/T1218/011) process as part of an "Early Bird injection."[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of taking screenshots.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of downloading additional files.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of creating a reverse shell.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of gathering system information.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of writing to a Registry Run key to establish.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |



## References

[^1]: [CyberBit Early Bird Apr 2018](https://www.cyberbit.com/blog/endpoint-security/new-early-bird-code-injection-technique-discovered/)


[^2]: TURNEDUP


[^3]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^4]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^5]: [FireEye APT33 Webinar Sept 2017](https://www.brighttalk.com/webcast/10703/275683)


