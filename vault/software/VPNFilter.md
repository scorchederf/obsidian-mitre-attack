---
aliases: 
    - S1010
    
mitre-attack: https://attack.mitre.org/software/S1010
---

## S1010

[VPNFilter](https://attack.mitre.org/software/S1010) is a multi-stage, modular platform with versatile capabilities to support both intelligence-collection and destructive cyber attack operations. [VPNFilter](https://attack.mitre.org/software/S1010) modules such as its packet sniffer ('ps') can collect traffic that passes through an infected device, allowing the theft of website credentials and monitoring of Modbus SCADA protocols. [^4]  [^1]  [VPNFilter](https://attack.mitre.org/software/S1010) was assessed to be replaced by [Sandworm Team](https://attack.mitre.org/groups/G0034) with [Cyclops Blink](https://attack.mitre.org/software/S0687) starting in 2019.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [VPNFilter](https://attack.mitre.org/software/S1010) has the capability to wipe a portion of an infected device's firmware.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Carl Hurd March 2019](https://www.youtube.com/watch?v=yuZazP22rpI)


[^2]: [NCSC CISA Cyclops Blink Advisory February 2022](https://www.ncsc.gov.uk/news/joint-advisory-shows-new-sandworm-malware-cyclops-blink-replaces-vpnfilter)


[^3]: [VPNFilter Router](https://www.zdnet.com/article/fbi-to-all-router-users-reboot-now-to-neuter-russias-vpnfilter-malware/)


[^4]: [William Largent June 2018](https://blog.talosintelligence.com/2018/06/vpnfilter-update.html)


