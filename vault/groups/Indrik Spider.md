---
aliases: 
    - Indrik Spider
    - Evil Corp
    - Manatee Tempest
    - DEV-0243
    - UNC2165
mitre-attack: https://attack.mitre.org/groups/G0119
---

## G0119

[Indrik Spider](https://attack.mitre.org/groups/G0119) is a Russia-based cybercriminal group that has been active since at least 2014. [Indrik Spider](https://attack.mitre.org/groups/G0119) initially started with the [Dridex](https://attack.mitre.org/software/S0384) banking Trojan, and then by 2017 they began running ransomware operations using [BitPaymer](https://attack.mitre.org/software/S0570), [WastedLocker](https://attack.mitre.org/software/S0612), and Hades ransomware. Following U.S. sanctions and an indictment in 2019, [Indrik Spider](https://attack.mitre.org/groups/G0119) changed their tactics and diversified their toolset.[^12] [^5] [^8] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Indrik Spider](https://attack.mitre.org/groups/G0119) used [Cobalt Strike](https://attack.mitre.org/software/S0154) to carry out credential dumping using ProcDump.[^2]  |
| [[Malware\|T1587.001]] | Malware | [Indrik Spider](https://attack.mitre.org/groups/G0119) has developed malware for their operations, including ransomware such as [BitPaymer](https://attack.mitre.org/software/S0570) and [WastedLocker](https://attack.mitre.org/software/S0612).[^12]  |
| [[Create Account\|T1136]] | Create Account | [Indrik Spider](https://attack.mitre.org/groups/G0119) used `wmic.exe` to add a new user to the system.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Indrik Spider](https://attack.mitre.org/groups/G0119) has modified registry keys to prepare for ransomware execution and to disable common administrative utilities.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Indrik Spider](https://attack.mitre.org/groups/G0119) used fake updates for FlashPlayer plugin and Google Chrome as initial infection vectors.[^12]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used the win32_service WMI class to retrieve a list of services from the system.[^2]   |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Indrik Spider](https://attack.mitre.org/groups/G0119) has purchased access to victim VPNs to facilitate access to victim environments.[^4]     |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Indrik Spider](https://attack.mitre.org/groups/G0119) used [PsExec](https://attack.mitre.org/software/S0029) to leverage Windows Defender to disable scanning of all downloaded files and to restrict real-time monitoring.[^2]  [Indrik Spider](https://attack.mitre.org/groups/G0119) has used `MpCmdRun` to revert the definitions in Microsoft Defender.[^4]  Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) has used WMI to stop or uninstall and reset anti-virus products and other defensive services.[^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Indrik Spider](https://attack.mitre.org/groups/G0119) has stored collected data in a .tmp file.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used RDP for lateral movement.[^4]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Indrik Spider](https://attack.mitre.org/groups/G0119) has accessed and exported passwords from password managers.[^4]  |
| [[Gather Victim Network Information\|T1590]] | Gather Victim Network Information | [Indrik Spider](https://attack.mitre.org/groups/G0119) has downloaded tools, such as the Advanced Port Scanner utility and Lansweeper, to conduct internal reconnaissance of the victim network. [Indrik Spider](https://attack.mitre.org/groups/G0119) has also accessed the victim’s VMware VCenter, which had information about host configuration, clusters, etc.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used PowerShell [Empire](https://attack.mitre.org/software/S0363) for execution of malware.[^12] [^2]   |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has collected credentials from infected systems, including domain accounts.[^12]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Indrik Spider](https://attack.mitre.org/groups/G0119) has searched files to obtain and exfiltrate credentials.[^4]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Indrik Spider](https://attack.mitre.org/groups/G0119) has exfiltrated data using [Rclone](https://attack.mitre.org/software/S1040) or MEGASync prior to deploying ransomware.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used batch scripts on victim's machines.[^12] [^4]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used Group Policy Objects to deploy batch scripts.[^12] [^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used WMIC to execute commands on remote computers.[^2]   |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used valid accounts for initial access and lateral movement.[^4]  [Indrik Spider](https://attack.mitre.org/groups/G0119) has also maintained access to the victim environment through the VPN infrastructure.[^4]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Indrik Spider](https://attack.mitre.org/groups/G0119) has encrypted domain-controlled systems using [BitPaymer](https://attack.mitre.org/software/S0570).[^12]  Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) used [PsExec](https://attack.mitre.org/software/S0029) to execute a ransomware script.[^4]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to empty log files.[^2]  Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) has cleared all event logs using `wevutil`.[^4]     |
| [[Local Account\|T1136.001]] | Local Account | [Indrik Spider](https://attack.mitre.org/groups/G0119) has created local system accounts and has added the accounts to privileged groups.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used PowerView to enumerate all Windows Server, Windows Server 2003, and Windows 7 instances in the Active Directory database.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used malicious JavaScript files for several components of their attack.[^2]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has created email accounts to communicate with their ransomware victims, to include providing payment and decryption details.[^12]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Indrik Spider](https://attack.mitre.org/groups/G0119) has downloaded additional scripts, malware, and tools onto a compromised host.[^12] [^2] [^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used [PsExec](https://attack.mitre.org/software/S0029) to stop services prior to the execution of ransomware.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used a service account to extract copies of the `Security` Registry hive.[^4]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Indrik Spider](https://attack.mitre.org/groups/G0119) has conducted Kerberoasting attacks using a module from GitHub.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Indrik Spider](https://attack.mitre.org/groups/G0119) has attempted to get users to click on a malicious zipped file.[^2]   |
| [[SSH\|T1021.004]] | SSH | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used SSH for lateral movement.[^4]  |
| [[Server\|T1584.004]] | Server | [Indrik Spider](https://attack.mitre.org/groups/G0119) has served fake updates via legitimate websites that have been compromised.[^12] 	 |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [^12]  |
| [[Donut\|S0695]] | Donut | [^3]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^12] [^4]  |
| [[PsExec\|S0029]] | PsExec | [^2]  |
| [[WastedLocker\|S0612]] | WastedLocker | [^3] [^5] [^9] [^10]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^5] [^9] [^4]  |
| [[Dridex\|S0384]] | Dridex | [^12] [^5] [^8]  |
| [[BitPaymer\|S0570]] | BitPaymer | [^12] [^5]  |



## References

[^1]: UNC2165


[^2]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


[^3]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^4]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^5]: [Crowdstrike EvilCorp March 2021](https://www.crowdstrike.com/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)


[^6]: Manatee Tempest


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: [Treasury EvilCorp Dec 2019](https://home.treasury.gov/news/press-releases/sm845)


[^9]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^10]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)


[^11]: Evil Corp


[^12]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^13]: DEV-0243


