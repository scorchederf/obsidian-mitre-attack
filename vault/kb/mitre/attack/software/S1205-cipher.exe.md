---
aliases: 
    - S1205
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1205-cipher.exe
---

## Description

[[kb/mitre/attack/software/S1205-cipher.exe\|cipher.exe]] is a native Microsoft utility that manages encryption of directories and files on NTFS (New Technology File System) partitions by using the Encrypting File System (EFS).[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1561.001-Disk_Content_Wipe\|T1561.001]] | Disk Content Wipe | [[kb/mitre/attack/software/S1205-cipher.exe\|cipher.exe]] can be used to overwrite deleted data in specified folders.[^1]  |





> [!info]- References
> [^1]: [Nearest Neighbor Volexity](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)

> [^2]: [cipher.exe](https://support.microsoft.com/en-us/topic/cipher-exe-security-tool-for-the-encrypting-file-system-56c85edd-85cf-ac07-f2f7-ca2d35dab7e4)


