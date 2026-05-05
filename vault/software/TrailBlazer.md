---
aliases: 
    - S0682
    
mitre-attack: https://attack.mitre.org/software/S0682
---

## S0682

[TrailBlazer](https://attack.mitre.org/software/S0682) is a modular malware that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Junk Data\|T1001.001]] | Junk Data | [TrailBlazer](https://attack.mitre.org/software/S0682) has used random identifier strings to obscure its C2 operations and result codes.[^1]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [TrailBlazer](https://attack.mitre.org/software/S0682) can masquerade its C2 traffic as legitimate Google Notifications HTTP requests.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TrailBlazer](https://attack.mitre.org/software/S0682) has used HTTP requests for C2.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [TrailBlazer](https://attack.mitre.org/software/S0682) has used filenames that match the name of the compromised system in attempt to avoid detection.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [TrailBlazer](https://attack.mitre.org/software/S0682) has the ability to use WMI for persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


