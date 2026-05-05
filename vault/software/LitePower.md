---
aliases: 
    - S0680
    
mitre-attack: https://attack.mitre.org/software/S0680
---

## S0680

[LitePower](https://attack.mitre.org/software/S0680) is a downloader and second stage malware that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [LitePower](https://attack.mitre.org/software/S0680) can determine if the current user has admin privileges.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LitePower](https://attack.mitre.org/software/S0680) has the ability to download payloads containing system commands to a compromised host.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [LitePower](https://attack.mitre.org/software/S0680) can query the Registry for keys added to execute COM hijacking.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [LitePower](https://attack.mitre.org/software/S0680) can use a PowerShell script to execute commands.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [LitePower](https://attack.mitre.org/software/S0680) can take system screenshots and save them to `%AppData%`.[^1]  |
| [[Native API\|T1106]] | Native API | [LitePower](https://attack.mitre.org/software/S0680) can use various API calls.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LitePower](https://attack.mitre.org/software/S0680) can use HTTP and HTTPS for C2 communications.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [LitePower](https://attack.mitre.org/software/S0680) can send collected data, including screenshots, over its C2 channel.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [LitePower](https://attack.mitre.org/software/S0680) can create a scheduled task to enable persistence mechanisms.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [LitePower](https://attack.mitre.org/software/S0680) has the ability to list local drives.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [LitePower](https://attack.mitre.org/software/S0680) can identify installed AV software.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LitePower](https://attack.mitre.org/software/S0680) has the ability to enumerate the OS architecture.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[WIRTE\|G0090]] | WIRTE |



## References

[^1]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


