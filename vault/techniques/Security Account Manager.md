---
aliases: 
    - T1003.002
mitre-attack: https://attack.mitre.org/techniques/T1003/002
tactic: 
     - Credential Access
platforms:
     - Windows
permissions required:
     - none
---

## T1003.002

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the `net user` command. Enumerating the SAM database requires SYSTEM level access.<br><br>A number of tools can be used to retrieve the SAM file through in-memory techniques:<br><br>* pwdumpx.exe<br>* [gsecdump](https://attack.mitre.org/software/S0008)<br>* [Mimikatz](https://attack.mitre.org/software/S0002)<br>* secretsdump.py<br><br>Alternatively, the SAM can be extracted from the Registry with Reg:<br><br>* `reg save HKLM\sam sam`<br>* `reg save HKLM\system system`<br><br>Creddump7 can then be used to process the SAM database locally to retrieve hashes.[^35] <br><br>Notes: <br><br>* RID 500 account is the local, built-in administrator.<br>* RID 501 is the guest account.<br>* User accounts start with a RID of 1,000+.<br>


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Impacket\|S0357]] | Impacket | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.[^7]  |
| [[Fgdump\|S0120]] | Fgdump | [Fgdump](https://attack.mitre.org/software/S0120) can dump Windows password hashes.[^62]  |
| [[pwdump\|S0006]] | pwdump | [pwdump](https://attack.mitre.org/software/S0006) can be used to dump credentials from the SAM.[^274]  |
| [[Mimikatz\|S0002]] | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the SAM table.[^188] [^170] [^311] [^132]  |
| [[gsecdump\|S0008]] | gsecdump | [gsecdump](https://attack.mitre.org/software/S0008) can dump Windows password hashes from the SAM.[^172]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump usernames and hashed passwords from the SAM.[^32]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by dumping SAM/SECURITY hive.[^305]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [CosmicDuke](https://attack.mitre.org/software/S0050) collects Windows account hashes.[^195]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has the capability to harvest credentials and passwords from the SAM database.[^272] 	 |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) can dump the SAM database.[^165]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can recover hashed passwords.[^144]  |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022)'s Credential Dumper module can dump encrypted password hashes from SAM registry keys, including `HKLM\SAM\SAM\Domains\Account\F` and `HKLM\SAM\SAM\Domains\Account\Users\*\V`.[^289]  |
| [[CozyCar\|S0046]] | CozyCar | Password stealer and NTLM stealer modules in [CozyCar](https://attack.mitre.org/software/S0046) harvest stored credentials from the victim, including credentials used as part of Windows NTLM user authentication.[^225]  |
| [[POWERTON\|S0371]] | POWERTON | [POWERTON](https://attack.mitre.org/software/S0371) has the ability to dump password hashes.[^176]  |
| [[Mivast\|S0080]] | Mivast | [Mivast](https://attack.mitre.org/software/S0080) has the capability to gather NTLM password information.[^166]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has acquired credentials from the SAM/SECURITY registry hives.[^354]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has dropped and executed SecretsDump to dump password hashes.[^61]  |
| [[Daggerfly\|G1034]] | Daggerfly | [Daggerfly](https://attack.mitre.org/groups/G1034) used [Reg](https://attack.mitre.org/software/S0075) to dump the Security Account Manager (SAM) hive from victim machines for follow-on credential extraction.[^239]  |
| [[Ember Bear\|G1003]] | Ember Bear | [Ember Bear](https://attack.mitre.org/groups/G1003) acquires victim credentials by extracting registry hives such as the Security Account Manager through commands such as `reg save`.[^185] [^222]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has dumped credentials, including by using gsecdump.[^65] [^151]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has used the `reg save` command to save registry hives.[^351]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has copied and exfiltrated the SAM Registry hive from targeted systems.[^221]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting tools wmiexec.vbs and secretsdump.py to dump credentials.[^190] [^308]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used vssadmin to copy registry hives including SAM.[^340] [^243]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) extracted user account data from the Security Account Managerr (SAM), making a copy of this database from the registry using the `reg save` command or by exploiting volume shadow copies.[^187]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has extracted the SAM and SYSTEM registry hives using the `reg.exe` binary for obtaining password hashes from a compromised machine.[^203]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used `reg` commands to dump specific hives from the Windows Registry, such as the SAM hive, and obtain password hashes.[^178]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used [gsecdump](https://attack.mitre.org/software/S0008) to dump credentials. They have also dumped credentials from domain controllers.[^284] [^79]  |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) dumped the SAM file on victim machines to capture credentials.[^103]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[User Training\|M1017]] | User Training | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[Operating System Configuration\|M1028]] | Operating System Configuration | Consider disabling or restricting NTLM.[^301]  |
| [[Password Policies\|M1027]] | Password Policies | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Privileged Account Management\|M1026]] | Privileged Account Management | Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Security Account Manager\|T1003.002]] | Security Account Manager |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^11]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^15]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^16]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^17]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^18]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^19]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^20]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^21]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^22]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^23]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^24]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^25]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^26]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^27]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^28]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^29]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^30]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^31]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^32]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


