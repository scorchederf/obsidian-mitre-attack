---
aliases: 
    - T1560.001
mitre-attack: https://attack.mitre.org/techniques/T1560/001
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1560.001

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.<br><br>Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as `tar` on Linux and macOS or `zip` on Windows systems. <br><br>On Windows, `diantz` or ` makecab` may be used to package collected files into a cabinet (.cab) file. `diantz` may also be used to download and compress files from remote locations (i.e. [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002)).[^183]  `xcopy` on Windows can copy files and directories with a variety of options. Additionally, adversaries may use [certutil](https://attack.mitre.org/software/S0160) to Base64 encode collected data before exfiltration. <br><br>Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.[^379] [^229] [^24] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [certutil](https://attack.mitre.org/software/S0160) may be used to Base64 encode collected data.[^56] [^228]  |
| [[PoshC2\|S0378]] | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for compressing data using ZIP.[^185]  |
| [[Rclone\|S1040]] | Rclone | [Rclone](https://attack.mitre.org/software/S1040) can compress files using `gzip` prior to exfiltration.[^385]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can zip files and folders for upload.[^332]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can compress data with Zip before sending it over C2.[^108]  |
| [[WindTail\|S0466]] | WindTail | [WindTail](https://attack.mitre.org/software/S0466) has the ability to use the macOS built-in zip utility to archive files.[^107]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used 7zip, RAR and zip files to archive collected data for exfiltration.[^39] [^88]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) used WinRAR rar.exe to archive files for exfiltration.[^171] [^262]  [TONESHELL](https://attack.mitre.org/software/S1239) has also utilized a unique 13-character password consisting of upper lower case and digits to protect RAR archives.[^262]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can zip and encrypt data collected on a target system.[^393]  |
| [[iKitten\|S0278]] | iKitten | [iKitten](https://attack.mitre.org/software/S0278) will zip up the /Library/Keychains directory before exfiltrating it.[^303]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can use WinRAR to create a password-protected archive for files of interest.[^330]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has used utilities such as `WinRAR` to archive data prior to exfiltration.[^318]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) uses WinRAR to compress data that is intended to be exfiltrated.[^157]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) was seen using a RAR archiver tool to compress/decompress data.[^309]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has used 7Zip to compress .txt, .pdf, .xls or .doc files prior to exfiltration.[^409]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has Gzipped information and saved it to a random temp file before exfil.[^396] 	 |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has collected and archived sensitive data in a zip file.[^35]  |
| [[DustySky\|S0062]] | DustySky | [DustySky](https://attack.mitre.org/software/S0062) can compress files via RAR while staging data to be exfiltrated.[^40]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) has archived collected materials in RAR format.[^224]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has archived collected files within a zip file prior to exfiltration to include `/tmp/out.zip`.[^347]  |
| [[CORALDECK\|S0212]] | CORALDECK | [CORALDECK](https://attack.mitre.org/software/S0212) has created password-protected RAR, WinImage, and zip archives to be exfiltrated.[^64]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) creates a RAR archive based on collected files on the victim's machine.[^154]  |
| [[OopsIE\|S0264]] | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) compresses collected files with GZipStream before sending them to its C2 server.[^42]  |
| [[Crutch\|S0538]] | Crutch | [Crutch](https://attack.mitre.org/software/S0538) has used the WinRAR utility to compress and encrypt stolen files.[^209]  |
| [[ccf32\|S1043]] | ccf32 | [ccf32](https://attack.mitre.org/software/S1043) has used `xcopy \\<target_host>\c$\users\public\path.7z c:\users\public\bin\<target_host>.7z /H /Y` to archive collected files.[^165]  |
| [[SampleCheck5000\|S1168]] | SampleCheck5000 | [SampleCheck5000](https://attack.mitre.org/software/S1168) can gzip compress files uploaded to a shared mailbox used for C2 and exfiltration.[^204]  |
| [[Daserf\|S0187]] | Daserf | [Daserf](https://attack.mitre.org/software/S0187) hides collected data in password-protected .rar archives.[^110]  |
| [[Calisto\|S0274]] | Calisto | [Calisto](https://attack.mitre.org/software/S0274) uses the `zip -r` command to compress the data collected on the local system.[^314] [^100]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can compress and archive collected files using WinRAR.[^225] [^7]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can xcopy for file collection on targeted systems.[^85]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to compress files with zip.[^227]  |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022) can encrypt and compress files using Gzip prior to exfiltration.[^349]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can create a ZIP archive with specified files and directories.[^284]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) has compressed data before exfiltrating it using a tool called Abbrevia.[^300]   |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has archived data into ZIP files on compromised machines.[^73]  |
| [[UNC3886\|G1048]] | UNC3886 | [UNC3886](https://attack.mitre.org/groups/G1048) has used Gzip and the Windows command `makecab` to compress files and stolen credentials from victim systems.[^207] [^84]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used 7-Zip to archive data.[^158]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used several publicly available tools, including WinRAR and 7zip, to compress collected files and memory dumps prior to exfiltration.[^389] [^137]  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used WinRAR to compress stolen files into an archive prior to exfiltration.[^340]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has used QuickZip to archive stolen files before exfiltration.[^358]  [Kimsuky](https://attack.mitre.org/groups/G0094) has used the Send() function to compress all collected data into a zip file named init,.zip, then renames it to init.dat, before exfiltration.[^79]  |
| [[Play\|G1040]] | Play | <br>[Play](https://attack.mitre.org/groups/G1040) has used WinRAR to compress files prior to exfiltration.[^68] [^177]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has encrypted files stolen from connected USB drives into a RAR file before exfiltration.[^258]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has used a variety of utilities, including WinRAR, to archive collected data with password protection.[^371]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) is known to use 7Zip and RAR with passwords to encrypt data prior to exfiltration.[^74] [^109]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has archived the ntds.dit database as a multi-volume password-protected archive with 7-Zip.[^257] [^233]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used gzip to archive dumped LSASS process memory and RAR to stage and compress local folders.[^95] [^223] [^254]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used 7-Zip and WinRAR to compress stolen files for exfiltration.[^221] [^180]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has used WinRAR and 7-Zip to compress an archive stolen data.[^214]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used the native Windows cabinet creation tool, makecab.exe, likely to compress stolen data to be uploaded.[^77]  |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has compressed data into password-protected RAR archives prior to exfiltration.[^87] [^130]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has used the JAR/ZIP file format for exfiltrated files.[^271]  |
| [[Akira\|G1024]] | Akira | [Akira](https://attack.mitre.org/groups/G1024) uses utilities such as WinRAR to archive data prior to exfiltration.[^118]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used RAR to create password-protected archives of collected documents prior to exfiltration.[^187] [^179]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has used WinRAR “Rar.exe” to archive stolen files before exfiltration.[^262]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used [TONESHELL](https://attack.mitre.org/software/S1239) and post-exploitation tools such as RemCom and [Impacket](https://attack.mitre.org/software/S0357) to execute WinRAR `rar.exe` to archive files for exfiltration.[^171]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used gzip for Linux OS and a modified RAR software to archive data on Windows hosts.[^11] [^293]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has leveraged  xcopy, 7zip, and RAR to stage and compress collected documents prior to exfiltration.[^232]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has compressed files before exfiltration using TAR and RAR.[^143] [^235] [^269]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used rar.exe and the Makecab utility to archive files of interest prior to exfiltration.[^116] [^406] [^296]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has stored collected data in a password protected compressed file prior to exfiltration.[^355]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) created a RAR archive of targeted files for exfiltration.[^134]  Additionally, [APT41](https://attack.mitre.org/groups/G0096) used the makecab.exe utility to both download tools, such as NATBypass, to the victim network and to archive a file for exfiltration.[^75]  |
| [[INC Ransom\|G1032]] | INC Ransom | [INC Ransom](https://attack.mitre.org/groups/G1032) has used 7-Zip and WinRAR to archive collected data prior to exfiltration.[^10] [^333] [^230] [^278]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has compressed the dump output of compromised credentials with a 7zip binary.[^248]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used WinRAR to compress and encrypt stolen data prior to exfiltration.[^216] [^193]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used RAR to compress collected data before exfiltration.[^117]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has downloaded 7-Zip to decompress password protected archives.[^402]   |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) used 7zip to archive extracted data in preparation for exfiltration.[^129]  |
| [[Sea Turtle\|G1041]] | Sea Turtle | [Sea Turtle](https://attack.mitre.org/groups/G1041) used the tar utility to create a local archive of email data on a victim system.[^210]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has used tools to compress data before exfilling it.[^243]  |
| [[APT1\|G0006]] | APT1 | [APT1](https://attack.mitre.org/groups/G0006) has used RAR to compress files before moving them outside of the victim network.[^70]  |
| [[Sowbug\|G0054]] | Sowbug | [Sowbug](https://attack.mitre.org/groups/G0054) extracted documents and bundled them into a RAR archive.[^291]  |
| [[APT33\|G0064]] | APT33 | [APT33](https://attack.mitre.org/groups/G0064) has used WinRAR to compress data prior to exfil.[^106] 	<br> |
| [[Lotus Blossom\|G0030]] | Lotus Blossom | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used WinRAR for compressing data in RAR format.[^224] [^32]  |
| [[Gallmaker\|G0084]] | Gallmaker | [Gallmaker](https://attack.mitre.org/groups/G0084) has used WinZip, likely to archive data prior to exfiltration.[^78]  |
| [[CopyKittens\|G0052]] | CopyKittens | [CopyKittens](https://attack.mitre.org/groups/G0052) uses ZPP, a .NET console program, to compress files with ZIP.[^288]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Audit\|M1047]] | Audit | System scans can be performed to identify unauthorized archival utilities. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Archive via Utility\|T1560.001]] | Archive via Utility |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^11]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^12]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^13]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^14]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^15]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^16]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^17]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^18]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^19]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^20]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^21]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^22]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^23]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^24]: [WinZip Homepage](https://www.winzip.com/win/en/)


[^25]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^26]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^27]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^28]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^29]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^30]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^31]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^32]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^33]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^34]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^35]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^36]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^37]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^38]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^39]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^40]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^41]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^42]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^43]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^44]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^45]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^46]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^47]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^48]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^49]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^50]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^51]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^52]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^53]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^54]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^55]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^56]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)


