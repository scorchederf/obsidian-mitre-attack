---
aliases: 
    - Lotus Blossom
    - DRAGONFISH
    - Spring Dragon
    - RADIUM
    - Raspberry Typhoon
    - Bilbug
    - Thrip
mitre-attack: https://attack.mitre.org/groups/G0030
---

## G0030

[Lotus Blossom](https://attack.mitre.org/groups/G0030) is a long-standing threat group largely targeting various entities in Asia since at least 2009. In addition to government and related targets, [Lotus Blossom](https://attack.mitre.org/groups/G0030) has also targeted entities such as digital certificate issuers.[^13] [^11] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `ipconfig` and `netstat` to gather network information on compromised hosts.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has configured tools such as [Sagerunex](https://attack.mitre.org/software/S1210) to run as Windows services.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used `net` commands and tools such as [AdFind](https://attack.mitre.org/software/S0552) to profile domain accounts associated with victim machines and make Active Directory queries.[^3] [^11]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has locally staged compressed and archived data for follow-on exfiltration.[^3]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has retrieved process tokens for processes to adjust the privileges of the launch process or other items.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `net` to profile local system users.[^3]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly available tools such as the Venom proxy tool to proxy traffic out of victim environments.[^3]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly-available tools to steal cookies from browsers such as Chrome.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has installed tools such as [Sagerunex](https://attack.mitre.org/software/S1210) by writing them to the Windows registry.[^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `netstat` to identify system network connections.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used WMI to enable lateral movement.[^3]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used tools such as [AdFind](https://attack.mitre.org/software/S0552) to make Active Directory queries.[^11]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has performed checks to determine if a victim machine is able to access the Internet.[^3]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used tools such as the publicly available HTran tool for proxying traffic in victim environments.[^3]  |
| [[Tool\|T1588.002]] | Tool | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used publicly-available tools such as a Python-based cookie stealer for Chrome browsers, [Impacket](https://attack.mitre.org/software/S0357), and the Venom proxy tool.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Ping](https://attack.mitre.org/software/S0097) to identify remote systems.[^11]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `dir` to examine the local filesystem of victim machines.[^3]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used custom tools to compress and archive data on victim systems.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used WinRAR for compressing data in RAR format.[^3] [^11]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used port scanners to enumerate services on remote hosts.[^11]  |
| [[Query Registry\|T1012]] | Query Registry | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has run commands such as `reg query HKLM\SYSTEM\CurrentControlSet\Services\[service name]\Parameters` to verify if installed implants are running as a service.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [certutil](https://attack.mitre.org/software/S0160) during operations.[^11]  |
| [[Impacket\|S0357]] | Impacket | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Impacket](https://attack.mitre.org/software/S0357) during operations.[^3]  |
| [[NBTscan\|S0590]] | NBTscan | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [NBTscan](https://attack.mitre.org/software/S0590) during operations.[^11]  |
| [[Ping\|S0097]] | Ping | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Ping](https://attack.mitre.org/software/S0097) to verify connectivity to remote hosts.[^11]  |
| [[AdFind\|S0552]] | AdFind | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [AdFind](https://attack.mitre.org/software/S0552) to query Active Directory in victim environments.[^11]  |
| [[Emissary\|S0082]] | Emissary | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Emissary](https://attack.mitre.org/software/S0082).[^10] [^4]  |
| [[Hannotog\|S1211]] | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) is a backdoor associated with [Lotus Blossom](https://attack.mitre.org/groups/G0030) operations.[^11]  |
| [[Elise\|S0081]] | Elise | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used [Elise](https://attack.mitre.org/software/S0081).[^14] [^5]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Lotus Blossom](https://attack.mitre.org/groups/G0030) is the exclusive user of [Sagerunex](https://attack.mitre.org/software/S1210), and has employed variants of this in operations since 2016.[^11] [^3]  |



## References

[^1]: Lotus Blossom


[^2]: Spring Dragon


[^3]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^4]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^5]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^6]: RADIUM


[^7]: Raspberry Typhoon


[^8]: DRAGONFISH


[^9]: Bilbug


[^10]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^11]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^12]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^13]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^14]: [Spring Dragon Jun 2015](https://securelist.com/the-spring-dragon-apt/70726/)


[^15]: Thrip


