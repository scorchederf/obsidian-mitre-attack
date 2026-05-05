---
aliases: 
    - S0027
    
mitre-attack: https://attack.mitre.org/software/S0027
---

## S0027

[Zeroaccess](https://attack.mitre.org/software/S0027) is a kernel-mode [Rootkit](https://attack.mitre.org/techniques/T1014) that attempts to add victims to the ZeroAccess botnet, often for monetary gain. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Rootkit\|T1014]] | Rootkit | [Zeroaccess](https://attack.mitre.org/software/S0027) is a kernel-mode rootkit.[^1]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | Some variants of the [Zeroaccess](https://attack.mitre.org/software/S0027) Trojan have been known to store data in Extended Attributes.[^2]  |




## References

[^1]: [Sophos ZeroAccess](https://sophosnews.files.wordpress.com/2012/04/zeroaccess2.pdf)


[^2]: [Ciubotariu 2014](http://www.symantec.com/connect/blogs/trojanzeroaccessc-hidden-ntfs-ea)


