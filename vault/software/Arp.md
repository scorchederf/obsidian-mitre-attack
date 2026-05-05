---
aliases: 
    - S0099
    
mitre-attack: https://attack.mitre.org/software/S0099
---

## S0099

[Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Arp](https://attack.mitre.org/software/S0099) can be used to display a host's ARP cache, which may include address resolutions for remote systems.[^4] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Arp](https://attack.mitre.org/software/S0099) can be used to display ARP configuration information on the host.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |
| [[BlackByte\|G1043]] | BlackByte |
| [[APT32\|G0050]] | APT32 |
| [[Orangeworm\|G0071]] | Orangeworm |



## References

[^1]: [Palo Alto ARP](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-reference/cortex-xdr-analytics-alert-reference/uncommon-arp-cache-listing-via-arp-exe.html)


[^2]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^3]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^4]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)


[^5]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^6]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


