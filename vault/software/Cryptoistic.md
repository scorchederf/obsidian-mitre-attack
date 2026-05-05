---
aliases: 
    - S0498
    
mitre-attack: https://attack.mitre.org/software/S0498
---

## S0498

[Cryptoistic](https://attack.mitre.org/software/S0498) is a backdoor, written in Swift, that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [Cryptoistic](https://attack.mitre.org/software/S0498) can retrieve files from the local file system.[^1]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Cryptoistic](https://attack.mitre.org/software/S0498) can engage in encrypted communications with C2.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Cryptoistic](https://attack.mitre.org/software/S0498) has the ability delete files from a compromised host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cryptoistic](https://attack.mitre.org/software/S0498) can scan a directory to identify files for deletion.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cryptoistic](https://attack.mitre.org/software/S0498) has the ability to send and receive files.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Cryptoistic](https://attack.mitre.org/software/S0498) can use TCP in communications with C2.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Cryptoistic](https://attack.mitre.org/software/S0498) can gather data on the user of a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


