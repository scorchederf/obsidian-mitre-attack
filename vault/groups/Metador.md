---
aliases: 
    - Metador
mitre-attack: https://attack.mitre.org/groups/G1013
---

## G1013

[Metador](https://attack.mitre.org/groups/G1013) is a suspected cyber espionage group that was first reported in September 2022. [Metador](https://attack.mitre.org/groups/G1013) has targeted a limited number of telecommunication companies, internet service providers, and universities in the Middle East and Africa. Security researchers named the group [Metador](https://attack.mitre.org/groups/G1013) based on the "I am meta" string in one of the group's malware samples and the expectation of Spanish-language responses from C2 servers.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Metador](https://attack.mitre.org/groups/G1013) has used HTTP for C2.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Metador](https://attack.mitre.org/groups/G1013) has used the Windows command line to execute commands.[^2]  |
| [[Malware\|T1588.001]] | Malware | [Metador](https://attack.mitre.org/groups/G1013) has used unique malware in their operations, including [metaMain](https://attack.mitre.org/software/S1059) and [Mafalda](https://attack.mitre.org/software/S1060).[^2]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Metador](https://attack.mitre.org/groups/G1013) has established persistence through the use of a WMI event subscription combined with unusual living-off-the-land binaries such as `cdb.exe`.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Metador](https://attack.mitre.org/groups/G1013) has encrypted their payloads.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Metador](https://attack.mitre.org/groups/G1013) has quickly deleted `cbd.exe` from a compromised host following the successful deployment of their malware.[^2]   |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Metador](https://attack.mitre.org/groups/G1013) has used TCP for C2.[^2]  |
| [[Tool\|T1588.002]] | Tool | [Metador](https://attack.mitre.org/groups/G1013) has used Microsoft's Console Debugger in some of their operations.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Metador](https://attack.mitre.org/groups/G1013) has downloaded tools and malware onto a compromised system.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mafalda\|S1060]] | Mafalda | [^2] [^1]  |
| [[metaMain\|S1059]] | metaMain | [^2] [^1]  |



## References

[^1]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^2]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


