---
aliases: 
    - APT32
    - SeaLotus
    - OceanLotus
    - APT-C-00
    - Canvas Cyclone
    - BISMUTH
mitre-attack: https://attack.mitre.org/groups/G0050
---

## G0050

[APT32](https://attack.mitre.org/groups/G0050) is a suspected Vietnam-based threat group that has been active since at least 2014. The group has targeted multiple private sector industries as well as foreign governments, dissidents, and journalists with a strong focus on Southeast Asian countries like Vietnam, the Philippines, Laos, and Cambodia. They have extensively used strategic web compromises to compromise victims.[^5] [^10] [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [APT32](https://attack.mitre.org/groups/G0050) has used pass the hash for lateral movement.[^11]  |
| [[Masquerading\|T1036]] | Masquerading | [APT32](https://attack.mitre.org/groups/G0050) has disguised a Cobalt Strike beacon as a Flash Installer.[^11]  |
| [[JavaScript\|T1059.007]] | JavaScript | [APT32](https://attack.mitre.org/groups/G0050) has used JavaScript for drive-by downloads and C2 communications.[^11] [^9]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [APT32](https://attack.mitre.org/groups/G0050) used WMI to deploy their tools on remote machines and to gather information about the Outlook process.[^11]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [APT32](https://attack.mitre.org/groups/G0050) compromised McAfee ePO to move laterally by distributing malware as a software deployment task.[^5]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [APT32](https://attack.mitre.org/groups/G0050) has deployed tools after moving laterally using administrative accounts.[^11] 	 |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | [APT32](https://attack.mitre.org/groups/G0050) used NTFS alternate data streams to hide their payloads.[^11]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [APT32](https://attack.mitre.org/groups/G0050) used Outlook Credential Dumper to harvest credentials stored in Windows registry.[^15] [^11]  |
| [[Process Injection\|T1055]] | Process Injection | [APT32](https://attack.mitre.org/groups/G0050) malware has injected a Cobalt Strike beacon into Rundll32.exe.[^11]  |
| [[PubPrn\|T1216.001]] | PubPrn | [APT32](https://attack.mitre.org/groups/G0050) has used PubPrn.vbs within execution scripts to execute malware, possibly bypassing defenses.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT32](https://attack.mitre.org/groups/G0050) has sent spearphishing emails with a malicious executable disguised as a document or spreadsheet.[^7] [^15] [^11] [^20] [^23] [^14]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the `net view` command to show all shares available, including the administrative shares such as `C$` and `ADMIN$`.[^11]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT32](https://attack.mitre.org/groups/G0050) collected the victim's username and executed the `whoami` command on the victim's machine. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to collect the username on the victim's machine. [^23] [^7] [^11]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | An [APT32](https://attack.mitre.org/groups/G0050) backdoor can use HTTP over a non-standard TCP port (e.g 14146) which is specified in the backdoor configuration.[^20]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT32](https://attack.mitre.org/groups/G0050) has collected the OS version and computer name from victims. One of the group's backdoors can also query the Windows Registry to gather system information, and another macOS backdoor performs a fingerprint of the machine on its first connection to the C&C server. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to identify the name of the infected host.[^7] [^20] [^16] [^23]  |
| [[Domains\|T1583.001]] | Domains | [APT32](https://attack.mitre.org/groups/G0050) has set up and operated websites to gather information and deliver malware.[^9]  |
| [[Query Registry\|T1012]] | Query Registry | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor can query the Windows Registry to gather system information. [^20]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [APT32](https://attack.mitre.org/groups/G0050) has used the `Invoke-Obfuscation` framework to obfuscate their PowerShell.[^5] [^17] [^11]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT32](https://attack.mitre.org/groups/G0050) has used cmd.exe for execution.[^11]   |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor can exfiltrate data by encoding it in the subdomain field of DNS packets.[^20]  |
| [[DLL\|T1574.001]] | DLL | [APT32](https://attack.mitre.org/groups/G0050) ran legitimately-signed executables from Symantec and McAfee which load a malicious DLL. The group also side-loads its backdoor by dropping a library and a legitimate, signed executable (AcroTranscoder).[^15] [^11] [^20]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT32](https://attack.mitre.org/groups/G0050) has sent spearphishing emails containing malicious links.[^7] [^15] [^23] [^9] [^14]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [APT32](https://attack.mitre.org/groups/G0050) has used malicious links to direct users to web pages designed to harvest credentials.[^9]  |
| [[Local Account\|T1087.001]] | Local Account | [APT32](https://attack.mitre.org/groups/G0050) enumerated administrative users using the commands `net localgroup administrators`.[^11]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT32](https://attack.mitre.org/groups/G0050) has used PowerShell-based tools, PowerShell one-liners, and shellcode loaders for execution.[^5] [^15] [^11]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT32](https://attack.mitre.org/groups/G0050) used Mimikatz and customized versions of Windows Credential Dumper to harvest credentials.[^15] [^11]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [APT32](https://attack.mitre.org/groups/G0050) performed network scanning on the network to search for open ports, services, OS finger-printing, and other vulnerabilities.[^11]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [APT32](https://attack.mitre.org/groups/G0050) has stood up websites containing numerous articles and content scraped from the Internet to make them appear legitimate, but some of these pages include malicious JavaScript to profile the potential victim or infect them via a fake software update.[^9]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has exfiltrated data using the already opened channel with its C&C server.[^20]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [APT32](https://attack.mitre.org/groups/G0050) has used hidden or non-printing characters to help masquerade service names, such as appending a Unicode no-break space character to a legitimate service name. [APT32](https://attack.mitre.org/groups/G0050) has also impersonated the legitimate Flash installer file name "install_flashplayer.exe".[^5]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [APT32](https://attack.mitre.org/groups/G0050) used GetPassword_x64 to harvest credentials.[^15] [^11]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [APT32](https://attack.mitre.org/groups/G0050) has used legitimate local admin account credentials.[^5]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [APT32](https://attack.mitre.org/groups/G0050) has conducted targeted surveillance against activists and bloggers.[^14]  |
| [[Timestomp\|T1070.006]] | Timestomp | [APT32](https://attack.mitre.org/groups/G0050) has used scheduled task raw XML with a backdated timestamp of June 2, 2016. The group has also set the creation time of the files dropped by the second stage of the exploit to match the creation time of kernel32.dll. Additionally, [APT32](https://attack.mitre.org/groups/G0050) has used a random value to modify the timestamp of the file storing the clientID.[^5] [^20] [^16]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [APT32](https://attack.mitre.org/groups/G0050) has infected victims by tricking them into visiting compromised watering hole websites.[^7] [^9]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT32](https://attack.mitre.org/groups/G0050) malware has used rundll32.exe to execute an initial infection process.[^11]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [APT32](https://attack.mitre.org/groups/G0050) has used COM scriptlets to download Cobalt Strike beacons.[^11] 	 |
| [[Modify Registry\|T1112]] | Modify Registry | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has modified the Windows Registry to store the backdoor's configuration. [^20] 	 |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [APT32](https://attack.mitre.org/groups/G0050) has used email for C2 via an Office macro.[^15] [^11]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has used LZMA compression and RC4 encryption before exfiltration.[^20]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT32](https://attack.mitre.org/groups/G0050) has lured targets to download a Cobalt Strike beacon by including a malicious link within spearphishing emails.[^11] [^9] [^14]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT32](https://attack.mitre.org/groups/G0050) has used JavaScript that communicates over HTTP or HTTPS to attacker controlled domains to download additional frameworks. The group has also used downloaded encrypted payloads over HTTP.[^10] [^11]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT32](https://attack.mitre.org/groups/G0050) has renamed a NetCat binary to kb-10233.exe to masquerade as a Windows update. [APT32](https://attack.mitre.org/groups/G0050) has also renamed a Cobalt Strike beacon payload to install_flashplayers.exe. [^11] [^9]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor can receive a “delete” command.[^16]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has stored its configuration in a registry key.[^20]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT32](https://attack.mitre.org/groups/G0050) has added JavaScript to victim websites to download additional frameworks that profile and compromise website visitors.[^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT32](https://attack.mitre.org/groups/G0050) has used scheduled tasks to persist on victim systems.[^5] [^15] [^11] [^20]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [APT32](https://attack.mitre.org/groups/G0050) has moved and renamed pubprn.vbs to a .txt file to avoid detection.[^13]  |
| [[Windows Service\|T1543.003]] | Windows Service | [APT32](https://attack.mitre.org/groups/G0050) modified Windows Services to ensure PowerShell scripts were loaded on the system. [APT32](https://attack.mitre.org/groups/G0050) also creates a Windows service to establish persistence.[^7] [^11] [^20]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [APT32](https://attack.mitre.org/groups/G0050) has hosted malicious payloads in Dropbox, Amazon S3, and Google Drive for use during targeting.[^9]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor changes the permission of the file it wants to execute to 755.[^16]  |
| [[Service Execution\|T1569.002]] | Service Execution | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has used Windows services as a way to execute its malicious payload. [^20]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [APT32](https://attack.mitre.org/groups/G0050) has enumerated DC servers using the command `net group "Domain Controllers" /domain`. The group has also used the `ping` command.[^11]  |
| [[Mshta\|T1218.005]] | Mshta | [APT32](https://attack.mitre.org/groups/G0050) has used mshta.exe for code execution.[^15] [^11]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor possesses the capability to list files and directories on a machine. [^20] 	<br> |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [APT32](https://attack.mitre.org/groups/G0050) has cleared select event log entries.[^5]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT32](https://attack.mitre.org/groups/G0050) has used macros, COM scriptlets, and VBS scripts.[^15] [^11]   |
| [[Tool\|T1588.002]] | Tool | [APT32](https://attack.mitre.org/groups/G0050) has obtained and used tools such as [Mimikatz](https://attack.mitre.org/software/S0002) and [Cobalt Strike](https://attack.mitre.org/software/S0154), and a variety of other open-source tools from GitHub.[^5] [^15]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [APT32](https://attack.mitre.org/groups/G0050) used [Net](https://attack.mitre.org/software/S0039) to use Windows' hidden network shares to copy their tools to remote machines for execution.[^11]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | [APT32](https://attack.mitre.org/groups/G0050) successfully gained remote access by using pass the ticket.[^11]  |
| [[Web Services\|T1583.006]] | Web Services | [APT32](https://attack.mitre.org/groups/G0050) has set up Dropbox, Amazon S3, and Google Drive to host malicious downloads.[^9]  |
| [[Web Shell\|T1505.003]] | Web Shell | [APT32](https://attack.mitre.org/groups/G0050) has used Web shells to maintain access to victim websites.[^10]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [APT32](https://attack.mitre.org/groups/G0050)'s macOS backdoor hides the clientID file via a chflags function.[^16]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the `ipconfig /all` command to gather the IP address from the system.[^11]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [APT32](https://attack.mitre.org/groups/G0050) includes garbage code to mislead anti-malware software and researchers.[^7] [^20]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT32](https://attack.mitre.org/groups/G0050) used the `netstat -anpo tcp` command to display TCP connections on the victim's machine.[^11]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [APT32](https://attack.mitre.org/groups/G0050) has used the WindowStyle parameter to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows. [^5]  [^11]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT32](https://attack.mitre.org/groups/G0050) has performed code obfuscation, including encoding payloads using Base64 and using a framework called "Dont-Kill-My-Cat (DKMC). [APT32](https://attack.mitre.org/groups/G0050) also encrypts the library used for network exfiltration with AES-256 in CBC mode in their macOS backdoor.[^5] [^17] [^7] [^15] [^11] [^20] [^16]  |
| [[Keylogging\|T1056.001]] | Keylogging | [APT32](https://attack.mitre.org/groups/G0050) has abused the PasswordChangeNotify to monitor for and capture account password changes.[^11]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [APT32](https://attack.mitre.org/groups/G0050) has collected e-mail addresses for activists and bloggers in order to target them with spyware.[^14]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [APT32](https://attack.mitre.org/groups/G0050) created a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053) that used regsvr32.exe to execute a COM scriptlet that dynamically downloaded a backdoor and injected it into memory. The group has also used regsvr32 to run their backdoor.[^20] [^5] [^11]   |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [APT32](https://attack.mitre.org/groups/G0050) has used CVE-2016-7255 to escalate privileges.[^5]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [APT32](https://attack.mitre.org/groups/G0050) has set up Facebook pages in tandem with fake websites.[^9]  |
| [[Office Application Startup\|T1137]] | Office Application Startup | [APT32](https://attack.mitre.org/groups/G0050) have replaced Microsoft Outlook's VbaProject.OTM file to install a backdoor macro for persistence.[^15] [^11]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT32](https://attack.mitre.org/groups/G0050) has used RTF document that includes an exploit to execute malicious code. (CVE-2017-11882)[^20]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT32](https://attack.mitre.org/groups/G0050) has attempted to lure users to execute a malicious dropper delivered via a spearphishing attachment.[^7] [^15] [^20] [^23] [^14]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT32](https://attack.mitre.org/groups/G0050) established persistence using Registry Run keys, both to execute PowerShell and VBS scripts as well as to execute their backdoor directly.[^15] [^11] [^20]  |
| [[Web Service\|T1102]] | Web Service | [APT32](https://attack.mitre.org/groups/G0050) has used Dropbox, Amazon S3, and Google Drive to host malicious downloads.[^9]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^11]  |
| [[ipconfig\|S0100]] | ipconfig | [^11]  |
| [[Arp\|S0099]] | Arp | [^11]  |
| [[netsh\|S0108]] | netsh | [^11]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^5] [^15] [^11]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [^19]  |
| [[KOMPROGO\|S0156]] | KOMPROGO | [^5]  |
| [[Kerrdown\|S0585]] | Kerrdown | [^14] [^21]  |
| [[WINDSHIELD\|S0155]] | WINDSHIELD | [^5]  |
| [[SOUNDBITE\|S0157]] | SOUNDBITE | [^5]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^5] [^10] [^15] [^11] [^9] [^14] [^21]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [^8] [^14]  |
| [[Goopy\|S0477]] | Goopy | [^11]  |
| [[Denis\|S0354]] | Denis | [^15] [^11]  |
| [[PHOREAL\|S0158]] | PHOREAL | [^5]  |



## References

[^1]: OceanLotus


[^2]: [Twitter ItsReallyNick Status Update APT32 PubPrn](https://x.com/ItsReallyNick/status/944321013084573697)


[^3]: SeaLotus


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^6]: APT-C-00


[^7]: [ESET OceanLotus](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)


[^8]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^9]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)


[^10]: [Volexity OceanLotus Nov 2017](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)


[^11]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^12]: APT32


[^13]: [Twitter ItsReallyNick APT32 pubprn Masquerade](https://x.com/ItsReallyNick/status/945681177108762624)


[^14]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)


[^15]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^16]: [ESET OceanLotus macOS April 2019](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)


[^17]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^18]: Canvas Cyclone


[^19]: [netlab360 rotajakiro vs oceanlotus](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)


[^20]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^21]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


[^22]: BISMUTH


[^23]: [FireEye APT32 April 2020](https://www.fireeye.com/blog/threat-research/2020/04/apt32-targeting-chinese-government-in-covid-19-related-espionage.html)


