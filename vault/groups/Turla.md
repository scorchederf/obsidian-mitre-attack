---
aliases: 
    - Turla
    - IRON HUNTER
    - Group 88
    - Waterbug
    - WhiteBear
    - Snake
    - Krypton
    - Venomous Bear
    - Secret Blizzard
    - BELUGASTURGEON
mitre-attack: https://attack.mitre.org/groups/G0010
---

## G0010

[Turla](https://attack.mitre.org/groups/G0010) is a cyber espionage threat group that has been attributed to Russia's Federal Security Service (FSB).  They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. [Turla](https://attack.mitre.org/groups/G0010) is known for conducting watering hole and spearphishing campaigns, and leveraging in-house tools and malware, such as [Uroburos](https://attack.mitre.org/software/S0022).[^29] [^6] [^15] [^17] [^39] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Web Services\|T1584.006]] | Web Services | [Turla](https://attack.mitre.org/groups/G0010) has frequently used compromised WordPress sites for C2 infrastructure.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Turla](https://attack.mitre.org/groups/G0010) has modified Registry values to store payloads.[^34] [^10]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Turla](https://attack.mitre.org/groups/G0010) has used `net localgroup` and `net localgroup Administrators` to enumerate group information, including members of the local administrators group.[^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Turla](https://attack.mitre.org/groups/G0010) has used a custom decryption routine, which pulls key and salt values from other artifacts such as a WMI filter or [PowerShell Profile](https://attack.mitre.org/techniques/T1546/013), to decode encrypted PowerShell payloads.[^34]  |
| [[Tool\|T1588.002]] | Tool | [Turla](https://attack.mitre.org/groups/G0010) has obtained and customized publicly-available tools like [Mimikatz](https://attack.mitre.org/software/S0002).[^10]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Turla](https://attack.mitre.org/groups/G0010) has used various JavaScript-based backdoors.[^17] 	 |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can impersonate or steal process tokens before executing commands.[^34] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Turla](https://attack.mitre.org/groups/G0010) has used VBS scripts throughout its operations.[^10] 	 |
| [[PowerShell Profile\|T1546.013]] | PowerShell Profile | [Turla](https://attack.mitre.org/groups/G0010) has used PowerShell profiles to maintain persistence on an infected machine.[^34]  |
| [[Web Services\|T1583.006]] | Web Services | [Turla](https://attack.mitre.org/groups/G0010) has created web accounts including Dropbox and GitHub for C2 and document exfiltration.[^5]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Turla](https://attack.mitre.org/groups/G0010) has used Metasploit to perform reflective DLL injection in order to escalate privileges.[^32] [^20]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Turla](https://attack.mitre.org/groups/G0010) has used shellcode to download Meterpreter after compromising a victim.[^32]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Turla](https://attack.mitre.org/groups/G0010) has gathered credentials from the Windows Credential Manager tool.[^10] 	 |
| [[Proxy\|T1090]] | Proxy | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have included local UPnP RPC proxies.[^34] 	 |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Turla](https://attack.mitre.org/groups/G0010) has exploited vulnerabilities in the VBoxDrv.sys driver to obtain kernel mode privileges.[^33]  |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover Group Policy details using the `gpresult` command.[^9]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover active local network connections using the `netstat -an`, `net use`, `net file`, and `net session` commands.[^29] [^9]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also enumerated the IPv4 TCP connection table via the `GetTcpTable2` API call.[^34]  |
| [[Native API\|T1106]] | Native API | [Turla](https://attack.mitre.org/groups/G0010) and its RPC backdoors have used APIs calls for various tasks related to subverting AMSI and accessing then executing commands through RPC and/or named pipes.[^34]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Turla](https://attack.mitre.org/groups/G0010) has used multiple backdoors which communicate with a C2 server via email attachments.[^35]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Turla](https://attack.mitre.org/groups/G0010) used `net use` commands to connect to lateral systems within a network.[^29]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | A [Turla](https://attack.mitre.org/groups/G0010) Javascript backdoor added a local_update_check value under the Registry key `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` to establish persistence. Additionally, a [Turla](https://attack.mitre.org/groups/G0010) custom executable containing Metasploit shellcode is saved to the Startup folder to gain persistence.[^17] [^32] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can upload files from victim machines.[^34]  |
| [[Query Registry\|T1012]] | Query Registry | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover information in the Windows Registry with the `reg query` command.[^29]  [Turla](https://attack.mitre.org/groups/G0010) has also retrieved PowerShell payloads hidden in Registry keys as well as checking keys associated with null session named pipes .[^34]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover running services and associated processes using the `tasklist /svc` command.[^29]  |
| [[Brute Force\|T1110]] | Brute Force | [Turla](https://attack.mitre.org/groups/G0010) may attempt to connect to systems within a victim's network using `net use` commands and a predefined list or collection of passwords.[^29]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can be used to transfer files to/from victim machines on the local network.[^34] [^10]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Turla](https://attack.mitre.org/groups/G0010) has infected victims using watering holes.[^9] [^24]  |
| [[Server\|T1584.004]] | Server | [Turla](https://attack.mitre.org/groups/G0010) has used compromised servers as infrastructure.[^2] [^18] [^21]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Turla](https://attack.mitre.org/groups/G0010) has used `net user /domain` to enumerate domain accounts.[^9]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Turla](https://attack.mitre.org/groups/G0010) has used a AMSI bypass, which patches the in-memory amsi.dll, in PowerShell scripts to bypass Windows antimalware products.[^34]  |
| [[File／Path Exclusions\|T1564.012]] | File／Path Exclusions | [Turla](https://attack.mitre.org/groups/G0010) has placed [LunarWeb](https://attack.mitre.org/software/S1141) install files into directories that are excluded from scanning.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used `fsutil fsinfo drives` to list connected drives.[^9]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Turla](https://attack.mitre.org/groups/G0010) has used WebDAV to upload stolen USB files to a cloud drive.[^10]  [Turla](https://attack.mitre.org/groups/G0010) has also exfiltrated stolen files to OneDrive and 4shared.[^9]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | A [Turla](https://attack.mitre.org/groups/G0010) JavaScript backdoor has used Google Apps Script as its C2 server.[^17] [^32]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Turla](https://attack.mitre.org/groups/G0010) has used HTTP and HTTPS for C2 communications.[^17] [^32]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover the system time by using the `net time` command.[^29]  |
| [[Local Account\|T1087.001]] | Local Account | [Turla](https://attack.mitre.org/groups/G0010) has used `net user` to enumerate local accounts on the system.[^9] [^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Turla](https://attack.mitre.org/groups/G0010) has used spearphishing via a link to get users to download and run their malware.[^17]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Turla](https://attack.mitre.org/groups/G0010) has compromised internal network systems to act as a proxy to forward traffic to C2.[^21]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Turla](https://attack.mitre.org/groups/G0010) has used WMI event filters and consumers to establish persistence.[^34]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Turla](https://attack.mitre.org/groups/G0010) has encrypted files stolen from connected USB drives into a RAR file before exfiltration.[^10]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have used cmd.exe to execute commands.[^34] [^10]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover running processes using the `tasklist /v` command.[^29]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also enumerated processes associated with specific open ports or named pipes.[^34]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover network configuration details using the `arp -a`, `nbtstat -n`, `net config`, `ipconfig /all`, and `route` commands, as well as [NBTscan](https://attack.mitre.org/software/S0590).[^29] [^10] [^9]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also retrieved registered RPC interface information from process memory.[^34]  |
| [[Malware\|T1587.001]] | Malware | [Turla](https://attack.mitre.org/groups/G0010) has developed its own unique malware for use in operations.[^2]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can collect files from USB thumb drives.[^34] [^10]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Turla](https://attack.mitre.org/groups/G0010) has obtained information on security software, including security logging information that may indicate whether their malware has been detected.[^9]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Turla](https://attack.mitre.org/groups/G0010) has used PowerShell to execute commands/scripts, in some cases via a custom executable or code from [Empire](https://attack.mitre.org/software/S0363)'s PSInject.[^32] [^34] [^10]  [Turla](https://attack.mitre.org/groups/G0010) has also used PowerShell scripts to load and execute malware in memory. |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Turla](https://attack.mitre.org/groups/G0010) has used encryption (including salted 3DES via [PowerSploit](https://attack.mitre.org/software/S0194)'s `Out-EncryptedScript.ps1`), random variable names, and base64 encoding to obfuscate PowerShell commands and payloads.[^34]  |
| [[Python\|T1059.006]] | Python | [Turla](https://attack.mitre.org/groups/G0010) has used IronPython scripts as part of the [IronNetInjector](https://attack.mitre.org/software/S0581) toolchain to drop payloads.[^26]  |
| [[Databases\|T1213.006]] | Databases | [Turla](https://attack.mitre.org/groups/G0010) has used a custom .NET tool to collect documents from an organization's internal central database.[^9]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover remote systems on a local network using the `net view` and `net view /DOMAIN` commands. [Turla](https://attack.mitre.org/groups/G0010) has also used `net group "Domain Computers" /domain`, `net group "Domain Controllers" /domain`, and `net group "Exchange Servers" /domain` to enumerate domain computers, including the organization's DC and Exchange Server.[^29] [^9]  |
| [[Malware\|T1588.001]] | Malware | [Turla](https://attack.mitre.org/groups/G0010) has used malware obtained after compromising other threat actors, such as [OilRig](https://attack.mitre.org/groups/G0049).[^1] [^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Turla](https://attack.mitre.org/groups/G0010) has used `net group "Domain Admins" /domain` to identify domain administrators.[^9]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Turla](https://attack.mitre.org/groups/G0010) has used the Registry to store encrypted and encoded payloads.[^34] [^10]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Turla](https://attack.mitre.org/groups/G0010) established persistence by adding a Shell value under the Registry key `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon`.[^17]  |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | [Turla](https://attack.mitre.org/groups/G0010) has modified variables in kernel memory to turn off Driver Signature Enforcement after exploiting vulnerabilities that obtained kernel mode privileges.[^33] [^22]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Turla](https://attack.mitre.org/groups/G0010) attempted to trick targets into clicking on a link featuring a seemingly legitimate domain from Adobe.com to download their malware and gain initial access.[^17]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used `tracert` to check internet connectivity.[^9]  |
| [[Web Service\|T1102]] | Web Service | [Turla](https://attack.mitre.org/groups/G0010) has used legitimate web services including Pastebin, Dropbox, and GitHub for C2 communications.[^18] [^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover operating system configuration details using the `systeminfo` and `set` commands.[^29] [^9]  |
| [[Virtual Private Server\|T1584.003]] | Virtual Private Server | [Turla](https://attack.mitre.org/groups/G0010) has used the VPS infrastructure of compromised Iranian threat actors.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Turla](https://attack.mitre.org/groups/G0010) has named components of [LunarWeb](https://attack.mitre.org/software/S1141) to mimic Zabbix agent logs.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [Turla](https://attack.mitre.org/groups/G0010) has also used [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-ReflectivePEInjection.ps1` to reflectively load a PowerShell payload into a random process on the victim system.[^34]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Turla](https://attack.mitre.org/groups/G0010) has abused local accounts that have the same password across the victim’s network.[^5]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used `net accounts` and `net accounts /domain` to acquire password policy information.[^9]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover files in specific locations on the hard disk %TEMP% directory, the current user's desktop, the Program Files directory, and Recent.[^29] [^9]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also searched for files matching the `lPH*.dll` pattern.[^34]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | Based on comparison of [Gazer](https://attack.mitre.org/software/S0168) versions, [Turla](https://attack.mitre.org/groups/G0010) made an effort to obfuscate strings in the malware that could be used as IoCs, including the mutex name and named pipe.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^29]  |
| [[certutil\|S0160]] | certutil | [^10]  |
| [[Tasklist\|S0057]] | Tasklist | [^29]  |
| [[Arp\|S0099]] | Arp | [^29]  |
| [[Empire\|S0363]] | Empire | [^36] [^5]  |
| [[netstat\|S0104]] | netstat | [^29]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^29] [^3]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^32] [^10]  |
| [[IronNetInjector\|S0581]] | IronNetInjector | [^26]  |
| [[nbtstat\|S0102]] | nbtstat | [^29]  |
| [[NBTscan\|S0590]] | NBTscan | [^10]  |
| [[Reg\|S0075]] | Reg | [^29]  |
| [[PsExec\|S0029]] | PsExec | [^10]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [^12]  |
| [[TinyTurla\|S0668]] | TinyTurla | [^21]  |
| [[HyperStack\|S0537]] | HyperStack | [^18]  |
| [[Kazuar\|S0265]] | Kazuar | [^19] [^21]  |
| [[LunarLoader\|S1143]] | LunarLoader | [^3]  |
| [[Epic\|S0091]] | Epic | [^29] [^24]  |
| [[LightNeuron\|S0395]] | LightNeuron | [^27] [^24]  |
| [[Gazer\|S0168]] | Gazer | [^6]  |
| [[Uroburos\|S0022]] | Uroburos | [^29] [^39]  |
| [[Crutch\|S0538]] | Crutch | [^5] [^21]  |
| [[Mosquito\|S0256]] | Mosquito | [^17] [^32] [^24]  |
| [[LunarMail\|S1142]] | LunarMail | [^3]  |
| [[Carbon\|S0335]] | Carbon | [^11] [^24]  |
| [[Penquin\|S0587]] | Penquin | [^7]  |
| [[ComRAT\|S0126]] | ComRAT | [^31] [^26] [^24]  |
| [[PowerStallion\|S0393]] | PowerStallion | [^34]  |
| [[LunarWeb\|S1141]] | LunarWeb | [^3]  |



## References

[^1]: [NSA NCSC Turla OilRig](https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_Turla_20191021%20ver%204%20-%20nsa.gov.pdf)


[^2]: [Recorded Future Turla Infra 2020](https://www.recordedfuture.com/research/turla-apt-infrastructure)


[^3]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^4]: Group 88


[^5]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^6]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)


[^7]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^10]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^11]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)


[^12]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^13]: Secret Blizzard


[^14]: Krypton


[^15]: [CrowdStrike VENOMOUS BEAR](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-march-venomous-bear/)


[^16]: WhiteBear


[^17]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^18]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


[^19]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^20]: [Github Rapid7 Meterpreter Elevate](https://github.com/rapid7/meterpreter/tree/master/source/extensions/priv/server/elevate)


[^21]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^22]: [GitHub Turla Driver Loader](https://github.com/hfiref0x/TDL)


[^23]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^24]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


[^25]: IRON HUNTER


[^26]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


[^27]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^28]: BELUGASTURGEON


[^29]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^30]: Waterbug


[^31]: [Symantec Waterbug](https://www.threatminer.org/report.php?q=waterbug-attack-group.pdf&y=2015#gsc.tab=0&gsc.q=waterbug-attack-group.pdf&gsc.page=1)


[^32]: [ESET Turla Mosquito May 2018](https://www.welivesecurity.com/2018/05/22/turla-mosquito-shift-towards-generic-tools/)


[^33]: [Unit42 AcidBox June 2020](https://unit42.paloaltonetworks.com/acidbox-rare-malware/)


[^34]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^35]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^36]: [ESET Turla August 2018](https://www.welivesecurity.com/wp-content/uploads/2018/08/Eset-Turla-Outlook-Backdoor.pdf)


[^37]: Turla


[^38]: Venomous Bear


[^39]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^40]: Snake


