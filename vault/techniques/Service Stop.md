---
aliases: 
    - T1489
mitre-attack: https://attack.mitre.org/techniques/T1489
tactic: 
     - Impact
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## T1489

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.[^35] [^291]  <br><br>Adversaries may accomplish this by disabling individual services of high importance to an organization, such as `MSExchangeIS`, which will make Exchange content inaccessible.[^291]  In some cases, adversaries may stop or disable many or all services to render systems unusable.[^35]  Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [Data Destruction](https://attack.mitre.org/techniques/T1485) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.[^191] [^180] <br><br>Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.[^245] [^114] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[EKANS\|S0605]] | EKANS | [EKANS](https://attack.mitre.org/software/S0605) stops database, data backup solution, antivirus, and ICS-related processes.[^278] [^173] [^372]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has terminated an existing process to ensure that its own new process can execute.[^159]  |
| [[AvosLocker\|S1053]] | AvosLocker | [AvosLocker](https://attack.mitre.org/software/S1053) has terminated specific processes before encryption.[^321]  |
| [[RobbinHood\|S0400]] | RobbinHood | [RobbinHood](https://attack.mitre.org/software/S0400) stops 181 Windows services on the system before beginning the encryption process.[^324]   |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to terminate specified services.[^199]  |
| [[Prestige\|S1058]] | Prestige | [Prestige](https://attack.mitre.org/software/S1058) has attempted to stop the MSSQL Windows service to ensure successful encryption using `C:\Windows\System32\net.exe stop MSSQLSERVER`.[^285]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has terminated Chrome and Brave browsers using the `taskkill` command on Windows and the `killall` command on other systems such as Linux and macOS.[^43]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also utilized it’s `ssh_kill` command to terminate Chrome and Brave browser processes.[^165]  |
| [[Hannotog\|S1211]] | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) can stop Windows services.[^36]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has the capability to terminate services related to backups, security, databases, communication, filesharing and websites.[^24] [^100] [^284]  [Medusa Ransomware](https://attack.mitre.org/software/S1244) has also utilized the `taskkill /F /IM <process> /T` command to stop targeted processes and `net stop <process>` command to stop designated services.[^100] [^284]  |
| [[Olympic Destroyer\|S0365]] | Olympic Destroyer | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses the API call `ChangeServiceConfigW` to disable all services on the affected system.[^35]  |
| [[BlackByte 2.0 Ransomware\|S1181]] | BlackByte 2.0 Ransomware | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) can terminate running services.[^177]  |
| [[Conti\|S0575]] | Conti | [Conti](https://attack.mitre.org/software/S0575) can stop up to 146 Windows services related to security, backup, database, and email solutions through the use of `net stop`.[^347]  |
| [[Megazord\|S1191]] | Megazord | [Megazord](https://attack.mitre.org/software/S1191) has the ability to terminate a list of services and processes.[^266]  |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) will terminate services using the Service Control Manager (SCM) API.[^377]   |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to stop VM services on compromised networks.[^33] [^386]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | [Ragnar Locker](https://attack.mitre.org/software/S0481) has attempted to stop services associated with business applications and databases to release the lock on files used by these applications so they may be encrypted.[^210]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) looks for and attempts to stop database processes.[^382]  |
| [[Cheerscrypt\|S1096]] | Cheerscrypt | [Cheerscrypt](https://attack.mitre.org/software/S1096) has the ability to terminate VM processes on compromised hosts through execution of `esxcli vm process kill`.[^76] <br> |
| [[Babuk\|S0638]] | Babuk | [Babuk](https://attack.mitre.org/software/S0638) can stop specific services related to backups.[^259] [^353] [^334]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) has a hardcoded list of services and processes to terminate.[^19]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can terminate targeted processes and services related to security, backup, database management, and other applications that could stop or interfere with encryption.[^312] [^315] [^358] [^110]  |
| [[Netwalker\|S0457]] | Netwalker | [Netwalker](https://attack.mitre.org/software/S0457) can terminate system processes and services, some of which relate to backup software.[^68]  |
| [[WannaCry\|S0366]] | WannaCry | [WannaCry](https://attack.mitre.org/software/S0366) attempts to kill processes associated with Exchange, Microsoft SQL Server, and MySQL to make it possible to encrypt their data stores.[^96] [^191]  |
| [[Pay2Key\|S0556]] | Pay2Key | [Pay2Key](https://attack.mitre.org/software/S0556) can stop the MS SQL service at the end of the encryption process to release files locked by the service.[^283]  |
| [[Royal\|S1073]] | Royal | [Royal](https://attack.mitre.org/software/S1073) can use `RmShutDown` to kill  applications and services using the resources that are targeted for encryption.[^34]  |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has terminated active processes and services based on a hardcoded list using the `CloseServiceHandle()` function.[^202]  [Embargo](https://attack.mitre.org/software/S1247) has also leveraged MS4Killer to terminate processes contained in an embedded list of security software process names that were XOR-encrypted.[^103]  |
| [[MegaCortex\|S0576]] | MegaCortex | [MegaCortex](https://attack.mitre.org/software/S0576) can stop and disable services on the system.[^39]   |
| [[Akira _v2\|S1194]] | Akira _v2 | [Akira _v2](https://attack.mitre.org/software/S1194) can stop running virtual machines.[^85] [^9] [^266]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has called `kill.bat` for stopping services, disabling services and killing processes.[^30]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to stop the Volume Shadow Copy service.[^289]  |
| [[Pysa\|S0583]] | Pysa | [Pysa](https://attack.mitre.org/software/S0583) can stop services and processes.[^109]   |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can automatically terminate processes that may interfere with the encryption or file extraction processes.[^222]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to stop services on the infected host.[^73]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) has the capability to stop services and kill processes.[^207] [^44]  |
| [[ROADSWEEP\|S1150]] | ROADSWEEP | [ROADSWEEP](https://attack.mitre.org/software/S1150) can disable critical services and processes.[^331]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) can kill processes and delete services.[^208]  |
| [[PHASEJAM\|S9014]] | PHASEJAM | [PHASEJAM](https://attack.mitre.org/software/S9014) has disabled the `cgi-server` process on Ivanti Connect Secure appliances.[^174]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) can kill several processes and services related to backups and security solutions.[^60] [^205]   |
| [[Meteor\|S0688]] | Meteor | [Meteor](https://attack.mitre.org/software/S0688) can disconnect all network adapters on a compromised host using `powershell -Command "Get-WmiObject -class Win32_NetworkAdapter | ForEach { If ($.NetEnabled) { $.Disable() } }" > NUL`.[^340]  |
| [[Maze\|S0449]] | Maze | [Maze](https://attack.mitre.org/software/S0449) has stopped SQL services to ensure it can encrypt any database.[^230]   |
| [[VIRTUALPITA\|S1217]] | VIRTUALPITA | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can start and stop the `vmsyslogd` service.[^189]  |
| [[KillDisk\|S0607]] | KillDisk | [KillDisk](https://attack.mitre.org/software/S0607) terminates various processes to get the user to reboot the victim machine.[^156]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can terminate specific services on compromised hosts.[^197] [^224] [^46] [^378]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604)’s data wiper module writes zeros into the registry keys in `SYSTEM\CurrentControlSet\Services` to render a system inoperable.[^330]  |
| [[DRYHOOK\|S9013]] | DRYHOOK | [DRYHOOK](https://attack.mitre.org/software/S9013) has terminated all instances of the `cgi-server` process before activating the modified DSAuth.pm file.[^174]  |
| [[INC Ransomware\|S1139]] | INC Ransomware | [INC Ransomware](https://attack.mitre.org/software/S1139) can issue a command to kill a process on compromised hosts.[^335]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has the capability to stop processes and services.[^82]  |
| [[Indrik Spider\|G0119]] | Indrik Spider | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used [PsExec](https://attack.mitre.org/software/S0029) to stop services prior to the execution of ransomware.[^187]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has terminated services related to backups, security, databases, communication, filesharing and websites.[^24] [^100] [^284]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used taskkill.exe and net.exe to stop backup, catalog, cloud, and other services prior to network encryption.[^354]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has stopped the MSExchangeIS service to render Exchange contents inaccessible to users.[^225]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has disabled actively running virtual environments using the `KillMe` function to include VMware, Microsoft Hypervisors, and VirtualBox.[^78]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) attempts to stop the MSSQL Windows service to ensure successful encryption of locked files.[^285]   |
| [[LAPSUS$\|G1004]] | LAPSUS$ | [LAPSUS$](https://attack.mitre.org/groups/G1004) has shut down virtual machines from within a victim's on-premise VMware ESXi infrastructure.[^27]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Out-of-Band Communications Channel\|M1060]] | Out-of-Band Communications Channel | Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident.[^26]  |
| [[Network Segmentation\|M1030]] | Network Segmentation | Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions. |
| [[User Account Management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. |
| [[Restrict File and Directory Permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[Restrict Registry Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |





## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^8]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^9]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^10]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^11]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^15]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^16]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^17]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^18]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^19]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^20]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^21]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^22]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^23]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^24]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^25]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^26]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^27]: [NCC Group LAPSUS Apr 2022](https://research.nccgroup.com/2022/04/28/lapsus-recent-techniques-tactics-and-procedures/)


[^28]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^29]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^30]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^31]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^32]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^33]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^34]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^35]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)


[^36]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^37]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^38]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^39]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^40]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^41]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^42]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^43]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^44]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^45]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^46]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)


[^47]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^48]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^49]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^50]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^51]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^52]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^53]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^54]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^55]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^56]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^57]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^58]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^59]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^60]: [Unit42 Clop April 2021](https://unit42.paloaltonetworks.com/clop-ransomware/)


[^61]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^62]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^63]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^64]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^65]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^66]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^67]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^68]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)


