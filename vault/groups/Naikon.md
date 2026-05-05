---
aliases: 
    - Naikon
mitre-attack: https://attack.mitre.org/groups/G0019
---

## G0019

[Naikon](https://attack.mitre.org/groups/G0019) is assessed to be a state-sponsored cyber espionage group attributed to the Chinese People’s Liberation Army’s (PLA) Chengdu Military Region Second Technical Reconnaissance Bureau (Military Unit Cover Designator 78020).[^3]  Active since at least 2010, [Naikon](https://attack.mitre.org/groups/G0019) has primarily conducted operations against government, military, and civil organizations in Southeast Asia, as well as against international bodies such as the United Nations Development Programme (UNDP) and the Association of Southeast Asian Nations (ASEAN).[^3] [^5]  <br><br>While [Naikon](https://attack.mitre.org/groups/G0019) shares some characteristics with [APT30](https://attack.mitre.org/groups/G0013), the two groups do not appear to be exact matches.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Naikon](https://attack.mitre.org/groups/G0019) has used administrator credentials for lateral movement in compromised networks.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Naikon](https://attack.mitre.org/groups/G0019) has used a netbios scanner for remote machine identification.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Naikon](https://attack.mitre.org/groups/G0019) has modified a victim's Windows Run registry to establish persistence.[^4]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Naikon](https://attack.mitre.org/groups/G0019) uses commands such as `netsh advfirewall firewall` to discover local firewall settings.[^5]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Naikon](https://attack.mitre.org/groups/G0019) has used the LadonGo scanner to scan target networks.[^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Naikon](https://attack.mitre.org/groups/G0019) has used WMIC.exe for lateral movement.[^4]  |
| [[Add-ins\|T1137.006]] | Add-ins | [Naikon](https://attack.mitre.org/groups/G0019) has used the RoyalRoad exploit builder to drop a second stage loader, intel.wll, into the Word Startup folder on the compromised host.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Naikon](https://attack.mitre.org/groups/G0019) uses commands such as `netsh interface show` to discover network interface settings.[^5]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Naikon](https://attack.mitre.org/groups/G0019) has disguised malicious programs as Google Chrome, Adobe, and VMware executables.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Naikon](https://attack.mitre.org/groups/G0019) has used malicious e-mail attachments to deliver malware.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Naikon](https://attack.mitre.org/groups/G0019) renamed a malicious service `taskmgr` to appear to be a legitimate version of Task Manager.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Naikon](https://attack.mitre.org/groups/G0019) has used schtasks.exe for lateral movement in compromised networks.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Naikon](https://attack.mitre.org/groups/G0019) has convinced victims to open malicious attachments to execute malware.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Naikon](https://attack.mitre.org/groups/G0019) has used DLL side-loading to load malicious DLL's into legitimate executables.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^5] [^4]  |
| [[Tasklist\|S0057]] | Tasklist | [^5]  |
| [[netsh\|S0108]] | netsh | [^5]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^5]  |
| [[Ping\|S0097]] | Ping | [^5] [^4]  |
| [[ftp\|S0095]] | ftp | [^5]  |
| [[PsExec\|S0029]] | PsExec | [^5]  |
| [[HDoor\|S0061]] | HDoor | [^5]  |
| [[WinMM\|S0059]] | WinMM | [^5] [^3]  |
| [[Nebulae\|S0630]] | Nebulae | [^4]  |
| [[RainyDay\|S0629]] | RainyDay | [^4]  |
| [[SslMM\|S0058]] | SslMM | [^5] [^3]  |
| [[Aria-body\|S0456]] | Aria-body | [^2] [^4]  |
| [[Sys10\|S0060]] | Sys10 | [^5]  |
| [[RARSTONE\|S0055]] | RARSTONE | [^5] [^3]  |



## References

[^1]: [Baumgartner Golovkin Naikon 2015](https://securelist.com/the-naikon-apt/69953/)


[^2]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^3]: [CameraShy](http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf)


[^4]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^5]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^6]: Naikon


