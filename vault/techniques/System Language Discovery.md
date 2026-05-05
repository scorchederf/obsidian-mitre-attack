---
aliases: 
    - T1614.001
mitre-attack: https://attack.mitre.org/techniques/T1614/001
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1614.001

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities.[^60] <br><br>There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as [Query Registry](https://attack.mitre.org/techniques/T1012) and calls to [Native API](https://attack.mitre.org/techniques/T1106) functions.[^30]  <br><br>For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language` or parsing the outputs of Windows API functions `GetUserDefaultUILanguage`, `GetSystemDefaultUILanguage`, `GetKeyboardLayoutList` and `GetUserDefaultLangID`.[^199] [^220] [^331] <br><br>On a macOS or Linux system, adversaries may query `locale` to retrieve the value of the `$LANG` environment variable.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Spark\|S0543]] | Spark | [Spark](https://attack.mitre.org/software/S0543) has checked the results of the `GetKeyboardLayoutList` and the language name returned by `GetLocaleInfoA` to make sure they contain the word “Arabic” before executing.[^159]  |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) lists all the keyboard layouts installed on the victim’s system using `GetKeyboardLayoutList` API and checks against a hardcoded language code list. If a match if found, SynAck sleeps for 300 seconds and then exits without encrypting files.[^331]   |
| [[SharpStage\|S0546]] | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546)  has been used to target Arabic-speaking users and used code that checks if the compromised machine has the Arabic language installed.[^242]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) has attempted to detect if a compromised host had a Japanese keyboard via the Windows API call `GetKeyboardType`.[^321]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) queries the system's keyboard mapping to determine the language used on the system. It will terminate execution if it detects LANG_RUSSIAN, LANG_BELARUSIAN, LANG_KAZAK, or LANG_UKRAINIAN.[^172]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has checked supported languages on the compromised system.[^193]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) can determine if a victim's computer is running an operating system with specific language preferences.[^341]  |
| [[DropBook\|S0547]] | DropBook | [DropBook](https://attack.mitre.org/software/S0547) has checked for the presence of Arabic language in the infected machine's settings.[^242]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can check the systems `LANG` environmental variable to prevent infecting devices from Armenia (`hy_AM`), Belarus (`be_BY`), Kazakhstan (`kk_KZ`), Russia (`ru_RU`), and Ukraine (`uk_UA`).[^161]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can identify the system language on a compromised host.[^91]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) checks and will terminate execution if the compromised system’s language ID is not Spanish or Portuguese.[^28] [^152]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) used the following command to check the country/language of the active console: <br>` cmd.exe /c chcp >&2`.[^14] <br> |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can use the `GetKeyboardLayout` API to check if a compromised host's keyboard is set to Persian.[^46]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) checks for specific keyboard layouts and OS languages to avoid targeting Commonwealth of Independent States (CIS) entities.[^353]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) can check whether the target system is using Japanese, Taiwanese, or English through detection of specific Windows Security and Internet Explorer dialog.[^68]   |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) has attempted to determine if a compromised system was using a Japanese keyboard via the `GetKeyboardType` API call.[^321]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can check if Russian language is installed on the infected machine by using the function `GetKeyboardLayoutList`.[^20]   |
| [[DEATHRANSOM\|S0616]] | DEATHRANSOM | Some versions of [DEATHRANSOM](https://attack.mitre.org/software/S0616) have performed language ID and keyboard layout checks; if either of these matched Russian, Kazakh, Belarusian, Ukrainian or Tatar [DEATHRANSOM](https://attack.mitre.org/software/S0616) would exit.[^276]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) will not affect machines with language settings matching a defined exlusion list of mainly Eastern European languages.[^293] [^330]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can looks for the “en_US” locale on the victim’s machine.[^8]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has identified the system language settings by checking for `ru_RU`, `ru-RU`, `ru`, and `Russian` to prevent execution in a Russian associated device.[^291]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) can retrieve system default language and time zone.[^192]  |
| [[BlackByte Ransomware\|S1180]] | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) identifies the language on the victim system.[^167]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) variants check system language settings via keyboard layout or similar mechanisms.[^64] [^129]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can perform a check to ensure that the operating system's keyboard and language settings are not set to Russian.[^105]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has been observed to query the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language` and the value `InstallLanguage`. If the machine has the value 0x419 (Russian), 0x422 (Ukrainian), or 0x423 (Belarusian), it stops execution.[^30]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can check if a targeted machine is using a set of Eastern European languages and exit without infection if so.[^326] [^131]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can check the system language using `GetUserDefaultUILanguage` and `GetSystemDefaultUILanguage`. If the language is found in the list, the process terminates.[^184] <br> |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) has used `Accept-Language` to identify hosts in the United Kingdom, United States, France, and Spain.[^289]   |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) has checked the keyboard language using the GetKeyboardLayout() function to avoid installation on Russian-language or other Commonwealth of Independent States-language machines; it will also check the `GetTextCharset` function.[^190]   |
| [[StealBit\|S1200]] | StealBit | [StealBit](https://attack.mitre.org/software/S1200) can determine system location based on the default language setting and will not execute on systems located in former Soviet countries.[^217]  |
| [[Maze\|S0449]] | Maze | [Maze](https://attack.mitre.org/software/S0449) has checked the language of the machine with function `GetUserDefaultUILanguage` and terminated execution if the language matches with an entry in the predefined list.[^243]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) uses AppleScript to check the host's language and location with the command `user locale of (get system info)`.[^147]  |
| [[Malteiro\|G1026]] | Malteiro | [Malteiro](https://attack.mitre.org/groups/G1026) will terminate [Mispadu](https://attack.mitre.org/software/S1122)'s infection process if the language of the victim machine is not Spanish or Portuguese.[^152]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has used implants to collect the system language ID of a compromised machine.[^91]  |
| [[Storm-0501\|G1053]] | Storm-0501 | [Storm-0501](https://attack.mitre.org/groups/G1053) has identified system language codes on a compromised host to determine if the victim falls under a non-supported language code that is prohibited for targeting, including victims associated with Russia and other Commonwealth of Independent States (CIS) that may draw attention of law enforcement in countries where the ransomware operator or affiliates may reside/operate from.[^200] [^90]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has deployed shellcode to check for Japanese Microsoft Office settings.[^164]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) identified system language settings to determine follow-on execution.[^265]  |






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


[^8]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^11]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^15]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^16]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^17]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^18]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^19]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^20]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^21]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^22]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^23]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^24]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^25]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^26]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^27]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^28]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)


