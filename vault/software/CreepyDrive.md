---
aliases: 
    - S1023
    
mitre-attack: https://attack.mitre.org/software/S1023
---

## S1023

[CreepyDrive](https://attack.mitre.org/software/S1023) is a custom implant has been used by [POLONIUM](https://attack.mitre.org/groups/G1005) since at least early 2022 for C2 with and exfiltration to actor-controlled OneDrive accounts.[^1] <br><br>[POLONIUM](https://attack.mitre.org/groups/G1005) has used a similar implant called CreepyBox that relies on actor-controlled DropBox accounts.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CreepyDrive](https://attack.mitre.org/software/S1023) can use HTTPS for C2 using the Microsoft Graph API.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [CreepyDrive](https://attack.mitre.org/software/S1023) can use cloud services including OneDrive for data exfiltration.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [CreepyDrive](https://attack.mitre.org/software/S1023) can use OneDrive for C2.[^1]  |
| [[Application Access Token\|T1550.001]] | Application Access Token | [CreepyDrive](https://attack.mitre.org/software/S1023) can use legitimate OAuth refresh tokens to authenticate with OneDrive.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CreepyDrive](https://attack.mitre.org/software/S1023) can specify the local file path to upload files from.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CreepyDrive](https://attack.mitre.org/software/S1023) can download files to the compromised host.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CreepyDrive](https://attack.mitre.org/software/S1023) can use Powershell for execution, including the cmdlets `Invoke-WebRequest` and `Invoke-Expression`.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CreepyDrive](https://attack.mitre.org/software/S1023) can upload files to C2 from victim machines.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[POLONIUM\|G1005]] | POLONIUM |



## References

[^1]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


