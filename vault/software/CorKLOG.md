---
aliases: 
    - S1235
    
mitre-attack: https://attack.mitre.org/software/S1235
---

## S1235

[CorKLOG](https://attack.mitre.org/software/S1235) is a keylogger known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. [CorKLOG](https://attack.mitre.org/software/S1235) is delivered through a RAR archive (e.g., src.rar), which contains two files: an executable (lcommute.exe) and the [CorKLOG](https://attack.mitre.org/software/S1235) DLL (mscorsvc.dll).  [CorKLOG](https://attack.mitre.org/software/S1235) has established persistence on the system by creating services or with scheduled tasks.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Code Signing\|T1553.002]] | Code Signing | [CorKLOG](https://attack.mitre.org/software/S1235) has used legitimate signed binaries such as lcommute.exe for follow-on execution of malicious DLLs through DLL side-loading.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [CorKLOG](https://attack.mitre.org/software/S1235) has captured keystrokes.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CorKLOG](https://attack.mitre.org/software/S1235) has decoded XOR encrypted strings.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [CorKLOG](https://attack.mitre.org/software/S1235) has created a service to establish persistence.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [CorKLOG](https://attack.mitre.org/software/S1235) has encrypted collected contents using RC4.[^1]   [CorKLOG](https://attack.mitre.org/software/S1235) has also utilized XOR encrypted strings.[^1]  |
| [[DLL\|T1574.001]] | DLL | [CorKLOG](https://attack.mitre.org/software/S1235) has leveraged legitimate binaries to conduct DLL side-loading.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [CorKLOG](https://attack.mitre.org/software/S1235) has achieved persistence through the creation of a scheduled task named TableInputServices by using the command `schtasks /create /tn TabletlnputServices /tr /sc minute /mo 10 /f`.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [CorKLOG](https://attack.mitre.org/software/S1235) has stored the captured data in an encrypted file using a 48-character RC4 key.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