[^69]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^70]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^71]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^72]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^73]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^74]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^75]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^76]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)


[^77]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^78]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^79]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^80]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^81]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^82]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^83]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^84]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^85]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


[^86]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^87]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^88]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^89]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^90]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^91]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^92]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^93]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^94]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^95]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^96]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)


[^97]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^98]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^99]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^100]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^101]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^102]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^103]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^104]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^105]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^106]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^107]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^108]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^109]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)


[^110]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)


[^111]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^112]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^113]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^114]: [AWS DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)


[^115]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^116]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^117]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^118]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^119]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^120]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^121]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^122]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^123]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^124]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^125]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^126]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^127]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^128]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^129]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^130]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^131]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^132]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^133]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^134]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^135]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^136]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^137]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^138]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^139]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^140]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^141]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^142]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^143]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^144]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^145]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^146]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^147]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^148]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^149]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^150]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^151]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^152]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^153]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^154]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^155]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^156]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)


[^157]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^158]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^159]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^160]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^161]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^162]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^163]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^164]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^165]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^166]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^167]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^168]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^169]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^170]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^171]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^172]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^173]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)


[^174]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^175]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^176]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^177]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^178]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^179]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^180]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^181]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^182]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^183]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^184]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^185]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^186]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^187]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


[^188]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^189]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^190]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^191]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)


