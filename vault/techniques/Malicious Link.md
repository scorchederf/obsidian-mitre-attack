---
aliases: 
    - T1204.001
mitre-attack: https://attack.mitre.org/techniques/T1204/001
tactic: 
     - Execution
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1204.001

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002). Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203). Links may also lead users to download files that require execution via [Malicious File](https://attack.mitre.org/techniques/T1204/002).


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has relied upon a user downloading a file from a OneDrive link for execution.[^10] [^353]  |
| [[Pony\|S0453]] | Pony | [Pony](https://attack.mitre.org/software/S0453) has attempted to lure targets into clicking links in spoofed emails from legitimate banks.[^387] 	 |
| [[ROAMINGHOUSE\|S9026]] | ROAMINGHOUSE | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) has been executed through luring victims into clicking links to download malicious ZIP files.[^254]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) has been executed through convincing victims into clicking malicious links.[^217] [^43]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has relied upon users clicking on a malicious link delivered through spearphishing.[^263] [^13]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) has been executed through malicious links presented to users as internet search results.[^427] [^243]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has relied on victims to click on a malicious link send via phishing campaigns.[^244]  |
| [[Snip3\|S1086]] | Snip3 | [Snip3](https://attack.mitre.org/software/S1086) has been executed through luring victims into clicking malicious links.[^304]  |
| [[GuLoader\|S0561]] | GuLoader | [GuLoader](https://attack.mitre.org/software/S0561) has relied upon users clicking on links to malicious documents.[^43]  |
| [[ObliqueRAT\|S0644]] | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) has gained execution on targeted systems through luring users to click on links to malicious URLs.[^49] [^7]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) has lured victims into interacting with malicious links on compromised websites for execution.[^306]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) has been executed through malicious links within spearphishing emails.[^394]  |
| [[Javali\|S0528]] | Javali | [Javali](https://attack.mitre.org/software/S0528) has achieved execution through victims clicking links to malicious websites.[^82]  |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has been executed via malicious links embedded in e-mails spoofing the Ministries of Education, Culture, Sports, Science and Technology of Japan.[^90]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) has been executed through malicious links distributed in email campaigns.[^232] [^293]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has relied on users to click on a malicious link delivered via a spearphishing.[^392]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has relied upon users clicking on a malicious link delivered through phishing.[^309]  |
| [[Kerrdown\|S0585]] | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) has gained execution through victims opening malicious links.[^93]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) has used malicious links to gain execution on victim machines.[^376] [^83]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can gain execution after a user clicks on a malicious link to decoy landing pages hosted on Google Docs.[^41] [^326] [^393]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has been executed via malicious links in e-mails.[^166]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) has relied on a user to click a malicious link within a spearphishing email.[^392]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) has compromised victims via links to URLs hosting malicious content.[^287]  |
| [[Melcoz\|S0530]] | Melcoz | [Melcoz](https://attack.mitre.org/software/S0530) has gained execution through victims opening malicious links.[^82]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has relied on victims clicking on a malicious link delivered via email.[^75]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) has been executed by luring victims into clicking links in spearphishing emails.[^31] [^176] <br> |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584)'s spearphishing links required user interaction to navigate to the malicious website.[^132]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) has gained execution through users opening malicious links.[^36] [^38] [^207] [^223] [^323] [^125] [^390] <br> |
| [[Hancitor\|S0499]] | Hancitor | [Hancitor](https://attack.mitre.org/software/S0499) has relied upon users clicking on a malicious link delivered through phishing.[^273]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has lured victims into clicking malicious Dropbox download links delivered through spearphishing.[^426]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has lured victims into clicking a malicious link delivered through spearphishing.[^100]  |
| [[Elderwood\|G0066]] | Elderwood | [Elderwood](https://attack.mitre.org/groups/G0066) has leveraged multiple types of spearphishing in order to attempt to get a user to open links.[^28] [^280]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used malicious links to lure victims into downloading malware.[^277]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has used links embedded in emails to lure users into downloading malicious files.[^89]  |
| [[APT-C-36\|G0099]] | APT-C-36 | [APT-C-36](https://attack.mitre.org/groups/G0099) has used malicious links in emails, often impersonating official notifications and documents, to direct users to execute malicious payloads.[^141]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has delivered malicious links to achieve execution on the target system.[^52] [^127] [^265] [^39]  |
| [[Daggerfly\|G1034]] | Daggerfly | [Daggerfly](https://attack.mitre.org/groups/G1034) has used strategic website compromise to deliver a malicious link requiring user interaction.[^74]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has used lures to get users to click links in emails and attachments. For example, [TA505](https://attack.mitre.org/groups/G0092) makes their malware look like legitimate Microsoft Word documents, .pdf and/or .lnk files. [^188] [^101] [^85] [^165] [^240] [^37] [^47] [^262]  |
| [[BlackTech\|G0098]] | BlackTech | [BlackTech](https://attack.mitre.org/groups/G0098) has used e-mails with malicious links to lure victims into installing malware.[^166] 	  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006)  has sent spearphishing emails that required the user to click on a malicious link and subsequently open a decoy document with a malicious loader.[^360]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has lured victims into clicking malicious links.[^120]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has tricked unwitting recipients into clicking on malicious hyperlinks within emails crafted to resemble trustworthy senders.[^245]  |
| [[TA577\|G1037]] | TA577 | [TA577](https://attack.mitre.org/groups/G1037) has lured users into executing malicious JavaScript files by sending malicious links via email.[^232]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has used spearphishing via a link to get users to download and run their malware.[^276]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) has used spearphishing with links to try to get users to click, download and open malicious files.[^256] [^169] [^106] [^287]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has tricked unwitting recipients into clicking on malicious hyperlinks within emails crafted to resemble trustworthy senders.[^23] [^208]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has attempted to lure victims into opening malicious links embedded in emails.[^8] [^201]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has used various forms of spearphishing attempting to get a user to click on a malicious link.[^296] [^228]  |
| [[EXOTIC LILY\|G1011]] | EXOTIC LILY | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) has used malicious links to lure users into executing malicious payloads.[^219]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails containing malicious links that require users to execute a file or macro to infect the victim machine.[^418] [^364] [^394]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has sent spearphishing emails in an attempt to lure users to click on a malicious link.[^227] [^137]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has distributed URLs in phishing e-mails that link to lure documents.[^239] [^320] [^235]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has used links to execute a malicious Visual Basic script.[^210]   |
| [[Transparent Tribe\|G0134]] | Transparent Tribe | [Transparent Tribe](https://attack.mitre.org/groups/G0134) has directed users to open URLs hosting malicious content.[^49] [^7]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has lured targets to download a Cobalt Strike beacon by including a malicious link within spearphishing emails.[^409] [^337] [^93]  |
| [[Leviathan\|G0065]] | Leviathan | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing email links attempting to get a user to click.[^407] [^344]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has sent malicious links including links directing victims to a Google Drive folder.[^345] [^151] [^73] [^124] [^411] [^300]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized webpages with Javascript code that downloads malicious payloads to the victim device.[^335]  |
| [[TA2541\|G1018]] | TA2541 | [TA2541](https://attack.mitre.org/groups/G1018) has used malicious links to cloud and web services to gain execution on victim machines.[^170] [^217]  |
| [[Mustard Tempest\|G1020]] | Mustard Tempest | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has lured users into downloading malware through malicious links in fake advertisements and spearphishing emails.[^92] [^306]  |
| [[Molerats\|G0021]] | Molerats | [Molerats](https://attack.mitre.org/groups/G0021) has sent malicious links via email trick users into opening a RAR archive and running an executable.[^50] [^199]   |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used emails with malicious links to lure victims into installing malware.[^314] [^308] [^123]  |
| [[Saint Bear\|G1031]] | Saint Bear | [Saint Bear](https://attack.mitre.org/groups/G1031) has, in addition to email-based phishing attachments, used malicious websites masquerading as legitimate entities to host links to malicious files for user execution.[^392] [^241]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has used malicious links to infect the victim machines.[^274] [^343]  |
| [[FIN4\|G0085]] | FIN4 | [FIN4](https://attack.mitre.org/groups/G0085) has lured victims to click malicious links delivered via spearphishing emails (often sent from compromised accounts).[^156] [^94]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has lured victims to click on a malicious link that led to download of a malicious payload.[^316]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also leveraged links to malicious payloads on social media and code repositories.[^316]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has lured targets to click on malicious links to gain execution in the target environment.[^237] [^206] [^17] [^33]  |
| [[Windshift\|G0112]] | Windshift | [Windshift](https://attack.mitre.org/groups/G0112) has used links embedded in e-mails to lure victims into executing malicious code.[^131]  |
| [[Confucius\|G0142]] | Confucius | [Confucius](https://attack.mitre.org/groups/G0142) has lured victims into clicking on a malicious link sent through spearphishing.[^388]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has attempted to get users to click on a link pointing to a malicious HTML file leading to follow-on malicious content.[^143] [^338]    |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has lured victims into clicking malicious links delivered through spearphishing.[^196]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used malicious links in e-mails to lure victims into downloading malware.[^112] [^377]  |
| [[Mofang\|G0103]] | Mofang | [Mofang](https://attack.mitre.org/groups/G0103)'s spearphishing emails required a user to click the link to connect to a compromised website.[^261]  |
| [[Machete\|G0095]] | Machete | [Machete](https://attack.mitre.org/groups/G0095) has has relied on users opening malicious links delivered through spearphishing to execute malware.[^278] [^421] [^140]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) has mimicked legitimate government-related domains to deliver malicious webpages containing links to documents or other content for user execution.[^416] [^216]  |
| [[APT33\|G0064]] | APT33 | [APT33](https://attack.mitre.org/groups/G0064) has lured users to click links to malicious HTML applications delivered via spearphishing emails.[^114] [^116]  |
| [[Evilnum\|G0120]] | Evilnum | [Evilnum](https://attack.mitre.org/groups/G0120) has sent spearphishing emails designed to trick the recipient into opening malicious shortcut links which downloads a .LNK file.[^429]  |
| [[LazyScripter\|G0140]] | LazyScripter | [LazyScripter](https://attack.mitre.org/groups/G0140) has relied upon users clicking on links to malicious files.[^75]  |
| [[TA578\|G1038]] | TA578 | [TA578](https://attack.mitre.org/groups/G1038) has placed malicious links in contact forms on victim sites, often spoofing a copyright complaint, to redirect users to malicious file downloads.[^232]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Network Intrusion Prevention\|M1031]] | Network Intrusion Prevention | If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity. |
| [[Restrict Web-Based Content\|M1021]] | Restrict Web-Based Content | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| [[User Training\|M1017]] | User Training | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Malicious Link\|T1204.001]] | Malicious Link |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Talos Transparent Tribe May 2021](https://blog.talosintelligence.com/2021/05/transparent-tribe-infra-and-targeting.html)


[^8]: [ClearSky Kittens Back 3 August 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/The-Kittens-are-Back-in-Town-3.pdf)


[^9]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^10]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^11]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^12]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^13]: [Carbon Black Emotet Apr 2019](https://www.carbonblack.com/2019/04/24/cb-tau-threat-intelligence-notification-emotet-utilizing-wmi-to-launch-powershell-encoded-code/)


[^14]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^15]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^16]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^17]: [Rewterz Sidewinder COVID-19 June 2020](https://www.rewterz.com/articles/analysis-on-sidewinder-apt-group-covid-19)


[^18]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^19]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^20]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^21]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^22]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^23]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^24]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^25]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^26]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^27]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^28]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^29]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^30]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^31]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)


