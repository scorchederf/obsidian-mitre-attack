---
aliases: 
    - S0471
    
mitre-attack: https://attack.mitre.org/software/S0471
---

## S0471

[build_downer](https://attack.mitre.org/software/S0471) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [build_downer](https://attack.mitre.org/software/S0471) has the ability to use the `WinExec` API to execute malware on a compromised host.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [build_downer](https://attack.mitre.org/software/S0471) has added itself to the Registry Run key as "NVIDIA" to appear legitimate.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [build_downer](https://attack.mitre.org/software/S0471) has the ability to add itself to the Registry Run key for persistence.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [build_downer](https://attack.mitre.org/software/S0471) can extract malware from a downloaded JPEG.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [build_downer](https://attack.mitre.org/software/S0471) has the ability to determine the local time to ensure malware installation only happens during the hours that the infected system is active.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [build_downer](https://attack.mitre.org/software/S0471) has the ability to detect if the infected host is running an anti-virus process.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [build_downer](https://attack.mitre.org/software/S0471) has the ability to send system volume information to C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [build_downer](https://attack.mitre.org/software/S0471) has the ability to download files from C2 to the infected host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


