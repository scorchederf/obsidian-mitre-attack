---
aliases: 
    - S1205
    
mitre-attack: https://attack.mitre.org/software/S1205
---

## S1205

[cipher.exe](https://attack.mitre.org/software/S1205) is a native Microsoft utility that manages encryption of directories and files on NTFS (New Technology File System) partitions by using the Encrypting File System (EFS).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [cipher.exe](https://attack.mitre.org/software/S1205) can be used to overwrite deleted data in specified folders.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Nearest Neighbor Volexity](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)


[^2]: [cipher.exe](https://support.microsoft.com/en-us/topic/cipher-exe-security-tool-for-the-encrypting-file-system-56c85edd-85cf-ac07-f2f7-ca2d35dab7e4)