[^32]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^33]: [Cyble Sidewinder September 2020](https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/)


[^34]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^35]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^36]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)


[^37]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)


[^38]: [Kroll Qakbot June 2020](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)


[^39]: [ClearSky OilRig Jan 2017](http://www.clearskysec.com/oilrig/)


[^40]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^41]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^42]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^43]: [Unit 42 NETWIRE April 2020](https://unit42.paloaltonetworks.com/guloader-installing-netwire-rat/)


[^44]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^45]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^46]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^47]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^48]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^49]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^50]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^51]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^52]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^53]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^54]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^55]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^56]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^57]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^58]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^59]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^60]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^61]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^62]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^63]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^64]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^65]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^66]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^67]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^68]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^69]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^70]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^71]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^72]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^73]: [Crowdstrike MUSTANG PANDA June 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)


[^74]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^75]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^76]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^77]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^78]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^79]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^80]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^81]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^82]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


[^83]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^84]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^85]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^86]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^87]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^88]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^89]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^90]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^91]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^92]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^93]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)


[^94]: [FireEye Hacking FIN4 Video Dec 2014](https://www2.fireeye.com/WBNR-14Q4NAMFIN4.html)


[^95]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^96]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^97]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^98]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^99]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^100]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^101]: [Proofpoint TA505 June 2018](https://www.proofpoint.com/us/threat-insight/post/ta505-shifts-times)


[^102]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^103]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^104]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^105]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^106]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^107]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^108]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^109]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^110]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^111]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^112]: [Google Election Threats October 2020](https://blog.google/threat-analysis-group/how-were-tackling-evolving-online-threats/)


[^113]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^114]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^115]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^116]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^117]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^118]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^119]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^120]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^121]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^122]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^123]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^124]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^125]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^126]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^127]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^128]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^129]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^130]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^131]: [SANS Windshift August 2018](https://www.scribd.com/document/661837258/WINDSHIFT-summit-archive-1554718868)


[^132]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^133]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^134]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^135]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^136]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^137]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^138]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^139]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^140]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^141]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^142]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^143]: [unit42_gamaredon_dec2022](https://unit42.paloaltonetworks.com/trident-ursa/)


[^144]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^145]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^146]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^147]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^148]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^149]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^150]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^151]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^152]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^153]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^154]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^155]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^156]: [FireEye Hacking FIN4 Dec 2014](https://www.mandiant.com/sites/default/files/2021-09/rpt-fin4.pdf)


[^157]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^158]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^159]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^160]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^161]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^162]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^163]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^164]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^165]: [Cybereason TA505 April 2019](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)


