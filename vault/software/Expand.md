---
aliases: 
    - S0361
    
mitre-attack: https://attack.mitre.org/software/S0361
---

## S0361

[Expand](https://attack.mitre.org/software/S0361) is a Windows utility used to expand one or more compressed CAB files.[^3]  It has been used by [BBSRAT](https://attack.mitre.org/software/S0127) to decompress a CAB file into executable content.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Expand](https://attack.mitre.org/software/S0361) can be used to decompress a local or remote CAB file into an executable.[^3]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Expand](https://attack.mitre.org/software/S0361) can be used to download or upload a file over a network share.[^2]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Expand](https://attack.mitre.org/software/S0361) can be used to download or copy a file into an alternate data stream.[^2]  |




## References

[^1]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


[^2]: [LOLBAS Expand](https://lolbas-project.github.io/lolbas/Binaries/Expand/)


[^3]: [Microsoft Expand Utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)


