---
aliases: 
    - S0082
    
mitre-attack: https://attack.mitre.org/software/S0082
---

## S0082

[Emissary](https://attack.mitre.org/software/S0082) is a Trojan that has been used by [Lotus Blossom](https://attack.mitre.org/groups/G0030). It shares code with [Elise](https://attack.mitre.org/software/S0081), with both Trojans being part of a malware group referred to as LStudio.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | Variants of [Emissary](https://attack.mitre.org/software/S0082) have added Run Registry keys to establish persistence.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Variants of [Emissary](https://attack.mitre.org/software/S0082) encrypt payloads using various XOR ciphers, as well as a custom algorithm that uses the "srand" and "rand" functions.[^1] [^3]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Emissary](https://attack.mitre.org/software/S0082) injects its DLL file into a newly spawned Internet Explorer process.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | Variants of [Emissary](https://attack.mitre.org/software/S0082) have used rundll32.exe in Registry values added to establish persistence.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute the command `ipconfig /all`.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Emissary](https://attack.mitre.org/software/S0082) has the capability to create a remote shell and execute specified commands.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute ver and systeminfo commands.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | The C2 server response to a beacon sent by a variant of [Emissary](https://attack.mitre.org/software/S0082) contains a 36-character GUID value that is used as an encryption key for subsequent network communications. Some variants of [Emissary](https://attack.mitre.org/software/S0082) use various XOR operations to encrypt C2 data.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Emissary](https://attack.mitre.org/software/S0082) uses HTTP or HTTPS for C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Emissary](https://attack.mitre.org/software/S0082) has the capability to download files from the C2 server.[^1]  |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute `gpresult`.[^3]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute the command `net localgroup administrators`.[^3]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute the command `net start` to interact with services.[^3]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | A variant of [Emissary](https://attack.mitre.org/software/S0082) appends junk data to the end of its DLL file to create a large file that may exceed the maximum size that anti-virus programs can scan.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Emissary](https://attack.mitre.org/software/S0082) is capable of configuring itself as a service.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |



## References

[^1]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^2]: Emissary


[^3]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


