---
aliases: 
    - APT41
    - Wicked Panda
    - Brass Typhoon
    - BARIUM
mitre-attack: https://attack.mitre.org/groups/G0096
---

## G0096

[APT41](https://attack.mitre.org/groups/G0096) is a threat group that researchers have assessed as Chinese state-sponsored espionage group that also conducts financially-motivated operations. Active since at least 2012, [APT41](https://attack.mitre.org/groups/G0096) has been observed targeting various industries, including but not limited to healthcare, telecom, technology, finance, education, retail and video game industries in 14 countries.[^20]  Notable behaviors include using a wide range of malware and tools to complete mission objectives. [APT41](https://attack.mitre.org/groups/G0096) overlaps at least partially with public reporting on groups including BARIUM and [Winnti Group](https://attack.mitre.org/groups/G0044).[^9] [^10] <br>

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT41](https://attack.mitre.org/groups/G0096) used compromised credentials to log on to other systems.[^9] [^15]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT41](https://attack.mitre.org/groups/G0096) uses multiple built-in commands such as `systeminfo` and `net config Workstation` to enumerate victim system basic configuration information.[^5]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [APT41](https://attack.mitre.org/groups/G0096) gained access to production environments where they could inject malicious code into legitimate, signed files and widely distribute them to end users.[^9]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [APT41](https://attack.mitre.org/groups/G0096) used `net group` commands to enumerate various Windows user groups and permissions.[^5]  |
| [[Wordlist Scanning\|T1595.003]] | Wordlist Scanning | [APT41](https://attack.mitre.org/groups/G0096) leverages various tools and frameworks to brute-force directories on web servers.[^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT41](https://attack.mitre.org/groups/G0096) leveraged PowerShell to deploy malware families in victims’ environments.[^9] [^6]  |
| [[Rootkit\|T1014]] | Rootkit | [APT41](https://attack.mitre.org/groups/G0096) deployed rootkits on Linux systems.[^9] [^15]  |
| [[Domain Account\|T1087.002]] | Domain Account | [APT41](https://attack.mitre.org/groups/G0096) used built-in `net` commands to enumerate domain administrator users.[^5]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [APT41](https://attack.mitre.org/groups/G0096) used BrowserGhost, a tool designed to obtain credentials from browsers, to retrieve information from password stores.[^5]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT41](https://attack.mitre.org/groups/G0096) attempted to masquerade their files as popular anti-virus software.[^9] [^10]  |
| [[Windows Service\|T1543.003]] | Windows Service | [APT41](https://attack.mitre.org/groups/G0096) modified legitimate Windows services to install malware backdoors.[^9] [^10]  [APT41](https://attack.mitre.org/groups/G0096) created the StorSyncSvc service to provide persistence for [Cobalt Strike](https://attack.mitre.org/software/S0154).[^6]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [APT41](https://attack.mitre.org/groups/G0096) used exploit payloads that initiate download via [ftp](https://attack.mitre.org/software/S0095).[^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [APT41](https://attack.mitre.org/groups/G0096) has used MiPing to discover active systems in the victim network.[^2]   |
| [[Software Packing\|T1027.002]] | Software Packing | [APT41](https://attack.mitre.org/groups/G0096) uses packers such as Themida to obfuscate malicious files.[^5]  |
| [[Code Signing\|T1553.002]] | Code Signing | [APT41](https://attack.mitre.org/groups/G0096) leveraged code-signing certificates to sign malware when targeting both gaming and non-gaming organizations.[^9] [^10]  |
| [[Scan Databases\|T1596.005]] | Scan Databases | [APT41](https://attack.mitre.org/groups/G0096) uses the Chinese website fofa.su, similar to the Shodan scanning service, for passive scanning of victims.[^5]  |
| [[Tool\|T1588.002]] | Tool | [APT41](https://attack.mitre.org/groups/G0096) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [pwdump](https://attack.mitre.org/software/S0006), [PowerSploit](https://attack.mitre.org/software/S0194), and [Windows Credential Editor](https://attack.mitre.org/software/S0005).[^9]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [APT41](https://attack.mitre.org/groups/G0096) has added user accounts to the User and Admin groups.[^9]   |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [APT41](https://attack.mitre.org/groups/G0096) has transferred implant files using Windows Admin Shares and the Server Message Block (SMB) protocol, then executes files through Windows Management Instrumentation (WMI).[^15] [^2]  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | [APT41](https://attack.mitre.org/groups/G0096) used a hidden shell script in `/etc/rc.d/init.d` to leverage the `ADORE.XSEC`backdoor and `Adore-NG` rootkit.[^20]  |
| [[Local Account\|T1136.001]] | Local Account | [APT41](https://attack.mitre.org/groups/G0096) has created user accounts.[^9]   |
| [[Bootkit\|T1542.003]] | Bootkit | [APT41](https://attack.mitre.org/groups/G0096) deployed Master Boot Record bootkits on Windows systems to hide their malware and maintain persistence on victim systems.[^9]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [APT41](https://attack.mitre.org/groups/G0096) attempted to remove evidence of some of its activity by clearing Windows security and system events.[^9]  |
| [[Local Account\|T1087.001]] | Local Account | [APT41](https://attack.mitre.org/groups/G0096) used built-in `net` commands to enumerate local administrator groups.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT41](https://attack.mitre.org/groups/G0096) used HTTP to download payloads for CVE-2019-19781 and CVE-2020-10189 exploits.[^6]   |
| [[Network Share Discovery\|T1135]] | Network Share Discovery |  [APT41](https://attack.mitre.org/groups/G0096) used the `net share` command as part of network reconnaissance.[^9] [^10]  |
| [[Network Boundary Bridging\|T1599]] | Network Boundary Bridging | [APT41](https://attack.mitre.org/groups/G0096) used `NATBypass` to bypass firewall restrictions and to access compromised systems via RDP.[^2]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [APT41](https://attack.mitre.org/groups/G0096) has encrypted payloads using the Data Protection API (DPAPI), which relies on keys tied to specific user accounts on specific machines. [APT41](https://attack.mitre.org/groups/G0096) has also environmentally keyed second stage malware with an RC5 key derived in part from the infected system's volume serial number.[^18]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [APT41](https://attack.mitre.org/groups/G0096) used scheduled tasks created via Group Policy Objects (GPOs) to deploy ransomware.[^20]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [APT41](https://attack.mitre.org/groups/G0096) used the Acunetix SQL injection vulnerability scanner in target reconnaissance operations, as well as the JexBoss tool to identify vulnerabilities in Java applications.[^5]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT41](https://attack.mitre.org/groups/G0096) has uploaded files and data from a compromised host.[^10]  |
| [[External Remote Services\|T1133]] | External Remote Services | [APT41](https://attack.mitre.org/groups/G0096) compromised an online billing/payment service using VPN access between a third-party service provider and the targeted payment service.[^9] <br> |
| [[File Deletion\|T1070.004]] | File Deletion | [APT41](https://attack.mitre.org/groups/G0096) deleted files from the system.[^9] [^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT41](https://attack.mitre.org/groups/G0096) sent spearphishing emails with attachments such as compiled HTML (.chm) files to initially compromise their victims.[^9]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [APT41](https://attack.mitre.org/groups/G0096) developed a custom injector that enables an Event Tracing for Windows (ETW) bypass, making malicious processes invisible to Windows logging.[^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT41](https://attack.mitre.org/groups/G0096) used a compromised account to create a scheduled task on a system.[^9] [^15]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT41](https://attack.mitre.org/groups/G0096) created and modified startup files for persistence.[^9] [^10]  [APT41](https://attack.mitre.org/groups/G0096) added a registry key in `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost` to establish persistence for [Cobalt Strike](https://attack.mitre.org/software/S0154).[^6]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [APT41](https://attack.mitre.org/groups/G0096) leveraged sticky keys to establish persistence.[^9]   |
| [[Brute Force\|T1110]] | Brute Force | [APT41](https://attack.mitre.org/groups/G0096) performed password brute-force attacks on the local admin account.[^9]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [APT41](https://attack.mitre.org/groups/G0096) uses tools such as [Mimikatz](https://attack.mitre.org/software/S0002) to enable lateral movement via captured password hashes.[^5]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [APT41](https://attack.mitre.org/groups/G0096) has configured payloads to load via LD_PRELOAD.[^15] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT41](https://attack.mitre.org/groups/G0096) used `cmd.exe /c` to execute commands on remote machines.[^9] <br>[APT41](https://attack.mitre.org/groups/G0096) used a batch file to install persistence for the [Cobalt Strike](https://attack.mitre.org/software/S0154) BEACON loader.[^6]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [APT41](https://attack.mitre.org/groups/G0096) extracted user account data from the Security Account Managerr (SAM), making a copy of this database from the registry using the `reg save` command or by exploiting volume shadow copies.[^5]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [APT41](https://attack.mitre.org/groups/G0096) has used DGAs to change their C2 servers monthly.[^9]  |
| [[Service Execution\|T1569.002]] | Service Execution | [APT41](https://attack.mitre.org/groups/G0096) used  svchost.exe and [Net](https://attack.mitre.org/software/S0039) to execute a system service installed to launch a [Cobalt Strike](https://attack.mitre.org/software/S0154) BEACON loader.[^6] [^10]  |
| [[DNS\|T1071.004]] | DNS | [APT41](https://attack.mitre.org/groups/G0096) used DNS for C2 communications.[^9] [^10]   |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [APT41](https://attack.mitre.org/groups/G0096) used a malware variant called WIDETONE to conduct port scans on specified subnets.[^9]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT41](https://attack.mitre.org/groups/G0096) created a RAR archive of targeted files for exfiltration.[^9]  Additionally, [APT41](https://attack.mitre.org/groups/G0096) used the makecab.exe utility to both download tools, such as NATBypass, to the victim network and to archive a file for exfiltration.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT41](https://attack.mitre.org/groups/G0096) has used rundll32.exe to execute a loader.[^15]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [APT41](https://attack.mitre.org/groups/G0096) used legitimate websites for C2 through dead drop resolvers (DDR), including GitHub, Pastebin, and Microsoft TechNet.[^9]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [APT41](https://attack.mitre.org/groups/G0096) used the Steam community page as a fallback mechanism for C2.[^9]   |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [APT41](https://attack.mitre.org/groups/G0096) has obtained information about accounts, lists of employees, and plaintext and hashed passwords from databases.[^5]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [APT41](https://attack.mitre.org/groups/G0096) deployed a Monero cryptocurrency mining tool in a victim’s environment.[^9] [^20]  |
| [[NTDS\|T1003.003]] | NTDS | [APT41](https://attack.mitre.org/groups/G0096) used ntdsutil to obtain a copy of the victim environment `ntds.dit` file.[^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT41](https://attack.mitre.org/groups/G0096) has enumerated IP addresses of network resources and used the `netstat` command as part of network reconnaissance. The group has also used a malware variant, HIGHNOON, to enumerate active RDP sessions.[^9] [^10]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [APT41](https://attack.mitre.org/groups/G0096) used Linux shell commands for system survey and information gathering prior to exploitation of vulnerabilities such as CVE-2019-19871.[^6]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [APT41](https://attack.mitre.org/groups/G0096) used a ransomware called Encryptor RaaS to encrypt files on the targeted systems and provide a ransom note to the user.[^9]  [APT41](https://attack.mitre.org/groups/G0096) also used Microsoft Bitlocker to encrypt workstations and Jetico’s BestCrypt to encrypt servers.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [APT41](https://attack.mitre.org/groups/G0096) collected MAC addresses from victim machines.[^9] [^10]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT41](https://attack.mitre.org/groups/G0096) has executed `whoami` commands, including using the WMIEXEC utility to execute this on remote machines.[^9] [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT41](https://attack.mitre.org/groups/G0096) used [certutil](https://attack.mitre.org/software/S0160) to download additional files.[^6] [^15] [^10]  [APT41](https://attack.mitre.org/groups/G0096) downloaded post-exploitation tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) via command shell following initial access.[^5]  [APT41](https://attack.mitre.org/groups/G0096) has uploaded Procdump   and NATBypass to a staging directory and has used these tools in follow-on activities.[^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT41](https://attack.mitre.org/groups/G0096) leveraged the follow exploits in their operations: CVE-2012-0158, CVE-2015-1641, CVE-2017-0199, CVE-2017-11882, and CVE-2019-3396.[^9]   |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [APT41](https://attack.mitre.org/groups/G0096) used compiled HTML (.chm) files for targeting.[^9]   |
| [[Modify Registry\|T1112]] | Modify Registry | [APT41](https://attack.mitre.org/groups/G0096) used a malware variant called GOODLUCK to modify the registry in order to steal credentials.[^9] [^10]  |
| [[Proxy\|T1090]] | Proxy | [APT41](https://attack.mitre.org/groups/G0096) used a tool called CLASSFON to covertly proxy network communications.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT41](https://attack.mitre.org/groups/G0096) has used hashdump, [Mimikatz](https://attack.mitre.org/software/S0002), Procdump, and the Windows Credential Editor to dump password hashes from memory and authenticate to other user accounts.[^9] [^10] [^2]  |
| [[Impersonation\|T1684.001]] | Impersonation | [APT41](https://attack.mitre.org/groups/G0096) impersonated an employee at a video game developer company to send phishing emails.[^20]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [APT41](https://attack.mitre.org/groups/G0096) cloned victim user Git repositories during intrusions.[^5]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [APT41](https://attack.mitre.org/groups/G0096) used [BITSAdmin](https://attack.mitre.org/software/S0190) to download and install payloads.[^6] [^15]  |
| [[Query Registry\|T1012]] | Query Registry | [APT41](https://attack.mitre.org/groups/G0096) queried registry values to determine items such as configured RDP ports and network configurations.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT41](https://attack.mitre.org/groups/G0096) has executed `file /bin/pwd` on exploited victims, perhaps to return architecture related information.[^6]  |
| [[Process Injection\|T1055]] | Process Injection | [APT41](https://attack.mitre.org/groups/G0096) malware TIDYELF loaded the main WINTERLOVE component by injecting it into the iexplore.exe process.[^9]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [APT41](https://attack.mitre.org/groups/G0096) used RDP for lateral movement.[^9] [^15]  [APT41](https://attack.mitre.org/groups/G0096) used NATBypass to expose local RDP ports on compromised systems to the Internet.[^2]   |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [APT41](https://attack.mitre.org/groups/G0096) exploited CVE-2020-10189 against Zoho ManageEngine Desktop Central through unsafe deserialization, and CVE-2019-19781 to compromise Citrix Application Delivery Controllers (ADC) and gateway devices.[^6]  [APT41](https://attack.mitre.org/groups/G0096) leveraged vulnerabilities such as ProxyLogon exploitation or SQL injection for initial access.[^5]  [APT41](https://attack.mitre.org/groups/G0096) exploited CVE-2021-26855 against a vulnerable Microsoft Exchange Server to gain initial access to the victim network.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [APT41](https://attack.mitre.org/groups/G0096) uses remote shares to move and remotely execute payloads during lateral movemement.[^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [APT41](https://attack.mitre.org/groups/G0096) used VMProtected binaries in multiple intrusions.[^6]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [APT41](https://attack.mitre.org/groups/G0096) used the storescyncsvc.dll BEACON backdoor to download a secondary backdoor.[^6]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [APT41](https://attack.mitre.org/groups/G0096) transfers post-exploitation files dividing the payload into fixed-size chunks to evade detection.[^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [APT41](https://attack.mitre.org/groups/G0096) used WMI in several ways, including for execution of commands via WMIEXEC as well as for persistence via [PowerSploit](https://attack.mitre.org/software/S0194).[^9] [^10]  [APT41](https://attack.mitre.org/groups/G0096) has executed files through Windows Management Instrumentation (WMI).[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [APT41](https://attack.mitre.org/groups/G0096) used a keylogger called GEARSHIFT on a target system.[^9]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [APT41](https://attack.mitre.org/groups/G0096) attempted to remove evidence of some of its activity by deleting Bash histories.[^9]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [APT41](https://attack.mitre.org/groups/G0096) has created services to appear as benign system tools.[^10]  |
| [[DLL\|T1574.001]] | DLL | [APT41](https://attack.mitre.org/groups/G0096) has used search order hijacking to execute malicious payloads, such as [Winnti for Windows](https://attack.mitre.org/software/S0141).[^15]  [APT41](https://attack.mitre.org/groups/G0096) has also used legitimate executables to perform DLL side-loading of their malware.[^9]   |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^9]  |
| [[certutil\|S0160]] | certutil | [^6]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^9]  |
| [[Impacket\|S0357]] | Impacket | [APT41](https://attack.mitre.org/groups/G0096) used [Impacket](https://attack.mitre.org/software/S0357) to dump LSA secrets on one of the domain controllers in the victim network.[^2]  |
| [[ipconfig\|S0100]] | ipconfig | [^10]  |
| [[Empire\|S0363]] | Empire | [^15]  |
| [[dsquery\|S0105]] | dsquery | [^1]  |
| [[netstat\|S0104]] | netstat | [^9]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^6]  |
| [[sqlmap\|S0225]] | sqlmap | [^5]  |
| [[pwdump\|S0006]] | pwdump | [^9]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^9] [^10]  |
| [[Ping\|S0097]] | Ping | [^9] [^10]  |
| [[ftp\|S0095]] | ftp | [^6]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) is used by [APT41](https://attack.mitre.org/groups/G0096).[^11]  |
| [[DUSTPAN\|S1158]] | DUSTPAN | [DUSTPAN](https://attack.mitre.org/software/S1158) has been used by [APT41](https://attack.mitre.org/groups/G0096) in various campaigns since at least 2021.[^12] [^11]  |
| [[ASPXSpy\|S0073]] | ASPXSpy | [^9]  |
| [[China Chopper\|S0020]] | China Chopper | [APT41](https://attack.mitre.org/groups/G0096) used the `China Chopper` web shell as a persistence mechanism on compromised Microsoft Exchange servers.[^2] [^9]  |
| [[LightSpy\|S1185]] | LightSpy | [^14]  |
| [[PlugX\|S0013]] | PlugX | [APT41](https://attack.mitre.org/groups/G0096) used a variant of [PlugX](https://attack.mitre.org/software/S0013) to connect to Windows and Linux systems via SSH and Samba/CIFS.[^20] [^9]  |
| [[KEYPLUG\|S1051]] | KEYPLUG | [^1]  |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [^15]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^9]  |
| [[Derusbi\|S0021]] | Derusbi | [^9]  |
| [[MESSAGETAP\|S0443]] | MESSAGETAP | [^3] [^15]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^6] [^10]  |
| [[MOPSLED\|S1221]] | MOPSLED | [^13]  |
| [[ROCKBOOT\|S0112]] | ROCKBOOT | [^9]  |
| [[ZxShell\|S0412]] | ZxShell | [^9]  |
| [[BLACKCOFFEE\|S0069]] | BLACKCOFFEE | [^9]  |
| [[njRAT\|S0385]] | njRAT | [^9]  |
| [[ShadowPad\|S0596]] | ShadowPad | [^9] [^21]  |



## References

[^1]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^2]: [apt41_dcsocytec_dec2022](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)


[^3]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)


[^4]: BARIUM


[^5]: [Rostovcev APT41 2021](https://www.group-ib.com/blog/apt41-world-tour-2021/)


[^6]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: APT41


[^9]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^10]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^11]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^12]: [Google Cloud APT41 2022](https://cloud.google.com/blog/topics/threat-intelligence/apt41-us-state-governments)


[^13]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^14]: [MelikovBlackBerry LightSpy 2024](https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india)


[^15]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^16]: [FireEye APT41 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^17]: Wicked Panda


[^18]: [Twitter ItsReallyNick APT41 EK](https://x.com/ItsReallyNick/status/1189622925286084609)


[^19]: Brass Typhoon


[^20]: [apt41_mandiant](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^21]: [Recorded Future RedEcho Feb 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


