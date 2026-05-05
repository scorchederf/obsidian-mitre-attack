---
aliases: 
    - T1572
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1572-Protocol_Tunneling
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. <br><br>There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.[^7] [^6]  <br><br>[[kb/mitre/attack/techniques/T1572-Protocol_Tunneling\|Protocol Tunneling]] may also be abused by adversaries during [[kb/mitre/attack/techniques/T1568-Dynamic_Resolution\|Dynamic Resolution]]. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.[^3]  <br><br>Adversaries may also leverage [[kb/mitre/attack/techniques/T1572-Protocol_Tunneling\|Protocol Tunneling]] in conjunction with [[kb/mitre/attack/techniques/T1090-Proxy\|Proxy]] and/or [[kb/mitre/attack/techniques/T1001.003-Protocol_or_Service_Impersonation\|Protocol or Service Impersonation]] to further conceal C2 communications and infrastructure. 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can tunnel RDP and other services securely over internet connections.[^12] [^11] [^5] [^8]  |
| [[kb/mitre/attack/software/S0699-Mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] can use SOCKS proxies to tunnel traffic through another protocol.[^10]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can use DNS over HTTPS for C2.[^4] [^1]  |
| [[kb/mitre/attack/software/S1144-FRP\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-FRP\|FRP]] can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.[^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level.  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Consider filtering network traffic to untrusted or known bad domains and resources.  |






> [!info]- References
> [^1]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)

> [^2]: [FRP GitHub](https://github.com/fatedier/frp)

> [^3]: [BleepingComp Godlua JUL19](https://www.bleepingcomputer.com/news/security/new-godlua-malware-evades-traffic-monitoring-via-dns-over-https/)

> [^4]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^5]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)

> [^6]: [Sygnia Abyss Locker 2025](https://www.sygnia.co/blog/abyss-locker-ransomware-attack-analysis/)

> [^7]: [SSH Tunneling](https://www.ssh.com/ssh/tunneling)

> [^8]: [Trend Micro Ngrok September 2020](https://www.trendmicro.com/en_us/research/20/i/analysis-of-a-convoluted-attack-chain-involving-ngrok.html)

> [^9]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^10]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^11]: [Cyware Ngrok May 2019](https://cyware.com/news/cyber-attackers-leverage-tunneling-service-to-drop-lokibot-onto-victims-systems-6f610e44)

> [^12]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


