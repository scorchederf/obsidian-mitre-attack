---
aliases: 
    - S0272
    
mitre-attack: https://attack.mitre.org/software/S0272
---

## S0272

[NDiskMonitor](https://attack.mitre.org/software/S0272) is a custom backdoor written in .NET that appears to be unique to [Patchwork](https://attack.mitre.org/groups/G0040). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [NDiskMonitor](https://attack.mitre.org/software/S0272) obtains the victim username and encrypts the information to send over its C2 channel.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [NDiskMonitor](https://attack.mitre.org/software/S0272) uses AES to encrypt certain information sent over its C2 channel.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NDiskMonitor](https://attack.mitre.org/software/S0272) can download and execute a file from given URL.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NDiskMonitor](https://attack.mitre.org/software/S0272) obtains the victim computer name and encrypts the information to send over its C2 channel.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [NDiskMonitor](https://attack.mitre.org/software/S0272) can obtain a list of all files and directories as well as logical drives.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^2]: NDiskMonitor


