---
aliases: 
    - T1070.006
mitre-attack: https://attack.mitre.org/techniques/T1070/006
tactic: 
     - Stealth
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## T1070.006

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files.<br><br>In Windows systems, both the `$STANDARD_INFORMATION` (`$SI`) and `$FILE_NAME` (`$FN`) attributes record times in a Master File Table (MFT) file.[^33]  `$SI` (dates/time stamps) is displayed to the end user, including in the File System view, while `$FN` is dealt with by the kernel.[^269] <br><br>Modifying the `$SI` attribute is the most common method of timestomping because it can be modified at the user level using API calls. `$FN` timestomping, however, typically requires interacting with the system kernel or moving or renaming a file.[^33] <br><br>Adversaries modify timestamps on files so that they do not appear conspicuous to forensic investigators or file analysis tools. In order to evade detections that rely on identifying discrepancies between the `$SI` and `$FN` attributes, adversaries may also engage in “double timestomping” by modifying times on both attributes simultaneously.[^356] <br><br>In Linux systems and on ESXi servers, threat actors may attempt to perform timestomping using commands such as `touch -a -m -t <timestamp> <filename>` (which sets access and modification times to a specific value) or `touch -r <filename> <filename>` (which sets access and modification times to match those of another file).[^314] [^201] <br><br>Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools.[^326] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can timestomp any files or payloads placed on a target machine to help them blend in.[^119]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has modified file and directory timestamps.[^221] [^72]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can change or create the last access or write times.[^154]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) extracts and writes driver files that match the times of other legitimate files.[^321]  |
| [[SEASHARPEE\|S0185]] | SEASHARPEE | [SEASHARPEE](https://attack.mitre.org/software/S0185) can timestomp files on victims using a Web shell.[^234]  |
| [[TDTESS\|S0164]] | TDTESS | After creating a new service for persistence, [TDTESS](https://attack.mitre.org/software/S0164) sets the file creation time for the service to the creation time of the victim's legitimate svchost.exe file.[^256]  |
| [[Misdat\|S0083]] | Misdat | Many [Misdat](https://attack.mitre.org/software/S0083) samples were programmed using Borland Delphi, which will mangle the default PE compile timestamp of a file.[^344]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) modifies the time of a file as specified by the control server.[^368]  |
| [[UPSTYLE\|S1164]] | UPSTYLE | [UPSTYLE](https://attack.mitre.org/software/S1164) restores timestamps to original values following modification.[^67]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has modified file timestamps from the export address table (EAT) to make it difficult to discern when the module was created. [^20]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) has the ability to timestomp a file.[^199]  |
| [[BlackByte 2.0 Ransomware\|S1181]] | BlackByte 2.0 Ransomware | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) can timestomp files for defense evasion and anti-forensics purposes.[^175]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) samples were timestomped by the authors by setting the PE timestamps to all zero values. [InvisiMole](https://attack.mitre.org/software/S0260) also has a built-in command to modify file times.[^140]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can time stomp its executable, previously dating it between 2010 to 2021.[^329]  |
| [[China Chopper\|S0020]] | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can change the timestamp of files.[^252] [^350] [^148]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) time-stomped its DLL in order to evade detection.[^110]  |
| [[POSHSPY\|S0150]] | POSHSPY | [POSHSPY](https://attack.mitre.org/software/S0150) modifies timestamps of all downloaded executables to match a randomly selected file created prior to 2013.[^227]  |
| [[MultiLayer Wiper\|S1135]] | MultiLayer Wiper | [MultiLayer Wiper](https://attack.mitre.org/software/S1135) changes timestamps of overwritten files to either 1601.1.1 for NTFS filesystems, or 1980.1.1 for all other filesystems.[^113]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) performs timestomping of a CAB file it creates.[^297]  |
| [[Gazer\|S0168]] | Gazer | For early [Gazer](https://attack.mitre.org/software/S0168) versions, the compilation timestamp was faked.[^56]  |
| [[3PARA RAT\|S0066]] | 3PARA RAT | [3PARA RAT](https://attack.mitre.org/software/S0066) has a command to set certain attributes such as creation/modification timestamps on files.[^60]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) has changed the creation date of files.[^202]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can change the timestamp of specified filenames.[^29]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) can change the modified time for files to evade forensic detection.[^355] 	 |
| [[BPFDoor\|S1161]] | BPFDoor | [BPFDoor](https://attack.mitre.org/software/S1161) uses the `utimes()` function to change the executable's timestamp.[^55]   |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438) has manipulated the time of last access to files and registry keys after they have been created or modified.[^333]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can modify the Creation, Access, and Write timestamps for malicious DLLs to match those of the genuine Windows DLL user32.dll.[^379]  |
| [[Derusbi\|S0021]] | Derusbi | The [Derusbi](https://attack.mitre.org/software/S0021) malware supports timestomping.[^316] [^370]  |
| [[Kobalos\|S0641]] | Kobalos | [Kobalos](https://attack.mitre.org/software/S0641) can modify timestamps of replaced files, such as `ssh` with the added credential stealer or `sshd` used to deploy [Kobalos](https://attack.mitre.org/software/S0641).[^162]   |
| [[HiddenFace\|S9023]] | HiddenFace |  [HiddenFace](https://attack.mitre.org/software/S9023) can alter timestamps for directory content on targeted machines.[^198] [^374] [^263]  |
| [[OwaAuth\|S0072]] | OwaAuth | [OwaAuth](https://attack.mitre.org/software/S0072) has a command to timestop a file or directory.[^305]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can timestomp any files or payloads placed on a target machine to help them blend in.[^163] [^14]  |
| [[USBStealer\|S0136]] | USBStealer | [USBStealer](https://attack.mitre.org/software/S0136) sets the timestamps of its dropper files to the last-access and last-write timestamps of a standard Windows library chosen on the system.[^353]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can use the `touch -t` command to change timestamps.[^219] [^141]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to use the Linux API function `utime` to change the timestamps of modified firmware update images.[^213]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) has the capability to create and modify file timestamps.[^31]  |
| [[SPAWNCHIMERA\|S9024]] | SPAWNCHIMERA | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has updated the timestamp using the `touch` command.[^86]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can set the timestamps for its worker and service components to match that of cmd.exe.[^323]  |
| [[PowerStallion\|S0393]] | PowerStallion | [PowerStallion](https://attack.mitre.org/software/S0393) modifies the MAC times of its local log files to match that of the victim's desktop.ini file.[^214]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can change the `CreationTime`, `LastAccessTime`, and `LastWriteTime` file time attributes when executed with `SYSTEM` privileges.[^231]  |
| [[Psylo\|S0078]] | Psylo | [Psylo](https://attack.mitre.org/software/S0078) has a command to conduct timestomping by setting a specified file’s timestamps to match those of a system file in the System32 directory.[^7]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to perform timestomping of files on targeted systems.[^364]  |
| [[BitPaymer\|S0570]] | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) can modify the timestamp of an executable so that it can be identified and restored by the decryption tool.[^35]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) can modify file or directory timestamps.[^232]  |
| [[UNC3886\|G1048]] | UNC3886 | [UNC3886](https://attack.mitre.org/groups/G1048) has used scripts to timestomp ESXi hosts prior to installing malicious vSphere Installation Bundles (VIBs).[^367]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families use timestomping, including modifying the last write timestamp of a specified Registry key to a random date, as well as copying the timestamp for legitimate .exe files (such as calc.exe or mspaint.exe) to its dropped files.[^287] [^218] [^149] [^128]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has manipulated timestamps for creation or compilation dates to defeat anti-forensics.[^96]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has performed timestomping on victim files.[^97]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has used timestomping to alter the Standard Information timestamps on their web shells to match other files in the same directory.[^387]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has modified data timestamps to mimic files that are in the same folder on a compromised host.[^347]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has used scheduled task raw XML with a backdated timestamp of June 2, 2016. The group has also set the creation time of the files dropped by the second stage of the exploit to match the creation time of kernel32.dll. Additionally, [APT32](https://attack.mitre.org/groups/G0050) has used a random value to modify the timestamp of the file storing the clientID.[^58] [^138] [^132]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has modified file timestamps.[^241]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has modified file timestamps from the export address table (EAT) in malware to make it difficult to identify creation times.[^20]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used a Windows version of the Linux `touch` command to modify the date and time stamp on DLLs.[^260]  |
| [[Rocke\|G0106]] | Rocke | [Rocke](https://attack.mitre.org/groups/G0106) has changed the time stamp of certain files.[^381] 	 |






### Sub-techniques
| ID | Name |
| --- | --- |
| [[Timestomp\|T1070.006]] | Timestomp |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^11]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^15]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^16]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^17]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^18]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^19]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^20]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^21]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^22]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^23]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^24]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^25]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^26]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^27]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^28]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^29]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^30]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^31]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^32]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^33]: [Inversecos Timestomping 2022](https://www.inversecos.com/2022/04/defence-evasion-technique-timestomping.html)


[^34]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^35]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^36]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^37]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^38]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^39]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^40]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^41]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^42]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^43]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^44]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^45]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^46]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^47]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^48]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^49]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^50]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^51]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^52]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^53]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^54]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^55]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)


