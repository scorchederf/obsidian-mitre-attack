---
aliases: 
    - S9016
    
mitre-attack: https://attack.mitre.org/software/S9016
---

## S9016

[Caminho](https://attack.mitre.org/software/S9016) is a downloader that has been used by threat actors since at least 2025 to deliver various strains of malware such as XWorm.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Caminho](https://attack.mitre.org/software/S9016) can deobfuscate downloaded files prior to execution.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Caminho](https://attack.mitre.org/software/S9016) has launched and hollowed out MSBuild.exe to host malicious code.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Caminho](https://attack.mitre.org/software/S9016) can use junk code for obfuscation.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Caminho](https://attack.mitre.org/software/S9016) can use code flattening for payload obfuscation.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Caminho](https://attack.mitre.org/software/S9016) has the ability to download files onto compromised hosts.[^1]  |
| [[Native API\|T1106]] | Native API | [Caminho](https://attack.mitre.org/software/S9016) can use `System.Net.WebClient.downloadString()` for file download.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT-C-36\|G0099]] | APT-C-36 |



## References

[^1]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


[^2]: VMDetectLoader


