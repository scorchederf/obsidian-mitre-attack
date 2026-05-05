---
aliases: 
    - OilRig
    - COBALT GYPSY
    - IRN2
    - APT34
    - Helix Kitten
    - Evasive Serpens
    - Hazel Sandstorm
    - EUROPIUM
    - ITG13
    - Earth Simnavaz
    - Crambus
    - TA452
mitre-attack: https://attack.mitre.org/groups/G0049
---

## G0049

[OilRig](https://attack.mitre.org/groups/G0049) is a suspected Iranian threat group that has targeted Middle Eastern and international victims since at least 2014. The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. It appears the group carries out supply chain attacks, leveraging the trust relationship between organizations to attack their primary targets. The group works on behalf of the Iranian government based on infrastructure details that contain references to Iran, use of Iranian infrastructure, and targeting that aligns with nation-state interests.[^4] [^3] [^7] [^27] [^24] [^39] [^38] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [OilRig](https://attack.mitre.org/groups/G0049) has obtained stolen code signing certificates to digitally sign malware.[^7]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tool named VALUEVAULT to steal credentials from the Windows Credential Manager.[^14]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run `hostname` and `systeminfo` on a victim.[^27] [^24] [^14] [^11] [^42] <br>	 |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [Mimikatz](https://attack.mitre.org/software/S0002) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [OilRig](https://attack.mitre.org/groups/G0049) malware ISMAgent falls back to its DNS tunneling mechanism if it is unable to reach the C2 server over HTTP.[^26]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OilRig](https://attack.mitre.org/groups/G0049) has used HTTP for C2.[^39] [^18] [^14]  |
| [[Data from Local System\|T1005]] | Data from Local System | [OilRig](https://attack.mitre.org/groups/G0049) has used PowerShell to upload files from compromised systems.[^6]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [OilRig](https://attack.mitre.org/groups/G0049) has modified Windows firewall rules to enable remote access.[^42]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [OilRig](https://attack.mitre.org/groups/G0049) has used macros to deliver malware such as [QUADAGENT](https://attack.mitre.org/software/S0269) and [OopsIE](https://attack.mitre.org/software/S0264).[^4] [^26] [^29] [^38] [^15]  [OilRig](https://attack.mitre.org/groups/G0049) has used batch scripts.[^4] [^26] [^29] [^38] [^15]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [OilRig](https://attack.mitre.org/groups/G0049) has used Remote Desktop Protocol for lateral movement. The group has also used tunneling tools to tunnel RDP into the environment.[^39] [^18] [^33] [^42] [^42]  |
| [[Web Shell\|T1505.003]] | Web Shell | [OilRig](https://attack.mitre.org/groups/G0049) has used web shells, often to maintain access to a victim network.[^39] [^18] [^33] [^6]  |
| [[Malware\|T1587.001]] | Malware | [OilRig](https://attack.mitre.org/groups/G0049) actively developed and used a series of downloaders during 2022.[^36]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [OilRig](https://attack.mitre.org/groups/G0049) has hosted malware on fake websites designed to target specific audiences.[^7]  |
| [[Masquerading\|T1036]] | Masquerading | [OilRig](https://attack.mitre.org/groups/G0049) has used .doc file extensions to mask malicious executables.[^11]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [OilRig](https://attack.mitre.org/groups/G0049) has incorporated remote monitoring and management (RMM) tools into their operations including [ngrok](https://attack.mitre.org/software/S0508).[^6]  |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [OilRig](https://attack.mitre.org/groups/G0049) has used a CHM payload to load and execute another malicious file once delivered to a victim.[^27]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used the publicly available tool SoftPerfect Network Scanner as well as a custom tool called GOLDIRONY to conduct network scanning.[^18]  |
| [[Local Account\|T1087.001]] | Local Account | [OilRig](https://attack.mitre.org/groups/G0049) has run `net user`, `net user /domain`, `net group “domain admins” /domain`, and `net group “Exchange Trusted Subsystem” /domain` to get account listings on a victim.[^27]  |
| [[Outlook Home Page\|T1137.004]] | Outlook Home Page | [OilRig](https://attack.mitre.org/groups/G0049) has abused the Outlook Home Page feature for persistence. [OilRig](https://attack.mitre.org/groups/G0049) has also used CVE-2017-11774 to roll back the initial patch designed to protect against Home Page abuse.[^32]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [OilRig](https://attack.mitre.org/groups/G0049) has used `net group /domain`, `net group “domain admins” /domain`, and `net group “Exchange Trusted Subsystem” /domain` to find domain group permission settings.[^27]  |
| [[Screen Capture\|T1113]] | Screen Capture | [OilRig](https://attack.mitre.org/groups/G0049) has a tool called CANDYKING to capture a screenshot of user's desktop.[^18]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [OilRig](https://attack.mitre.org/groups/G0049) has used Wireshark’s usbcapcmd utility to capture USB traffic.[^42]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used `sc query` on a victim to gather information about services.[^27]  |
| [[Password Filter DLL\|T1556.002]] | Password Filter DLL | [OilRig](https://attack.mitre.org/groups/G0049) has registered a password filter DLL in order to drop malware.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [OilRig](https://attack.mitre.org/groups/G0049) has used PowerShell scripts for execution, including use of a macro to run a PowerShell command to decode file contents.[^4] [^25] [^43] [^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [OilRig](https://attack.mitre.org/groups/G0049) has deleted files associated with their payload after execution.[^4] [^29]  |
| [[Tool\|T1588.002]] | Tool | [OilRig](https://attack.mitre.org/groups/G0049) has made use of the publicly available tools including Plink and [Mimikatz](https://attack.mitre.org/software/S0002).[^42] [^6]   |
| [[Malicious File\|T1204.002]] | Malicious File | [OilRig](https://attack.mitre.org/groups/G0049) has delivered macro-enabled documents that required targets to click the "enable content" button to execute the payload on the system.[^29] [^38] [^43] [^11] [^7]  |
| [[External Remote Services\|T1133]] | External Remote Services | [OilRig](https://attack.mitre.org/groups/G0049) uses remote services such as VPN, Citrix, or OWA to persist in an environment.[^18]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | <br>[OilRig](https://attack.mitre.org/groups/G0049) has used an exfiltration tool named STEALHOOK to retreive valid domain credentials.[^6]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used net.exe in a script with `net accounts /domain` to find the password policy of a domain.[^10]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [OilRig](https://attack.mitre.org/groups/G0049) has compromised email accounts to send phishing emails.[^7]  |
| [[Domain Account\|T1087.002]] | Domain Account | [OilRig](https://attack.mitre.org/groups/G0049) has run `net user`, `net user /domain`, `net group “domain admins” /domain`, and `net group “Exchange Trusted Subsystem” /domain` to get account listings on a victim.[^27]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | A [OilRig](https://attack.mitre.org/groups/G0049) macro has run a PowerShell command to decode file contents. [OilRig](https://attack.mitre.org/groups/G0049) has also used [certutil](https://attack.mitre.org/software/S0160) to decode base64-encoded files on victims.[^4] [^25] [^29] [^33]  |
| [[Code Signing\|T1553.002]] | Code Signing | [OilRig](https://attack.mitre.org/groups/G0049) has signed its malware with stolen certificates.[^7]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [OilRig](https://attack.mitre.org/groups/G0049) has exfiltrated data via Microsoft Exchange and over FTP separately from its primary C2 channel over DNS.[^24] [^6]  |
| [[Brute Force\|T1110]] | Brute Force | [OilRig](https://attack.mitre.org/groups/G0049) has used brute force techniques to obtain credentials.[^18] [^37]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [OilRig](https://attack.mitre.org/groups/G0049) has used VBScript macros for execution on compromised hosts.[^11]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [OilRig](https://attack.mitre.org/groups/G0049) has sent spearphising emails with malicious links to potential victims.[^29] [^7]  |
| [[Modify Registry\|T1112]] | Modify Registry | [OilRig](https://attack.mitre.org/groups/G0049) has used reg.exe to modify system configuration.[^42] [^6]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used tools to identify if a mouse is connected to a targeted system.[^11]  |
| [[DNS\|T1071.004]] | DNS | [OilRig](https://attack.mitre.org/groups/G0049) has used DNS for C2 including the publicly available `requestbin.net` tunneling service.[^39] [^18] [^14] [^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OilRig](https://attack.mitre.org/groups/G0049) had downloaded remote files onto victim infrastructure.[^4] [^6]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used `netstat -an` on a victim to get a listing of network connections.[^27]  |
| [[Windows Service\|T1543.003]] | Windows Service | [OilRig](https://attack.mitre.org/groups/G0049) has used a compromised Domain Controller to create a service on a remote host.[^42] <br> |
| [[Supply Chain Compromise\|T1195]] | Supply Chain Compromise | [OilRig](https://attack.mitre.org/groups/G0049) has leveraged compromised organizations to conduct supply chain attacks on government entities.[^6]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [OilRig](https://attack.mitre.org/groups/G0049) has delivered malicious links to achieve execution on the target system.[^29] [^38] [^43] [^7]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [OilRig](https://attack.mitre.org/groups/G0049) has used compromised credentials to access other systems on a victim network.[^39] [^18] [^33] [^37]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [OilRig](https://attack.mitre.org/groups/G0049) used the [PowerExchange](https://attack.mitre.org/software/S1173) utility and other tools to create tunnels to C2 servers.[^18]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [OilRig](https://attack.mitre.org/groups/G0049) has sent spearphising emails with malicious attachments to potential victims using compromised and/or spoofed email accounts.[^29] [^38] [^43] [^7]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [OilRig](https://attack.mitre.org/groups/G0049) has created scheduled tasks that run a VBScript to execute a payload on victim machines.[^29] [^38] [^14] [^11]  |
| [[Automated Collection\|T1119]] | Automated Collection | [OilRig](https://attack.mitre.org/groups/G0049) has used automated collection.[^39]  |
| [[Domains\|T1583.001]] | Domains | [OilRig](https://attack.mitre.org/groups/G0049) has set up fake VPN portals, conference sign ups, and job application websites to target victims.[^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [OilRig](https://attack.mitre.org/groups/G0049) has employed keyloggers including KEYPUNCH and LONGWATCH.[^18] [^14] [^42] 	<br> |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [OilRig](https://attack.mitre.org/groups/G0049) has named a downloaded copy of the Plink tunneling utility as \ProgramData\Adobe.exe.[^42]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run `whoami` on a victim.[^27] [^24] [^11]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [OilRig](https://attack.mitre.org/groups/G0049) has used LinkedIn to send spearphishing links.[^14]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [OilRig](https://attack.mitre.org/groups/G0049) has used the Plink utility and other tools to create tunnels to C2 servers.[^39] [^18] [^14] [^42]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [OilRig](https://attack.mitre.org/groups/G0049) has used WMI for execution.[^18] [^42] <br> |
| [[SSH\|T1021.004]] | SSH | [OilRig](https://attack.mitre.org/groups/G0049) has used Putty to access compromised systems.[^39]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [OilRig](https://attack.mitre.org/groups/G0049) has used infostealer tools to copy clipboard data.[^42]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [OilRig](https://attack.mitre.org/groups/G0049) has encrypted and encoded data in its malware, including by using base64.[^4] [^38] [^39] [^43] [^15]  |
| [[Local Groups\|T1069.001]] | Local Groups | [OilRig](https://attack.mitre.org/groups/G0049) has used `net localgroup administrators` to find local administrators on compromised systems.[^27] [^42] <br> |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  |
| [[Process Discovery\|T1057]] | Process Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run `tasklist` on a victim's machine and used infostealers to capture processes.[^27] [^42]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.[^39] [^18] [^40] [^14]  [OilRig](https://attack.mitre.org/groups/G0049) has also used tool named PICKPOCKET to dump passwords from web browsers.[^14]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run `ipconfig /all` on a victim.[^27] [^24]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [OilRig](https://attack.mitre.org/groups/G0049) has exploited CVE-2024-30088 to run arbitrary code in the context of `SYSTEM`.[^6]  |
| [[Query Registry\|T1012]] | Query Registry | [OilRig](https://attack.mitre.org/groups/G0049) has used `reg query “HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default”` on a victim to query the Registry.[^27]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [OilRig](https://attack.mitre.org/groups/G0049) has used various types of scripting for execution.[^4] [^26] [^29] [^38] [^15]  |
| [[System Checks\|T1497.001]] | System Checks | [OilRig](https://attack.mitre.org/groups/G0049) has used macros to verify if a mouse is connected to a compromised machine.[^11]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [OilRig](https://attack.mitre.org/groups/G0049) has exploited the Windows Kernel Elevation of Privilege vulnerability, CVE-2024-30088.[^6]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [OilRig](https://attack.mitre.org/groups/G0049) has tested malware samples to determine AV detection and subsequently modified the samples to ensure AV evasion.[^3] [^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^27] [^4] [^42] <br> |
| [[certutil\|S0160]] | certutil | [^4] [^42]  |
| [[ipconfig\|S0100]] | ipconfig | [^27]  |
| [[Tasklist\|S0057]] | Tasklist | [^27] [^4]  |
| [[ngrok\|S0508]] | ngrok | [^6]  |
| [[netstat\|S0104]] | netstat | [^27] [^4] [^42]  |
| [[Systeminfo\|S0096]] | Systeminfo | [^4]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^39] [^18] [^40] [^42]  |
| [[LaZagne\|S0349]] | LaZagne | [^40]  |
| [[Reg\|S0075]] | Reg | [^27] [^4]  |
| [[ftp\|S0095]] | ftp | [^24]  |
| [[PsExec\|S0029]] | PsExec | [^18]  |
| [[SEASHARPEE\|S0185]] | SEASHARPEE | [^18]  |
| [[POWRUNER\|S0184]] | POWRUNER | [^4]  |
| [[PowerExchange\|S1173]] | PowerExchange | [^42]  |
| [[ODAgent\|S1170]] | ODAgent | [^36]  |
| [[RDAT\|S0495]] | RDAT | [^8]  |
| [[ISMInjector\|S0189]] | ISMInjector | [^25]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [^38]  |
| [[ZeroCleare\|S1151]] | ZeroCleare | [OilRig](https://attack.mitre.org/groups/G0049) collaborated on the destructive portion of the [ZeroCleare](https://attack.mitre.org/software/S1151) attack.[^37]  |
| [[OopsIE\|S0264]] | OopsIE | [^29]  |
| [[OilCheck\|S1171]] | OilCheck | [^36]  |
| [[SampleCheck5000\|S1168]] | SampleCheck5000 | [^31]  |
| [[OilBooster\|S1172]] | OilBooster | [^36]  |
| [[Solar\|S1166]] | Solar | [^31]  |
| [[RGDoor\|S0258]] | RGDoor | [^35]  |
| [[Mango\|S1169]] | Mango | [^31]  |
| [[BONDUPDATER\|S0360]] | BONDUPDATER | [^4]  [^12]  |
| [[SideTwist\|S0610]] | SideTwist | [^11]  |
| [[Helminth\|S0170]] | Helminth | [^27] [^18] [^43]  |



## References

[^1]: Crambus


[^2]: EUROPIUM


[^3]: [Palo Alto OilRig April 2017](http://researchcenter.paloaltonetworks.com/2017/04/unit42-oilrig-actors-provide-glimpse-development-testing-efforts/)


[^4]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^5]: [Proofpoint Iranian Aligned Attacks JAN 2020](https://www.proofpoint.com/us/corporate-blog/post/iranian-state-sponsored-and-aligned-attacks-what-you-need-know-and-steps-protect)


[^6]: [Trend Micro Earth Simnavaz October 2024](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)


[^7]: [ClearSky OilRig Jan 2017](http://www.clearskysec.com/oilrig/)


[^8]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^9]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^10]: [FireEye Targeted Attacks Middle East Banks](https://web.archive.org/web/20200618235708/https://www.fireeye.com/blog/threat-research/2016/05/targeted_attacksaga.html)


[^11]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^12]: [Palo Alto OilRig Sep 2018](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)


[^13]: TA452


[^14]: [FireEye APT34 July 2019](https://www.fireeye.com/blog/threat-research/2019/07/hard-pass-declining-apt34-invite-to-join-their-professional-network.html)


[^15]: [Unit42 OilRig Nov 2018](https://unit42.paloaltonetworks.com/unit42-analyzing-oilrigs-ops-tempo-testing-weaponization-delivery/)


[^16]: ITG13


[^17]: Hazel Sandstorm


[^18]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^19]: OilRig


[^20]: Earth Simnavaz


[^21]: [Secureworks COBALT GYPSY Threat Profile](https://www.secureworks.com/research/threat-profiles/cobalt-gypsy)


[^22]: IRN2


[^23]: COBALT GYPSY


[^24]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)


[^25]: [OilRig New Delivery Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)


[^26]: [OilRig ISMAgent July 2017](https://researchcenter.paloaltonetworks.com/2017/07/unit42-oilrig-uses-ismdoor-variant-possibly-linked-greenbug-threat-group/)


[^27]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^28]: Helix Kitten


[^29]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^30]: APT34


[^31]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^32]: [FireEye Outlook Dec 2019](https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html)


[^33]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^34]: Evasive Serpens


[^35]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)


[^36]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^37]: [IBM ZeroCleare Wiper December 2019](https://securityintelligence.com/posts/new-destructive-wiper-zerocleare-targets-energy-sector-in-the-middle-east/)


[^38]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^39]: [Unit42 OilRig Playbook 2023](https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)


[^40]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^41]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^42]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^43]: [Crowdstrike Helix Kitten Nov 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/)


