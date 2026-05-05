---
aliases: 
    - S0183
    
mitre-attack: https://attack.mitre.org/software/S0183
---

## S0183

[Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Tor](https://attack.mitre.org/software/S0183) encapsulates traffic in multiple layers of encryption, using TLS by default.[^8]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | Traffic traversing the [Tor](https://attack.mitre.org/software/S0183) network will be forwarded to multiple nodes before exiting the [Tor](https://attack.mitre.org/software/S0183) network and continuing on to its intended destination.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[APT28\|G0007]] | APT28 |
| [[APT29\|G0016]] | APT29 |
| [[Water Galura\|G1050]] | Water Galura |
| [[Leviathan\|G0065]] | Leviathan |



## References

[^1]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^2]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^3]: Tor


[^4]: [BushidoToken Qilin RaaS JUN 2024](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)


[^5]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)


[^6]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^7]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^8]: [Dingledine Tor The Second-Generation Onion Router](http://www.dtic.mil/dtic/tr/fulltext/u2/a465464.pdf)


[^9]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)


[^10]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^11]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


