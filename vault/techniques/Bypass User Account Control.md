---
aliases: 
    - T1548.002
mitre-attack: https://attack.mitre.org/techniques/T1548/002
tactic: 
     - Privilege Escalation
platforms:
     - Windows
permissions required:
     - none
---

## T1548.002

Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action.[^122] <br><br>If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs can elevate privileges or execute some elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) objects without prompting the user through the UAC notification box.[^95] [^63]  An example of this is use of [Rundll32](https://attack.mitre.org/techniques/T1218/011) to load a specifically crafted DLL which loads an auto-elevated [Component Object Model](https://attack.mitre.org/techniques/T1559/001) object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user.[^254] <br><br>Many methods have been discovered to bypass UAC. The Github readme page for UACME contains an extensive list of methods[^5]  that have been discovered and implemented, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as:<br><br>* `eventvwr.exe` can auto-elevate and execute a specified binary or script.[^369] [^77] <br><br>Another bypass is possible through some lateral movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on remote systems and default to high integrity.[^44] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[UACMe\|S0116]] | UACMe | [UACMe](https://attack.mitre.org/software/S0116) contains many methods for bypassing Windows User Account Control on multiple versions of the operating system.[^5]  |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.[^258]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.[^173]     |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) includes various modules to attempt to bypass UAC for escalation of privileges.[^135]  |
| [[PoshC2\|S0378]] | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) can utilize multiple methods to bypass UAC.[^182]  |
| [[CSPY Downloader\|S0527]] | CSPY Downloader | [CSPY Downloader](https://attack.mitre.org/software/S0527) can bypass UAC using the SilentCleanup task to execute the binary with elevated privileges.[^111]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) has a command for UAC bypassing.[^66]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) has 2 methods for elevating integrity. It can bypass UAC through `eventvwr.exe` and `sdclt.exe`.[^338]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.[^109]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | <br>[QuasarRAT](https://attack.mitre.org/software/S0262) can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.[^31]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can bypass UAC to escalate privileges.[^289]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to bypass UAC to deploy post exploitation tools with elevated privileges.[^305]  |
| [[Downdelph\|S0134]] | Downdelph | [Downdelph](https://attack.mitre.org/software/S0134) bypasses UAC to escalate privileges by using a custom “RedirectEXE” shim database.[^33]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | An older variant of [PLAINTEE](https://attack.mitre.org/software/S0254) performs UAC bypass.[^392]  |
| [[Bad Rabbit\|S0606]] | Bad Rabbit | [Bad Rabbit](https://attack.mitre.org/software/S0606) has attempted to bypass UAC and gain elevated administrative privileges.[^9]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can utilize the CMSTPLUA COM interface and the SilentCleanup task to bypass UAC.[^225]   |
| [[WastedLocker\|S0612]] | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) can perform a UAC bypass if it is not executed with administrator rights or if the infected host runs Windows Vista or later.[^368]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can use fileless UAC bypass and create an elevated COM object to escalate privileges.[^157] [^47]  |
| [[ZeroT\|S0230]] | ZeroT | Many [ZeroT](https://attack.mitre.org/software/S0230) samples can perform UAC bypass by using eventvwr.exe to execute a malicious file.[^50]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) will use the legitimate Windows utility fodhelper.exe to run processes at elevated privileges without requiring a User Account Control prompt.[^294]  |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) can bypass UAC to escalate privileges.[^35]   |
| [[HTTPTroy\|S9007]] | HTTPTroy | [HTTPTroy](https://attack.mitre.org/software/S9007) has leveraged the ability to execute commands with system privileges using the `srun <EXECUTABLE> <ARGS>` command.[^108]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can make use of the Windows `SilentCleanup` scheduled task to execute its payload with elevated privileges.[^336]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) attempts to bypass default User Access Control (UAC) settings by exploiting a backward-compatibility setting found in Windows 7 and later.[^218]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) has hijacked the cryptbase.dll within migwiz.exe to escalate privileges. This prevented the User Access Control window from appearing.[^236]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) bypasses UAC using the CMSTPLUA COM interface.[^388]   |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) has the ability to bypass UAC using a `passuac.dll` file.[^289] [^87]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) uses two distinct User Account Control (UAC) bypass techniques to escalate privileges.[^367]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can bypass UAC to execute code with elevated privileges through an elevated Component Object Model (COM) interface.[^361]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has attempted to bypass UAC using `fodhelper.exe` to escalate privileges.[^342]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) installer can use UAC bypass techniques to install the payload.[^86]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has bypassed UAC by performing token impersonation as well as an RPC-based method, this included bypassing UAC set to “AlwaysNotify".[^204] [^79]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) attempts to disable UAC remote restrictions by modifying the Registry.[^220]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can attempt to run the program as admin, then show a fake error message and a legitimate UAC bypass prompt to the user in an attempt to socially engineer the user into escalating privileges.[^60]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can bypass UAC by registering as the default handler for .MSC files.[^78]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) contains UAC bypass code for both 32- and 64-bit systems.[^139]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can bypass UAC through creating the Registry key  `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\ICM\Calibration`.[^357] [^156]  |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) performs UAC bypass.[^2] [^97]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use a number of known techniques to bypass Windows UAC.[^178] [^17]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can use [UACMe](https://attack.mitre.org/software/S0116) for privilege escalation.[^215] [^10] 	 |
| [[Lokibot\|S0447]] | Lokibot | <br>[Lokibot](https://attack.mitre.org/software/S0447) has utilized multiple techniques to bypass UAC.[^154]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can use a variant of the sysprep UAC bypass.[^331]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) will perform UAC bypass either through fodhelper.exe or eventvwr.exe.[^69]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can bypass standard user access controls by using stolen tokens to launch processes at an elevated security context.[^81]  |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) has presented the user with a UAC prompt to elevate privileges while installing.[^121]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can bypass UAC to elevate process privileges on a compromised host.[^372]  |
| [[AutoIt backdoor\|S0129]] | AutoIt backdoor | [AutoIt backdoor](https://attack.mitre.org/software/S0129) attempts to escalate privileges by bypassing User Access Control.[^213]  |
| [[H1N1\|S0132]] | H1N1 | [H1N1](https://attack.mitre.org/software/S0132) bypasses user access control by using a DLL hijacking vulnerability in the Windows Update Standalone Installer (wusa.exe).[^352]  |
| [[BitPaymer\|S0570]] | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) can suppress UAC prompts by setting the `HKCU\Software\Classes\ms-settings\shell\open\command` registry key on Windows 10 or `HKCU\Software\Classes\mscfile\shell\open\command` on Windows 7 and launching the `eventvwr.msc` process, which launches [BitPaymer](https://attack.mitre.org/software/S0570) with elevated privileges.[^37]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) contains functionality to bypass UAC.[^229] [^4]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use `sdclt.exe` to bypass UAC in Windows 10 to escalate privileges; for older Windows versions [WarzoneRAT](https://attack.mitre.org/software/S0670) can use the IFileOperation exploit to bypass the UAC module.[^152] [^113]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has attempted to bypass UAC using Component Object Model (COM) interface.[^316]  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used the Fodhelper UAC bypass technique to gain elevated privileges.[^312]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) bypassed User Access Control (UAC).[^231]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has bypassed UAC.[^174]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) has bypassed UAC.[^373]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) uses various techniques to bypass UAC.[^73] [^90]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has used the legitimate application `ieinstal.exe` to bypass UAC.[^194]   |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used a Windows 10 specific tool and xxmm to bypass UAC for privilege escalation.[^89] [^129]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) has a function in the initial dropper to bypass Windows UAC in order to execute the next payload with higher privileges.[^168]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can use a public UAC bypass method to elevate privileges.[^270]  |
| [[Evilnum\|G0120]] | Evilnum | [Evilnum](https://attack.mitre.org/groups/G0120) has used PowerShell to bypass UAC.[^377]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[User Account Control\|M1052]] | User Account Control | Although UAC bypass techniques exist, it is still prudent to use the highest enforcement level for UAC when possible and mitigate bypass opportunities that exist with techniques such as [DLL](https://attack.mitre.org/techniques/T1574/001). |
| [[Privileged Account Management\|M1026]] | Privileged Account Management | Remove users from the local administrator group on systems. |
| [[Audit\|M1047]] | Audit | Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate.[^5]  |
| [[Update Software\|M1051]] | Update Software | Consider updating Windows to the latest version and patch level to utilize the latest protective measures against UAC bypass.[^5]  |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^7]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^8]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^9]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)


[^10]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^11]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^12]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^13]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^14]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^15]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^16]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^17]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^18]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^19]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^20]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^21]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^22]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^23]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^24]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^25]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^26]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^27]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^28]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^29]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^30]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^31]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^32]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^33]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^34]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^35]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^36]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^37]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^38]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^39]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^40]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^41]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^42]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^43]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^44]: [SANS UAC Bypass](http://pen-testing.sans.org/blog/pen-testing/2013/08/08/psexec-uac-bypass)


[^45]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^46]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^47]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^48]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^49]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^50]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^51]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^52]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^53]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^54]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^55]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^56]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^57]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^58]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^59]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^60]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^61]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^62]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^63]: [MSDN COM Elevation](https://msdn.microsoft.com/en-us/library/ms679687.aspx)


[^64]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^65]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^66]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)


