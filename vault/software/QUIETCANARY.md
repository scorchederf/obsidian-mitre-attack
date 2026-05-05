---
aliases: 
    - S1076
    
mitre-attack: https://attack.mitre.org/software/S1076
---

## S1076

[QUIETCANARY](https://attack.mitre.org/software/S1076) is a backdoor tool written in .NET that has been used since at least 2022 to gather and exfiltrate data from victim networks.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [QUIETCANARY](https://attack.mitre.org/software/S1076) can RC4 encrypt C2 communications.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [QUIETCANARY](https://attack.mitre.org/software/S1076) can use a custom parsing routine to decode the command codes and additional parameters from the C2 before executing them.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [QUIETCANARY](https://attack.mitre.org/software/S1076) can identify the default proxy setting on a compromised host.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [QUIETCANARY](https://attack.mitre.org/software/S1076) can execute processes in a hidden window.[^2]  |
| [[Data Staged\|T1074]] | Data Staged | [QUIETCANARY](https://attack.mitre.org/software/S1076) has the ability to stage data prior to exfiltration.[^2]  |
| [[Native API\|T1106]] | Native API | [QUIETCANARY](https://attack.mitre.org/software/S1076) can call `System.Net.HttpWebRequest` to identify the default proxy configured on the victim computer.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [QUIETCANARY](https://attack.mitre.org/software/S1076) can use HTTPS for C2 communications.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [QUIETCANARY](https://attack.mitre.org/software/S1076) has the ability to retrieve information from the Registry.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [QUIETCANARY](https://attack.mitre.org/software/S1076) can base64 encode C2 communications.[^2]  |




## References

[^1]: Tunnus


[^2]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


