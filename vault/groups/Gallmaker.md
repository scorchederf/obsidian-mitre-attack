---
aliases: 
    - Gallmaker
mitre-attack: https://attack.mitre.org/groups/G0084
---

## G0084

[Gallmaker](https://attack.mitre.org/groups/G0084) is a cyberespionage group that has targeted victims in the Middle East and has been active since at least December 2017. The group has mainly targeted victims in the defense, military, and government sectors.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [Gallmaker](https://attack.mitre.org/groups/G0084) sent victims a lure document with a warning that asked victims to “enable content” for execution.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Gallmaker](https://attack.mitre.org/groups/G0084) obfuscated shellcode used during execution.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Gallmaker](https://attack.mitre.org/groups/G0084) has used WinZip, likely to archive data prior to exfiltration.[^2]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Gallmaker](https://attack.mitre.org/groups/G0084) attempted to exploit Microsoft’s DDE protocol in order to gain access to victim machines and for execution.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Gallmaker](https://attack.mitre.org/groups/G0084) used PowerShell to download additional payloads and for execution.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Gallmaker](https://attack.mitre.org/groups/G0084) sent emails with malicious Microsoft Office documents attached.[^2]  |




## References

[^1]: Gallmaker


[^2]: [Symantec Gallmaker Oct 2018](https://www.symantec.com/blogs/threat-intelligence/gallmaker-attack-group)


