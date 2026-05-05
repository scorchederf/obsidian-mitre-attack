---
aliases: 
    - S0043
    
mitre-attack: https://attack.mitre.org/software/S0043
---

## S0043

[BUBBLEWRAP](https://attack.mitre.org/software/S0043) is a full-featured, second-stage backdoor used by the [admin@338](https://attack.mitre.org/groups/G0018) group. It is set to run when the system boots and includes functionality to check, upload, and register plug-ins that can further enhance its capabilities. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BUBBLEWRAP](https://attack.mitre.org/software/S0043) can communicate using HTTP or HTTPS.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [BUBBLEWRAP](https://attack.mitre.org/software/S0043) can communicate using SOCKS.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BUBBLEWRAP](https://attack.mitre.org/software/S0043) collects system information, including the operating system version and hostname.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[admin@338\|G0018]] | admin@338 |



## References

[^1]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


