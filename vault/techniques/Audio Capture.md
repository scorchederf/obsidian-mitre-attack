---
aliases: 
    - T1123
mitre-attack: https://attack.mitre.org/techniques/T1123
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1123

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.[^311] <br><br>Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[PowerSploit\|S0194]] | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-MicrophoneAudio` Exfiltration module can record system microphone audio.[^100] [^212]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can capture data from the system’s microphone.[^59] [^280]  |
| [[Imminent Monitor\|S0434]] | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote microphone monitoring capability.[^34] [^183]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can record sound with the microphone.[^94]  |
| [[DOGCALL\|S0213]] | DOGCALL | [DOGCALL](https://attack.mitre.org/software/S0213) can capture microphone data from the victim's machine.[^330]  |
| [[Janicab\|S0163]] | Janicab | [Janicab](https://attack.mitre.org/software/S0163) captured audio and sent it out to a C2 server.[^274] [^56]  |
| [[EvilGrab\|S0152]] | EvilGrab | [EvilGrab](https://attack.mitre.org/software/S0152) has the capability to capture audio from a victim machine.[^193]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can perform audio surveillance using microphones.[^108]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) captures audio from the computer’s microphone.[^339] [^220] [^2]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can record sound using input audio devices.[^135] [^42]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) can perform audio capture.[^328]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) can listen in to victims' conversations through the system’s microphone.[^205] [^201]  |
| [[LightSpy\|S1185]] | LightSpy | [LightSpy](https://attack.mitre.org/software/S1185) uses Apple's built-in AVFoundation Framework library to capture and manage audio recordings then transform them to JSON blobs for exfiltration.[^38]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) has an audio capture and eavesdropping module.[^146]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) has modules that are capable of capturing audio.[^75]  |
| [[T9000\|S0098]] | T9000 | [T9000](https://attack.mitre.org/software/S0098) uses the Skype API to record audio and video calls. It writes encrypted data to `%APPDATA%\Intel\Skype`.[^66]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) can perform microphone recording.[^132]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438)'s has a plugin that is capable of recording audio using available input sound devices.[^311]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can load a module to leverage the LAME encoder and `mciSendStringW` to control and capture audio.[^352]  |
| [[Derusbi\|S0021]] | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is capable of performing audio captures.[^238]  |
| [[MgBot\|S1146]] | MgBot | [MgBot](https://attack.mitre.org/software/S1146) can capture input and output audio streams from infected devices.[^17] [^244]  |
| [[Cadelspy\|S0454]] | Cadelspy | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to record audio from the compromised host.[^21]  |
| [[Cobian RAT\|S0338]] | Cobian RAT | [Cobian RAT](https://attack.mitre.org/software/S0338) has a feature to perform voice recording on the victim’s machine.[^215]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) can capture audio feeds from the system.[^323] [^178]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to capture VoiceIP application audio on an infected host.[^163]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) has a plugin for microphone interception.[^261] [^88]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) has the ability to record audio.[^63]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) can capture microphone recordings.[^219]  |
| [[MacSpy\|S0282]] | MacSpy | [MacSpy](https://attack.mitre.org/software/S0282) can record the sounds from microphones on a computer.[^253]  |
| [[Flame\|S0143]] | Flame | [Flame](https://attack.mitre.org/software/S0143) can record audio using any existing hardware recording devices.[^336] [^188]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) has used an audio capturing utility known as SOUNDWAVE that captures microphone input.[^62]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered audio during a Zoom session.[^299]  |







## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^11]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^15]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^16]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^17]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)


[^18]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^19]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^20]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^21]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


[^22]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^23]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^24]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^25]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^26]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^27]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^28]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^29]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^30]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^31]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^32]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^33]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^34]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)


[^35]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^36]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^37]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^38]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^39]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^40]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^41]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^42]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^43]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^44]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^45]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^46]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^47]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^48]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^49]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^50]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^51]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^52]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^53]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^54]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^55]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^56]: [Janicab](https://web.archive.org/web/20230331162455/https://www.thesafemac.com/new-signed-malware-called-janicab/)


[^57]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^58]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^59]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)


[^60]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^61]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^62]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^63]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)


[^64]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^65]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^66]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)


[^67]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^68]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^69]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^70]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^71]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^72]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^73]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^74]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^75]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)


[^76]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^77]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^78]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^79]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^80]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^81]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^82]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^83]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^84]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^85]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^86]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^87]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^88]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)


[^89]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^90]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^91]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^92]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^93]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^94]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^95]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^96]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^97]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^98]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^99]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^100]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^101]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^102]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^103]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^104]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^105]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^106]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^107]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^108]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^109]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^110]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^111]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^112]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^113]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^114]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^115]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^116]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^117]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^118]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^119]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^120]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^121]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^122]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^123]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^124]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^125]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^126]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^127]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^128]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^129]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^130]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^131]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^132]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^133]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^134]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^135]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^136]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^137]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^138]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^139]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^140]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^141]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^142]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^143]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^144]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^145]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^146]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^147]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^148]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^149]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^150]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^151]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^152]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^153]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^154]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^155]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^156]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^157]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^158]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^159]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^160]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^161]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^162]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^163]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^164]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^165]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^166]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^167]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^168]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^169]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^170]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^171]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^172]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^173]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^174]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^175]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^176]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^177]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^178]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^179]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^180]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^181]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^182]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^183]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^184]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^185]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^186]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^187]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^188]: [Kaspersky Flame Functionality](https://securelist.com/flame-bunny-frog-munch-and-beetlejuice-2/32855/)


[^189]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^190]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^191]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^192]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^193]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^194]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^195]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^196]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^197]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^198]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^199]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^200]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^201]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^202]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^203]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^204]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^205]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^206]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^207]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^208]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^209]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^210]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^211]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^212]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^213]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^214]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^215]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)


[^216]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^217]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^218]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^219]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^220]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^221]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^222]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^223]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^224]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^225]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^226]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^227]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^228]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^229]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^230]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^231]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^232]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^233]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^234]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^235]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^236]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^237]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^238]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^239]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^240]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^241]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^242]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^243]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^244]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^245]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^246]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^247]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^248]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^249]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^250]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^251]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^252]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^253]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^254]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^255]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^256]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^257]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^258]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^259]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^260]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^261]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^262]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^263]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^264]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^265]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^266]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^267]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^268]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^269]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^270]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^271]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^272]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^273]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^274]: [f-secure janicab](https://www.f-secure.com/weblog/archives/00002576.html)


[^275]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^276]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^277]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^278]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^279]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^280]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^281]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^282]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^283]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^284]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^285]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^286]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^287]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^288]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^289]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^290]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^291]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^292]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^293]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^294]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^295]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^296]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^297]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^298]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^299]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^300]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^301]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^302]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^303]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^304]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^305]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^306]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^307]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^308]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^309]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^310]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^311]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^312]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^313]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^314]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^315]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^316]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^317]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^318]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^319]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^320]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^321]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^322]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^323]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)


[^324]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^325]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^326]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^327]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^328]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^329]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^330]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^331]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^332]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^333]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^334]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^335]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^336]: [Kaspersky Flame](https://securelist.com/the-flame-questions-and-answers-51/34344/)


[^337]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^338]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^339]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)


[^340]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^341]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^342]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^343]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^344]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^345]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^346]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^347]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^348]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^349]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^350]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^351]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^352]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^353]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^354]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^355]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^356]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^357]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^358]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^359]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^360]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^361]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


