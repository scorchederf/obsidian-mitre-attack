---
aliases: 
    - S0508
    
mitre-attack: https://attack.mitre.org/software/S0508
---

## S0508

[ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.[^3] [^12] [^9] [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [ngrok](https://attack.mitre.org/software/S0508) can be used to proxy connections to machines located behind NAT or firewalls.[^7] [^3]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to configure servers for data exfiltration.[^7]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [ngrok](https://attack.mitre.org/software/S0508) can provide DGA for C2 servers through the use of random URL strings that change every 12 hours.[^3]  |
| [[Web Service\|T1102]] | Web Service | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to proxy C2 connections to ngrok service subdomains.[^3]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [ngrok](https://attack.mitre.org/software/S0508) can tunnel RDP and other services securely over internet connections.[^12] [^9] [^7] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[Fox Kitten\|G0117]] | Fox Kitten |



## References

[^1]: [CrowdStrike PIONEER KITTEN August 2020](https://www.crowdstrike.com/blog/who-is-pioneer-kitten/)


[^2]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^3]: [Zdnet Ngrok September 2018](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)


[^4]: [Trend Micro Ngrok September 2020](https://www.trendmicro.com/en_us/research/20/i/analysis-of-a-convoluted-attack-chain-involving-ngrok.html)


[^5]: [Trend Micro Earth Simnavaz October 2024](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)


[^6]: [CrowdStrike Scattered Spider JUL 2025](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)


[^7]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)


[^8]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^9]: [Cyware Ngrok May 2019](https://cyware.com/news/cyber-attackers-leverage-tunneling-service-to-drop-lokibot-onto-victims-systems-6f610e44)


[^10]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


[^11]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^12]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


