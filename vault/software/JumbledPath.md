---
aliases: 
    - S1206
    
mitre-attack: https://attack.mitre.org/software/S1206
---

## S1206

[JumbledPath](https://attack.mitre.org/software/S1206) is a custom-built utility written in GO that has been used by [Salt Typhoon](https://attack.mitre.org/groups/G1045) since at least 2024 for packet capture on remote Cisco devices. [JumbledPath](https://attack.mitre.org/software/S1206) is compiled as an ELF binary using x86-64 architecture which makes it potentially useable across Linux operating systems and network devices from multiple vendors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Network Sniffing\|T1040]] | Network Sniffing | [JumbledPath](https://attack.mitre.org/software/S1206) has the ability to perform packet capture on remote devices via actor-defined jump-hosts.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [JumbledPath](https://attack.mitre.org/software/S1206) can impair logging on all devices used along its connection path to compromised hosts.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [JumbledPath](https://attack.mitre.org/software/S1206) can communicate over a unique series of connections to send and retrieve data from exploited devices.[^1]  |
| [[Hide Infrastructure\|T1665]] | Hide Infrastructure | [JumbledPath](https://attack.mitre.org/software/S1206) can use a chain of jump hosts to communicate with compromised devices to obscure actor infrastructure.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [JumbledPath](https://attack.mitre.org/software/S1206) can compress and encrypt exfiltrated packet captures from targeted devices.[^1]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [JumbledPath](https://attack.mitre.org/software/S1206) can clear logs on all devices used along its connection path to compromised network infrastructure.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Salt Typhoon\|G1045]] | Salt Typhoon |



## References

[^1]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)


