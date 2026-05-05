---
aliases: 
    - S1232
    
mitre-attack: https://attack.mitre.org/software/S1232
---

## S1232

[SplatDropper](https://attack.mitre.org/software/S1232) is a loader that utilizes native windows API to deliver its payload to the victim environment.  [SplatDropper](https://attack.mitre.org/software/S1232) has been delivered through RAR archives and used legitimate executable for DLL side-loading.  [SplatDropper](https://attack.mitre.org/software/S1232) is known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [SplatDropper](https://attack.mitre.org/software/S1232) has utilized hashed Native Windows API calls.[^1]  |
| [[DLL\|T1574.001]] | DLL | [SplatDropper](https://attack.mitre.org/software/S1232) has leveraged legitimate binaries to conduct DLL side-loading.[^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [SplatDropper](https://attack.mitre.org/software/S1232) has leveraged hashed Windows API calls using a seed value of "131313".[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SplatDropper](https://attack.mitre.org/software/S1232) has also utilized XOR encrypted payload.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [SplatDropper](https://attack.mitre.org/software/S1232) has used legitimate signed binaries such as BugSplatHD64.exe for follow-on execution of malicious DLLs through DLL side-loading.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SplatDropper](https://attack.mitre.org/software/S1232) has decoded XOR encrypted payload.[^1]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [SplatDropper](https://attack.mitre.org/software/S1232) has deleted its malicious payload and removed its own created service to avoid leaving traces of its presence on victim devices.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [SplatDropper](https://attack.mitre.org/software/S1232) has created a service to execute a payload.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


