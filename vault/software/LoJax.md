---
aliases: 
    - S0397
    
mitre-attack: https://attack.mitre.org/software/S0397
---

## S0397

[LoJax](https://attack.mitre.org/software/S0397) is a UEFI rootkit used by [APT28](https://attack.mitre.org/groups/G0007) to persist remote access software on targeted systems.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [LoJax](https://attack.mitre.org/software/S0397) has modified the Registry key `‘HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute’` from `‘autocheck autochk *’` to `‘autocheck autoche *’`.[^2]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [LoJax](https://attack.mitre.org/software/S0397) has loaded an embedded NTFS DXE driver to be able to access and write to NTFS partitions.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [LoJax](https://attack.mitre.org/software/S0397) has modified the Registry key `‘HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute’` from `‘autocheck autochk *’` to `‘autocheck autoche *’` in order to execute its payload during Windows startup.[^2]  |
| [[System Firmware\|T1542.001]] | System Firmware | [LoJax](https://attack.mitre.org/software/S0397) is a UEFI BIOS rootkit deployed to persist remote access software on some targeted systems.[^2]   |
| [[Rootkit\|T1014]] | Rootkit | [LoJax](https://attack.mitre.org/software/S0397) is a UEFI BIOS rootkit deployed to persist remote access software on some targeted systems.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: LoJax


[^2]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