[^29]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^30]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^31]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^32]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^33]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^34]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^35]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^36]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^37]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^38]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^39]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^40]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^41]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^42]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^43]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^44]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^45]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^46]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^47]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^48]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^49]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^50]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^51]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^52]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^53]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^54]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^55]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^56]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^57]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^58]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^59]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^60]: [Malware System Language Check](https://www.welivesecurity.com/2009/01/15/malware-trying-to-avoid-some-countries/)


[^61]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^62]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^63]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^64]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)


[^65]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^66]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^67]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^68]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^69]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^70]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^71]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^72]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^73]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^74]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^75]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^76]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^77]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^78]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^79]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^80]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^81]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^82]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^83]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^84]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^85]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^86]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^87]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^88]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^89]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^90]: [Google Mandiant Storm-0501 Sabbath Ransomware November 2021](https://cloud.google.com/blog/topics/threat-intelligence/sabbath-ransomware-affiliate/)


[^91]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^92]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^93]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^94]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^95]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^96]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^97]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^98]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^99]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^100]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^101]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^102]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^103]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^104]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^105]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^106]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^107]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^108]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^109]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^110]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^111]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^112]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^113]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^114]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^115]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^116]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^117]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^118]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^119]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^120]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^121]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^122]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^123]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^124]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^125]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^126]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^127]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^128]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^129]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^130]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^131]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)


[^132]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^133]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^134]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^135]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^136]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^137]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^138]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^139]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^140]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^141]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^142]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^143]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^144]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^145]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^146]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^147]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^148]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^149]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^150]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^151]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^152]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)


[^153]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^154]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^155]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^156]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^157]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^158]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^159]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^160]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^161]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^162]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^163]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^164]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^165]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^166]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^167]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^168]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^169]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^170]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^171]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^172]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)


[^173]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^174]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^175]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^176]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^177]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^178]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^179]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^180]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^181]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^182]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^183]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^184]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)


[^185]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^186]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^187]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^188]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^189]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^190]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)


[^191]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^192]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)


[^193]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)


[^194]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^195]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^196]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^197]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^198]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^199]: [Darkside Ransomware Cybereason](https://www.cybereason.com/blog/cybereason-vs-darkside-ransomware)


[^200]: [Avertium Storm-0501 Sabbath Ransomware Arcane January 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-sabbath-ransomware-gang)


[^201]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^202]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^203]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^204]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^205]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^206]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^207]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^208]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^209]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^210]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^211]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^212]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^213]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^214]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^215]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^216]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^217]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


[^218]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^219]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^220]: [Securelist JSWorm](https://securelist.com/evolution-of-jsworm-ransomware/102428/)


[^221]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^222]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^223]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^224]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^225]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^226]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^227]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^228]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^229]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^230]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^231]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^232]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^233]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^234]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^235]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^236]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^237]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^238]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^239]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^240]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^241]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^242]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^243]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)


[^244]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^245]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^246]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^247]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^248]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^249]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^250]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^251]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^252]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^253]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^254]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^255]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^256]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^257]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^258]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^259]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^260]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^261]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^262]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^263]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^264]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^265]: [Picus BlackByte 2022](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)


[^266]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^267]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^268]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^269]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^270]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^271]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^272]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^273]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^274]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^275]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^276]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^277]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^278]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^279]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^280]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^281]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^282]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^283]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^284]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^285]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^286]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^287]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^288]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^289]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^290]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^291]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^292]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^293]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)


[^294]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^295]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^296]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^297]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^298]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^299]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^300]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^301]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^302]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^303]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^304]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^305]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^306]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^307]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^308]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^309]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^310]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^311]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^312]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^313]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^314]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^315]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^316]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^317]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^318]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^319]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^320]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^321]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^322]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^323]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^324]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^325]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^326]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^327]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^328]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^329]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^330]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^331]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^332]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^333]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^334]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^335]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^336]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^337]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^338]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^339]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^340]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^341]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^342]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^343]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^344]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^345]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^346]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^347]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^348]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^349]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^350]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^351]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^352]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^353]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^354]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^355]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^356]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^357]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^358]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^359]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


