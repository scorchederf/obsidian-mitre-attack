---
aliases: 
    - T1614
mitre-attack: https://attack.mitre.org/techniques/T1614
tactic: 
     - Discovery
platforms:
     - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## T1614

<br>Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.[^38] [^211] [^151]  Windows API functions such as `GetLocaleInfoW` can also be used to determine the locale of the host.[^38]  In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.[^305] [^177] <br><br>Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.[^154] [^211] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can identify the location of targeted devices.[^270]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can determine the country a victim host is located in.[^26]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) does not run any tasks or install additional malware if the victim machine is based in Russia.[^295]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034) has checked the victim machine’s location by obtaining the culture name of the machine.[^282]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected the internal IP address, IP geolocation information of the infected host and sends the data to a C2 server.[^152]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also leveraged the “pay” module to obtain region name, country, city, zip code, ISP, latitude and longitude using “http://ip-api.com/json”.[^35]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can identify the geographical location of a victim host.[^101] 	  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138)  can use IP geolocation to determine if the person browsing to a compromised site is within a targeted territory such as the US, Canada, Germany, and South Korea.[^189]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has a function where the C2 endpoint can identify the geographical location of a victim host based on request headers, execution environment and runtime conditions.[^304]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can determine the geographical location of a victim host by checking the language.[^161] <br> |
| [[SameCoin\|S9030]] | SameCoin | [SameCoin](https://attack.mitre.org/software/S9030) can attempt to connect to the Israel Home Front Command site, oref.org[.]il, which is only reachable from within Israel to verify the target's location.[^69]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | Before executing malicious code, [Ragnar Locker](https://attack.mitre.org/software/S0481) checks the Windows API `GetLocaleInfoW` and doesn't encrypt files if it finds a former Soviet country.[^38]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) can use IP-based geolocation to limit infections to victims in North America, Europe, and a small number of Asian-Pacific nations.[^262]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) can identity the OS locale of a compromised host.[^129]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has obtained the location of the victim device by leveraging `GetSystemDefaultLCID`.[^329]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can use `kernel32!GetGeoInfo` to determine system location.[^79]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) queries system locale information during execution.[^332]  Later versions of [DarkGate](https://attack.mitre.org/software/S1111) query `GetSystemDefaultLCID` for locale information to determine if the malware is executing in Russian-speaking countries.[^347]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has conducted system locale checks to see if the compromised host is in Russia, Ukraine, Belarus, Armenia, Kazakhstan, or Moldova.[^144] [^309]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged geofencing logic to detect whether it is operating in a Russian associated time zone to determine whether it continues to execute.[^285]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has gathered detailed information about victims’ systems, such as IP addresses, and geolocation.[^201] [^108] [^288]  [RedLine Stealer](https://attack.mitre.org/software/S1240) has also checked the IP from where it was being executed and leveraged an opensource geolocation IP-lookup service. [^145]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) can collected the country code of a compromised machine.[^93]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) collects the `Locale Name` of the infected device via `GetUserDefaultLocaleName` to determine whether the string `ru` is included, but in analyzed samples no action is taken if present.[^116]  |
| [[AshTag\|S9031]] | AshTag | [AshTag](https://attack.mitre.org/software/S9031) can check geolocation on targeted systems.[^58]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can identify the country code on a compromised host.[^283]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) can identify the geographical location of a victim host.[^31]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has obtained the victim's system current location.[^190]  |
| [[SideCopy\|G1008]] | SideCopy | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the country location of a compromised host.[^165]  |






### Sub-techniques
| ID | Name |
| --- | --- |
| [[System Language Discovery\|T1614.001]] | System Language Discovery |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^8]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^9]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^10]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^11]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^12]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^13]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^14]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^15]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^16]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^17]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^18]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^19]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^20]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^21]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^22]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^23]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^24]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^25]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^26]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^27]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^28]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^29]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^30]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^31]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^32]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^33]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^34]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^35]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^36]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^37]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^38]: [FBI Ragnar Locker 2020](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)


[^39]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^40]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^41]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^42]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^43]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^44]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^45]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^46]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^47]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^48]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^49]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^50]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^51]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^52]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^53]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^54]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^55]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^56]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^57]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^58]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^59]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^60]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^61]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^62]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^63]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^64]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^65]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^66]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^67]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^68]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^69]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^70]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^71]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^72]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^73]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^74]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^75]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^76]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^77]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^78]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^79]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^80]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^81]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^82]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^83]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^84]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^85]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^86]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^87]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^88]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^89]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^90]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^91]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^92]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^93]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^94]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^95]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^96]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^97]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^98]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^99]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^100]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^101]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^102]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^103]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^104]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^105]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^106]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^107]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^108]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)


[^109]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^110]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^111]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^112]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^113]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^114]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^115]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^116]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^117]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^118]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^119]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^120]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^121]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^122]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^123]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^124]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^125]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^126]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^127]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^128]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^129]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^130]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^131]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^132]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^133]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^134]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^135]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^136]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^137]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^138]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^139]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^140]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^141]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^142]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^143]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^144]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^145]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)


[^146]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^147]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^148]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^149]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^150]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^151]: [Bleepingcomputer RAT malware 2020](https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/)


[^152]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^153]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^154]: [Securelist Trasparent Tribe 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^155]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^156]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^157]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^158]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^159]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^160]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^161]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^162]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^163]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^164]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^165]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^166]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^167]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^168]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^169]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^170]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^171]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^172]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^173]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^174]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^175]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^176]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^177]: [Microsoft Azure Instance Metadata 2021](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows)


[^178]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^179]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^180]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^181]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^182]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^183]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^184]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^185]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^186]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^187]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^188]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^189]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)


[^190]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^191]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^192]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^193]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^194]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^195]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^196]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^197]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^198]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^199]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^200]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^201]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)


[^202]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^203]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^204]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^205]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^206]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^207]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^208]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^209]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^210]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^211]: [Sophos Geolocation 2016](https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/)


[^212]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^213]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^214]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^215]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^216]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^217]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^218]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^219]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^220]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^221]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^222]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^223]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^224]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^225]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^226]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^227]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^228]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^229]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^230]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^231]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^232]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^233]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^234]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^235]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^236]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^237]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^238]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^239]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^240]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^241]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^242]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^243]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^244]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^245]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^246]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^247]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^248]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^249]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^250]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^251]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^252]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^253]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^254]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^255]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^256]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^257]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^258]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^259]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^260]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^261]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^262]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^263]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^264]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^265]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^266]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^267]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^268]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^269]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^270]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^271]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^272]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^273]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^274]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^275]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^276]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^277]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^278]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^279]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^280]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^281]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^282]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)


[^283]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^284]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^285]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^286]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^287]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^288]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)


[^289]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^290]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^291]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^292]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^293]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^294]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^295]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^296]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^297]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^298]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^299]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^300]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^301]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^302]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^303]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^304]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^305]: [AWS Instance Identity Documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)


[^306]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^307]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^308]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^309]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^310]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^311]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^312]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^313]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^314]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^315]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^316]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^317]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^318]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^319]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^320]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^321]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^322]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^323]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^324]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^325]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^326]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^327]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^328]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^329]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^330]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^331]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^332]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^333]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^334]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^335]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^336]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^337]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^338]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^339]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^340]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^341]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^342]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^343]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^344]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^345]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^346]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^347]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)


[^348]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^349]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^350]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^351]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^352]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^353]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^354]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


