---
aliases: 
    - S9027
    
mitre-attack: https://attack.mitre.org/software/S9027
---

## S9027

[ANELLDR](https://attack.mitre.org/software/S9027), a loader that has been in use since at least 2018, was designed to decrypt and execute [UPPERCUT](https://attack.mitre.org/software/S0275) in memory. [ANELLDR](https://attack.mitre.org/software/S9027) can use anti-analysis techniques and is known to share code overlap with [HiddenFace](https://attack.mitre.org/software/S9023).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [ANELLDR](https://attack.mitre.org/software/S9027) can use the `ZwSetInformationThread` to enable debugger evasion.[^2] <br> |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ANELLDR](https://attack.mitre.org/software/S9027) can enumerate files in the current directory to search for encrypted payload files.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ANELLDR](https://attack.mitre.org/software/S9027) can decrypt encrypted payload data using AES-256-CBC and subsequently execute the payload in memory.[^2] <br> |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [ANELLDR](https://attack.mitre.org/software/S9027) can update its encryption key to AES-256-CBC and re-encrypt its payload, overwriting the original payload file with the newly encrypted data.[^2] <br> |
| [[DLL\|T1574.001]] | DLL | [ANELLDR](https://attack.mitre.org/software/S9027) can use DLL sideloading from a legitimate application to initiate execution. [^2]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [ANELLDR](https://attack.mitre.org/software/S9027) can call `ZwSetInformationThread` with the second argument set to `ThreadHideFromDebugger (0x11)` to evade being debugged.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [ANELLDR](https://attack.mitre.org/software/S9027) can use junk code for payload obfuscation.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ANELLDR](https://attack.mitre.org/software/S9027) code implements anti-analysis techniques including control flow flattening and Mixed Boolean Arithmetic (MBA).[^2]  |




## References

[^1]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