[^57]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^58]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^59]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^60]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^61]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^62]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^63]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^64]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^65]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^66]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^67]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^68]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


[^69]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^70]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^71]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^72]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^73]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^74]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^75]: [apt41_dcsocytec_dec2022](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)


[^76]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^77]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


[^78]: [Symantec Gallmaker Oct 2018](https://www.symantec.com/blogs/threat-intelligence/gallmaker-attack-group)


[^79]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^80]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^81]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^82]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^83]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^84]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^85]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^86]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^87]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^88]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^89]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^90]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^91]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^92]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^93]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^94]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^95]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^96]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^97]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^98]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^99]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^100]: [Symantec Calisto July 2018](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)


[^101]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^102]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^103]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^104]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^105]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^106]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^107]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)


[^108]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^109]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^110]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


[^111]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^112]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^113]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^114]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^115]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^116]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^117]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^118]: [Secureworks GOLD SAHARA](https://www.secureworks.com/research/threat-profiles/gold-sahara)


[^119]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^120]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^121]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^122]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^123]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^124]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^125]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^126]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^127]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^128]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^129]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^130]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^131]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^132]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^133]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^134]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^135]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^136]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^137]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^138]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^139]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^140]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^141]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^142]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^143]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)


[^144]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^145]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^146]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^147]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^148]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^149]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^150]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^151]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^152]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^153]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^154]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^155]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^156]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^157]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^158]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^159]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^160]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^161]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^162]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^163]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^164]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^165]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^166]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^167]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^168]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^169]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^170]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^171]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^172]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^173]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^174]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^175]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^176]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^177]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^178]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^179]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^180]: [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)


