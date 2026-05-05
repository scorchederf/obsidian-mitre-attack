---
aliases: 
    - Volt Typhoon
    - BRONZE SILHOUETTE
    - Vanguard Panda
    - DEV-0391
    - UNC3236
    - Voltzite
    - Insidious Taurus
    - DazedToad
mitre-attack: https://attack.mitre.org/groups/G1017
---

## G1017

[Volt Typhoon](https://attack.mitre.org/groups/G1017) is a People's Republic of China (PRC) state-sponsored actor that has been active since at least 2021, primarily targeting critical infrastructure organizations in the US and its territories including Guam. [Volt Typhoon](https://attack.mitre.org/groups/G1017)'s targeting and pattern of behavior have been assessed as pre-positioning to enable lateral movement to operational technology (OT) assets for potential destructive or disruptive attacks. [Volt Typhoon](https://attack.mitre.org/groups/G1017) has emphasized stealth in operations using web shells, living-off-the-land (LOTL) binaries, hands on keyboard activities, and stolen credentials.[^12] [^1] [^8] [^13] . The group has leveraged compromised SOHO routers to proxy command and control traffic and obscure its infrastructure, activity associated with the KV botnet.[^3] . <br><br>Reporting indicates a separate initial access cluster, SYLVANITE, has been observed exploiting internet-facing edge devices and transferring access to [Volt Typhoon](https://attack.mitre.org/groups/G1017), also tracked as VOLTZITE, for follow-on operations. [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used commercial tools, LOTL utilities, and appliances already present on the system for network service discovery.[^12]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has enumerated directories containing vulnerability testing and cyber related content and facilities data such as construction drawings.[^12]  |
| [[Identify Roles\|T1591.004]] | Identify Roles | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has identified key network and IT staff members pre-compromise at targeted organizations.[^12] <br> |
| [[Process Discovery\|T1057]] | Process Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has enumerated running processes on targeted systems including through the use of [Tasklist](https://attack.mitre.org/software/S0057).[^1] [^13] [^12]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has moved laterally to the Domain Controller via RDP using a compromised account with domain administrator privileges.[^12]  |
| [[Server\|T1584.004]] | Server | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used compromised Paessler Router Traffic Grapher (PRTG) servers from other organizations for C2.[^13] [^12]  |
| [[Proxy\|T1090]] | Proxy | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used compromised devices and customized versions of open source tools  such as [FRP](https://attack.mitre.org/software/S1144) (Fast Reverse Proxy), Earthworm, and [Impacket](https://attack.mitre.org/software/S0357) to proxy network traffic.[^1] [^8] [^12]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has queried the Registry on compromised systems for information on installed software.[^8] [^12]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) relies primarily on valid credentials for persistence.[^12]  |
| [[Network Devices\|T1584.008]] | Network Devices | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has compromised small office and home office (SOHO) network edge devices, many of which were located in the same geographic area as the victim, to proxy network traffic.[^1] [^8]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has created and accessed a file named rult3uil.log on compromised domain controllers to capture keypresses and command execution.[^12]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used legitimate looking filenames for compressed copies of the ntds.dit database and used names including cisco_up.exe, cl64.exe, vm3dservice.exe, watchdogd.exe, Win.exe, WmiPreSV.exe, and WmiPrvSE.exe for the Earthworm and Fast Reverse Proxy tools.[^8] [^13] [^12]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has appended copies of the ntds.dit database with a .gif file extension.[^13]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used the Windows command line to perform hands-on-keyboard activities in targeted environments including for discovery.[^1] [^8] [^13] [^12] <br> |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has gained initial access through exploitation of multiple vulnerabilities in internet-facing software and appliances such as Fortinet, Ivanti (formerly Pulse Secure), NETGEAR, Citrix, and Cisco.[^13] [^12]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has attempted to obtain credentials from OpenSSH, realvnc, and PuTTY.[^8] <br> |
| [[Data Staged\|T1074]] | Data Staged | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has staged collected data in password-protected archives.[^1]  |
| [[Gather Victim Network Information\|T1590]] | Gather Victim Network Information | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted extensive pre-compromise reconnaissance to learn about the target organization’s network.[^12]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has archived the ntds.dit database as a multi-volume password-protected archive with 7-Zip.[^13] [^12]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained the victim's system timezone.[^12]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has run `net group` in compromised environments to discover domain groups.[^13]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has executed multiple commands to enumerate network topology and settings including  `ipconfig`, `netsh interface firewall show all`, and `netsh interface portproxy show all`.[^8]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used multiple methods, including [Ping](https://attack.mitre.org/software/S0097), to enumerate systems on compromised networks.[^1] [^13]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has leveraged WMIC for execution, remote system discovery, and to create and use temporary directories.[^1] [^8] [^13] [^12]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used VPNs to connect to victim environments and enable post-exploitation actions.[^12]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used Base64-encoded data to transfer payloads and commands, including deobfuscation via [certutil](https://attack.mitre.org/software/S0160).[^13]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has copied web shells between servers in targeted environments.[^13]  |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted pre-compromise web searches for victim information.[^12]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has discovered file system types, drive names, size, and free space on compromised systems.[^1] [^8] [^13] [^12]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has targeted the personal emails of key network and IT staff at victim organizations.[^12]  |
| [[System Checks\|T1497.001]] | System Checks | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has run system checks to determine if they were operating in a virtualized environment.[^1]  |
| [[NTDS\|T1003.003]] | NTDS | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used ntds.util to create domain controller installation media containing usernames and password hashes.[^1] [^8] [^13] [^12] <br> |
| [[Software Packing\|T1027.002]] | Software Packing | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used the Ultimate Packer for Executables (UPX) to obfuscate the FRP client files BrightmetricAgent.exe and SMSvcService.ex) and the port scanning utility ScanLine.[^12]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used a version of the Awen web shell that employed AES encryption and decryption for C2 communications.[^13]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has attempted to access hashed credentials from the LSASS process memory space.[^1] [^12] <br> |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has selectively cleared Windows Event Logs, system logs, and other technical artifacts to remove evidence of intrusion activity.[^12]  |
| [[Botnet\|T1584.005]] | Botnet | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used compromised Cisco and NETGEAR end-of-life SOHO routers implanted with KV Botnet malware to support operations.[^12] <br> |
| [[Gather Victim Host Information\|T1592]] | Gather Victim Host Information | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted pre-compromise reconnaissance for victim host information.[^12]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used `netstat -ano` on compromised hosts to enumerate network connections.[^8] [^13]                                                     |
| [[Local Account\|T1087.001]] | Local Account | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has executed `net user` and `quser` to enumerate local account information.[^12]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has targeted the browsing history of network administrators.[^12]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used PowerShell including for remote system discovery.[^1] [^8] [^12] <br> |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used `wevtutil.exe` and the PowerShell command `Get-EventLog security` to enumerate Windows logs to search for successful logons.[^8] [^12]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has gained initial access by exploiting privilege escalation vulnerabilities in the operating system or network services.[^12]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained a screenshot of the victim's system using the gdi32.dll and gdiplus.dll libraries.[^12]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used the built-in [netsh](https://attack.mitre.org/software/S0108) `port proxy` command to create proxies on compromised systems to facilitate access.[^1] [^12]  |
| [[Exploits\|T1587.004]] | Exploits | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has exploited zero-day vulnerabilities for initial access.[^12]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used multi-hop proxies for command-and-control infrastructure.[^12]  |
| [[Search Victim-Owned Websites\|T1594]] | Search Victim-Owned Websites | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted pre-compromise reconnaissance on victim-owned sites.[^12]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used public tools and executed the PowerShell command `Get-EventLog security -instanceid 4624` to identify associated user and computer account names.[^8] [^13] [^12]  |
| [[Modify Registry\|T1112]] | Modify Registry | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used `netsh` to create a PortProxy Registry modification on a compromised server running the Paessler Router Traffic Grapher (PRTG).[^12]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used webshells, including ones named AuditReport.jspx and iisstart.aspx, in compromised environments.[^13]  |
| [[System Binary Proxy Execution\|T1218]] | System Binary Proxy Execution | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used native tools and processes including living off the land binaries or “LOLBins" to maintain and expand access to the victim networks.[^12]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used Brightmetricagent.exe which contains a command- line interface (CLI) library that can leverage command shells including Z Shell (zsh).[^12]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used `net start` to list running services.[^12]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used commercial tools, LOTL utilities, and appliances already present on the system for group and user discovery.[^12]  |
| [[Virtual Private Server\|T1584.003]] | Virtual Private Server | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has compromised Virtual Private Servers (VPS) to proxy C2 traffic.[^12]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | <br><br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has targeted network administrator browser data including browsing history and stored credentials.[^12] <br> |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted extensive reconnaissance pre-compromise to gain information about the targeted organization.[^12]  |
| [[Network Topology\|T1590.004]] | Network Topology | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has conducted extensive reconnaissance of victim networks including identifying network topologies.[^12]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has collected window title information from compromised systems.[^12] <br> |
| [[Local Groups\|T1069.001]] | Local Groups | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has run `net localgroup administrators` in compromised environments to enumerate accounts.[^8] <br> |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained victim's screen dimension and display device information.[^12]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has run `rd /S` to delete their working directories and deleted systeminfo.dat from `C:\Users\Public\Documentsfiles`.[^13] [^12] <br> |
| [[Vulnerabilities\|T1588.006]] | Vulnerabilities | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used publicly available exploit code for initial access.[^12]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has downloaded an outdated version of comsvcs.dll to a compromised domain controller in a non-standard folder.[^12]  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained credentials insecurely stored on targeted network appliances.[^12]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used compromised domain accounts to authenticate to devices on compromised networks.[^1] [^13] [^12]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has stolen files from a sensitive file server and the Active Directory database from targeted environments, and used [Wevtutil](https://attack.mitre.org/software/S0645) to extract event log information.[^8] [^13] [^12]  |
| [[Direct Volume Access\|T1006]] | Direct Volume Access | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has executed the Windows-native `vssadmin` command to create volume shadow copies.[^12]  |
| [[Query Registry\|T1012]] | Query Registry | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has queried the Registry on compromised systems, `reg query hklm\software\`, for information on installed software including PuTTY.[^8] [^12]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has gathered victim identify information during pre-compromise reconnaissance. [^12]  |
| [[Tool\|T1588.002]] | Tool | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used legitimate network and forensic tools and customized versions of open-source tools for C2.[^1] [^12]  |
| [[Scan Databases\|T1596.005]] | Scan Databases | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used FOFA, Shodan, and Censys to search for exposed victim infrastructure.[^12]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has run `net group /dom` and `net group "Domain Admins" /dom` in compromised environments for account discovery.[^8] [^13]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained the victim's system current location.[^12]  |
| [[Clear Network Connection History and Configurations\|T1070.007]] | Clear Network Connection History and Configurations | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has inspected server logs to remove their IPs.[^13]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has employed [Ping](https://attack.mitre.org/software/S0097) to check network connectivity.[^12]  |
| [[Private Keys\|T1552.004]] | Private Keys | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has accessed a Local State file that contains the AES key used to encrypt passwords stored in the Chrome browser.[^12]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has saved stolen files including the `ntds.dit` database and the `SYSTEM` and `SECURITY` Registry hives locally to the `C:\Windows\Temp\` directory.[^8] [^13]  |
| [[Network Security Appliances\|T1590.006]] | Network Security Appliances | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has identified target network security measures as part of pre-compromise reconnaissance.[^12]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^13] [^12]  |
| [[certutil\|S0160]] | certutil | [^13] [^12]  |
| [[Impacket\|S0357]] | Impacket | [^1] [^8] [^12]  |
| [[ipconfig\|S0100]] | ipconfig | [^8]  |
| [[Tasklist\|S0057]] | Tasklist | [^8] [^13] [^12]  |
| [[FRP\|S1144]] | FRP | [^1] [^8]  |
| [[netstat\|S0104]] | netstat | [^13] [^12]  |
| [[netsh\|S0108]] | netsh | [^1] [^8] [^12]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^8] [^13] [^12]  |
| [[Nltest\|S0359]] | Nltest | [^13] [^12]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^8] [^12]  |
| [[Ping\|S0097]] | Ping | [^1] [^12]  |
| [[cmd\|S0106]] | cmd | [^12]  |
| [[Reg\|S0075]] | Reg | [^12]  |
| [[Wevtutil\|S0645]] | Wevtutil | [^8] [^12]  |
| [[PsExec\|S0029]] | PsExec | [^12] <br> |
| [[VersaMem\|S1154]] | VersaMem | [VersaMem](https://attack.mitre.org/software/S1154) was used by [Volt Typhoon](https://attack.mitre.org/groups/G1017) as part of [Versa Director Zero Day Exploitation](https://attack.mitre.org/campaigns/C0039).[^5]  |



## References

[^1]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^2]: UNC3236


[^3]: [DOJ KVBotnet 2024](https://www.justice.gov/opa/pr/us-government-disrupts-botnet-peoples-republic-china-used-conceal-hacking-critical)


[^4]: Voltzite


[^5]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)


[^6]: Vanguard Panda


[^7]: [Dragos 2025 Year in Review](https://5943619.hs-sites.com/hubfs/312-Year-in-Review/2026/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf?hsCtaAttrib=205683189348)


[^8]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^9]: DazedToad


[^10]: Insidious Taurus


[^11]: BRONZE SILHOUETTE


[^12]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^13]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^14]: DEV-0391


[^15]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