[^166]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^167]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^168]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^169]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^170]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


[^171]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^172]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^173]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^174]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^175]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^176]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)


[^177]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^178]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^179]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^180]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^181]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^182]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^183]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^184]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^185]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^186]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^187]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^188]: [Proofpoint TA505 Sep 2017](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)


[^189]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^190]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^191]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^192]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^193]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^194]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^195]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^196]: [FireEye Clandestine Wolf](https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html)


[^197]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^198]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^199]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^200]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^201]: [Certfa Charming Kitten January 2021](https://blog.certfa.com/posts/charming-kitten-christmas-gift/)


[^202]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^203]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^204]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^205]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^206]: [Rewterz Sidewinder APT April 2020](https://www.rewterz.com/threats/sidewinder-apt-group-campaign-analysis)


[^207]: [Trend Micro Qakbot December 2020](https://success.trendmicro.com/en-US/solution/KA-0011282)


[^208]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^209]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^210]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^211]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^212]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^213]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^214]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^215]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^216]: [CERT-UA WinterVivern 2023](https://cert.gov.ua/article/3761104)


[^217]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)


[^218]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^219]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^220]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^221]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^222]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^223]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^224]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^225]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^226]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^227]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^228]: [Secureworks IRON RITUAL USAID Phish May 2021](https://www.secureworks.com/blog/usaid-themed-phishing-campaign-leverages-us-elections-lure)


[^229]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^230]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^231]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^232]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^233]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^234]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^235]: [Proofpoint TA450 Phishing March 2024](https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta450-uses-embedded-links-pdf-attachments-latest-campaign)