[^181]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^182]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^183]: [diantz.exe_lolbas](https://lolbas-project.github.io/lolbas/Binaries/Diantz/)


[^184]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^185]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


[^186]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^187]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)


[^188]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^189]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^190]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^191]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^192]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^193]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^194]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^195]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^196]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^197]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^198]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^199]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^200]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^201]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^202]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^203]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^204]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^205]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^206]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^207]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^208]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^209]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^210]: [Hunt Sea Turtle 2024](https://www.huntandhackett.com/blog/turkish-espionage-campaigns)


[^211]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^212]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^213]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^214]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^215]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^216]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^217]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^218]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^219]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^220]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^221]: [Microsoft HAFNIUM March 2020](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)


[^222]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^223]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^224]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^225]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^226]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^227]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^228]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)


[^229]: [WinRAR Homepage](https://www.rarlab.com/)


[^230]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^231]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^232]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^233]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^234]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^235]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^236]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^237]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^238]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^239]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^240]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^241]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^242]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^243]: [aptsim](http://carnal0wnage.attackresearch.com/2012/09/more-on-aptsim.html)


[^244]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^245]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^246]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^247]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^248]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^249]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^250]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^251]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^252]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^253]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^254]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^255]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^256]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^257]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^258]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^259]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^260]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^261]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^262]: [Unit42 Chinese VSCode 06 September 2024](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)


[^263]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^264]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^265]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^266]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^267]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^268]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^269]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^270]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^271]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^272]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^273]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^274]: [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)


[^275]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^276]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^277]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^278]: [Huntress INC Ransomware May 2024](https://www.huntress.com/blog/lolbin-to-inc-ransomware)


[^279]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^280]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^281]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^282]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^283]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^284]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^285]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^286]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^287]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^288]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^289]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^290]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^291]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^292]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^293]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^294]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^295]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^296]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^297]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^298]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^299]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^300]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^301]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^302]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^303]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^304]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^305]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^306]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^307]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^308]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^309]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^310]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^311]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^312]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^313]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^314]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)


[^315]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^316]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^317]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^318]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^319]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^320]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^321]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^322]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^323]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^324]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^325]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^326]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^327]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^328]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^329]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^330]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^331]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^332]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^333]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^334]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^335]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^336]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^337]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^338]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^339]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^340]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^341]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^342]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^343]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^344]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^345]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^346]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^347]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^348]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^349]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^350]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^351]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^352]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^353]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^354]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^355]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^356]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^357]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^358]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^359]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^360]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^361]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^362]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^363]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^364]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^365]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^366]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^367]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^368]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^369]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^370]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^371]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^372]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^373]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^374]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^375]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^376]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^377]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^378]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^379]: [7zip Homepage](https://www.7-zip.org/)


[^380]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^381]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^382]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^383]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^384]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^385]: [Rclone](https://rclone.org)


[^386]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^387]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^388]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^389]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^390]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^391]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^392]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^393]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^394]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^395]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^396]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)


[^397]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^398]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^399]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^400]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^401]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^402]: [trendmicro_redcurl](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)


[^403]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^404]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^405]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^406]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^407]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^408]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^409]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^410]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^411]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^412]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^413]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^414]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^415]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^416]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^417]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^418]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^419]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^420]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


