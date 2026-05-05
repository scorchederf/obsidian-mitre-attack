---
aliases: 
    - S1166
    
mitre-attack: https://attack.mitre.org/software/S1166
---

## S1166

[Solar](https://attack.mitre.org/software/S1166) is a C#/.NET backdoor that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Outer Space](https://attack.mitre.org/campaigns/C0042) campaign to download, execute, and exfiltrate files.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Solar](https://attack.mitre.org/software/S1166) can create scheduled tasks named Earth and Venus, which run every 30 and 40 seconds respectively, to support C2 and exfiltration.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Solar](https://attack.mitre.org/software/S1166) has the ability to download and execute files.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Solar](https://attack.mitre.org/software/S1166) can automatically exfitrate files from compromised systems.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Solar](https://attack.mitre.org/software/S1166) can XOR encrypt C2 communications.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Solar](https://attack.mitre.org/software/S1166) can send staged files to C2 for exfiltration.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Solar](https://attack.mitre.org/software/S1166) can send basic information about the infected host to C2.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Solar](https://attack.mitre.org/software/S1166) has the ability to delete staged files after they are uploaded to C2.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Solar](https://attack.mitre.org/software/S1166) can Base64-encode and gzip compress C2 communications including command outputs.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


