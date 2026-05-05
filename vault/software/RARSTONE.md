---
aliases: 
    - S0055
    
mitre-attack: https://attack.mitre.org/software/S0055
---

## S0055

[RARSTONE](https://attack.mitre.org/software/S0055) is malware used by the [Naikon](https://attack.mitre.org/groups/G0019) group that has some characteristics similar to [PlugX](https://attack.mitre.org/software/S0013). [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | After decrypting itself in memory, [RARSTONE](https://attack.mitre.org/software/S0055) downloads a DLL file from its C2 server and loads it in the memory space of a hidden Internet Explorer process. This “downloaded” file is actually not dropped onto the system.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [RARSTONE](https://attack.mitre.org/software/S0055) uses SSL to encrypt its communication with its C2 server.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RARSTONE](https://attack.mitre.org/software/S0055) obtains installer properties from Uninstall Registry Key entries to obtain information about installed applications and how to uninstall certain applications.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RARSTONE](https://attack.mitre.org/software/S0055) downloads its backdoor component from a C2 server and loads it directly into memory.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [CameraShy](http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf)


[^2]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^3]: [Camba RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/bkdr_rarstone-new-rat-to-watch-out-for/)


[^4]: [Aquino RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/rarstone-found-in-targeted-attacks/)