[^67]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^68]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^69]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^70]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^71]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^72]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^73]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)


[^74]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^75]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^76]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^77]: [Fortinet Fareit](https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware)


[^78]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^79]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^80]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^81]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)


[^82]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^83]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^84]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^85]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^86]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^87]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^88]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^89]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^90]: [NaumaanProofpoint_GlobalClickFix_April2025](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)


[^91]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^92]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^93]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^94]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^95]: [TechNet Inside UAC](https://technet.microsoft.com/en-US/magazine/2009.07.uac.aspx)


[^96]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^97]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^98]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^99]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^100]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^101]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^102]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^103]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^104]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^105]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^106]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^107]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^108]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^109]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^110]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^111]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^112]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^113]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)


[^114]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^115]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^116]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^117]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^118]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^119]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^120]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^121]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^122]: [TechNet How UAC Works](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works)


[^123]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^124]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^125]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^126]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^127]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^128]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^129]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^130]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^131]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^132]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^133]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^134]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^135]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^136]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^137]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^138]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^139]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^140]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^141]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^142]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^143]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^144]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^145]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^146]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^147]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^148]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^149]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^150]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^151]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^152]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^153]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^154]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^155]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^156]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)


[^157]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^158]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^159]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^160]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^161]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^162]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^163]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^164]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^165]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^166]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^167]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^168]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^169]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^170]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^171]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^172]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^173]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^174]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^175]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^176]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^177]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^178]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)