[^33]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^34]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^35]: [GitHub Creddump7](https://github.com/Neohapsis/creddump7)


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


[^51]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^52]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^53]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^54]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^55]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^56]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^57]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^58]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^59]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^60]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^61]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^62]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^63]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^64]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^65]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^66]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^67]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^68]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^69]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^70]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^71]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^72]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^73]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^74]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^75]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^76]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^77]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^78]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^79]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


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


[^93]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^94]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^95]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^96]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^97]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^98]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^99]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^100]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^101]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^102]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^103]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


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


[^125]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^126]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^127]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^128]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^129]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^130]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^131]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^132]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


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


[^144]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)


[^145]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^146]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^147]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^148]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^149]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^150]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^151]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^152]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^153]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^154]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^155]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^156]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^157]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^158]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^159]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^160]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^161]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^162]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^163]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^164]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^165]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^166]: [Symantec Backdoor.Mivast](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)


[^167]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^168]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^169]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^170]: [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)


[^171]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^172]: [Microsoft Gsecdump](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=HackTool:Win32/Gsecdump)


[^173]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^174]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^175]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^176]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^177]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^178]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^179]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^180]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^181]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^182]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^183]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^184]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^185]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^186]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^187]: [Rostovcev APT41 2021](https://www.group-ib.com/blog/apt41-world-tour-2021/)


[^188]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)


[^189]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^190]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^191]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^192]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^193]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^194]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^195]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^196]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^197]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^198]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^199]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^200]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^201]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^202]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^203]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^204]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^205]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^206]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^207]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^208]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^209]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^210]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^211]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^212]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^213]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^214]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^215]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^216]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^217]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^218]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^219]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^220]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^221]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^222]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^223]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^224]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^225]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^226]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^227]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^228]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^229]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^230]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^231]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^232]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^233]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^234]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^235]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^236]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^237]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^238]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^239]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^240]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^241]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^242]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^243]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^244]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^245]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^246]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^247]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^248]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^249]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^250]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^251]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^252]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^253]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^254]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^255]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^256]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^257]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^258]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^259]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^260]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^261]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^262]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^263]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^264]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^265]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^266]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^267]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^268]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^269]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^270]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^271]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^272]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^273]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^274]: [Wikipedia pwdump](https://en.wikipedia.org/wiki/Pwdump)


[^275]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^276]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^277]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^278]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^279]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^280]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^281]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^282]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^283]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^284]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^285]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^286]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^287]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^288]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^289]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^290]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^291]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^292]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^293]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^294]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^295]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^296]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^297]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^298]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^299]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^300]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^301]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^302]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^303]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^304]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^305]: [Github Koadic](https://github.com/offsecginger/koadic)


[^306]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^307]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^308]: [Github AD-Pentest-Script](https://github.com/Twi1ight/AD-Pentest-Script/blob/master/wmiexec.vbs)


[^309]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^310]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^311]: [Directory Services Internals DPAPI Backup Keys Oct 2015](https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/)


[^312]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^313]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^314]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^315]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^316]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^317]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^318]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^319]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^320]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^321]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^322]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^323]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^324]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^325]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^326]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^327]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^328]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^329]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^330]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^331]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^332]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^333]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^334]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^335]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^336]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^337]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^338]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^339]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^340]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^341]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^342]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^343]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^344]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^345]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^346]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^347]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^348]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^349]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^350]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^351]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^352]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^353]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^354]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


[^355]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


