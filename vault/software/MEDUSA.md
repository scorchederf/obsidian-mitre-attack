---
aliases: 
    - S1220
    
mitre-attack: https://attack.mitre.org/software/S1220
---

## S1220

[MEDUSA](https://attack.mitre.org/software/S1220) is an open-source rootkit that is capable of dynamic linker hijacking, command execution, and logging credentials.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[SSH Hijacking\|T1563.001]] | SSH Hijacking | [MEDUSA](https://attack.mitre.org/software/S1220) can be configured to capture SSH credentials via SSH hijacking.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [MEDUSA](https://attack.mitre.org/software/S1220) can XOR encrypt configuration strings.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [MEDUSA](https://attack.mitre.org/software/S1220) is a rootkit with command execution and credential logging capabilities.[^1] <br> |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [MEDUSA](https://attack.mitre.org/software/S1220) can execute code through dynamic linker hijacking of  the `LD_PRELOAD` library.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


