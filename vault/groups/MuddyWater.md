---
aliases: 
    - MuddyWater
    - Earth Vetala
    - MERCURY
    - Static Kitten
    - Seedworm
    - TEMP.Zagros
    - Mango Sandstorm
    - TA450
    - MuddyKrill
mitre-attack: https://attack.mitre.org/groups/G0069
---

## G0069

[MuddyWater](https://attack.mitre.org/groups/G0069) is a cyber espionage group assessed to be a subordinate element within Iran's Ministry of Intelligence and Security (MOIS).[^10]  Since at least 2017, [MuddyWater](https://attack.mitre.org/groups/G0069) has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. [MuddyWater](https://attack.mitre.org/groups/G0069) has reused domains dating back to October 2025, and has a preference for NameCheap and Hosterdaddy Private Limited (AS136557). In late 2025 and early 2026, [MuddyWater](https://attack.mitre.org/groups/G0069) used commercial satellite internet (i.e., Starlink) for command and control (C2) communication. [^1] [^34] [^25] [^12] [^29] [^31] [^2] [^8] [^35] [^33] [^36] [^37]    

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [MuddyWater](https://attack.mitre.org/groups/G0069) has sent targeted spearphishing e-mails with malicious links.[^24] [^28] [^21]  |
| [[Office Template Macros\|T1137.001]] | Office Template Macros | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a Word Template, Normal.dotm, for persistence.[^2]  |
| [[DLL\|T1574.001]] | DLL | [MuddyWater](https://attack.mitre.org/groups/G0069) maintains persistence on victim networks through side-loading dlls to trick legitimate programs into running malware.[^8]  |
| [[Tool\|T1588.002]] | Tool | MuddyWater has used legitimate tools [ConnectWise](https://attack.mitre.org/software/S0591), [RemoteUtilities](https://attack.mitre.org/software/S0592), and SimpleHelp to gain access to the target environment.[^24] [^22] [^36] [^33]  |
| [[Mshta\|T1218.005]] | Mshta | [MuddyWater](https://attack.mitre.org/groups/G0069) has used mshta.exe to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload and to pass a PowerShell one-liner for execution.[^14] [^18]  |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | [MuddyWater](https://attack.mitre.org/groups/G0069) has leveraged ClickFix type tactics enticing victims to copy and paste malicious PowerShell code.[^33]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that leveraged WMI for execution and querying host information.[^18] [^29] [^15] [^8]  |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [MuddyWater](https://attack.mitre.org/groups/G0069) has used compromised mailboxes within target organizations to send spearphishing emails.[^1]     |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349).[^25] [^12]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [MuddyWater](https://attack.mitre.org/groups/G0069) has compromised third parties and used compromised accounts to send spearphishing emails with targeted attachments to recipients.[^25] [^14] [^18] [^31] [^24] [^28] [^8] [^21] [^36] [^3]  [MuddyWater](https://attack.mitre.org/groups/G0069) has also sent spearphishing emails with the attachment Cybersecurity.doc, which served as the primarily payload for the next stage.[^13]   |
| [[Domains\|T1583.001]] | Domains | [MuddyWater](https://attack.mitre.org/groups/G0069) has established domains, some of which appeared to spoof legitimate domains for use in operations.[^33]   |
| [[Network Topology\|T1590.004]] | Network Topology | [MuddyWater](https://attack.mitre.org/groups/G0069) has mapped target networks; access to this information and more is then shared/sold to other Iran threat actors.[^7]   |
| [[Component Object Model\|T1559.001]] | Component Object Model | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that has the capability to execute malicious code via COM, DCOM, and Outlook.[^18] [^31] [^8]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [MuddyWater](https://attack.mitre.org/groups/G0069) has used ports 8043 and 8848 for botnet C2 communication.[^7]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a custom tool for creating reverse shells.[^12]  |
| [[Malware\|T1588.001]] | Malware | [MuddyWater](https://attack.mitre.org/groups/G0069) has used publicly available malware for operations, likely to blend in with other cybercriminals.[^34]   |
| [[CMSTP\|T1218.003]] | CMSTP | [MuddyWater](https://attack.mitre.org/groups/G0069) has used CMSTP.exe and a malicious INF to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload.[^14]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [MuddyWater](https://attack.mitre.org/groups/G0069) has disguised malicious executables and used filenames and Registry key names associated with Windows Defender.[^14] [^15] [^24]  |
| [[Domain Account\|T1087.002]] | Domain Account | [MuddyWater](https://attack.mitre.org/groups/G0069) has used `cmd.exe net user /domain` to enumerate domain users.[^28]  |
| [[JavaScript\|T1059.007]] | JavaScript | [MuddyWater](https://attack.mitre.org/groups/G0069) has used JavaScript files to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload.[^29] [^14] [^8]  |
| [[Web Services\|T1583.006]] | Web Services | [MuddyWater](https://attack.mitre.org/groups/G0069) has used file sharing services including OneHub, Sync, and TeraBox to distribute tools.[^24] [^28] [^21] [^36]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [MuddyWater](https://attack.mitre.org/groups/G0069) has used VBScript files to execute its [POWERSTATS](https://attack.mitre.org/software/S0223) payload, as well as macros.[^14] [^38] [^18] [^12] [^29] [^31] [^2] [^28] [^35]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to collect the victim’s IP address and domain name.[^18]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [MuddyWater](https://attack.mitre.org/groups/G0069) has added Registry Run key `KCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemTextEncoding` to establish persistence.[^14] [^18] [^15] [^2] [^28] [^35]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MuddyWater](https://attack.mitre.org/groups/G0069) has decoded base64-encoded PowerShell, JavaScript, and VBScript.[^14] [^38] [^29] [^35]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can execute PowerShell scripts via DDE.[^18]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used Daniel Bohannon’s Invoke-Obfuscation framework and obfuscated PowerShell scripts.[^25] [^32]  The group has also used other obfuscation methods, including Base64 obfuscation of VBScripts and PowerShell commands.[^25] [^14] [^18] [^15] [^31] [^28] [^35]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used the .NET csc.exe tool to compile executables from downloaded C# code.[^29]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to check running processes against a hard-coded list of security tools often used by malware researchers.[^18]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MuddyWater](https://attack.mitre.org/groups/G0069) has stored a decoy PDF file within a victim's `%temp%` folder.[^35]  |
| [[Screen Capture\|T1113]] | Screen Capture | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can capture screenshots of the victim’s machine.[^18]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MuddyWater](https://attack.mitre.org/groups/G0069) has used HTTP for C2 communications.[^31] [^28]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [MuddyWater](https://attack.mitre.org/groups/G0069) can disable the system's local proxy settings.[^28]  |
| [[Software Discovery\|T1518]] | Software Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a PowerShell backdoor to check for Skype connectivity on the target machine.[^28]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that checked if the ProgramData folder had folders or files with the keywords "Kasper," "Panda," or "ESET."[^18]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [MuddyWater](https://attack.mitre.org/groups/G0069) uses various techniques to bypass UAC.[^29] [^33]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can upload additional files to the victim’s machine.[^18] [^29] [^2] [^28]  [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell commands to install remote management and monitoring (RMM) software on the victim’s machine to conduct espionage and to exfiltrate data.[^33]   |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [MuddyWater](https://attack.mitre.org/groups/G0069) has used AES to encrypt C2 responses.[^35]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [MuddyWater](https://attack.mitre.org/groups/G0069) has attempted to exfiltrate data to Wasabi, a cloud storage service, using [Rclone](https://attack.mitre.org/software/S1040).[^3]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [MuddyWater](https://attack.mitre.org/groups/G0069) has run tools including Browser64 to steal passwords saved in victim web browsers.[^12] [^28]  |
| [[Phishing\|T1566]] | Phishing | [MuddyWater](https://attack.mitre.org/groups/G0069) has sent phishing emails to targets from the email address support@microsoftonlines[.]com.[^33]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [MuddyWater](https://attack.mitre.org/groups/G0069) has used the native Windows cabinet creation tool, makecab.exe, likely to compress stolen data to be uploaded.[^12]  |
| [[Impersonation\|T1684.001]] | Impersonation | [MuddyWater](https://attack.mitre.org/groups/G0069) has used support@microsoftonlines[.]com to send phishing emails that masqueraded as security updates from Microsoft.[^33]  [MuddyWater](https://attack.mitre.org/groups/G0069) has also impersonated TMCell (Altyn Asyr CJSC), the primary mobile operator in Turkmenistan, sending phishing emails with the email domain info@tmcell.[^13]   |
| [[Python\|T1059.006]] | Python | [MuddyWater](https://attack.mitre.org/groups/G0069) has developed tools in Python including [Out1](https://attack.mitre.org/software/S0594).[^28]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a PowerShell backdoor to check for Skype connections on the target machine.[^28]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s OS version and machine name.[^18] [^15] [^2] [^28] [^35]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349) and other tools, including by dumping passwords saved in victim email.[^25] [^12] [^28]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to obtain a list of running processes on the system.[^18] [^31]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [MuddyWater](https://attack.mitre.org/groups/G0069) has used tools to encode C2 communications including Base64 encoding.[^31] [^28]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [MuddyWater](https://attack.mitre.org/groups/G0069) has used one C2 to obtain enumeration scripts and monitor web logs, but a different C2 to send data back.[^15]   |
| [[Proxy\|T1090]] | Proxy | [MuddyWater](https://attack.mitre.org/groups/G0069) has used NordVPN to proxy phishing emails, making them appear to originate from France.[^1]     |
| [[Malicious Link\|T1204.001]] | Malicious Link | [MuddyWater](https://attack.mitre.org/groups/G0069) has distributed URLs in phishing e-mails that link to lure documents.[^24] [^28] [^21]  |
| [[Steganography\|T1027.003]] | Steganography | [MuddyWater](https://attack.mitre.org/groups/G0069) has stored obfuscated JavaScript code in an image file named temp.jpg.[^29]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [Mimikatz](https://attack.mitre.org/software/S0002) and procdump64.exe.[^25] [^12] [^28]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [MuddyWater](https://attack.mitre.org/groups/G0069) has used scheduled tasks to establish persistence.[^2]  |
| [[External Proxy\|T1090.002]] | External Proxy | [MuddyWater](https://attack.mitre.org/groups/G0069) has controlled [POWERSTATS](https://attack.mitre.org/software/S0223) from behind a proxy network to obfuscate the C2 location.[^12]  [MuddyWater](https://attack.mitre.org/groups/G0069) has used a series of compromised websites that victims connected to randomly to relay information to command and control (C2).[^2] [^28]  [MuddyWater](https://attack.mitre.org/groups/G0069) has also used go-socks5 variants to bypass firewalls and Network Address Translation (NAT), to communicate with a hardcoded C2 server, and to exfiltrate data.[^36]     |
| [[Malicious File\|T1204.002]] | Malicious File | [MuddyWater](https://attack.mitre.org/groups/G0069) has attempted to get users to open malicious PDF attachment and to enable macros and launch malicious Microsoft Word documents delivered via spearphishing emails.[^25] [^14] [^18] [^15] [^31] [^2] [^24] [^28] [^8] [^35] [^21]  Additionally, [MuddyWater](https://attack.mitre.org/groups/G0069) has used a Word document with a malicious Visual Basic for Applications (VBA) macro; when enabled, the CertificationKit.ini payload is constructed and executed.[^13]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s username.[^18] [^28]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [MuddyWater](https://attack.mitre.org/groups/G0069) has leveraged RMM solutions including ScreenConnect, AteraAgent, SimpleHelp, Action1, Level, and PDQ to facilitate follow-on actions within compromised hosts to include data exfiltration.[^28] [^24] [^21] [^22] [^1] [^33] [^7]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MuddyWater](https://attack.mitre.org/groups/G0069) has used C2 infrastructure to receive exfiltrated data.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell for execution.[^14] [^38] [^18] [^12] [^29] [^15] [^2] [^28] [^8] [^35] [^33]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [MuddyWater](https://attack.mitre.org/groups/G0069) has used web services including OneHub to distribute remote access tools.[^24]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that leveraged rundll32.exe in a Registry Run key to execute a .dll.[^18]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [MuddyWater](https://attack.mitre.org/groups/G0069) has run a tool that steals passwords saved in victim email.[^12]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Microsoft Exchange memory corruption vulnerability (CVE-2020-0688).[^8]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Microsoft Netlogon vulnerability (CVE-2020-1472).[^8]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [MuddyWater](https://attack.mitre.org/groups/G0069) has exploited the Office vulnerability CVE-2017-0199 for execution.[^31]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [MuddyWater](https://attack.mitre.org/groups/G0069) has performed credential dumping with [LaZagne](https://attack.mitre.org/software/S0349).[^25] [^12]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[RemoteUtilities\|S0592]] | RemoteUtilities | [^28]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^17]  |
| [[Empire\|S0363]] | Empire | [^17]  |
| [[Rclone\|S1040]] | Rclone | [^3]   |
| [[Out1\|S0594]] | Out1 | [^28]  |
| [[ConnectWise\|S0591]] | ConnectWise | [^24] [^28]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^25] [^17]  |
| [[LaZagne\|S0349]] | LaZagne | [^12] [^17]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [^17] [^12]  |
| [[Koadic\|S0250]] | Koadic | [^2] [^17]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [^6]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [^17]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyWater](https://attack.mitre.org/groups/G0069) has used [MuddyViper](https://attack.mitre.org/software/S9032) during operations.[^36]    |
| [[Fooder\|S9033]] | Fooder | [MuddyWater](https://attack.mitre.org/groups/G0069) has used [Fooder](https://attack.mitre.org/software/S9033) during operations.[^36]    |
| [[Mori\|S1047]] | Mori | [^8]  |
| [[LP-Notes\|S9036]] | LP-Notes | [MuddyWater](https://attack.mitre.org/groups/G0069) has used [LP-Notes](https://attack.mitre.org/software/S9036) during operations.[^36]    |
| [[PowGoop\|S1046]] | PowGoop | [^8]  |
| [[STARWHALE\|S1037]] | STARWHALE | [^8]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [^25] [^14] [^29] [^12] [^31]  |
| [[Small Sieve\|S1035]] | Small Sieve | [^8] [^9]  |



## References

[^1]: [FalconFeeds_Iran_Mar2026](https://falconfeeds.io/blogs/the-digital-redoubt-irans-national-information-network-cyber-conflict)


[^2]: [Reaqta MuddyWater November 2017](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)


[^3]: [SOCRadar_MuddyWaterDindoor_Mar2026](https://socradar.io/blog/iran-muddywater-dindoor-malware-us-networks/)


[^4]: Mango Sandstorm


[^5]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^6]: [Checkpoint_MOISCyberCrime_Mar2026](https://research.checkpoint.com/2026/iranian-mois-actors-the-cyber-crime-connection/)


[^7]: [FalconFeeds_MuddyWaterPSRust_Mar2026](https://falconfeeds.io/blogs/muddywater-in-the-iran-israel-cyber-war-from-powershell-scripts-to-rust-implants)


[^8]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^9]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^10]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)


[^11]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


[^12]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


[^13]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^14]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^15]: [Talos MuddyWater May 2019](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)


[^16]: Earth Vetala


[^17]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^18]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^19]: MuddyKrill


[^20]: Seedworm


[^21]: [Proofpoint TA450 Phishing March 2024](https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta450-uses-embedded-links-pdf-attachments-latest-campaign)


[^22]: [group-ib_muddywater_infra](https://www.group-ib.com/blog/muddywater-infrastructure/)


[^23]: TA450


[^24]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)


[^25]: [Unit 42 MuddyWater Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/)


[^26]: TEMP.Zagros


[^27]: MuddyWater


[^28]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^29]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)


[^30]: Static Kitten


[^31]: [ClearSky MuddyWater June 2019](https://www.clearskysec.com/wp-content/uploads/2019/06/Clearsky-Iranian-APT-group-%E2%80%98MuddyWater%E2%80%99-Adds-Exploits-to-Their-Arsenal.pdf)


[^32]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^33]: [NaumaanProofpoint_GlobalClickFix_April2025](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)


[^34]: [Huntio_IranInfra_Mar2026](https://hunt.io/blog/iranian-apt-infrastructure-state-aligned-clusters)


[^35]: [Talos MuddyWater Jan 2022](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)


[^36]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^37]: [SymantecCarbonBlack_Seedworm_Mar2026](https://www.security.com/threat-intelligence/iran-cyber-threat-activity-us)


[^38]: [MuddyWater TrendMicro June 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/another-potential-muddywater-campaign-uses-powershell-based-prb-backdoor/)


[^39]: MERCURY


