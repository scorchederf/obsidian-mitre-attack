---
aliases: 
    - S0033
    
mitre-attack: https://attack.mitre.org/software/S0033
---

## S0033

[NetTraveler](https://attack.mitre.org/software/S0033) is malware that has been used in multiple cyber espionage campaigns for basic surveillance of victims. The earliest known samples have timestamps back to 2005, and the largest number of observed samples were created between 2010 and 2013. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [NetTraveler](https://attack.mitre.org/software/S0033) reports window names along with keylogger information to provide application context.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [NetTraveler](https://attack.mitre.org/software/S0033) contains a keylogger.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA459\|G0062]] | TA459 |



## References

[^1]: [Kaspersky NetTraveler](https://web.archive.org/web/20160326004042/http://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/kaspersky-the-net-traveler-part1-final.pdf)


[^2]: [Proofpoint TA459 April 2017](https://www.proofpoint.com/us/threat-insight/post/apt-targets-financial-analysts)


