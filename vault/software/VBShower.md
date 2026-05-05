---
aliases: 
    - S0442
    
mitre-attack: https://attack.mitre.org/software/S0442
---

## S0442

[VBShower](https://attack.mitre.org/software/S0442) is a backdoor that has been used by [Inception](https://attack.mitre.org/groups/G0100) since at least 2019. [VBShower](https://attack.mitre.org/software/S0442) has been used as a downloader for second stage payloads, including [PowerShower](https://attack.mitre.org/software/S0441).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [VBShower](https://attack.mitre.org/software/S0442) has the ability to execute VBScript files.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [VBShower](https://attack.mitre.org/software/S0442) has attempted to complicate forensic analysis by deleting all the files contained in `%APPDATA%\..\Local\Temporary Internet Files\Content.Word` and `%APPDATA%\..\Local Settings\Temporary Internet Files\Content.Word\`.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [VBShower](https://attack.mitre.org/software/S0442) used `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\\[a-f0-9A-F]{8}` to maintain persistence.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [VBShower](https://attack.mitre.org/software/S0442) has attempted to obtain a VBS script from command and control (C2) nodes over HTTP.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [VBShower](https://attack.mitre.org/software/S0442) has the ability to download VBS files to the target computer.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Inception\|G0100]] | Inception |



## References

[^1]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


