---
aliases: 
    - Threat Group-3390
    - Earth Smilodon
    - TG-3390
    - Emissary Panda
    - BRONZE UNION
    - APT27
    - Iron Tiger
    - LuckyMouse
    - Linen Typhoon
mitre-attack: https://attack.mitre.org/groups/G0027
---

## G0027

[Threat Group-3390](https://attack.mitre.org/groups/G0027) is a Chinese threat group that has extensively used strategic Web compromises to target victims.[^1]  The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.[^23] [^11] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used CVE-2014-6324 and CVE-2017-0213 to escalate privileges.[^23] [^16]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have split RAR files for exfiltration into parts.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited the Microsoft SharePoint vulnerability CVE-2019-0604 and CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065 in Exchange Server.[^19]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use the Hunter tool to conduct network service discovery for vulnerable systems.[^1] [^15]  |
| [[At\|T1053.002]] | At | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use [at](https://attack.mitre.org/software/S0110) to schedule tasks to run self-extracting RAR archives, which install [HTTPBrowser](https://attack.mitre.org/software/S0070) or [PlugX](https://attack.mitre.org/software/S0013) on other victims on a network.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can spawn `svchost.exe` and inject the payload into that process.[^10] [^11]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has locally staged encrypted archives for later exfiltration efforts.[^23]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited CVE-2018-0798 in Equation Editor.[^19]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exfiltrated stolen data to Dropbox.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) called Wrapikatz to dump credentials. They have also dumped credentials from domain controllers.[^1] [^23]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used command-line interfaces for execution.[^23] [^15]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Threat Group-3390](https://attack.mitre.org/groups/G0027) obtained a KeePass database from a compromised host.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used e-mail to deliver malicious attachments to victims.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can read and decrypt stored Registry values.[^10]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used [gsecdump](https://attack.mitre.org/software/S0008) to dump credentials. They have also dumped credentials from domain controllers.[^1] [^23]  |
| [[Compression\|T1027.015]] | Compression | [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware is compressed with LZNT1 compression.[^10] [^11] [^15]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has lured victims into opening malicious files containing malware.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `whoami` to collect system user information.[^2]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has hosted malicious payloads on Dropbox.[^2]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used a variety of Web shells.[^15]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Threat Group-3390](https://attack.mitre.org/groups/G0027)'s malware can add a Registry key to `Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^10] [^12]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can encrypt payloads using XOR. [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware is also obfuscated using Metasploit’s shikata_ga_nai encoder.[^10] [^11] [^15]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Threat Group-3390](https://attack.mitre.org/groups/G0027)'s malware can create a new service, sometimes naming it after the config information, to gain persistence.[^10] [^12]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has compromised third party service providers to gain access to victim's environments.[^16]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use [NBTscan](https://attack.mitre.org/software/S0590) to discover vulnerable systems.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has downloaded additional malware and tools, including through the use of `certutil`, onto a compromised host .[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors installed a credential logger on Microsoft Exchange servers. [Threat Group-3390](https://attack.mitre.org/groups/G0027) also leveraged the reconnaissance framework, ScanBox, to capture keystrokes.[^1] [^7] [^11]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used PowerShell for execution.[^23] [^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors obtain legitimate credentials using a variety of methods and use them to further lateral movement on victim networks.[^1]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has embedded malicious code into websites to screen a potential victim's IP address and then exploit their browser if they are of interest.[^9]  |
| [[Tool\|T1588.002]] | Tool | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has obtained and used tools such as [Impacket](https://attack.mitre.org/software/S0357), [pwdump](https://attack.mitre.org/software/S0006), [Mimikatz](https://attack.mitre.org/software/S0002), [gsecdump](https://attack.mitre.org/software/S0008), [NBTscan](https://attack.mitre.org/software/S0590), and [Windows Credential Editor](https://attack.mitre.org/software/S0005).[^15] [^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used the `net view` command.[^10]  |
| [[Domains\|T1583.001]] | Domains | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has registered domains for C2.[^12]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has extensively used strategic web compromises to target victims.[^1] [^11]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | During execution, [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware deobfuscates and decompresses code that was encoded with Metasploit’s shikata_ga_nai encoder as well as compressed with LZNT1 compression.[^11]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used [gsecdump](https://attack.mitre.org/software/S0008) to dump credentials. They have also dumped credentials from domain controllers.[^1] [^23]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors look for and use VPN profiles during an operation to access the network using external VPN services.[^1]  [Threat Group-3390](https://attack.mitre.org/groups/G0027) has also obtained OWA account credentials during intrusions that it subsequently used to attempt to regain access when evicted from a victim network.[^23]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Threat Group-3390](https://attack.mitre.org/groups/G0027) ran a command to compile an archive of file types of interest from the victim user's directories.[^23]  |
| [[Local Account\|T1087.001]] | Local Account | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `net user` to conduct internal discovery of systems.[^23]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has compromised the Able Desktop installer to gain access to victim's environments.[^19]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can use a public UAC bypass method to elevate privileges.[^10]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Threat Group-3390](https://attack.mitre.org/groups/G0027) ran a command to compile an archive of file types of interest from the victim user's directories.[^23]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used RAR to compress, encrypt, and password-protect files prior to exfiltration.[^23]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has packed malware and tools, including using VMProtect.[^2] [^19]  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has obtained stolen valid certificates, including from VMProtect and the Chinese instant messaging application Youdu, for their operations.[^12]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can use WMI to execute a binary.[^10]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware has used HTTP for C2.[^11]  |
| [[Network Share Connection Removal\|T1070.005]] | Network Share Connection Removal | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has detached network shares after exfiltrating files, likely to evade detection.[^23]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used WinRM to enable remote execution.[^23]  |
| [[DLL\|T1574.001]] | DLL | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has performed DLL search order hijacking to execute their payload.[^10]  [Threat Group-3390](https://attack.mitre.org/groups/G0027) has also used DLL side-loading, including by using legitimate Kaspersky antivirus variants as well as `rc.exe`, a legitimate Microsoft Resource Compiler.[^1] [^23] [^11] [^15] [^12]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has deleted existing logs and exfiltrated file archives from a victim.[^23] [^2]  |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used appcmd.exe to disable logging on a victim server.[^23]  |
| [[Upload Tool\|T1608.002]] | Upload Tool | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has staged tools, including [gsecdump](https://attack.mitre.org/software/S0008) and WCE, on previously compromised websites.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool has created new Registry keys under `HKEY_CURRENT_USER\Software\Classes\` and `HKLM\SYSTEM\CurrentControlSet\services`.[^10] [^19]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited MS17-010 to move laterally to other systems on the network.[^15] 	 |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has moved staged encrypted archives to Internet-facing servers that had previously been compromised with [China Chopper](https://attack.mitre.org/software/S0020) prior to exfiltration.[^23]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `net use` and `netstat` to conduct internal discovery of systems. The group has also used `quser.exe` to identify existing RDP sessions on a victim.[^23]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^23]  |
| [[certutil\|S0160]] | certutil | [^2]  |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^1]  |
| [[Impacket\|S0357]] | Impacket | [^15]  |
| [[ipconfig\|S0100]] | ipconfig | [^23]  |
| [[Tasklist\|S0057]] | Tasklist | [^2]  |
| [[netstat\|S0104]] | netstat | [^2]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^2]  |
| [[pwdump\|S0006]] | pwdump | [^15]  |
| [[Mimikatz\|S0002]] | Mimikatz | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used a modified version of Mimikatz called Wrapikatz.[^23] [^10] [^2] [^17] [^16]  |
| [[gsecdump\|S0008]] | gsecdump | [^1]  |
| [[NBTscan\|S0590]] | NBTscan | [^1] [^2]  |
| [[RCSession\|S0662]] | RCSession | [^19] [^2] [^16]  |
| [[ASPXSpy\|S0073]] | ASPXSpy | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used a modified version of ASPXSpy called ASPXTool.[^1] [^16]  |
| [[China Chopper\|S0020]] | China Chopper | [^1] [^23] [^10] [^15]  |
| [[HyperBro\|S0398]] | HyperBro | [^15] [^11] [^7] [^2] [^19]  |
| [[PlugX\|S0013]] | PlugX | [^1] [^23] [^10] [^2] [^16]  |
| [[Clambling\|S0660]] | Clambling | [^2] [^16] [^19]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^3]  |
| [[Pandora\|S0664]] | Pandora | [^19]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^2]  |
| [[SysUpdate\|S0663]] | SysUpdate | [^19]  |
| [[ZxShell\|S0412]] | ZxShell | [^3]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [^1] [^23] [^10] [^19]  |



## References

[^1]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^2]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^3]: [Secureworks BRONZEUNION Feb 2019](https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox)


[^4]: BRONZE UNION


[^5]: TG-3390


[^6]: Emissary Panda


[^7]: [Hacker News LuckyMouse June 2018](https://thehackernews.com/2018/06/chinese-watering-hole-attack.html)


[^8]: Linen Typhoon


[^9]: [Gallagher 2015](http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/)


[^10]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^11]: [Securelist LuckyMouse June 2018](https://securelist.com/luckymouse-hits-national-data-center/86083/)


[^12]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^13]: APT27


[^14]: Earth Smilodon


[^15]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^16]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^17]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^18]: Threat Group-3390


[^19]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^20]: LuckyMouse


[^21]: Iron Tiger


[^22]: [Microsoft Naming Conventions Frequently Updated](https://learn.microsoft.com/en-us/unified-secops-platform/microsoft-threat-actor-naming)


[^23]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


