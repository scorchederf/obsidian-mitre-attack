---
aliases: 
    - S0372
    
mitre-attack: https://attack.mitre.org/software/S0372
---

## S0372

[LockerGoga](https://attack.mitre.org/software/S0372) is ransomware that was first reported in January 2019, and has been tied to various attacks on European companies, including industrial and manufacturing firms.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [LockerGoga](https://attack.mitre.org/software/S0372) has been observed deleting its original launcher after execution.[^3]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [LockerGoga](https://attack.mitre.org/software/S0372) has encrypted files, including core Windows OS files, using RSA-OAEP MGF1 and then demanded Bitcoin be paid for the decryption key.[^3] [^2] [^4]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [LockerGoga](https://attack.mitre.org/software/S0372) has been observed shutting down infected systems.[^4]  |
| [[Account Access Removal\|T1531]] | Account Access Removal | [LockerGoga](https://attack.mitre.org/software/S0372) has been observed changing account passwords and logging off current users.[^3] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [LockerGoga](https://attack.mitre.org/software/S0372) installation has been immediately preceded by a "task kill" command in order to disable anti-virus.[^4]  |
| [[Code Signing\|T1553.002]] | Code Signing | [LockerGoga](https://attack.mitre.org/software/S0372) has been signed with stolen certificates in order to make it look more legitimate.[^4]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [LockerGoga](https://attack.mitre.org/software/S0372) has been observed moving around the victim network via SMB, indicating the actors behind this ransomware are manually copying files form computer to computer instead of self-propagating.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN6\|G0037]] | FIN6 |



## References

[^1]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^2]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)


[^3]: [CarbonBlack LockerGoga 2019](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)


[^4]: [Wired Lockergoga 2019](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)


