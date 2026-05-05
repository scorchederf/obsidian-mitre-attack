---
aliases: 
    - S0069
    
mitre-attack: https://attack.mitre.org/software/S0069
---

## S0069

[BLACKCOFFEE](https://attack.mitre.org/software/S0069) is malware that has been used by several Chinese groups since at least 2013. [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to enumerate files.[^2]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) uses Microsoft’s TechNet Web portal to obtain an encoded tag containing the IP address of a command and control server and then communicates separately with that IP address for C2. If the C2 server is discovered or shut down, the threat actors can update the encoded IP address on TechNet to maintain control of the victims’ machines.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to create a reverse shell.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to discover processes.[^2]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) uses Microsoft’s TechNet Web portal to obtain a dead drop resolver containing an encoded tag with the IP address of a command and control server.[^2] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to delete files.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has also obfuscated its C2 traffic as normal traffic to sites such as Github.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leviathan\|G0065]] | Leviathan |
| [[APT17\|G0025]] | APT17 |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^2]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)


[^3]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^4]: BLACKCOFFEE


