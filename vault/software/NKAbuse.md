---
aliases: 
    - S1107
    
mitre-attack: https://attack.mitre.org/software/S1107
---

## S1107

[NKAbuse](https://attack.mitre.org/software/S1107) is a Go-based, multi-platform malware abusing NKN (New Kind of Network) technology for data exchange between peers, functioning as a potent implant, and equipped with both flooder and backdoor capabilities.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [NKAbuse](https://attack.mitre.org/software/S1107) is initially installed and executed through an initial shell script.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [NKAbuse](https://attack.mitre.org/software/S1107) will check victim systems to ensure only one copy of the malware is running.[^2]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [NKAbuse](https://attack.mitre.org/software/S1107) utilizes external services such as `ifconfig.me` to identify the victim machine's IP address.[^2]  |
| [[Network Denial of Service\|T1498]] | Network Denial of Service | [NKAbuse](https://attack.mitre.org/software/S1107) enables multiple types of network denial of service capabilities across several protocols post-installation.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NKAbuse](https://attack.mitre.org/software/S1107) conducts multiple system checks and includes these in subsequent "heartbeat" messages to the malware's command and control server.[^2]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [NKAbuse](https://attack.mitre.org/software/S1107) has abused the NKN public blockchain protocol for its C2 communications.[^1] [^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [NKAbuse](https://attack.mitre.org/software/S1107) can take screenshots of the victim machine.[^2]  |
| [[Cron\|T1053.003]] | Cron | [NKAbuse](https://attack.mitre.org/software/S1107) uses a Cron job to establish persistence when infecting Linux hosts.[^2]  |




## References

[^1]: [NKAbuse BC](https://www.bleepingcomputer.com/news/security/new-nkabuse-malware-abuses-nkn-blockchain-for-stealthy-comms/#google_vignette)


[^2]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)


