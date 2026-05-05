---
aliases: 
    - POLONIUM
    - Plaid Rain
mitre-attack: https://attack.mitre.org/groups/G1005
---

## G1005

[POLONIUM](https://attack.mitre.org/groups/G1005) is a Lebanon-based group that has primarily targeted Israeli organizations, including critical manufacturing, information technology, and defense industry companies, since at least February 2022. Security researchers assess [POLONIUM](https://attack.mitre.org/groups/G1005) has coordinated their operations with multiple actors affiliated with Iran’s Ministry of Intelligence and Security (MOIS), based on victim overlap as well as common techniques and tooling.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [POLONIUM](https://attack.mitre.org/groups/G1005) has exfiltrated stolen data to [POLONIUM](https://attack.mitre.org/groups/G1005)-owned OneDrive and Dropbox accounts.[^2]   |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [POLONIUM](https://attack.mitre.org/groups/G1005) has used OneDrive and DropBox for C2.[^2]  |
| [[Proxy\|T1090]] | Proxy | [POLONIUM](https://attack.mitre.org/groups/G1005) has used the AirVPN service for operational activity.[^2]  |
| [[Tool\|T1588.002]] | Tool | [POLONIUM](https://attack.mitre.org/groups/G1005) has obtained and used tools such as AirVPN and plink in their operations.[^2]   |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [POLONIUM](https://attack.mitre.org/groups/G1005) has used compromised credentials from an IT company to target downstream customers including a law firm and aviation company.[^2]  |
| [[Web Services\|T1583.006]] | Web Services | [POLONIUM](https://attack.mitre.org/groups/G1005) has created and used legitimate Microsoft OneDrive accounts for their operations.[^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [POLONIUM](https://attack.mitre.org/groups/G1005) has used valid compromised credentials to gain access to victim environments.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[CreepyDrive\|S1023]] | CreepyDrive | [^2]  |
| [[CreepySnail\|S1024]] | CreepySnail | [^2]  |



## References

[^1]: Plaid Rain


[^2]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^3]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


