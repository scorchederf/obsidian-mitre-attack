---
aliases: 
    - S0470
    
mitre-attack: https://attack.mitre.org/software/S0470
---

## S0470

[BBK](https://attack.mitre.org/software/S0470) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Injection\|T1055]] | Process Injection | [BBK](https://attack.mitre.org/software/S0470) has the ability to inject shellcode into svchost.exe.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [BBK](https://attack.mitre.org/software/S0470) can extract a malicious Portable Executable (PE) from a photo.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BBK](https://attack.mitre.org/software/S0470) has the ability to download files from C2 to the infected host.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BBK](https://attack.mitre.org/software/S0470) has the ability to use HTTP in communications with C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BBK](https://attack.mitre.org/software/S0470) has the ability to decrypt AES encrypted payloads.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BBK](https://attack.mitre.org/software/S0470) has the ability to use [cmd](https://attack.mitre.org/software/S0106) to run a Portable Executable (PE) on the compromised host.[^1]  |
| [[Native API\|T1106]] | Native API | [BBK](https://attack.mitre.org/software/S0470) has the ability to use the `CreatePipe` API to add a sub-process for execution via [cmd](https://attack.mitre.org/software/S0106).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


