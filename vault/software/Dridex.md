---
aliases: 
    - S0384
    
mitre-attack: https://attack.mitre.org/software/S0384
---

## S0384

[Dridex](https://attack.mitre.org/software/S0384) is a prolific banking Trojan that first appeared in 2014. By December 2019, the US Treasury estimated [Dridex](https://attack.mitre.org/software/S0384) had infected computers in hundreds of banks and financial institutions in over 40 countries, leading to more than $100 million in theft. [Dridex](https://attack.mitre.org/software/S0384) was created from the source code of the Bugat banking Trojan (also known as Cridex).[^3] [^1] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Dridex](https://attack.mitre.org/software/S0384) has encrypted traffic with RC4.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Dridex](https://attack.mitre.org/software/S0384) can abuse legitimate Windows executables to side-load malicious DLL files.[^11]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Dridex](https://attack.mitre.org/software/S0384) contains a module for VNC.[^3]  |
| [[Native API\|T1106]] | Native API | [Dridex](https://attack.mitre.org/software/S0384) has used the `OutputDebugStringW` function to avoid malware analysis as part of its anti-debugging technique.[^8]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Dridex](https://attack.mitre.org/software/S0384) can maintain persistence via the creation of scheduled tasks within system directories such as `windows\system32\`, `windows\syswow64,` `winnt\system32`, and `winnt\syswow64`.[^11]   |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Dridex](https://attack.mitre.org/software/S0384) can perform browser attacks via web injects to steal information such as credentials, certificates, and cookies.[^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Dridex](https://attack.mitre.org/software/S0384) has collected a list of installed software on the system.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Dridex](https://attack.mitre.org/software/S0384) has used POST requests and HTTPS for C2 communications.[^1] [^8]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Dridex](https://attack.mitre.org/software/S0384) can use `regsvr32.exe` to initiate malicious code.[^11]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Dridex](https://attack.mitre.org/software/S0384) has encrypted traffic with RSA.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Dridex](https://attack.mitre.org/software/S0384)'s strings are obfuscated using RC4.[^8]   |
| [[Proxy\|T1090]] | Proxy | [Dridex](https://attack.mitre.org/software/S0384) contains a backconnect module for tunneling network traffic through a victim's computer. Infected computers become part of a P2P botnet that can relay C2 traffic to other infected peers.[^3] [^8]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Dridex](https://attack.mitre.org/software/S0384) has collected the computer name and OS architecture information from the system.[^8]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Dridex](https://attack.mitre.org/software/S0384) can use multiple layers of proxy servers to hide terminal nodes in its infrastructure.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Dridex](https://attack.mitre.org/software/S0384) has relied upon users clicking on a malicious attachment delivered through spearphishing.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |
| [[Indrik Spider\|G0119]] | Indrik Spider |



## References

[^1]: [Kaspersky Dridex May 2017](https://securelist.com/dridex-a-history-of-evolution/78531/)


[^2]: Dridex


[^3]: [Dell Dridex Oct 2015](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)


[^4]: [IBM TA505 April 2020](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)


[^5]: [Proofpoint TA505 June 2018](https://www.proofpoint.com/us/threat-insight/post/ta505-shifts-times)


[^6]: [Crowdstrike EvilCorp March 2021](https://www.crowdstrike.com/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)


[^7]: [Treasury EvilCorp Dec 2019](https://home.treasury.gov/news/press-releases/sm845)


[^8]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)


[^9]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^10]: [Proofpoint TA505 Sep 2017](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)


[^11]: [Red Canary Dridex Threat Report 2021](https://redcanary.com/threat-detection-report/threats/dridex/)


[^12]: Bugat v5


