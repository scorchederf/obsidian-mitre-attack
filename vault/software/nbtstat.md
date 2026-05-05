---
aliases: 
    - S0102
    
mitre-attack: https://attack.mitre.org/software/S0102
---

## S0102

[nbtstat](https://attack.mitre.org/software/S0102) is a utility used to troubleshoot NetBIOS name resolution. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover local NetBIOS domain names. |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover current NetBIOS sessions. |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^2]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^3]: [TechNet Nbtstat](https://technet.microsoft.com/en-us/library/cc940106.aspx)


