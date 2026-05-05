---
aliases: 
    - S0469
    
mitre-attack: https://attack.mitre.org/software/S0469
---

## S0469

[ABK](https://attack.mitre.org/software/S0469) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [ABK](https://attack.mitre.org/software/S0469) has the ability to identify the installed anti-virus product on the compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ABK](https://attack.mitre.org/software/S0469) has the ability to decrypt AES encrypted payloads.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ABK](https://attack.mitre.org/software/S0469) has the ability to use HTTP in communications with C2.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [ABK](https://attack.mitre.org/software/S0469) has the ability to inject shellcode into svchost.exe.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ABK](https://attack.mitre.org/software/S0469) has the ability to download files from C2.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [ABK](https://attack.mitre.org/software/S0469) can extract a malicious Portable Executable (PE) from a photo.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ABK](https://attack.mitre.org/software/S0469) has the ability to use [cmd](https://attack.mitre.org/software/S0106) to run a Portable Executable (PE) on the compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


