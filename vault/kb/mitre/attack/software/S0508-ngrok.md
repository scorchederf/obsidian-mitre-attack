---
aliases: 
    - S0508
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0508-ngrok
---

## Description

[[kb/mitre/attack/software/S0508-ngrok\|ngrok]] is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.[^4] [^6] [^5] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can be used to proxy connections to machines located behind NAT or firewalls.[^2] [^4]  |
| [[kb/mitre/attack/techniques/T1102-Web_Service\|T1102]] | Web Service | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been used by threat actors to proxy C2 connections to ngrok service subdomains.[^4]  |
| [[kb/mitre/attack/techniques/T1567-Exfiltration_Over_Web_Service\|T1567]] | Exfiltration Over Web Service | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been used by threat actors to configure servers for data exfiltration.[^2]  |
| [[kb/mitre/attack/techniques/T1568.002-Domain_Generation_Algorithms\|T1568.002]] | Domain Generation Algorithms | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can provide DGA for C2 servers through the use of random URL strings that change every 12 hours.[^4]  |
| [[kb/mitre/attack/techniques/T1572-Protocol_Tunneling\|T1572]] | Protocol Tunneling | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can tunnel RDP and other services securely over internet connections.[^6] [^5] [^2] [^3]  |





> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)

> [^3]: [Trend Micro Ngrok September 2020](https://www.trendmicro.com/en_us/research/20/i/analysis-of-a-convoluted-attack-chain-involving-ngrok.html)

> [^4]: [Zdnet Ngrok September 2018](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)

> [^5]: [Cyware Ngrok May 2019](https://cyware.com/news/cyber-attackers-leverage-tunneling-service-to-drop-lokibot-onto-victims-systems-6f610e44)

> [^6]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


