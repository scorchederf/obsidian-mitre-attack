---
aliases: 
    - S1088
    
mitre-attack: https://attack.mitre.org/software/S1088
---

## S1088

[Disco](https://attack.mitre.org/software/S1088) is a custom implant that has been used by [MoustachedBouncer](https://attack.mitre.org/groups/G1019) since at least 2020 including in campaigns using targeted malicious content injection for initial access and command and control.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Disco](https://attack.mitre.org/software/S1088) can download files to targeted systems via SMB.[^1]  |
| [[Content Injection\|T1659]] | Content Injection | [Disco](https://attack.mitre.org/software/S1088) has achieved initial access and execution through content injection into DNS,  HTTP, and SMB replies to targeted hosts that redirect them to download malicious files.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Disco](https://attack.mitre.org/software/S1088) can create a scheduled task to run every minute for persistence.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Disco](https://attack.mitre.org/software/S1088) has been executed through inducing user interaction with malicious .zip and .msi files.[^1]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Disco](https://attack.mitre.org/software/S1088) can use SMB to transfer files.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MoustachedBouncer\|G1019]] | MoustachedBouncer |



## References

[^1]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


