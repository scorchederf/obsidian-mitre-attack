---
aliases: 
    - S0383
    
mitre-attack: https://attack.mitre.org/software/S0383
---

## S0383

[FlawedGrace](https://attack.mitre.org/software/S0383) is a fully featured remote access tool (RAT) written in C++ that was first observed in late 2017.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [FlawedGrace](https://attack.mitre.org/software/S0383) encrypts its C2 configuration files with AES in CBC mode.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^2]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^3]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


