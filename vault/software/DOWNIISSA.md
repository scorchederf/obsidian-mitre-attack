---
aliases: 
    - S9021
    
mitre-attack: https://attack.mitre.org/software/S9021
---

## S9021

[DOWNIISSA](https://attack.mitre.org/software/S9021) is a shellcode downloader that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) since at least 2022 to deploy payloads, including the [LODEINFO](https://attack.mitre.org/software/S9020) backdoor.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DOWNIISSA](https://attack.mitre.org/software/S9021) code is base64 encoded and XOR encrypted.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DOWNIISSA](https://attack.mitre.org/software/S9021) can download files to the compromised host.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [DOWNIISSA](https://attack.mitre.org/software/S9021) can delete files after download.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DOWNIISSA](https://attack.mitre.org/software/S9021) can decode strings prior to execution.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [DOWNIISSA](https://attack.mitre.org/software/S9021) can create an instance of msiexec.exe and inject [LODEINFO](https://attack.mitre.org/software/S9020) shellcode into the memory of the process.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [DOWNIISSA](https://attack.mitre.org/software/S9021) can inject shellcode directly into process memory including WINWORD.exe and msiexec.exe.[^1]  |
| [[Native API\|T1106]] | Native API | [DOWNIISSA](https://attack.mitre.org/software/S9021) can use the `URLDownloadToFileA()` API to download from remote resources.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


