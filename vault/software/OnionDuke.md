---
aliases: 
    - S0052
    
mitre-attack: https://attack.mitre.org/software/S0052
---

## S0052

[OnionDuke](https://attack.mitre.org/software/S0052) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2013 to 2015. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [OnionDuke](https://attack.mitre.org/software/S0052) steals credentials from its victims.[^3]  |
| [[Endpoint Denial of Service\|T1499]] | Endpoint Denial of Service | [OnionDuke](https://attack.mitre.org/software/S0052) has the capability to use a Denial of Service module.[^2]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [OnionDuke](https://attack.mitre.org/software/S0052) uses Twitter as a backup C2.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OnionDuke](https://attack.mitre.org/software/S0052) uses HTTP and HTTPS for C2.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [OnionDuke](https://attack.mitre.org/software/S0052) can use a custom decryption algorithm to decrypt strings.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^3]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