[^236]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^237]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^238]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^239]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)


[^240]: [ProofPoint SettingContent-ms July 2018](https://www.proofpoint.com/us/threat-insight/post/ta505-abusing-settingcontent-ms-within-pdf-files-distribute-flawedammyy-rat)


[^241]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^242]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^243]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)


[^244]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^245]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^246]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^247]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^248]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^249]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^250]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^251]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^252]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^253]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^254]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^255]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^256]: [Symantec Patchwork](http://www.symantec.com/connect/blogs/patchwork-cyberespionage-group-expands-targets-governments-wide-range-industries)


[^257]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^258]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^259]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^260]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^261]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^262]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^263]: [Trend Micro Banking Malware Jan 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/new-banking-malware-uses-network-sniffing-for-data-theft/)


[^264]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^265]: [Crowdstrike Helix Kitten Nov 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/)


[^266]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^267]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^268]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^269]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^270]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^271]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^272]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^273]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)


[^274]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^275]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^276]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^277]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^278]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^279]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^280]: [CSM Elderwood Sept 2012](https://www.csmonitor.com/USA/2012/0914/Stealing-US-business-secrets-Experts-ID-two-huge-cyber-gangs-in-China)


[^281]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^282]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^283]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^284]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^285]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^286]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^287]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^288]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^289]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^290]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^291]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^292]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^293]: [Bleeping Computer Latrodectus April 2024](https://www.bleepingcomputer.com/news/security/new-latrodectus-malware-attacks-use-microsoft-cloudflare-themes/)


[^294]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^295]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^296]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


