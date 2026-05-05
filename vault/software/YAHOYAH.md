---
aliases: 
    - S0388
    
mitre-attack: https://attack.mitre.org/software/S0388
---

## S0388

[YAHOYAH](https://attack.mitre.org/software/S0388) is a Trojan used by [Tropic Trooper](https://attack.mitre.org/groups/G0081) as a second-stage backdoor.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [YAHOYAH](https://attack.mitre.org/software/S0388) checks for the system’s Windows OS version and hostname.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [YAHOYAH](https://attack.mitre.org/software/S0388) uses HTTP GET requests to download other files that are executed in memory.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [YAHOYAH](https://attack.mitre.org/software/S0388) checks for antimalware solution processes on the system.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [YAHOYAH](https://attack.mitre.org/software/S0388) decrypts downloaded files before execution.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [YAHOYAH](https://attack.mitre.org/software/S0388) uses HTTP for C2.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [YAHOYAH](https://attack.mitre.org/software/S0388) encrypts its configuration file using a simple algorithm.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |



## References

[^1]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


