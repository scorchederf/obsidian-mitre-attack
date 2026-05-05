---
aliases: 
    - S0441
    
mitre-attack: https://attack.mitre.org/software/S0441
---

## S0441

[PowerShower](https://attack.mitre.org/software/S0441) is a PowerShell backdoor used by [Inception](https://attack.mitre.org/groups/G0100) for initial reconnaissance and to download and execute second stage payloads.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PowerShower](https://attack.mitre.org/software/S0441) has collected system information on the infected host.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to remove all files created during the dropper process.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to deploy a reconnaissance module to retrieve a list of the active processes.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerShower](https://attack.mitre.org/software/S0441) is a backdoor written in PowerShell.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PowerShower](https://attack.mitre.org/software/S0441) sets up persistence with a Registry run key.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PowerShower](https://attack.mitre.org/software/S0441) has used a PowerShell document stealer module to pack and exfiltrate .txt, .pdf, .xls or .doc files smaller than 5MB that were modified during the past two days.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to encode C2 communications with base64 encoding.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PowerShower](https://attack.mitre.org/software/S0441) has sent HTTP GET and POST requests to C2 servers to send information and receive instructions.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PowerShower](https://attack.mitre.org/software/S0441) has added a registry key so future powershell.exe instances are spawned off-screen by default, and has removed all registry entries that are left behind during the dropper process.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to identify the current Windows domain of the infected host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to identify the current user on the infected host.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [PowerShower](https://attack.mitre.org/software/S0441) has added a registry key so future powershell.exe instances are spawned with coordinates for a window position off-screen by default.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [PowerShower](https://attack.mitre.org/software/S0441) has used 7Zip to compress .txt, .pdf, .xls or .doc files prior to exfiltration.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to save and execute VBScript.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Inception\|G0100]] | Inception |



## References

[^1]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)


[^2]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