[^297]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^298]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^299]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^300]: [McAfee Dianxun March 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-dianxun.pdf)


[^301]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^302]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^303]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^304]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^305]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^306]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^307]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^308]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^309]: [FireEye Shining A Light on DARKSIDE May 2021](https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html)


[^310]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^311]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^312]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^313]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^314]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)


[^315]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^316]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^317]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^318]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^319]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^320]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^321]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^322]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^323]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^324]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^325]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^326]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)


[^327]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^328]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^329]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^330]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^331]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^332]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^333]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^334]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^335]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^336]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^337]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)


[^338]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^339]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^340]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^341]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^342]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^343]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^344]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^345]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)


[^346]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^347]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^348]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^349]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^350]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^351]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^352]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^353]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^354]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^355]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^356]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^357]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^358]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^359]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^360]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^361]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^362]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^363]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^364]: [Unit 42 Cobalt Gang Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-new-techniques-uncover-attribute-cobalt-gang-commodity-builders-infrastructure-revealed/)


[^365]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^366]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^367]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^368]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^369]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^370]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^371]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^372]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^373]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^374]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^375]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^376]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)


[^377]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^378]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^379]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^380]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^381]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^382]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^383]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^384]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^385]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^386]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^387]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


[^388]: [TrendMicro Confucius APT Aug 2021](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)


[^389]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^390]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^391]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^392]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^393]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^394]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^395]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^396]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^397]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^398]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^399]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^400]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^401]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^402]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^403]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^404]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^405]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^406]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^407]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^408]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^409]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^410]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^411]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^412]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^413]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^414]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^415]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^416]: [SentinelOne WinterVivern 2023](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)


[^417]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^418]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^419]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^420]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^421]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)


[^422]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^423]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^424]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^425]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^426]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^427]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^428]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^429]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^430]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^431]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^432]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^433]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^434]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^435]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^436]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^437]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^438]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^439]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^440]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^441]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^442]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^443]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^444]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^445]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


