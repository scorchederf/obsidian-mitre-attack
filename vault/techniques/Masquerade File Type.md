---
aliases: 
    - T1036.008
mitre-attack: https://attack.mitre.org/techniques/T1036/008
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1036.008

Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting, including the file’s signature, extension, icon, and contents. Various file types have a typical standard format, including how they are encoded and organized. For example, a file’s signature (also known as header or magic bytes) is the beginning bytes of a file and is often used to identify the file’s type. For example, the header of a JPEG file,  is ` 0xFF 0xD8` and the file extension is either `.JPE`, `.JPEG` or `.JPG`. <br><br>Adversaries may edit the header’s hex code and/or the file extension of a malicious payload in order to bypass file validation checks and/or input sanitization. This behavior is commonly used when payload files are transferred (e.g., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) and stored (e.g., [Upload Malware](https://attack.mitre.org/techniques/T1608/001)) so that adversaries may move their malware without triggering detections. <br><br>Common non-executable file types and extensions, such as text files (`.txt`) and image files (`.jpg`, `.gif`, etc.) may be typically treated as benign.  Based on this, adversaries may use a file extension to disguise malware, such as naming a PHP backdoor code with a file name of `test.gif`. A user may not know that a file is malicious due to the benign appearance and file extension.<br><br>Polyglot files, which are files that have multiple different file types and that function differently based on the application that will execute them, may also be used to disguise malicious malware and capabilities.[^202] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used Microsoft Word icons to hide malicious LNK files.[^238]  |
| [[AvosLocker\|S1053]] | AvosLocker | [AvosLocker](https://attack.mitre.org/software/S1053) has been disguised as a .jpg file.[^101]  |
| [[HeartCrypt\|S9018]] | HeartCrypt | [HeartCrypt](https://attack.mitre.org/software/S9018) can append a BMP header to encoded malicious payloads to masquerade them as BMP files.[^177]  |
| [[STATICPLUGIN\|S1238]] | STATICPLUGIN | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has masqueraded as a BMP file to hide its true MSI file extension.[^250]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) has historically been delivered via infected USB drives containing a malicious LNK object masquerading as a legitimate folder.[^253]  |
| [[Lumma Stealer\|S1213]] | Lumma Stealer | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used payloads that resemble benign file extensions such as .mp3, .accdb, and .pub, though the files contained malicious JavaScript content.[^51]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) has used a .NET downloader named 63342221.BAT and has used .jpg, .png, and .log as false extensions for malicious files.[^78]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) can download additional executable payloads that masquerade as GIF files.[^171]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) has been distributed as a DLL/HTML polyglot file.[^317] [^125]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) masquerades as a Microsoft Word Add-In file, with the extension `.wll`, but is a malicious DLL file.[^232] [^12]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has disguised it's true file structure as an application bundle by adding special characters to the filename and using the icon for legitimate Word documents.[^194]  |
| [[ANDROMEDA\|S1074]] | ANDROMEDA | [ANDROMEDA](https://attack.mitre.org/software/S1074) has been delivered through a LNK file disguised as a folder.[^30]  |
| [[QakBot\|S0650]] | QakBot | The [QakBot](https://attack.mitre.org/software/S0650) payload has been disguised as a PNG file and hidden within LNK files using a Microsoft File Explorer icon.[^92] [^294]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has appended copies of the ntds.dit database with a .gif file extension.[^201]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has masqueraded malicious executables as legitimate files that download [PlugX](https://attack.mitre.org/software/S0013) malware.[^11] [^318]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has crafted malware payloads to appear as Privacy-Enhanced Mail (PEM) files.[^155]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) masqueraded configuration files containing encryption keys as PNG files.[^64]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Execution Prevention\|M1038]] | Execution Prevention | Ensure that input sanitization is performed and that files are validated properly before execution; furthermore, implement a strict allow list to ensure that only authorized file types are processed.[^224]  Restrict and/or block execution of files where headers and extensions do not match. <br><br> |
| [[Behavior Prevention on Endpoint\|M1040]] | Behavior Prevention on Endpoint | Implement security controls on the endpoint, such as a Host Intrusion Prevention System (HIPS), to identify and prevent execution of files with mismatching file signatures. |
| [[Antivirus／Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically quarantine suspicious files.  |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type |



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


[^11]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^12]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^13]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^14]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^15]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^16]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^17]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^18]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^19]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^20]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^21]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^22]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^23]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^24]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^25]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^26]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^27]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^28]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^29]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^30]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^31]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^32]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^33]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^34]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^35]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^36]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^37]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^38]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^39]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^40]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^41]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^42]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^43]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^44]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^45]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^46]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^47]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^48]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^49]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^50]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^51]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)


