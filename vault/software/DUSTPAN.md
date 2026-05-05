---
aliases: 
    - S1158
    
mitre-attack: https://attack.mitre.org/software/S1158
---

## S1158

[DUSTPAN](https://attack.mitre.org/software/S1158) is an in-memory dropper written in C/C++ used by [APT41](https://attack.mitre.org/groups/G0096) since 2021 that decrypts and executes an embedded payload.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [DUSTPAN](https://attack.mitre.org/software/S1158) is often disguised as a legitimate Windows binary such as `w3wp.exe` or `conn.exe`.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DUSTPAN](https://attack.mitre.org/software/S1158) decrypts an embedded payload.[^2] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DUSTPAN](https://attack.mitre.org/software/S1158) decodes and decrypts embedded payloads.[^2]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [DUSTPAN](https://attack.mitre.org/software/S1158) can inject its decrypted payload into another process.[^2]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [DUSTPAN](https://attack.mitre.org/software/S1158) decrypts and executes an embedded payload.[^2] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [DUSTPAN](https://attack.mitre.org/software/S1158) can persist as a Windows Service in operations.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [Google Cloud APT41 2022](https://cloud.google.com/blog/topics/threat-intelligence/apt41-us-state-governments)


[^2]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


