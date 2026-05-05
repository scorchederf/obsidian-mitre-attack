---
aliases: 
    - S1140
    
mitre-attack: https://attack.mitre.org/software/S1140
---

## S1140

[Spica](https://attack.mitre.org/software/S1140) is a custom backdoor written in Rust that has been used by [Star Blizzard](https://attack.mitre.org/groups/G1033) since at least 2023.[^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [Spica](https://attack.mitre.org/software/S1140) can use an obfuscated PowerShell command to create a scheduled task for persistence.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Spica](https://attack.mitre.org/software/S1140) can upload and download files to and from compromised hosts.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Spica](https://attack.mitre.org/software/S1140) can archive collected documents for exfiltration.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Spica](https://attack.mitre.org/software/S1140) can list filesystem contents on targeted systems.[^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Spica](https://attack.mitre.org/software/S1140) has the ability to steal cookies from Chrome, Firefox, Opera, and Edge browsers.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Spica](https://attack.mitre.org/software/S1140) has created a scheduled task named `CalendarChecker` to establish persistence.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Spica](https://attack.mitre.org/software/S1140) has created a scheduled task named `CalendarChecker` for persistence on compromised hosts.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Spica](https://attack.mitre.org/software/S1140) can use JSON over WebSockets for C2 communications.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | Upon execution [Spica](https://attack.mitre.org/software/S1140) can decode an embedded .pdf and write it to the desktop as a decoy document.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Star Blizzard\|G1033]] | Star Blizzard |



## References

[^1]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)


