---
aliases: 
    - S0105
    
mitre-attack: https://attack.mitre.org/software/S0105
---

## S0105

[dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active Directory for information from a system within a domain. [^3]  It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Account\|T1087.002]] | Domain Account | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on user accounts within a domain.[^3] [^1]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on domain trusts with `dsquery * -filter "(objectClass=trustedDomain)" -attr *`.[^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on permission groups within a domain.[^3] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [dsquery](https://attack.mitre.org/software/S0105) has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^2]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^3]: [TechNet Dsquery](https://technet.microsoft.com/en-us/library/cc732952.aspx)


[^4]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


