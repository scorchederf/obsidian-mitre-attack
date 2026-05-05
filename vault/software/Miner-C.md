---
aliases: 
    - S0133
    
mitre-attack: https://attack.mitre.org/software/S0133
---

## S0133

[Miner-C](https://attack.mitre.org/software/S0133) is malware that mines victims for the Monero cryptocurrency. It has targeted FTP servers and Network Attached Storage (NAS) devices to spread. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Miner-C](https://attack.mitre.org/software/S0133) copies itself into the public folder of Network Attached Storage (NAS) devices and infects new victims who open the file.[^1]  |




## References

[^1]: [Softpedia MinerC](https://news.softpedia.com/news/cryptocurrency-mining-malware-discovered-targeting-seagate-nas-hard-drives-508119.shtml)


