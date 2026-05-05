---
aliases: 
    - Agrius
    - Pink Sandstorm
    - AMERICIUM
    - Agonizing Serpens
    - BlackShadow
mitre-attack: https://attack.mitre.org/groups/G1030
---

## G1030

[Agrius](https://attack.mitre.org/groups/G1030) is an Iranian threat actor active since 2020 notable for a series of ransomware and wiper operations in the Middle East, with an emphasis on Israeli targets.[^1] [^3]  Public reporting has linked [Agrius](https://attack.mitre.org/groups/G1030) to Iran's Ministry of Intelligence and Security (MOIS).[^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Agrius](https://attack.mitre.org/groups/G1030) used the tool [NBTscan](https://attack.mitre.org/software/S0590) to scan for remote, accessible hosts in victim environments.[^9]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Agrius](https://attack.mitre.org/groups/G1030) used several mechanisms to try to disable security tools. [Agrius](https://attack.mitre.org/groups/G1030) attempted to modify EDR-related services to disable auto-start on system reboot. [Agrius](https://attack.mitre.org/groups/G1030) used a publicly available driver, `GMER64.sys` typically used for anti-rootkit functionality, to selectively stop and remove security software processes.[^9]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Agrius](https://attack.mitre.org/groups/G1030) used the open-source port scanner `WinEggDrop` to perform detailed scans of hosts of interest in victim networks.[^9]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Agrius](https://attack.mitre.org/groups/G1030) attempted to acquire valid credentials for victim environments through various means to enable follow-on lateral movement.[^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Agrius](https://attack.mitre.org/groups/G1030) has deployed base64-encoded variants of [ASPXSpy](https://attack.mitre.org/software/S0073) to evade detection.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Agrius](https://attack.mitre.org/groups/G1030) typically deploys a variant of the [ASPXSpy](https://attack.mitre.org/software/S0073) web shell following initial access via exploitation.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Agrius](https://attack.mitre.org/groups/G1030) gathered data from database and other critical servers in victim environments, then used wiping mechanisms as an anti-analysis and anti-forensics mechanism.[^9]  |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Agrius](https://attack.mitre.org/groups/G1030) typically uses commercial VPN services for anonymizing last-hop traffic to victim networks, such as ProtonVPN.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Agrius](https://attack.mitre.org/groups/G1030) has used the folder, `C:\\windows\\temp\\s\\`, to stage data for exfiltration.[^9]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Agrius](https://attack.mitre.org/groups/G1030) engaged in password spraying via SMB in victim environments.[^9]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Agrius](https://attack.mitre.org/groups/G1030) used a custom tool, `sql.net4.exe`, to query SQL databases and then identify and extract personally identifiable information.[^9]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Agrius](https://attack.mitre.org/groups/G1030) dumped the SAM file on victim machines to capture credentials.[^9]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Agrius](https://attack.mitre.org/groups/G1030) used 7zip to archive extracted data in preparation for exfiltration.[^9]  |
| [[Masquerading\|T1036]] | Masquerading | [Agrius](https://attack.mitre.org/groups/G1030) used the Plink tool for tunneling and connections to remote machines, renaming it `systems.exe` in some instances.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Agrius](https://attack.mitre.org/groups/G1030) used tools such as [Mimikatz](https://attack.mitre.org/software/S0002) to dump LSASS memory to capture credentials in victim environments.[^9]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Agrius](https://attack.mitre.org/groups/G1030) tunnels RDP traffic through deployed web shells to access victim environments via compromised accounts.[^1]  [Agrius](https://attack.mitre.org/groups/G1030) used the Plink tool to tunnel RDP connections for remote access and lateral movement in victim environments.[^9]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Agrius](https://attack.mitre.org/groups/G1030) exploits public-facing applications for initial access to victim environments. Examples include widespread attempts to exploit CVE-2018-13379 in FortiOS devices and SQL injection activity.[^1]   |
| [[Brute Force\|T1110]] | Brute Force | [Agrius](https://attack.mitre.org/groups/G1030) engaged in various brute forcing activities via SMB in victim environments.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Agrius](https://attack.mitre.org/groups/G1030) uses [ASPXSpy](https://attack.mitre.org/software/S0073) web shells to enable follow-on command execution via `cmd.exe`.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Agrius](https://attack.mitre.org/groups/G1030) has deployed [IPsec Helper](https://attack.mitre.org/software/S1132) malware post-exploitation and registered it as a service for persistence.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Agrius](https://attack.mitre.org/groups/G1030) exfiltrated staged data using tools such as Putty and WinSCP, communicating with command and control servers.[^9]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Agrius](https://attack.mitre.org/groups/G1030) downloaded some payloads for follow-on execution from legitimate filesharing services such as `ufile.io` and `easyupload.io`.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [Agrius](https://attack.mitre.org/groups/G1030) used [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials from LSASS memory.[^9]  |
| [[NBTscan\|S0590]] | NBTscan | [Agrius](https://attack.mitre.org/groups/G1030) used [NBTscan](https://attack.mitre.org/software/S0590) to scan victim networks for existing and accessible hosts.[^9]  |
| [[Moneybird\|S1137]] | Moneybird | [Moneybird](https://attack.mitre.org/software/S1137) is associated with ransomware operations launched by [Agrius](https://attack.mitre.org/groups/G1030).[^3]  |
| [[Apostle\|S1133]] | Apostle | [Agrius](https://attack.mitre.org/groups/G1030) has used [Apostle](https://attack.mitre.org/software/S1133) as both a wiper and ransomware-like effects capability in intrusions.[^1]  |
| [[ASPXSpy\|S0073]] | ASPXSpy | [Agrius](https://attack.mitre.org/groups/G1030) relies on web shells for persistent access post exploitation, with an emphasis on variants of [ASPXSpy](https://attack.mitre.org/software/S0073).[^1]  |
| [[MultiLayer Wiper\|S1135]] | MultiLayer Wiper | [MultiLayer Wiper](https://attack.mitre.org/software/S1135) is associated with wiping operations linked to [Agrius](https://attack.mitre.org/groups/G1030).[^9]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [Agrius](https://attack.mitre.org/groups/G1030) uses [IPsec Helper](https://attack.mitre.org/software/S1132) as a post-exploitation remote access tool framework.[^1]  |
| [[BFG Agonizer\|S1136]] | BFG Agonizer | [BFG Agonizer](https://attack.mitre.org/software/S1136) has been used by [Agrius](https://attack.mitre.org/groups/G1030) for wiping operations.[^9]  |
| [[DEADWOOD\|S1134]] | DEADWOOD | [DEADWOOD](https://attack.mitre.org/software/S1134) has been used by [Agrius](https://attack.mitre.org/groups/G1030) in wiping operations.[^1]  |



## References

[^1]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^2]: Pink Sandstorm


[^3]: [CheckPoint Agrius 2023](https://research.checkpoint.com/2023/agrius-deploys-moneybird-in-targeted-attacks-against-israeli-organizations/)


[^4]: Agonizing Serpens


[^5]: AMERICIUM


[^6]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^7]: [Microsoft Iran Cyber 2023](https://www.microsoft.com/en-us/security/business/security-insider/wp-content/uploads/2023/05/Iran-turning-to-cyber-enabled-influence-operations-for-greater-effect-05022023.pdf)


[^8]: BlackShadow


[^9]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


