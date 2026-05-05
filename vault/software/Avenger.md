---
aliases: 
    - S0473
    
mitre-attack: https://attack.mitre.org/software/S0473
---

## S0473

[Avenger](https://attack.mitre.org/software/S0473) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Avenger](https://attack.mitre.org/software/S0473) has the ability to use [Tasklist](https://attack.mitre.org/software/S0057) to identify running processes.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Avenger](https://attack.mitre.org/software/S0473) has the ability to identify installed anti-virus products on a compromised host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Avenger](https://attack.mitre.org/software/S0473) has the ability to use HTTP in communication with C2.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Avenger](https://attack.mitre.org/software/S0473) has the ability to XOR encrypt files to be sent to C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Avenger](https://attack.mitre.org/software/S0473) has the ability to decrypt files downloaded from C2.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Avenger](https://attack.mitre.org/software/S0473) has the ability to browse files in directories such as Program Files and the Desktop.[^1]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Avenger](https://attack.mitre.org/software/S0473) can identify the domain of the compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Avenger](https://attack.mitre.org/software/S0473) has the ability to download files from C2 to a compromised host.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Avenger](https://attack.mitre.org/software/S0473) has the ability to inject shellcode into svchost.exe.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [Avenger](https://attack.mitre.org/software/S0473) can extract backdoor malware from downloaded images.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Avenger](https://attack.mitre.org/software/S0473) has the ability to identify the host volume ID.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Avenger](https://attack.mitre.org/software/S0473) has the ability to identify the OS architecture on a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


