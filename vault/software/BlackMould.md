---
aliases: 
    - S0564
    
mitre-attack: https://attack.mitre.org/software/S0564
---

## S0564

[BlackMould](https://attack.mitre.org/software/S0564) is a web shell based on [China Chopper](https://attack.mitre.org/software/S0020) for servers running Microsoft IIS. First reported in December 2019, it has been used in malicious campaigns by [GALLIUM](https://attack.mitre.org/groups/G0093) against telecommunication providers.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [BlackMould](https://attack.mitre.org/software/S0564) can enumerate local drives on a compromised host.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BlackMould](https://attack.mitre.org/software/S0564) can run cmd.exe with parameters.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BlackMould](https://attack.mitre.org/software/S0564) can send commands to C2 in the body of HTTP POST requests.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BlackMould](https://attack.mitre.org/software/S0564) can copy files on a compromised host.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BlackMould](https://attack.mitre.org/software/S0564) has the ability to find files on the targeted system.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BlackMould](https://attack.mitre.org/software/S0564) has the ability to download files to the victim's machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GALLIUM\|G0093]] | GALLIUM |



## References

[^1]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


