---
aliases: 
    - S0341
    
mitre-attack: https://attack.mitre.org/software/S0341
---

## S0341

[Xbash](https://attack.mitre.org/software/S0341) is a malware family that has targeted Linux and Microsoft Windows servers. The malware has been tied to the Iron Group, a threat actor group known for previous ransomware attacks. [Xbash](https://attack.mitre.org/software/S0341) was developed in Python and then converted into a self-contained Linux ELF executable by using PyInstaller.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Xbash](https://attack.mitre.org/software/S0341) uses HTTP for C2 communications.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Xbash](https://attack.mitre.org/software/S0341) has destroyed Linux-based databases as part of its ransomware capabilities.[^1] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Xbash](https://attack.mitre.org/software/S0341) can execute malicious VBScript payloads on the victim’s machine.[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [Xbash](https://attack.mitre.org/software/S0341) can use mshta for executing scripts.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Xbash](https://attack.mitre.org/software/S0341) can create a Startup item for persistence if it determines it is on a Windows system.[^1]  |
| [[Cron\|T1053.003]] | Cron | [Xbash](https://attack.mitre.org/software/S0341) can create a cronjob for persistence if it determines it is on a Linux system.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Xbash](https://attack.mitre.org/software/S0341) can attempt to exploit known vulnerabilities in Hadoop, Redis, or ActiveMQ when it finds those services running in order to conduct further execution.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Xbash](https://attack.mitre.org/software/S0341) can download additional malicious files from its C2 server.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Xbash](https://attack.mitre.org/software/S0341) can use scripts to invoke PowerShell to download a malicious PE executable or PE DLL for execution.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Xbash](https://attack.mitre.org/software/S0341) can execute malicious JavaScript payloads on the victim’s machine.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Xbash](https://attack.mitre.org/software/S0341) can perform port scanning of TCP and UDP ports.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Xbash](https://attack.mitre.org/software/S0341) has maliciously encrypted victim's database systems and demanded a cryptocurrency ransom be paid.[^1]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [Xbash](https://attack.mitre.org/software/S0341) can obtain a list of weak passwords from the C2 server to use for brute forcing as well as attempt to brute force services with open ports.[^1] [^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Xbash](https://attack.mitre.org/software/S0341) can use regsvr32 for executing scripts.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Xbash](https://attack.mitre.org/software/S0341) can collect IP addresses and local intranet information from a victim’s machine.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Xbash](https://attack.mitre.org/software/S0341) can obtain a webpage hosted on Pastebin to update its C2 domain list.[^1]  |




## References

[^1]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)


[^2]: [Trend Micro Xbash Sept 2018](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/new-multi-platform-xbash-packs-obfuscation-ransomware-coinminer-worm-and-botnet)


[^3]: Xbash


