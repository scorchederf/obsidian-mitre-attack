---
aliases: 
    - S0348
    
mitre-attack: https://attack.mitre.org/software/S0348
---

## S0348

[Cardinal RAT](https://attack.mitre.org/software/S0348) is a potentially low volume remote access trojan (RAT) observed since December 2015. [Cardinal RAT](https://attack.mitre.org/software/S0348) is notable for its unique utilization of uncompiled C# source code and the Microsoft Windows built-in csc.exe compiler.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cardinal RAT](https://attack.mitre.org/software/S0348) can execute commands.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cardinal RAT](https://attack.mitre.org/software/S0348) can download and execute additional payloads.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cardinal RAT](https://attack.mitre.org/software/S0348) checks its current working directory upon execution and also contains watchdog functionality that ensures its executable is located in the correct path (else it will rewrite the payload).[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Cardinal RAT](https://attack.mitre.org/software/S0348) can collect the username from a victim machine.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Cardinal RAT](https://attack.mitre.org/software/S0348) can log keystrokes.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Cardinal RAT](https://attack.mitre.org/software/S0348) uses a secret key with a series of XOR and addition operations to encrypt C2 traffic.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Cardinal RAT](https://attack.mitre.org/software/S0348) lures victims into executing malicious macros embedded within Microsoft Excel documents.[^1]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [Cardinal RAT](https://attack.mitre.org/software/S0348) applies compression to C2 traffic using the ZLIB library.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Cardinal RAT](https://attack.mitre.org/software/S0348) contains watchdog functionality that periodically ensures `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` is set to point to its executable.[^1]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [Cardinal RAT](https://attack.mitre.org/software/S0348) and its watchdog component are compiled and executed after being delivered to victims as embedded, uncompiled source code.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Cardinal RAT](https://attack.mitre.org/software/S0348) can act as a reverse proxy.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Cardinal RAT](https://attack.mitre.org/software/S0348) injects into a newly spawned process created from a native Windows executable.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Cardinal RAT](https://attack.mitre.org/software/S0348) can uninstall itself, including deleting its executable.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Cardinal RAT](https://attack.mitre.org/software/S0348) decodes many of its artifacts and is decrypted (AES-128) after being downloaded.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Cardinal RAT](https://attack.mitre.org/software/S0348) can collect the hostname, Microsoft Windows version, and processor architecture from a victim machine.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Cardinal RAT](https://attack.mitre.org/software/S0348) can communicate over multiple C2 host and port combinations.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Cardinal RAT](https://attack.mitre.org/software/S0348) is downloaded using HTTP over port 443.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Cardinal RAT](https://attack.mitre.org/software/S0348) sets `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` to point to its executable.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Cardinal RAT](https://attack.mitre.org/software/S0348) establishes Persistence by setting the  `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` Registry key to point to its executable.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Cardinal RAT](https://attack.mitre.org/software/S0348) contains watchdog functionality that ensures its process is always running, else spawns a new instance.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Cardinal RAT](https://attack.mitre.org/software/S0348) can capture screenshots.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Cardinal RAT](https://attack.mitre.org/software/S0348) encodes many of its artifacts and is encrypted (AES-128) when downloaded.[^1]   |




## References

[^1]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^2]: Cardinal RAT


