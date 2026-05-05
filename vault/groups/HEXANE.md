---
aliases: 
    - HEXANE
    - Lyceum
    - Siamesekitten
    - Spirlin
mitre-attack: https://attack.mitre.org/groups/G1001
---

## G1001

[HEXANE](https://attack.mitre.org/groups/G1001) is a cyber espionage threat group that has targeted oil & gas, telecommunications, aviation, and internet service provider organizations since at least 2017. Targeted companies have been located in the Middle East and Africa, including Israel, Saudi Arabia, Kuwait, Morocco, and Tunisia. [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.[^10] [^4] [^5] [^6] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used [Ping](https://attack.mitre.org/software/S0097) and `tracert` for network discovery.[^4]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [HEXANE](https://attack.mitre.org/groups/G1001) has run `cmdkey` on victim machines to identify stored credentials.[^4]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [HEXANE](https://attack.mitre.org/groups/G1001) has used Base64-encoded scripts.[^4]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [HEXANE](https://attack.mitre.org/groups/G1001) has identified specific potential victims at targeted organizations.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has collected the hostname of a compromised machine.[^4]  |
| [[Domains\|T1583.001]] | Domains | [HEXANE](https://attack.mitre.org/groups/G1001) has registered and operated domains for campaigns, often using a security or web technology theme or impersonating the targeted organization.[^8] [^10] [^5]  |
| [[Brute Force\|T1110]] | Brute Force | [HEXANE](https://attack.mitre.org/groups/G1001) has used brute force attacks to compromise valid credentials.[^8]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [HEXANE](https://attack.mitre.org/groups/G1001) has used a scheduled task to establish persistence for a keylogger.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [HEXANE](https://attack.mitre.org/groups/G1001) has relied on victim's executing malicious file attachments delivered via email or embedded within actor-controlled websites to deliver malware.[^8] [^10] [^5] [^11]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [HEXANE](https://attack.mitre.org/groups/G1001) has used cloud services, including OneDrive, for data exfiltration.[^7]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has established fraudulent LinkedIn accounts impersonating HR department employees to target potential victims with fake job offers.[^5]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used tools including [BITSAdmin](https://attack.mitre.org/software/S0190) to test internet connectivity from compromised hosts.[^4]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [HEXANE](https://attack.mitre.org/groups/G1001) has used WMI event subscriptions for persistence.[^4]  |
| [[Local Groups\|T1069.001]] | Local Groups | [HEXANE](https://attack.mitre.org/groups/G1001) has run `net localgroup` to enumerate local groups.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used `net view` to enumerate domain machines.[^4]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [HEXANE](https://attack.mitre.org/groups/G1001) has used remote desktop sessions for lateral movement.[^8]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has used compromised accounts to send spearphishing emails.[^8]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [HEXANE](https://attack.mitre.org/groups/G1001) has used password spraying attacks to obtain valid credentials.[^8]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [HEXANE](https://attack.mitre.org/groups/G1001) has used cloud services, including OneDrive, for C2.[^7]  |
| [[Tool\|T1588.002]] | Tool | [HEXANE](https://attack.mitre.org/groups/G1001) has acquired, and sometimes customized, open source tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Empire](https://attack.mitre.org/software/S0363), VNC remote access software, and DIG.net.[^4] [^8] [^11]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [HEXANE](https://attack.mitre.org/groups/G1001) has used a [Mimikatz](https://attack.mitre.org/software/S0002)-based tool and a PowerShell script to steal passwords from Google Chrome.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [HEXANE](https://attack.mitre.org/groups/G1001) has used PowerShell-based tools and scripts for discovery and collection on compromised hosts.[^8] [^9] [^4]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [HEXANE](https://attack.mitre.org/groups/G1001) has staged malware on fraudulent websites set up to impersonate targeted organizations.[^5]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [HEXANE](https://attack.mitre.org/groups/G1001) has targeted executives, human resources staff, and IT personnel for spearphishing.[^8] [^5] <br> |
| [[Email Accounts\|T1585.002]] | Email Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has established email accounts for use in domain registration including for ProtonMail addresses.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has run `whoami` on compromised machines to identify the current user.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HEXANE](https://attack.mitre.org/groups/G1001) has downloaded additional payloads and malicious scripts onto a compromised host.[^4]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used [netstat](https://attack.mitre.org/software/S0104) to monitor connections to specific ports.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has enumerated processes on targeted systems.[^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [HEXANE](https://attack.mitre.org/groups/G1001) has used a PowerShell-based keylogger named `kl.ps1`.[^8] [^4]  |
| [[Software Discovery\|T1518]] | Software Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has enumerated programs installed on an infected machine.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [HEXANE](https://attack.mitre.org/groups/G1001) has used a VisualBasic script named `MicrosoftUpdator.vbs` for execution of a PowerShell keylogger.[^4]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used a PowerShell-based keylogging tool to capture the window title.[^8]  |
| [[Identify Roles\|T1591.004]] | Identify Roles | [HEXANE](https://attack.mitre.org/groups/G1001) has identified executives, HR, and IT staff at victim organizations for further targeting.[^8] [^5]  |
| [[DNS Server\|T1583.002]] | DNS Server | [HEXANE](https://attack.mitre.org/groups/G1001) has set up custom DNS servers to send commands to compromised hosts via TXT records.[^11]  |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [HEXANE](https://attack.mitre.org/groups/G1001) has conducted internal spearphishing attacks against executives, HR, and IT personnel to gain information and access.[^8]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ipconfig\|S0100]] | ipconfig | [^5] [^11]  |
| [[Empire\|S0363]] | Empire | [^8]  |
| [[netstat\|S0104]] | netstat | [^4]  |
| [[PoshC2\|S0378]] | PoshC2 | [^8]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^4]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^4]  |
| [[Ping\|S0097]] | Ping | [^5]  |
| [[DnsSystem\|S1021]] | DnsSystem | [^11]  |
| [[Shark\|S1019]] | Shark | [^4] [^6]  |
| [[Milan\|S1015]] | Milan | [^4] [^6]  |
| [[DanBot\|S1014]] | DanBot | [^8]  |
| [[Kevin\|S1020]] | Kevin | [^4]  |



## References

[^1]: Lyceum


[^2]: Spirlin


[^3]: Siamesekitten


[^4]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^5]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^6]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^7]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^8]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^9]: [Kaspersky APT Trends Q1 April 2021](https://securelist.com/apt-trends-report-q1-2021/101967)


[^10]: [Dragos Hexane](https://dragos.com/resource/hexane/)


[^11]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