[^56]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)


[^57]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^58]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^59]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^60]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^61]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^62]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^63]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^64]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^65]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^66]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^67]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)


[^68]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^69]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^70]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^71]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^72]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)


[^73]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^74]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^75]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^76]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^77]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^78]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^79]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^80]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^81]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^82]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^83]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^84]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^85]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^86]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)


[^87]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^88]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^89]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^90]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^91]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^92]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^93]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^94]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^95]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^96]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^97]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^98]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^99]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^100]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^101]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^102]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^103]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^104]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^105]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^106]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^107]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^108]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^109]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^110]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^111]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^112]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^113]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^114]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^115]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^116]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^117]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^118]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^119]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^120]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^121]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^122]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^123]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^124]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^125]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^126]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^127]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^128]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^129]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^130]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^131]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^132]: [ESET OceanLotus macOS April 2019](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)


[^133]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^134]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^135]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^136]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^137]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^138]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^139]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^140]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^141]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


[^142]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^143]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^144]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^145]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^146]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^147]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^148]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^149]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^150]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^151]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^152]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^153]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^154]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^155]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^156]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^157]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^158]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^159]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^160]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^161]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^162]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)


[^163]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)


[^164]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^165]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^166]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^167]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^168]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^169]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^170]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^171]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^172]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^173]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^174]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^175]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^176]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^177]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^178]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^179]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^180]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^181]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^182]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^183]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^184]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^185]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^186]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^187]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^188]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^189]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^190]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^191]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^192]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^193]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^194]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^195]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^196]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^197]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^198]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^199]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^200]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^201]: [Juniper Networks ESXi Backdoor 2022](https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers)


