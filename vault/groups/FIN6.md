---
aliases: 
    - FIN6
    - Magecart Group 6
    - ITG08
    - Skeleton Spider
    - TAAL
    - Camouflage Tempest
mitre-attack: https://attack.mitre.org/groups/G0037
---

## G0037

[FIN6](https://attack.mitre.org/groups/G0037) is a cyber crime group that has stolen payment card data and sold it for profit on underground marketplaces. This group has aggressively targeted and compromised point of sale (PoS) systems in the hospitality and retail sectors.[^5] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [FIN6](https://attack.mitre.org/groups/G0037) has encoded data gathered from the victim with a simple substitution cipher and single-byte XOR using the 0xAA key, and Base64 with character permutation.[^5] [^18]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [FIN6](https://attack.mitre.org/groups/G0037) has targeted victims with e-mails containing malicious attachments.[^17]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [FIN6](https://attack.mitre.org/groups/G0037) has deployed a utility script named `kill.bat` to disable anti-virus.[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [FIN6](https://attack.mitre.org/groups/G0037) has used Metasploit’s [PsExec](https://attack.mitre.org/software/S0029) NTDSGRAB module to obtain a copy of the victim's Active Directory database.[^5]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [FIN6](https://attack.mitre.org/groups/G0037) has used scripting to iterate through a list of compromised PoS systems, copy data to a log file, and remove the original data files.[^5] [^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [FIN6](https://attack.mitre.org/groups/G0037) used the Plink command-line utility to create SSH tunnels to C2 servers.[^5]  |
| [[Databases\|T1213.006]] | Databases | [FIN6](https://attack.mitre.org/groups/G0037) has collected schemas and user accounts from systems running SQL Server.[^17]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [FIN6](https://attack.mitre.org/groups/G0037) has used encoded PowerShell commands.[^17]  |
| [[JavaScript\|T1059.007]] | JavaScript | [FIN6](https://attack.mitre.org/groups/G0037) has used malicious JavaScript to steal payment card data from e-commerce sites.[^18]  |
| [[Web Service\|T1102]] | Web Service | [FIN6](https://attack.mitre.org/groups/G0037) has used Pastebin and Google Storage to host content for their operations.[^1] 	<br> |
| [[Data from Local System\|T1005]] | Data from Local System | [FIN6](https://attack.mitre.org/groups/G0037) has collected and exfiltrated payment card data from compromised systems.[^18] [^9] [^16]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FIN6](https://attack.mitre.org/groups/G0037) has used Registry Run keys to establish persistence for its downloader tools known as HARDTACK and SHIPBREAD.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FIN6](https://attack.mitre.org/groups/G0037) has used `kill.bat` script to disable security tools.[^1]  |
| [[Tool\|T1588.002]] | Tool | [FIN6](https://attack.mitre.org/groups/G0037) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Cobalt Strike](https://attack.mitre.org/software/S0154), and [AdFind](https://attack.mitre.org/software/S0552).[^19] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FIN6](https://attack.mitre.org/groups/G0037) has removed files from victim machines.[^5]  |
| [[NTDS\|T1003.003]] | NTDS | [FIN6](https://attack.mitre.org/groups/G0037) has used Metasploit’s [PsExec](https://attack.mitre.org/software/S0029) NTDSGRAB module to obtain a copy of the victim's Active Directory database.[^5] [^1] 	 |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [FIN6](https://attack.mitre.org/groups/G0037) has used has used Metasploit’s named-pipe impersonation technique to escalate privileges.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [FIN6](https://attack.mitre.org/groups/G0037) has used tools to exploit Windows vulnerabilities in order to escalate privileges. The tools targeted CVE-2013-3660, CVE-2011-2005, and CVE-2010-4398, all of which could allow local users to access kernel-level privileges.[^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [FIN6](https://attack.mitre.org/groups/G0037) has used malicious documents to lure victims into allowing execution of PowerShell scripts.[^17]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [FIN6](https://attack.mitre.org/groups/G0037) has renamed the "psexec" service name to "mstdc" to masquerade as a legitimate Windows service.[^1] 	 |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [FIN6](https://attack.mitre.org/groups/G0037) has used fake job advertisements sent via LinkedIn to spearphish targets.[^19]  |
| [[PowerShell\|T1059.001]] | PowerShell |  [FIN6](https://attack.mitre.org/groups/G0037) has used PowerShell to gain access to merchant's networks, and a Metasploit PowerShell module to download and execute shellcode and to set up a local listener.[^5] [^1] [^17]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | Following data collection, [FIN6](https://attack.mitre.org/groups/G0037) has compressed log files into a ZIP archive prior to staging and exfiltration.[^5]  |
| [[Code Signing\|T1553.002]] | Code Signing | [FIN6](https://attack.mitre.org/groups/G0037) has used Comodo code-signing certificates.[^19] 	 |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [FIN6](https://attack.mitre.org/groups/G0037) used RDP to move laterally in victim networks.[^5] [^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [FIN6](https://attack.mitre.org/groups/G0037) has used a script to iterate through a list of compromised PoS systems, copy and remove data to a log file, and to bind to events from the submit payment button.[^5] [^18]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [FIN6](https://attack.mitre.org/groups/G0037) used publicly available tools (including Microsoft's built-in SQL querying tool, osql.exe) to map the internal network and conduct reconnaissance against Active Directory, Structured Query Language (SQL) servers, and NetBIOS.[^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [FIN6](https://attack.mitre.org/groups/G0037) has used scheduled tasks to establish persistence for various malware it uses, including downloaders known as HARDTACK and SHIPBREAD and [FrameworkPOS](https://attack.mitre.org/software/S0503).[^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [FIN6](https://attack.mitre.org/groups/G0037) has created Windows services to execute encoded PowerShell commands.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [FIN6](https://attack.mitre.org/groups/G0037) used publicly available tools (including Microsoft's built-in SQL querying tool, osql.exe) to map the internal network and conduct reconnaissance against Active Directory, Structured Query Language (SQL) servers, and NetBIOS.[^5]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [FIN6](https://attack.mitre.org/groups/G0037) has sent stolen payment card data to remote servers via HTTP POSTs.[^18]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FIN6](https://attack.mitre.org/groups/G0037) has used WMI to automate the remote execution of PowerShell scripts.[^19] 	 |
| [[Password Cracking\|T1110.002]] | Password Cracking | [FIN6](https://attack.mitre.org/groups/G0037) has extracted password hashes from ntds.dit to crack offline.[^5]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [FIN6](https://attack.mitre.org/groups/G0037) has used the Stealer One credential stealer to target e-mail and file transfer utilities including FTP.[^17]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [FIN6](https://attack.mitre.org/groups/G0037) has used Metasploit Bind and Reverse TCP stagers.[^18]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | To move laterally on a victim network, [FIN6](https://attack.mitre.org/groups/G0037) has used credentials stolen from various systems on which it gathered usernames and password hashes.[^5] [^1] [^17]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [FIN6](https://attack.mitre.org/groups/G0037) used the Plink command-line utility to create SSH tunnels to C2 servers.[^5]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [FIN6](https://attack.mitre.org/groups/G0037) has used [Windows Credential Editor](https://attack.mitre.org/software/S0005) for credential dumping.[^5] [^1] 	<br> |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [FIN6](https://attack.mitre.org/groups/G0037) has used the Stealer One credential stealer to target web browsers.[^17]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [FIN6](https://attack.mitre.org/groups/G0037) actors have compressed data from remote systems and moved it to another staging system before exfiltration.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^5]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^19]  |
| [[AdFind\|S0552]] | AdFind | [^1]  |
| [[PsExec\|S0029]] | PsExec | [^5] [^1]  |
| [[FrameworkPOS\|S0503]] | FrameworkPOS | [^2] [^13] [^17]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [^17]  |
| [[LockerGoga\|S0372]] | LockerGoga | [^1]  |
| [[Ryuk\|S0446]] | Ryuk | [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^1]  |
| [[More_eggs\|S0284]] | More_eggs | [^19] [^17]  |
| [[GrimAgent\|S0632]] | GrimAgent | [^8]  |
| [[Maze\|S0449]] | Maze | [^12]  |



## References

[^1]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^2]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)


[^3]: Skeleton Spider


[^4]: Magecart Group 6


[^5]: [FireEye FIN6 April 2016](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)


[^6]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^7]: ITG08


[^8]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^9]: [RiskIQ British Airways September 2018](https://web.archive.org/web/20181231220607/https://riskiq.com/blog/labs/magecart-british-airways-breach/)


[^10]: TAAL


[^11]: Camouflage Tempest


[^12]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


[^13]: [Crowdstrike Global Threat Report Feb 2018](https://crowdstrike.lookbookhq.com/global-threat-report-2018-web/cs-2018-global-threat-report)


[^14]: [Security Intelligence ITG08 April 2020](https://securityintelligence.com/posts/itg08-aka-fin6-partners-with-trickbot-gang-uses-anchor-framework/)


[^15]: FIN6


[^16]: [RiskIQ Newegg September 2018](https://web.archive.org/web/20181209083100/https://www.riskiq.com/blog/labs/magecart-newegg/)


[^17]: [Visa FIN6 Feb 2019](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)


[^18]: [Trend Micro FIN6 October 2019](https://www.trendmicro.com/en_us/research/19/j/fin6-compromised-e-commerce-platform-via-magecart-to-inject-credit-card-skimmers-into-thousands-of-online-shops.html)


[^19]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


