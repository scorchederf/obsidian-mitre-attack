---
aliases: 
    - S1190
    
mitre-attack: https://attack.mitre.org/software/S1190
---

## S1190

Kapeka is a backdoor written in C++ used against victims in Eastern Europe since at least mid-2022. Kapeka has technical overlaps with [Exaramel for Windows](https://attack.mitre.org/software/S0343) and [Prestige](https://attack.mitre.org/software/S1058) malware variants, both of which are linked to [Sandworm Team](https://attack.mitre.org/groups/G0034). Kapeka may have been used in advance of [Prestige](https://attack.mitre.org/software/S1058) deployment in late 2022.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Rundll32\|T1218.011]] | Rundll32 | [Kapeka](https://attack.mitre.org/software/S1190) is a Windows DLL file executed via ordinal by `rundll32.exe`.[^3] [^2]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Kapeka](https://attack.mitre.org/software/S1190) masquerades as a Microsoft Word Add-In file, with the extension `.wll`, but is a malicious DLL file.[^3] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kapeka](https://attack.mitre.org/software/S1190) utilizes WinAPI calls and registry queries to gather system information.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Kapeka](https://attack.mitre.org/software/S1190) allows for arbitrary Windows command execution.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Kapeka](https://attack.mitre.org/software/S1190) writes persistent configuration information to the victim host registry.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Kapeka](https://attack.mitre.org/software/S1190) persists via scheduled tasks.[^3] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Kapeka](https://attack.mitre.org/software/S1190) utilizes HTTP for command and control.[^2]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [Kapeka](https://attack.mitre.org/software/S1190) will clear registry values used for persistent configuration storage when uninstalled.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Kapeka](https://attack.mitre.org/software/S1190) utilizes JSON objects to send and receive information from command and control nodes.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Kapeka](https://attack.mitre.org/software/S1190) queries registry values for stored configuration information.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kapeka](https://attack.mitre.org/software/S1190) utilizes obfuscated JSON structures for various data storage and configuration management items.[^2]  |
| [[Proxy\|T1090]] | Proxy | [Kapeka](https://attack.mitre.org/software/S1190) can identify system proxy settings via `WinHttpGetIEProxyConfigForCurrentUser()` during initialization and utilize these settings for subsequent command and control operations.[^2]  |
| [[Native API\|T1106]] | Native API | [Kapeka](https://attack.mitre.org/software/S1190) utilizes WinAPI calls to gather victim system information.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kapeka](https://attack.mitre.org/software/S1190) utilizes AES-256 (CBC mode), XOR, and RSA-2048 encryption schemas for various configuration and other objects.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: KnuckleTouch


[^2]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^3]: [Microsoft KnuckleTouch 2024](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win64/KnuckleTouch.A!dha&threatId=-2147067254)


