---
aliases: 
    - APT39
    - ITG07
    - Chafer
    - Remix Kitten
mitre-attack: https://attack.mitre.org/groups/G0087
---

## G0087

[APT39](https://attack.mitre.org/groups/G0087) is one of several names for cyber espionage activity conducted by the Iranian Ministry of Intelligence and Security (MOIS) through the front company Rana Intelligence Computing since at least 2014. [APT39](https://attack.mitre.org/groups/G0087) has primarily targeted the travel, hospitality, academic, and telecommunications industries in Iran and across Asia, Africa, Europe, and North America to track individuals and entities considered to be a threat by the MOIS.[^12] [^7] [^8] [^3] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used [CrackMapExec](https://attack.mitre.org/software/S0488) and a custom port scanner known as BLUETORCH for network scanning.[^12] [^14]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT39](https://attack.mitre.org/groups/G0087) has maintained persistence using the startup folder.[^12]  |
| [[External Proxy\|T1090.002]] | External Proxy | [APT39](https://attack.mitre.org/groups/G0087) has used various tools to proxy C2 communications.[^14]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [APT39](https://attack.mitre.org/groups/G0087) has used malware to decrypt encrypted CAB files.[^8]  |
| [[Keylogging\|T1056.001]] | Keylogging | [APT39](https://attack.mitre.org/groups/G0087) has used tools for capturing keystrokes.[^6] [^8]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT39](https://attack.mitre.org/groups/G0087) has used various tools to steal files from the compromised host.[^6] [^8]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT39](https://attack.mitre.org/groups/G0087) has used PowerShell to execute malicious code.[^14] [^6]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [APT39](https://attack.mitre.org/groups/G0087) has used tools capable of stealing contents of the clipboard.[^6]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [APT39](https://attack.mitre.org/groups/G0087) has used different versions of Mimikatz to obtain credentials.[^14]  |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | [APT39](https://attack.mitre.org/groups/G0087) has used malware to turn off the `RequireSigned` feature which ensures only signed DLLs can be run on Windows.[^8]  |
| [[AppInit DLLs\|T1546.010]] | AppInit DLLs | [APT39](https://attack.mitre.org/groups/G0087) has used malware to set `LoadAppInit_DLLs` in the Registry key `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows` in order to establish persistence.[^8]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [APT39](https://attack.mitre.org/groups/G0087) has modified LNK shortcuts.[^12]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used the post exploitation tool [CrackMapExec](https://attack.mitre.org/software/S0488) to enumerate network shares.[^14]  |
| [[Service Execution\|T1569.002]] | Service Execution | [APT39](https://attack.mitre.org/groups/G0087) has used post-exploitation tools including RemCom and the Non-sucking Service Manager (NSSM) to execute processes.[^14] [^6]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT39](https://attack.mitre.org/groups/G0087) has used malware to drop encrypted CAB files.[^8]  |
| [[Tool\|T1588.002]] | Tool | [APT39](https://attack.mitre.org/groups/G0087) has modified and used customized versions of publicly-available tools like PLINK and [Mimikatz](https://attack.mitre.org/software/S0002).[^14] [^1]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [APT39](https://attack.mitre.org/groups/G0087) has been seen using RDP for lateral movement and persistence, in some cases employing the rdpwinst tool for mangement of multiple sessions.[^12] [^14]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT39](https://attack.mitre.org/groups/G0087) used [Remexi](https://attack.mitre.org/software/S0375) to collect usernames from the system.[^7]  |
| [[Software Packing\|T1027.002]] | Software Packing | [APT39](https://attack.mitre.org/groups/G0087) has packed tools with UPX, and has repacked a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) to thwart anti-virus detection.[^12] [^14]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [APT39](https://attack.mitre.org/groups/G0087) has exfiltrated stolen victim data through C2 communications.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT39](https://attack.mitre.org/groups/G0087) has sent spearphishing emails in an attempt to lure users to click on a malicious attachment.[^12] [^14] [^6] [^8]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT39](https://attack.mitre.org/groups/G0087) has created scheduled tasks for persistence.[^12] [^14] [^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT39](https://attack.mitre.org/groups/G0087) has used malware to delete files after they are deployed on a compromised host.[^8]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [APT39](https://attack.mitre.org/groups/G0087) has communicated with C2 through files uploaded to and downloaded from DropBox.[^14]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT39](https://attack.mitre.org/groups/G0087) has used WinRAR and 7-Zip to compress an archive stolen data.[^12]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT39](https://attack.mitre.org/groups/G0087) has installed ANTAK and ASPXSPY web shells.[^12]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT39](https://attack.mitre.org/groups/G0087) has downloaded tools to compromised hosts.[^6] [^8]  |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | [APT39](https://attack.mitre.org/groups/G0087) has utilized AutoIt malware scripts embedded in Microsoft Office documents or malicious links.[^8]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT39](https://attack.mitre.org/groups/G0087) has sent spearphishing emails in an attempt to lure users to click on a malicious link.[^12] [^8]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [APT39](https://attack.mitre.org/groups/G0087) has used the Smartftp Password Decryptor tool to decrypt FTP passwords.[^14]  |
| [[Screen Capture\|T1113]] | Screen Capture | [APT39](https://attack.mitre.org/groups/G0087) has used a screen capture utility to take screenshots on a compromised host.[^6] [^8]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT39](https://attack.mitre.org/groups/G0087) has used Mimikatz, Windows Credential Editor and ProcDump to dump credentials.[^12]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used [NBTscan](https://attack.mitre.org/software/S0590) and custom tools to discover remote systems.[^12] [^14] [^6]  |
| [[DNS\|T1071.004]] | DNS | [APT39](https://attack.mitre.org/groups/G0087) has used remote access tools that leverage DNS in communications with C2.[^14]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [APT39](https://attack.mitre.org/groups/G0087) has utilized custom scripts to perform internal reconnaissance.[^12] [^8]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [APT39](https://attack.mitre.org/groups/G0087) has utilized tools to aggregate data prior to exfiltration.[^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT39](https://attack.mitre.org/groups/G0087) has used tools with the ability to search for files on a compromised host.[^8]  |
| [[Query Registry\|T1012]] | Query Registry | [APT39](https://attack.mitre.org/groups/G0087) has used various strains of malware to query the Registry.[^8]  |
| [[Brute Force\|T1110]] | Brute Force | [APT39](https://attack.mitre.org/groups/G0087) has used Ncrack to reveal credentials.[^12]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [APT39](https://attack.mitre.org/groups/G0087) has used the BITS protocol to exfiltrate stolen data from a compromised host.[^8]  |
| [[Local Account\|T1136.001]] | Local Account | [APT39](https://attack.mitre.org/groups/G0087) has created accounts on multiple compromised hosts to perform actions within the network.[^14]  |
| [[Python\|T1059.006]] | Python | [APT39](https://attack.mitre.org/groups/G0087) has used a command line utility and a network scanner written in python.[^14] [^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT39](https://attack.mitre.org/groups/G0087) has used malware disguised as Mozilla Firefox and a tool named mfevtpse.exe to proxy C2 communications, closely mimicking a legitimate McAfee file mfevtps.exe.[^14] [^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT39](https://attack.mitre.org/groups/G0087) has used HTTP in communications with C2.[^14] [^8]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [APT39](https://attack.mitre.org/groups/G0087) used custom tools to create SOCK5 and custom protocol proxies between infected hosts.[^12] [^14]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [APT39](https://attack.mitre.org/groups/G0087) has used stolen credentials to compromise Outlook Web Access (OWA).[^12]  |
| [[Input Capture\|T1056]] | Input Capture | [APT39](https://attack.mitre.org/groups/G0087) has utilized tools to capture mouse movements.[^8]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT39](https://attack.mitre.org/groups/G0087) leveraged spearphishing emails with malicious links to initially compromise victims.[^12] [^8]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT39](https://attack.mitre.org/groups/G0087) leveraged spearphishing emails with malicious attachments to initially compromise victims.[^12] [^6] [^8]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [APT39](https://attack.mitre.org/groups/G0087) has used SMB for lateral movement.[^6]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [APT39](https://attack.mitre.org/groups/G0087) has used SQL injection for initial compromise.[^6]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT39](https://attack.mitre.org/groups/G0087) has utilized malicious VBS scripts in malware.[^8]  |
| [[SSH\|T1021.004]] | SSH | [APT39](https://attack.mitre.org/groups/G0087) used secure shell (SSH) to move laterally among their targets.[^12]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^12] [^9]  |
| [[pwdump\|S0006]] | pwdump | [^6]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^12] [^14] [^9] [^6]  |
| [[NBTscan\|S0590]] | NBTscan | [^12]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [^12] [^14]  |
| [[ftp\|S0095]] | ftp | [^8]  |
| [[PsExec\|S0029]] | PsExec | [^12] [^14] [^6]  |
| [[ASPXSpy\|S0073]] | ASPXSpy | [^12]  |
| [[Cadelspy\|S0454]] | Cadelspy | [^7]  |
| [[MechaFlounder\|S0459]] | MechaFlounder | [^11]  |
| [[Remexi\|S0375]] | Remexi | [^7] [^5] [^6]  |



## References

[^1]: [IBM ITG07 June 2019](https://securityintelligence.com/posts/observations-of-itg07-cyber-operations/)


[^2]: ITG07


[^3]: [Dept. of Treasury Iran Sanctions September 2020](https://home.treasury.gov/news/press-releases/sm1127)


[^4]: [DOJ Iran Indictments September 2020](https://www.justice.gov/opa/pr/department-justice-and-partner-departments-and-agencies-conduct-coordinated-actions-disrupt)


[^5]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^6]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


[^7]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


[^8]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^9]: [Dark Reading APT39 JAN 2019](https://www.darkreading.com/attacks-breaches/iran-ups-its-traditional-cyber-espionage-tradecraft/d/d-id/1333764)


[^10]: Remix Kitten


[^11]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^12]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^13]: APT39


[^14]: [BitDefender Chafer May 2020](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)


[^15]: Chafer


[^16]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


