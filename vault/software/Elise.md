---
aliases: 
    - S0081
    
mitre-attack: https://attack.mitre.org/software/S0081
---

## S0081

[Elise](https://attack.mitre.org/software/S0081) is a custom backdoor Trojan that appears to be used exclusively by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It is part of a larger group of tools referred to as LStudio, ST Group, and APT0LSTU.[^4] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | If installing itself as a service fails, [Elise](https://attack.mitre.org/software/S0081) instead writes itself as a file named svchost.exe saved in %APPDATA%\Microsoft\Network.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Elise](https://attack.mitre.org/software/S0081) can download additional files from the C2 server for execution.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Elise](https://attack.mitre.org/software/S0081) executes `systeminfo` after initial communication is made to the remote server.[^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Elise](https://attack.mitre.org/software/S0081) encrypts exfiltrated data with RC4.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Elise](https://attack.mitre.org/software/S0081) executes `net start` after initial communication is made to the remote server.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Elise](https://attack.mitre.org/software/S0081) configures itself as a service.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Elise](https://attack.mitre.org/software/S0081) executes `ipconfig /all` after initial communication is made to the remote server.[^4] [^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | After copying itself to a DLL file, a variant of [Elise](https://attack.mitre.org/software/S0081) calls the DLL file using rundll32.exe.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Elise](https://attack.mitre.org/software/S0081) enumerates processes via the `tasklist` command.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Elise](https://attack.mitre.org/software/S0081) encrypts several of its files, including configuration files.[^4]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Elise](https://attack.mitre.org/software/S0081) performs timestomping of a CAB file it creates.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | A variant of [Elise](https://attack.mitre.org/software/S0081) executes `dir C:\progra~1` when initially run.[^4] [^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Elise](https://attack.mitre.org/software/S0081) creates a file in `AppData\Local\Microsoft\Windows\Explorer` and stores all harvested data in that file.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Elise](https://attack.mitre.org/software/S0081) is capable of launching a remote shell on the host to delete itself.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Elise](https://attack.mitre.org/software/S0081) communicates over HTTP or HTTPS for C2.[^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Elise](https://attack.mitre.org/software/S0081) exfiltrates data using cookie values that are Base64-encoded.[^4]  |
| [[Local Account\|T1087.001]] | Local Account | [Elise](https://attack.mitre.org/software/S0081) executes `net user` after initial communication is made to the remote server.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | If establishing persistence by installation as a new service fails, one variant of [Elise](https://attack.mitre.org/software/S0081) establishes persistence for the created .exe file by setting the following Registry key: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\svchost : %APPDATA%\Microsoft\Network\svchost.exe`. Other variants have set the following Registry keys for persistence: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\imejp : [self]` and `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\IAStorD`.[^4] [^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Elise](https://attack.mitre.org/software/S0081) injects DLL files into iexplore.exe.[^4] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |



## References

[^1]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^2]: Page


[^3]: Elise


[^4]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^5]: [Spring Dragon Jun 2015](https://securelist.com/the-spring-dragon-apt/70726/)


[^6]: BKDR_ESILE


