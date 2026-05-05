---
aliases: 
    - S0638
    
mitre-attack: https://attack.mitre.org/software/S0638
---

## S0638

[Babuk](https://attack.mitre.org/software/S0638) is a Ransomware-as-a-service (RaaS) malware that has been used since at least 2021. The operators of [Babuk](https://attack.mitre.org/software/S0638) employ a "Big Game Hunting" approach to targeting major enterprises and operate a leak site to post stolen data as part of their extortion scheme.[^4] [^5] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Babuk](https://attack.mitre.org/software/S0638) can stop anti-virus services on a compromised host.[^4]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Babuk](https://attack.mitre.org/software/S0638) can use “WNetOpenEnumW” and “WNetEnumResourceW” to enumerate files in network resources for encryption.[^5]  |
| [[Native API\|T1106]] | Native API | [Babuk](https://attack.mitre.org/software/S0638) can use multiple Windows API calls for actions on compromised hosts including discovery and execution.[^4] [^5] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Babuk](https://attack.mitre.org/software/S0638) has the ability to unpack itself into memory using XOR.[^4] [^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Babuk](https://attack.mitre.org/software/S0638) can use ChaCha8 and ECDH to encrypt data.[^4] [^5] [^2] [^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | Versions of [Babuk](https://attack.mitre.org/software/S0638) have been packed.[^4] [^5] [^2]  |
| [[Service Stop\|T1489]] | Service Stop | [Babuk](https://attack.mitre.org/software/S0638) can stop specific services related to backups.[^4] [^5] [^6]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Babuk](https://attack.mitre.org/software/S0638) has the ability to delete shadow volumes using `vssadmin.exe delete shadows /all /quiet`.[^4] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Babuk](https://attack.mitre.org/software/S0638) has the ability to use the command line to control execution on compromised hosts.[^4] [^5]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Babuk](https://attack.mitre.org/software/S0638) has the ability to enumerate network shares.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Babuk](https://attack.mitre.org/software/S0638) can enumerate all services running on a compromised host.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Babuk](https://attack.mitre.org/software/S0638) has the ability to check running processes on a targeted system.[^4] [^5] [^6]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Babuk](https://attack.mitre.org/software/S0638) can enumerate disk volumes, get disk information, and query service status.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Babuk](https://attack.mitre.org/software/S0638) has the ability to enumerate files on a targeted system.[^5] [^6]  |




## References

[^1]: Babyk


[^2]: [Medium Babuk February 2021](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)


[^3]: Vasa Locker


[^4]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)


[^5]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)


[^6]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^7]: [CyberScoop Babuk February 2021](https://www.cyberscoop.com/babuk-ransomware-serco-attack/)


