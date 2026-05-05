---
aliases: 
    - S0437
    
mitre-attack: https://attack.mitre.org/software/S0437
---

## S0437

[Kivars](https://attack.mitre.org/software/S0437) is a modular remote access tool (RAT), derived from the Bifrost RAT, that was used by [BlackTech](https://attack.mitre.org/groups/G0098) in a 2010 campaign.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [Kivars](https://attack.mitre.org/software/S0437) has the ability to uninstall malware from the infected host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kivars](https://attack.mitre.org/software/S0437) has the ability to list drives on the infected host.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Kivars](https://attack.mitre.org/software/S0437) has the ability to initiate keylogging on the infected host.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Kivars](https://attack.mitre.org/software/S0437) has the ability to conceal its activity through hiding active windows.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Kivars](https://attack.mitre.org/software/S0437) has the ability to capture screenshots on the infected host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kivars](https://attack.mitre.org/software/S0437) has the ability to download and execute files.[^1]  |
| [[Remote Services\|T1021]] | Remote Services | [Kivars](https://attack.mitre.org/software/S0437) has the ability to remotely trigger keyboard input and mouse clicks. [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackTech\|G0098]] | BlackTech |



## References

[^1]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^2]: [Symantec Palmerworm Sep 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt)