[^202]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^203]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^204]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^205]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^206]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^207]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^208]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^209]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^210]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^211]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^212]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^213]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^214]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^215]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^216]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^217]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^218]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^219]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^220]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^221]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^222]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^223]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^224]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^225]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^226]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^227]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)


[^228]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^229]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^230]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^231]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^232]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^233]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^234]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^235]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^236]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^237]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^238]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^239]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^240]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^241]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^242]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^243]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^244]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^245]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^246]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^247]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^248]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^249]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^250]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^251]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^252]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^253]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^254]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^255]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^256]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^257]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^258]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^259]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^260]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^261]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^262]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^263]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^264]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^265]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^266]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^267]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^268]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^269]: [Magnet Forensics](https://www.magnetforensics.com/blog/expose-evidence-of-timestomping-with-the-ntfs-timestamp-mismatch-artifact-in-magnet-axiom-4-4/)


[^270]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^271]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^272]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^273]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^274]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^275]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^276]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^277]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^278]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^279]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^280]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^281]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^282]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^283]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^284]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^285]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^286]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^287]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^288]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^289]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^290]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^291]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^292]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^293]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^294]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^295]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^296]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^297]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^298]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^299]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^300]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^301]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^302]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^303]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^304]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^305]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^306]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^307]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^308]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^309]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^310]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^311]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^312]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^313]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^314]: [Inversecos Linux Timestomping](https://www.inversecos.com/2022/08/detecting-linux-anti-forensics.html)


[^315]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^316]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^317]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^318]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^319]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^320]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^321]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^322]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^323]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^324]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^325]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^326]: [WindowsIR Anti-Forensic Techniques](http://windowsir.blogspot.com/2013/07/howto-determinedetect-use-of-anti.html)


[^327]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^328]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^329]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^330]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^331]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^332]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^333]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^334]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^335]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^336]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^337]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^338]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^339]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^340]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^341]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^342]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^343]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^344]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^345]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^346]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^347]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^348]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^349]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^350]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)


[^351]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^352]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^353]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)


[^354]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^355]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)


[^356]: [Double Timestomping](https://x.com/matthewdunwoody/status/1519846657646604289)


[^357]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^358]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^359]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^360]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^361]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^362]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^363]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^364]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^365]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^366]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^367]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)


[^368]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^369]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^370]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^371]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^372]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^373]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^374]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^375]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^376]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^377]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^378]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^379]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^380]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^381]: [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)


[^382]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^383]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^384]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^385]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^386]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^387]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^388]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^389]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^390]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