[^52]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^53]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^54]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^55]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^56]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^57]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^58]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^59]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^60]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^61]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^62]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^63]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^64]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^65]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^66]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^67]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^68]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^69]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^70]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^71]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^72]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^73]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^74]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^75]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^76]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^77]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^78]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^79]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^80]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^81]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^82]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^83]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^84]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^85]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^86]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^87]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^88]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^89]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^90]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^91]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^92]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^93]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^94]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^95]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^96]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^97]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^98]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^99]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^100]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^101]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)


[^102]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^103]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^104]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^105]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^106]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^107]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^108]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^109]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^110]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^111]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^112]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^113]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^114]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^115]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^116]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^117]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^118]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^119]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^120]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^121]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^122]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^123]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^124]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^125]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^126]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^127]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^128]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^129]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^130]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^131]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^132]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^133]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^134]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^135]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^136]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^137]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^138]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^139]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^140]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^141]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^142]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^143]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^144]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^145]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^146]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^147]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^148]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^149]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^150]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^151]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^152]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^153]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^154]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^155]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^156]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^157]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^158]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^159]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^160]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^161]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^162]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^163]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^164]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^165]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^166]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^167]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^168]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^169]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^170]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^171]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^172]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^173]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^174]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^175]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^176]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^177]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)


[^178]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^179]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^180]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^181]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^182]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^183]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^184]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^185]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^186]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^187]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^188]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^189]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^190]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^191]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^192]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^193]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^194]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^195]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^196]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^197]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^198]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^199]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^200]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^201]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^202]: [polygot_icedID](https://unit42.paloaltonetworks.com/polyglot-file-icedid-payload)


[^203]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^204]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^205]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^206]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^207]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^208]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^209]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^210]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^211]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^212]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^213]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^214]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^215]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^216]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^217]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^218]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^219]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^220]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^221]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^222]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^223]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^224]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^225]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^226]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^227]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^228]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^229]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^230]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^231]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^232]: [Microsoft KnuckleTouch 2024](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win64/KnuckleTouch.A!dha&threatId=-2147067254)


[^233]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^234]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^235]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^236]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^237]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^238]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^239]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^240]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^241]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^242]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^243]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^244]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^245]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^246]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^247]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^248]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^249]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^250]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^251]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^252]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^253]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


[^254]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^255]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^256]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^257]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^258]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^259]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^260]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^261]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^262]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^263]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^264]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^265]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^266]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^267]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^268]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^269]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^270]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^271]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^272]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^273]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^274]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^275]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^276]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^277]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^278]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^279]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^280]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^281]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^282]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^283]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^284]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^285]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^286]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^287]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^288]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^289]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^290]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^291]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^292]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^293]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^294]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^295]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^296]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^297]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^298]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^299]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^300]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^301]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^302]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^303]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^304]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^305]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^306]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^307]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^308]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^309]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^310]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^311]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^312]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^313]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^314]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^315]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^316]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^317]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)


[^318]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^319]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^320]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^321]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^322]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^323]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^324]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^325]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^326]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^327]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^328]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^329]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^330]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^331]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^332]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^333]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^334]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^335]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^336]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^337]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^338]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^339]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


