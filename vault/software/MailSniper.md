---
aliases: 
    - S0413
    
mitre-attack: https://attack.mitre.org/software/S0413
---

## S0413

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [MailSniper](https://attack.mitre.org/software/S0413) can be used for searching through email in Exchange and Office 365 environments.[^1]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [MailSniper](https://attack.mitre.org/software/S0413) can be used for password spraying against Exchange and Office 365.[^1]  |
| [[Email Account\|T1087.003]] | Email Account | [MailSniper](https://attack.mitre.org/software/S0413) can be used to obtain account names from Exchange and Office 365 using the `Get-GlobalAddressList` cmdlet.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leafminer\|G0077]] | Leafminer |



## References

[^1]: [GitHub MailSniper](https://github.com/dafthack/MailSniper)


[^2]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^3]: [Black Hills Attacking Exchange MailSniper, 2016](https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/)


