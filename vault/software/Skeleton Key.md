---
aliases: 
    - S0007
    
mitre-attack: https://attack.mitre.org/software/S0007
---

## S0007

[Skeleton Key](https://attack.mitre.org/software/S0007) is malware used to inject false credentials into domain controllers with the intent of creating a backdoor password. [^2]  Functionality similar to [Skeleton Key](https://attack.mitre.org/software/S0007) is included as a module in [Mimikatz](https://attack.mitre.org/software/S0002).

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Controller Authentication\|T1556.001]] | Domain Controller Authentication | [Skeleton Key](https://attack.mitre.org/software/S0007) is used to patch an enterprise domain controller authentication process with a backdoor password. It allows adversaries to bypass the standard authentication system to use a defined password for all accounts authenticating to that domain controller.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Secureworks BRONZE FLEETWOOD Profile](https://www.secureworks.com/research/threat-profiles/bronze-fleetwood)


[^2]: [Dell Skeleton](https://www.secureworks.com/research/skeleton-key-malware-analysis)


