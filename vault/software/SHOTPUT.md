---
aliases: 
    - S0063
    
mitre-attack: https://attack.mitre.org/software/S0063
---

## S0063

[SHOTPUT](https://attack.mitre.org/software/S0063) is a custom backdoor used by [APT3](https://attack.mitre.org/groups/G0022). [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SHOTPUT](https://attack.mitre.org/software/S0063) is obscured using XOR encoding and appended to a valid GIF file.[^4] [^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to obtain a directory listing.[^5]  |
| [[Local Account\|T1087.001]] | Local Account | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to retrieve information about connected users.[^5]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to list all servers in the domain, as well as one to locate domain controllers on a domain.[^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [SHOTPUT](https://attack.mitre.org/software/S0063) uses [netstat](https://attack.mitre.org/software/S0104) to list TCP connection status.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to obtain a process listing.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT3\|G0022]] | APT3 |



## References

[^1]: Pirpi


[^2]: [FireEye Clandestine Fox Part 2](https://www.fireeye.com/blog/threat-research/2014/06/clandestine-fox-part-deux.html)


[^3]: Backdoor.APT.CookieCutter


[^4]: [FireEye Clandestine Wolf](https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html)


[^5]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)


