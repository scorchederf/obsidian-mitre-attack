---
aliases: 
    - S0218
    
mitre-attack: https://attack.mitre.org/software/S0218
---

## S0218

[SLOWDRIFT](https://attack.mitre.org/software/S0218) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) against academic and strategic victims in South Korea. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SLOWDRIFT](https://attack.mitre.org/software/S0218) collects and sends system information to its C2.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [SLOWDRIFT](https://attack.mitre.org/software/S0218) uses cloud based services for C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SLOWDRIFT](https://attack.mitre.org/software/S0218) downloads additional payloads.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^2]: SLOWDRIFT


