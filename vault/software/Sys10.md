---
aliases: 
    - S0060
    
mitre-attack: https://attack.mitre.org/software/S0060
---

## S0060

[Sys10](https://attack.mitre.org/software/S0060) is a backdoor that was used throughout 2013 by [Naikon](https://attack.mitre.org/groups/G0019). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Sys10](https://attack.mitre.org/software/S0060) uses an XOR 0x1 loop to encrypt its C2 domain.[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Sys10](https://attack.mitre.org/software/S0060) collects the group name of the logged-in user and sends it to the C2.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Sys10](https://attack.mitre.org/software/S0060) collects the computer name, OS versioning information, and OS install date and sends the information to the C2.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Sys10](https://attack.mitre.org/software/S0060) collects the local IP address of the victim and sends it to the C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sys10](https://attack.mitre.org/software/S0060) uses HTTP for C2.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Sys10](https://attack.mitre.org/software/S0060) collects the account name of the logged-in user and sends it to the C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


