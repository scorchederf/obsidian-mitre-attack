---
aliases: 
    - S1171
    
mitre-attack: https://attack.mitre.org/software/S1171
---

## S1171

[OilCheck](https://attack.mitre.org/software/S1171) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against targets in Israel. [OilCheck](https://attack.mitre.org/software/S1171) uses draft messages created in a shared email account for C2 communication.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [OilCheck](https://attack.mitre.org/software/S1171) can upload documents from compromised hosts to a shared Microsoft Office 365 Outlook email account for exfiltration.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OilCheck](https://attack.mitre.org/software/S1171) can download staged payloads from an actor-controlled infrastructure.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [OilCheck](https://attack.mitre.org/software/S1171) can use a REST-based Microsoft Graph API to access draft messages in a shared Microsoft Office 365 Outlook email account used for C2 communication.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


