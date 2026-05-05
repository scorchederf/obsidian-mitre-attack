---
aliases: 
    - MoustachedBouncer
mitre-attack: https://attack.mitre.org/groups/G1019
---

## G1019

[MoustachedBouncer](https://attack.mitre.org/groups/G1019) is a cyberespionage group that has been active since at least 2014 targeting foreign embassies in Belarus.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used plugins to execute PowerShell scripts.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used JavaScript to deliver malware hosted on HTML pages.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used malware plugins packed with Themida.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used plugins to take screenshots on targeted systems.[^1]  |
| [[Proxy\|T1090]] | Proxy | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used a reverse proxy tool similar to the GitHub repository revsocks.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has exploited CVE-2021-1732 to execute malware components with elevated rights.[^1]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has used plugins to save captured screenshots to `.\AActdata\` on an SMB share.[^1]  |
| [[Content Injection\|T1659]] | Content Injection | [MoustachedBouncer](https://attack.mitre.org/groups/G1019) has injected content into DNS, HTTP, and SMB replies to redirect specifically-targeted victims to a fake Windows Update page to download malware.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[SharpDisco\|S1089]] | SharpDisco | [^1]  |
| [[NightClub\|S1090]] | NightClub | [^1]  |
| [[Disco\|S1088]] | Disco | [^1]  |



## References

[^1]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


