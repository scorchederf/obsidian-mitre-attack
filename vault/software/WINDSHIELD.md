---
aliases: 
    - S0155
    
mitre-attack: https://attack.mitre.org/software/S0155
---

## S0155

[WINDSHIELD](https://attack.mitre.org/software/S0155) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [WINDSHIELD](https://attack.mitre.org/software/S0155) C2 traffic can communicate via TCP raw sockets.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [WINDSHIELD](https://attack.mitre.org/software/S0155) can gather the victim user name.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [WINDSHIELD](https://attack.mitre.org/software/S0155) can gather Registry values.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [WINDSHIELD](https://attack.mitre.org/software/S0155) can gather the victim computer name.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [WINDSHIELD](https://attack.mitre.org/software/S0155) is capable of file deletion along with other file system interaction.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