[^179]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^180]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^181]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^182]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


[^183]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^184]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^185]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^186]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^187]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^188]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^189]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^190]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^191]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^192]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^193]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^194]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^195]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^196]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^197]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^198]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^199]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^200]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^201]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^202]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^203]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^204]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^205]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^206]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^207]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^208]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^209]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^210]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^211]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^212]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^213]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^214]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^215]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^216]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^217]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^218]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^219]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^220]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^221]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^222]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^223]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^224]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^225]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^226]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^227]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^228]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^229]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^230]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^231]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^232]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^233]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^234]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^235]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^236]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^237]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^238]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^239]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^240]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^241]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^242]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^243]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^244]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^245]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^246]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^247]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^248]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^249]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^250]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^251]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^252]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^253]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^254]: [Davidson Windows](http://www.pretentiousname.com/misc/win7_uac_whitelist2.html)


[^255]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^256]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^257]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^258]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)


[^259]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^260]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^261]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^262]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^263]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^264]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^265]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^266]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^267]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^268]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^269]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^270]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^271]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^272]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^273]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^274]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^275]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^276]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^277]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^278]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^279]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^280]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^281]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^282]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^283]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^284]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^285]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^286]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^287]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^288]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^289]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^290]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^291]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^292]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^293]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^294]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


[^295]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^296]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^297]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^298]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^299]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^300]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^301]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^302]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^303]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^304]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^305]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^306]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^307]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^308]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^309]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^310]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^311]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^312]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^313]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^314]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^315]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^316]: [Intel471 Medusa Ransomware May 2025](https://www.intel471.com/blog/threat-hunting-case-study-medusa-ransomware)


[^317]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^318]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^319]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^320]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^321]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^322]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^323]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^324]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^325]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^326]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^327]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^328]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^329]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^330]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^331]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^332]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^333]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^334]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^335]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^336]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^337]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^338]: [Github Koadic](https://github.com/offsecginger/koadic)


[^339]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^340]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^341]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^342]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^343]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^344]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^345]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^346]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^347]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^348]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^349]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^350]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^351]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^352]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)


[^353]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^354]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^355]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^356]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^357]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^358]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^359]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^360]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^361]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^362]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^363]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^364]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^365]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^366]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^367]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^368]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^369]: [enigma0x3 Fileless UAC Bypass](https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/)


[^370]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^371]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^372]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^373]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^374]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^375]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^376]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^377]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^378]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^379]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^380]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^381]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^382]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^383]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^384]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^385]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^386]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^387]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^388]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^389]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^390]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^391]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^392]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^393]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^394]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^395]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


