---
aliases: 
    - S0361
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0361-Expand
---

## Description

[[kb/mitre/attack/software/S0361-Expand\|Expand]] is a Windows utility used to expand one or more compressed CAB files.[^3]  It has been used by BBSRAT to decompress a CAB file into executable content.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information\|T1140]] | Deobfuscate／Decode Files or Information | [[kb/mitre/attack/software/S0361-Expand\|Expand]] can be used to decompress a local or remote CAB file into an executable.[^3]  |
| [[kb/mitre/attack/techniques/T1564.004-NTFS_File_Attributes\|T1564.004]] | NTFS File Attributes | [[kb/mitre/attack/software/S0361-Expand\|Expand]] can be used to download or copy a file into an alternate data stream.[^2]  |
| [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0361-Expand\|Expand]] can be used to download or upload a file over a network share.[^2]  |





> [!info]- References
> [^1]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)

> [^2]: [LOLBAS Expand](https://lolbas-project.github.io/lolbas/Binaries/Expand/)

> [^3]: [Microsoft Expand Utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)


