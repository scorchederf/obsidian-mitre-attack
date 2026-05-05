---
aliases: 
    - S1221
    
mitre-attack: https://attack.mitre.org/software/S1221
---

## S1221

[MOPSLED](https://attack.mitre.org/software/S1221) is a shellcode-based modular backdoor that has been used by China-nexus cyber espionage actors including [UNC3886](https://attack.mitre.org/groups/G1048) and [APT41](https://attack.mitre.org/groups/G0096).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MOPSLED](https://attack.mitre.org/software/S1221) can communicate to C2 nodes over HTTP.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [MOPSLED](https://attack.mitre.org/software/S1221) can encrypt configuration files with a custom ChaCha20 algorithm.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MOPSLED](https://attack.mitre.org/software/S1221) can decrypt obfuscated configuration files.[^1]  |
| [[Web Service\|T1102]] | Web Service | [MOPSLED](https://attack.mitre.org/software/S1221) can use third-party web services such as GitHub and Google Drive for C2.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver |  [MOPSLED](https://attack.mitre.org/software/S1221) has the ability to retrieve a C2 address from a dead drop URL.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [MOPSLED](https://attack.mitre.org/software/S1221) can use a custom binary protocol over TCP for C2 communication.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


