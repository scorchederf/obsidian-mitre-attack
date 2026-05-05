---
aliases: 
    - S0472
    
mitre-attack: https://attack.mitre.org/software/S0472
---

## S0472

 [down_new](https://attack.mitre.org/software/S0472) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [down_new](https://attack.mitre.org/software/S0472) has the ability to download files to the compromised host.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to identify the system volume information of a compromised host.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [down_new](https://attack.mitre.org/software/S0472) has the ability to base64 encode C2 communications.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to list the directories on a compromised host.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to list running processes on a compromised host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to detect anti-virus products and processes on a compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [down_new](https://attack.mitre.org/software/S0472) has the ability to use HTTP in C2 communications.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to gather information on installed applications.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [down_new](https://attack.mitre.org/software/S0472) has the ability to identify the MAC address of a compromised host.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [down_new](https://attack.mitre.org/software/S0472) has the ability to AES encrypt C2 communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


