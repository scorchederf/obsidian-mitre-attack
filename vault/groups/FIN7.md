---
aliases: 
    - FIN7
    - GOLD NIAGARA
    - ITG14
    - Carbon Spider
    - ELBRUS
    - Sangria Tempest
mitre-attack: https://attack.mitre.org/groups/G0046
---

## G0046

[FIN7](https://attack.mitre.org/groups/G0046) is a financially-motivated threat group that has been active since 2013. [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. A portion of [FIN7](https://attack.mitre.org/groups/G0046) was operated out of a front company called Combi Security and often used point-of-sale malware for targeting efforts. Since 2020, [FIN7](https://attack.mitre.org/groups/G0046) shifted operations to big game hunting (BGH), including use of [REvil](https://attack.mitre.org/software/S0496) ransomware and their own Ransomware-as-a-Service (RaaS), Darkside. FIN7 may be linked to the [Carbanak](https://attack.mitre.org/groups/G0008) Group, but multiple threat groups have been observed using [Carbanak](https://attack.mitre.org/software/S0030), leading these groups to be tracked separately.[^6] [^8] [^20] [^35] [^13] [^25] [^19] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious Link\|T1204.001]] | Malicious Link | [FIN7](https://attack.mitre.org/groups/G0046) has used malicious links to lure victims into downloading malware.[^13]  |
| [[Code Signing\|T1553.002]] | Code Signing | [FIN7](https://attack.mitre.org/groups/G0046) has signed [Carbanak](https://attack.mitre.org/software/S0030) payloads with legally purchased code signing certificates. [FIN7](https://attack.mitre.org/groups/G0046) has also digitally signed their phishing documents, backdoors and other staging tools to bypass security controls.[^20] [^35]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [FIN7](https://attack.mitre.org/groups/G0046) has harvested valid administrative credentials for lateral movement.[^13]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [FIN7](https://attack.mitre.org/groups/G0046) used SQL scripts to help perform tasks on the victim's machine.[^35] [^27] [^35]  |
| [[SSH\|T1021.004]] | SSH | [FIN7](https://attack.mitre.org/groups/G0046) has used SSH to move laterally through victim environments.[^13]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [FIN7](https://attack.mitre.org/groups/G0046) has compromised targeted organizations through exploitation of CVE-2021-31207 in Exchange.[^21]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [FIN7](https://attack.mitre.org/groups/G0046) has used random junk code to obfuscate malware code.[^25]  |
| [[Link Target\|T1608.005]] | Link Target | [FIN7](https://attack.mitre.org/groups/G0046) has created a fake link that redirected to an adversary-controlled Dropbox that downloaded the malicious executable.[^29]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the command `cmd.exe /C quser` to collect user session information.[^25]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [FIN7](https://attack.mitre.org/groups/G0046) malware has created scheduled tasks to establish persistence.[^8] [^14] [^35] [^27]  Specifically, [FIN7](https://attack.mitre.org/groups/G0046) has used OpenSSH to establish persistence.[^29]   |
| [[VNC\|T1021.005]] | VNC | [FIN7](https://attack.mitre.org/groups/G0046) has used TightVNC to control compromised hosts.[^13]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [FIN7](https://attack.mitre.org/groups/G0046) has attempted to run Darkside ransomware with the filename sleep.exe.[^13]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has mimicked WsTaskLoad.exe, which is associated with the Wondershare software suite, by using a malicious executable under the same name.[^29]    |
| [[Hidden Window\|T1564.003]] | Hidden Window | [FIN7](https://attack.mitre.org/groups/G0046) has used .txt files to conceal PowerShell commands.[^18]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [FIN7](https://attack.mitre.org/groups/G0046) has conducted broad phishing campaigns using malicious links.[^13]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has sent spearphishing emails containing a typosquatted link to “ip-sccanner[.]com.”[^29]     |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [FIN7](https://attack.mitre.org/groups/G0046) has created a scheduled task named “AdobeFlashSync” to establish persistence.[^14]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [FIN7](https://attack.mitre.org/groups/G0046) has used `rundll32.exe` to execute malware on a compromised network.[^25]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FIN7](https://attack.mitre.org/groups/G0046) has used WMI to install malware on targeted systems.[^23]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [FIN7](https://attack.mitre.org/groups/G0046) has loaded a .NET assembly into the currect execution context via `Reflection.Assembly::Load`.[^18]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [FIN7](https://attack.mitre.org/groups/G0046) used VBS scripts to help perform tasks on the victim's machine.[^35] [^27] [^13]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [FIN7](https://attack.mitre.org/groups/G0046) has utilized the remote management tool Atera to download malware to a compromised system.[^25]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [FIN7](https://attack.mitre.org/groups/G0046) has used `attrib +h “C:\ProgramData\ssh”` to make the SSH folder hidden.[^29]    |
| [[PowerShell\|T1059.001]] | PowerShell | [FIN7](https://attack.mitre.org/groups/G0046) used a PowerShell script to launch shellcode that retrieved an additional payload.[^8] [^14] [^31] [^25] [^18]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has executed a custom obfuscation of the shellcode invoker in [PowerSploit](https://attack.mitre.org/software/S0194) called POWERTRASH.[^29]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [FIN7](https://attack.mitre.org/groups/G0046) has tunneled C2 traffic via OpenSSH.[^29]    |
| [[Application Shimming\|T1546.011]] | Application Shimming | [FIN7](https://attack.mitre.org/groups/G0046) has used application shim databases for persistence.[^2]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [FIN7](https://attack.mitre.org/groups/G0046) spear phishing campaigns have included malicious Word documents with DDE execution.[^22]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [FIN7](https://attack.mitre.org/groups/G0046) has used the command `net group "domain admins" /domain` to enumerate domain groups.[^25] [^29]    |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [FIN7](https://attack.mitre.org/groups/G0046) has used RDP to move laterally in victim environments.[^13] <br> |
| [[Input Injection\|T1674]] | Input Injection | FIN7 has used malicious USBs to emulate keystrokes to launch PowerShell to download and execute malware from the adversary's server.[^31] [^18]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [FIN7](https://attack.mitre.org/groups/G0046) has encrypted virtual disk volumes on ESXi servers using a version of Darkside ransomware.[^13] [^25]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has deployed ransomware as the end payload during big game hunting.[^29]    |
| [[Tool\|T1588.002]] | Tool | [FIN7](https://attack.mitre.org/groups/G0046) has utilized a variety of tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154), [PowerSploit](https://attack.mitre.org/software/S0194), and the remote management tool, Atera for targeting efforts.[^25]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [FIN7](https://attack.mitre.org/groups/G0046) has compiled a list of victims by filtering companies by revenue using Zoominfo, which is a service that provides business information.[^19]   |
| [[Service Execution\|T1569.002]] | Service Execution | [FIN7](https://attack.mitre.org/groups/G0046) has started the SSH service by executing `sc start sshd`.[^29]    |
| [[Web Services\|T1583.006]] | Web Services | [FIN7](https://attack.mitre.org/groups/G0046) has set up Amazon S3 buckets to host trojanized digital products.[^25]  |
| [[User Activity Based Checks\|T1497.002]] | User Activity Based Checks | [FIN7](https://attack.mitre.org/groups/G0046) used images embedded into document lures that only activate the payload when a user double clicks to avoid sandboxes.[^8]  |
| [[JavaScript\|T1059.007]] | JavaScript | [FIN7](https://attack.mitre.org/groups/G0046) used JavaScript scripts to help perform tasks on the victim's machine.[^35] [^27]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FIN7](https://attack.mitre.org/groups/G0046) malware has created Registry Run and RunOnce keys to establish persistence, and has also added items to the Startup folder.[^8] [^35]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [FIN7](https://attack.mitre.org/groups/G0046) has compromised a digital product website and modified multiple download links to point to trojanized versions of offered digital products.[^25]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [FIN7](https://attack.mitre.org/groups/G0046) has added a firewall rule to allow TCP port 59999 inbound and a rule to allow sshd.exe on TCP port 9898.[^29]    |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used csvde.exe, which is a built-in Windows command line tool, to export system information. Additionally, WsTaskLoad has gathered system information, such as operating system and hostname.[^29]   |
| [[Video Capture\|T1125]] | Video Capture | [FIN7](https://attack.mitre.org/groups/G0046) created a custom video recording capability that could be used to monitor operations in the victim's environment.[^35] [^4]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [FIN7](https://attack.mitre.org/groups/G0046) has used port-protocol mismatches on ports such as 53, 80, 443, and 8080 during C2.[^35]  [FIN7](https://attack.mitre.org/groups/G0046) has used TCP ports 59999 and 9898 for firewall rules.[^29]    |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FIN7](https://attack.mitre.org/groups/G0046) has decoded a malicious PowerShell script using `certutil -decode hex` and has decoded an XOR-obfuscated block of data with the key `qawsed1q2w3e`, which led to the installation of [Lizar](https://attack.mitre.org/software/S0681).[^18]   |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [FIN7](https://attack.mitre.org/groups/G0046) has used fragmented strings, environment variables, standard input (stdin), and native character-replacement functionalities to obfuscate commands.[^15] [^35] [^13]  |
| [[Domain Account\|T1087.002]] | Domain Account | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 and the executable WsTaskLoad to enumerate domain administrations by executing `net group “Domain Admins” /domain`.[^29]  [FIN7](https://attack.mitre.org/groups/G0046) has also used csvde.exe, which is a built-in Windows command line tool, to export Active Directory information.  |
| [[Malicious File\|T1204.002]] | Malicious File | [FIN7](https://attack.mitre.org/groups/G0046) lured victims to double-click on images in the attachments they sent which would then execute the hidden LNK file.[^8] [^23] [^13]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used malicious Microsoft Word and Excel files and Leo VBS to distribute an updated version of [JSS Loader](https://attack.mitre.org/software/S0648) and to distribute the Harpy backdoor.[^9]   |
| [[Process Discovery\|T1057]] | Process Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 to perform process discovery by executing `tasklist /v`. Additionally, WsTaskLoad.exe executes `tasklist /v` to perform process discovery.[^29]    |
| [[Mshta\|T1218.005]] | Mshta | [FIN7](https://attack.mitre.org/groups/G0046) has used mshta.exe to execute VBScript to execute malicious code on victim systems.[^8]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [FIN7](https://attack.mitre.org/groups/G0046) used legitimate services like Google Docs, Google Scripts, and Pastebin for C2.[^35]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FIN7](https://attack.mitre.org/groups/G0046) has downloaded additional malware to execute on the victim's machine, including by using a PowerShell script to launch shellcode that retrieves an additional payload.[^8] [^4] [^25] [^18]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [FIN7](https://attack.mitre.org/groups/G0046) has used compromised credentials for access as SYSTEM on Exchange servers.[^21]  |
| [[Identify Roles\|T1591.004]] | Identify Roles | [FIN7](https://attack.mitre.org/groups/G0046) has identified IT staff and employees who had higher levels of administrative rights.[^29]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 to execute `net time`.[^29]    |
| [[Domains\|T1583.001]] | Domains | [FIN7](https://attack.mitre.org/groups/G0046) has registered look-alike domains for use in phishing campaigns.[^23]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has registered a malicious domain as `advanced-ip-sccanner[.]com` that redirected to an adversary-controlled Dropbox which contained the malicious executable.[^29]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FIN7](https://attack.mitre.org/groups/G0046) has collected files and other sensitive information from a compromised network.[^13]  |
| [[Windows Service\|T1543.003]] | Windows Service | [FIN7](https://attack.mitre.org/groups/G0046) created new Windows services and added them to the startup directories for persistence.[^35]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [FIN7](https://attack.mitre.org/groups/G0046) actors have mailed USB drives to potential victims containing malware that downloads and installs various backdoors, including in some cases for ransomware operations.[^31]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used malicious USBs that acted as virtual keyboards to install malware and txt files that decode to PowerShell commands.[^18]   |
| [[DNS\|T1071.004]] | DNS | [FIN7](https://attack.mitre.org/groups/G0046) has performed C2 using DNS via A, OPT, and TXT records.[^35]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FIN7](https://attack.mitre.org/groups/G0046) used the command prompt to launch commands on the victim’s machine.[^35] [^27] [^25]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used cmd.exe to open the Run dialog by sending the “Windows + R” keys through malicious USBs acting as virtual keyboards.[^18]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [FIN7](https://attack.mitre.org/groups/G0046) sent spearphishing emails with either malicious Microsoft Documents or RTF files attached.[^8] [^4] [^27] [^23] [^13]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [FIN7](https://attack.mitre.org/groups/G0046) has staged legitimate software, that was trojanized to contain an Atera agent installer, on Amazon S3.[^25]  [FIN7](https://attack.mitre.org/groups/G0046) has also used an open directory web server as a staging server for payloads and other tools, such as OpenSSH and 7zip.[^3]   |
| [[Fallback Channels\|T1008]] | Fallback Channels | [FIN7](https://attack.mitre.org/groups/G0046)'s Harpy backdoor malware can use DNS as a backup channel for C2 if HTTP fails.[^26]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [FIN7](https://attack.mitre.org/groups/G0046) has used Kerberoasting PowerShell commands such as, `Invoke-Kerberoast` for credential access and to enable lateral movement.[^13] [^25]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [FIN7](https://attack.mitre.org/groups/G0046) has gained initial access by compromising a victim's software supply chain.[^25]  |
| [[Screen Capture\|T1113]] | Screen Capture | [FIN7](https://attack.mitre.org/groups/G0046) captured screenshots and desktop video recordings.[^4]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [FIN7](https://attack.mitre.org/groups/G0046) has exfiltrated stolen data to the MEGA file sharing site.[^13]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [FIN7](https://attack.mitre.org/groups/G0046) has exploited ZeroLogon (CVE-2020-1472) against vulnerable domain controllers.[^13]  |
| [[Malware\|T1587.001]] | Malware | [FIN7](https://attack.mitre.org/groups/G0046) has developed malware for use in operations, including the creation of infected removable media.[^31] [^12]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PowerSploit\|S0194]] | PowerSploit | [^13] [^25]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^13]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | <br>[^13]  |
| [[AdFind\|S0552]] | AdFind | [^13]  |
| [[GRIFFON\|S0417]] | GRIFFON | [^16] [^13] [^31] [^21]  |
| [[RDFSNIFFER\|S0416]] | RDFSNIFFER | [^12]  |
| [[HALFBAKED\|S0151]] | HALFBAKED | [^8] [^35]  |
| [[POWERSOURCE\|S0145]] | POWERSOURCE | [^6]  |
| [[SystemBC\|S9001]] | SystemBC | [^7]  |
| [[TEXTMATE\|S0146]] | TEXTMATE | [^6]  |
| [[BOOSTWRITE\|S0415]] | BOOSTWRITE | [^12]  |
| [[Carbanak\|S0030]] | Carbanak | [^6] [^35] [^4] [^17] [^13] [^31] [^25] [^29]  |
| [[SQLRat\|S0390]] | SQLRat | [^27]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^13] [^31] [^25]  |
| [[REvil\|S0496]] | REvil | [^17] [^13] [^31] [^21]  |
| [[Pillowmint\|S0517]] | Pillowmint | [^10] [^13]  |
| [[Maze\|S0449]] | Maze | [^21]  |
| [[JSS Loader\|S0648]] | JSS Loader | [^13] [^21]  |
| [[Lizar\|S0681]] | Lizar | [^33] [^1]  |



## References

[^1]: [Gemini FIN7 Oct 2021](https://geminiadvisory.io/fin7-ransomware-bastion-secure/)


[^2]: [FireEye FIN7 Shim Databases](https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html)


[^3]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)


[^4]: [DOJ FIN7 Aug 2018](https://www.justice.gov/opa/press-release/file/1084361/download)


[^5]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^6]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^7]: [BlackBasta](https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/)


[^8]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


[^9]: [Crowdstrike_CarbonSpider_Part2_Nov2024](https://www.crowdstrike.com/en-us/blog/carbon-spider-embraces-big-game-hunting-part-2/)


[^10]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)


[^11]: GOLD NIAGARA


[^12]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)


[^13]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^14]: [Morphisec FIN7 June 2017](http://blog.morphisec.com/fin7-attacks-restaurant-industry)


[^15]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)


[^16]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)


[^17]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


[^18]: [Gemini_FIN7_Jan2022](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)


[^19]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^20]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)


[^21]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^22]: [CyberScoop FIN7 Oct 2017](https://www.cyberscoop.com/fin7-dde-morphisec-fileless-malware/)


[^23]: [eSentire FIN7 July 2021](https://www.esentire.com/security-advisories/notorious-cybercrime-gang-fin7-lands-malware-in-law-firm-using-fake-legal-complaint-against-jack-daniels-owner-brown-forman-inc)


[^24]: FIN7


[^25]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^26]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^27]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)


[^28]: ITG14


[^29]: [BlackBerry_FIN7_April2024](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)


[^30]: ELBRUS


[^31]: [FBI Flash FIN7 USB](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)


[^32]: Carbon Spider


[^33]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)


[^34]: Sangria Tempest


[^35]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^36]: [Secureworks GOLD NIAGARA Threat Profile](https://www.secureworks.com/research/threat-profiles/gold-niagara)


