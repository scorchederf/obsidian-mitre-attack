---
aliases: 
    - S1102
    
mitre-attack: https://attack.mitre.org/software/S1102
---

## S1102

[Pcexter](https://attack.mitre.org/software/S1102) is an uploader that has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2023 to exfiltrate stolen files.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Pcexter](https://attack.mitre.org/software/S1102) has the ability to search for files in specified directories.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Pcexter](https://attack.mitre.org/software/S1102) can upload stolen files to OneDrive storage accounts via HTTP `POST`.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Pcexter](https://attack.mitre.org/software/S1102) has been distributed and executed as a DLL file named Vspmsg.dll via DLL side-loading.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Pcexter](https://attack.mitre.org/software/S1102) can upload files from targeted systems.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[ToddyCat\|G1022]] | ToddyCat |



## References

[^1]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


