---
aliases: 
    - S0597
    
mitre-attack: https://attack.mitre.org/software/S0597
---

## S0597

[GoldFinder](https://attack.mitre.org/software/S0597) is a custom HTTP tracer tool written in Go that logs the route a packet takes between a compromised network and a C2 server. It can be used to inform  threat actors of potential points of discovery or logging of their actions, including C2 related to other malware. [GoldFinder](https://attack.mitre.org/software/S0597) was discovered in early 2021 during an investigation into the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024) by [APT29](https://attack.mitre.org/groups/G0016).[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [GoldFinder](https://attack.mitre.org/software/S0597) performed HTTP GET requests to check internet connectivity and identify HTTP proxy servers and other redirectors that an HTTP request traveled through.[^4]  |
| [[Automated Collection\|T1119]] | Automated Collection | [GoldFinder](https://attack.mitre.org/software/S0597) logged and stored information related to the route or hops a packet took from a compromised machine to a hardcoded C2 server, including the target C2 URL, HTTP response/status code, HTTP response headers and values, and data received from the C2 node.[^4]    |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GoldFinder](https://attack.mitre.org/software/S0597) has used HTTP for C2.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: GoldFinder


[^2]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^3]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^4]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^5]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


