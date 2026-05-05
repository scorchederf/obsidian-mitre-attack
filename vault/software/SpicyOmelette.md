---
aliases: 
    - S0646
    
mitre-attack: https://attack.mitre.org/software/S0646
---

## S0646

[SpicyOmelette](https://attack.mitre.org/software/S0646) is a JavaScript based remote access tool that has been used by [Cobalt Group](https://attack.mitre.org/groups/G0080) since at least 2018.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SpicyOmelette](https://attack.mitre.org/software/S0646) can identify the system name of a compromised host.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [SpicyOmelette](https://attack.mitre.org/software/S0646) can enumerate running software on a targeted system.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [SpicyOmelette](https://attack.mitre.org/software/S0646) has been distributed via emails containing a malicious link that appears to be a PDF document.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SpicyOmelette](https://attack.mitre.org/software/S0646) has collected data and other information from a compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SpicyOmelette](https://attack.mitre.org/software/S0646) can download malicious files from threat actor controlled AWS URL's.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SpicyOmelette](https://attack.mitre.org/software/S0646) can identify the IP of a compromised system.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [SpicyOmelette](https://attack.mitre.org/software/S0646) has the ability to execute arbitrary JavaScript code on a compromised host.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [SpicyOmelette](https://attack.mitre.org/software/S0646) has been executed through malicious links within spearphishing emails.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [SpicyOmelette](https://attack.mitre.org/software/S0646) can identify payment systems, payment gateways, and ATM systems in compromised environments.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [SpicyOmelette](https://attack.mitre.org/software/S0646) has been signed with valid digital certificates.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SpicyOmelette](https://attack.mitre.org/software/S0646) can check for the presence of 29 different antivirus tools.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cobalt Group\|G0080]] | Cobalt Group |



## References

[^1]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