[^192]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^193]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^194]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^195]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^196]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^197]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)


[^198]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^199]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^200]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^201]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^202]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)


[^203]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^204]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^205]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)


[^206]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^207]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^208]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^209]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^210]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


[^211]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^212]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^213]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^214]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^215]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^216]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^217]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^218]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^219]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^220]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^221]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^222]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)


[^223]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^224]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)


[^225]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^226]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^227]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^228]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^229]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^230]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)


[^231]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^232]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^233]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^234]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^235]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^236]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^237]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^238]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^239]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^240]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^241]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^242]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^243]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^244]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^245]: [Datadog Security Labs Cloud Persistence 2025](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/)


[^246]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^247]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^248]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^249]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^250]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^251]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^252]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^253]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^254]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^255]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^256]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^257]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^258]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^259]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)


[^260]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^261]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^262]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^263]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^264]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^265]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^266]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^267]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^268]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^269]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^270]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^271]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^272]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^273]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^274]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^275]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^276]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^277]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^278]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)


[^279]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^280]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^281]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^282]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^283]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


[^284]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^285]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^286]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^287]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^288]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^289]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)


[^290]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^291]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^292]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^293]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^294]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^295]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^296]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^297]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^298]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^299]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^300]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^301]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^302]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^303]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^304]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^305]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^306]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^307]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^308]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^309]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^310]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^311]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^312]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)


[^313]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^314]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^315]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)


[^316]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^317]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^318]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^319]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^320]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^321]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)


[^322]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^323]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^324]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)


[^325]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^326]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^327]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^328]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^329]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^330]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)


[^331]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^332]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^333]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^334]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^335]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^336]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^337]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^338]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^339]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^340]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)


[^341]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^342]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^343]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^344]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^345]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^346]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^347]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^348]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^349]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^350]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^351]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^352]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^353]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)


[^354]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^355]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^356]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^357]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^358]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^359]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^360]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^361]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^362]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^363]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^364]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^365]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^366]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^367]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^368]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^369]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^370]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^371]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^372]: [Palo Alto Unit 42 EKANS](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)


[^373]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^374]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^375]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^376]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^377]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^378]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^379]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^380]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^381]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^382]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^383]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^384]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^385]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^386]: [Sophos BlackCat Jul 2022](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)


[^387]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^388]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^389]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


