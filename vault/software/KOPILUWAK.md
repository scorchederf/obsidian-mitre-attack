---
aliases: 
    - S1075
    
mitre-attack: https://attack.mitre.org/software/S1075
---

## S1075

[KOPILUWAK](https://attack.mitre.org/software/S1075) is a JavaScript-based reconnaissance tool that has been used for victim profiling and C2 since at least 2017.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [KOPILUWAK](https://attack.mitre.org/software/S1075) has used HTTP POST requests to send data to C2.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [KOPILUWAK](https://attack.mitre.org/software/S1075) has gained execution through malicious attachments.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can enumerate current running processes on the targeted machine.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can use [netstat](https://attack.mitre.org/software/S0104) and [Net](https://attack.mitre.org/software/S0039) to discover network shares.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can use [Arp](https://attack.mitre.org/software/S0099) to discover a target's network configuration setttings.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [KOPILUWAK](https://attack.mitre.org/software/S1075) has exfiltrated collected data to its C2 via POST requests.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can discover logical drive information on compromised hosts.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can use [netstat](https://attack.mitre.org/software/S0104), [Arp](https://attack.mitre.org/software/S0099), and [Net](https://attack.mitre.org/software/S0039) to discover current TCP connections.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [KOPILUWAK](https://attack.mitre.org/software/S1075) has been delivered to victims as a malicious email attachment.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [KOPILUWAK](https://attack.mitre.org/software/S1075) can gather information from compromised hosts.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [KOPILUWAK](https://attack.mitre.org/software/S1075) has piped the results from executed C2 commands to `%TEMP%\result2.dat` on the local machine.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [KOPILUWAK](https://attack.mitre.org/software/S1075) had used Javascript to perform its core functions.[^1]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [KOPILUWAK](https://attack.mitre.org/software/S1075) can conduct basic network reconnaissance on the victim machine with `whoami`, to get user details.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


