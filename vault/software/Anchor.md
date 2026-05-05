---
aliases: 
    - S0504
    
mitre-attack: https://attack.mitre.org/software/S0504
---

## S0504

[Anchor](https://attack.mitre.org/software/S0504) is one of a family of backdoor malware that has been used in conjunction with [TrickBot](https://attack.mitre.org/software/S0266) on selected high profile targets since at least 2018.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Anchor](https://attack.mitre.org/software/S0504) has used ICMP in C2 communications.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Anchor](https://attack.mitre.org/software/S0504) has used cmd.exe to run its self deletion routine.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Anchor](https://attack.mitre.org/software/S0504) can download additional payloads.[^1] [^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Anchor](https://attack.mitre.org/software/S0504) can terminate itself if specific execution flags are not present.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Anchor](https://attack.mitre.org/software/S0504) can determine the hostname and linux version on a compromised host.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Anchor](https://attack.mitre.org/software/S0504) can create a scheduled task for persistence.[^1]  |
| [[Cron\|T1053.003]] | Cron | [Anchor](https://attack.mitre.org/software/S0504) can install itself as a cron job.[^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Anchor](https://attack.mitre.org/software/S0504) can execute payloads via shell scripting.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Anchor](https://attack.mitre.org/software/S0504) has used HTTP and HTTPS in C2 communications.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Anchor](https://attack.mitre.org/software/S0504) has been signed with valid certificates to evade detection by security tools.[^1]  |
| [[DNS\|T1071.004]] | DNS | Variants of [Anchor](https://attack.mitre.org/software/S0504) can use DNS tunneling to communicate with C2.[^1] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Anchor](https://attack.mitre.org/software/S0504) can establish persistence by creating a service.[^1] 	 |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Anchor](https://attack.mitre.org/software/S0504) has obfuscated code with stack strings and string encryption.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Anchor](https://attack.mitre.org/software/S0504) can determine the public IP and location of a compromised host.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Anchor](https://attack.mitre.org/software/S0504) can self delete its dropper after the malware is successfully deployed.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Anchor](https://attack.mitre.org/software/S0504) has come with a packed payload.[^1]  |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [Anchor](https://attack.mitre.org/software/S0504) has used NTFS to hide files.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Anchor](https://attack.mitre.org/software/S0504) can create and execute services to load its payload.[^1] [^2]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Anchor](https://attack.mitre.org/software/S0504) can support windows execution via SMB shares.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Anchor](https://attack.mitre.org/software/S0504) can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^2]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)


[^3]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^4]: Anchor_DNS


