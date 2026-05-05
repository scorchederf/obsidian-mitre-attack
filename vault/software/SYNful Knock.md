---
aliases: 
    - S0519
    
mitre-attack: https://attack.mitre.org/software/S0519
---

## S0519

[SYNful Knock](https://attack.mitre.org/software/S0519) is a stealthy modification of the operating system of network devices that can be used to maintain persistence within a victim's network and provide new capabilities to the adversary.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Patch System Image\|T1601.001]] | Patch System Image | [SYNful Knock](https://attack.mitre.org/software/S0519) is malware that is inserted into a network device by patching the operating system image.[^1] [^2]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [SYNful Knock](https://attack.mitre.org/software/S0519) can be sent instructions via special packets to change its functionality. Code for new functionality can be included in these messages.[^1]  |
| [[Network Device Authentication\|T1556.004]] | Network Device Authentication | [SYNful Knock](https://attack.mitre.org/software/S0519) has the capability to add its own custom backdoor password when it modifies the operating system of the affected network device.[^1]  |




## References

[^1]: [Mandiant - Synful Knock](https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/)


[^2]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)


