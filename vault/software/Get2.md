---
aliases: 
    - S0460
    
mitre-attack: https://attack.mitre.org/software/S0460
---

## S0460

[Get2](https://attack.mitre.org/software/S0460) is a downloader written in C++ that has been used by [TA505](https://attack.mitre.org/groups/G0092) to deliver [FlawedGrace](https://attack.mitre.org/software/S0383), [FlawedAmmyy](https://attack.mitre.org/software/S0381), Snatch and [SDBbot](https://attack.mitre.org/software/S0461).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Get2](https://attack.mitre.org/software/S0460) has the ability to inject DLLs into processes.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify running processes on an infected host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify the computer name and Windows version of an infected host.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Get2](https://attack.mitre.org/software/S0460) has the ability to run executables with command-line arguments.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify the current username of an infected host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Get2](https://attack.mitre.org/software/S0460) has the ability to use HTTP to send information collected from an infected host to C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


