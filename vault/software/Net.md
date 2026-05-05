---
aliases: 
    - S0039
    
mitre-attack: https://attack.mitre.org/software/S0039
---

## S0039

The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. [^34] <br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, [^51]  much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using `net use` commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as `net1 user`.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | The `net accounts` and `net accounts /domain` commands with [Net](https://attack.mitre.org/software/S0039) can be used to obtain password policy information.[^51]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | Commands such as `net group /domain` can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.[^51]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | The `net time` command can be used in [Net](https://attack.mitre.org/software/S0039) to determine the local or remote system time.[^12]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Net](https://attack.mitre.org/software/S0039) commands used with the `/domain` flag can be used to gather information about and manipulate user accounts on the current domain.[^19]  |
| [[Local Account\|T1087.001]] | Local Account | Commands under `net user` can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate user accounts.[^51]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | The `net start` command can be used in [Net](https://attack.mitre.org/software/S0039) to find information about Windows services.[^51]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | Commands such as `net view` can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about available remote systems.[^51]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | The `net view \\remotesystem` and `net share` commands in [Net](https://attack.mitre.org/software/S0039) can be used to find shared drives and directories on remote and local systems respectively.[^51]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | Commands such as `net use` and `net session` can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about network connections from a particular host.[^51]  |
| [[Network Share Connection Removal\|T1070.005]] | Network Share Connection Removal | The `net use \\system\share /delete` command can be used in [Net](https://attack.mitre.org/software/S0039) to remove an established connection to a network share.[^24]  |
| [[Service Execution\|T1569.002]] | Service Execution | The `net start` and `net stop` commands can be used in [Net](https://attack.mitre.org/software/S0039) to execute or stop Windows services.[^51]  |
| [[Local Account\|T1136.001]] | Local Account | The `net user username \password` commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a local account.[^51]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | The `net localgroup` and `net group` commands in [Net](https://attack.mitre.org/software/S0039) can be used to add existing users to local and domain groups.[^41]  [^6]  |
| [[Local Groups\|T1069.001]] | Local Groups | Commands such as `net group` and `net localgroup` can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.[^51]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | Lateral movement can be done with [Net](https://attack.mitre.org/software/S0039) through `net use` commands to connect to the on remote systems.[^51]  |
| [[Domain Account\|T1136.002]] | Domain Account | The `net user username \password \domain` commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a domain account.[^51]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |
| [[Naikon\|G0019]] | Naikon |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[APT38\|G0082]] | APT38 |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[Deep Panda\|G0009]] | Deep Panda |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[OilRig\|G0049]] | OilRig |
| [[Threat Group-1314\|G0028]] | Threat Group-1314 |
| [[APT28\|G0007]] | APT28 |
| [[APT41\|G0096]] | APT41 |
| [[menuPass\|G0045]] | menuPass |
| [[Ke3chang\|G0004]] | Ke3chang |
| [[Leviathan\|G0065]] | Leviathan |
| [[APT5\|G1023]] | APT5 |
| [[Orangeworm\|G0071]] | Orangeworm |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[admin@338\|G0018]] | admin@338 |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[Chimera\|G0114]] | Chimera |
| [[APT1\|G0006]] | APT1 |
| [[FIN8\|G0061]] | FIN8 |
| [[TA505\|G0092]] | TA505 |
| [[ToddyCat\|G1022]] | ToddyCat |
| [[Turla\|G0010]] | Turla |
| [[APT33\|G0064]] | APT33 |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[APT29\|G0016]] | APT29 |
| [[APT32\|G0050]] | APT32 |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |



## References

[^1]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^2]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^3]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^4]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^5]: [DFIR Ryuk in 5 Hours October 2020](https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/)


[^6]: [Microsoft Net Group](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc754051(v=ws.11))


[^7]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^8]: [Alperovitch 2014](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)


[^9]: [Dell TG-1314](https://web.archive.org/web/20150626073312/http://www.secureworks.com/resources/blog/living-off-the-land/)


[^10]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^11]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^12]: [TechNet Net Time](https://technet.microsoft.com/bb490716.aspx)


[^13]: [Microsoft Storm-0501 Embargo Ransomware August 2025](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)


[^14]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^15]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^16]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^17]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^18]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^19]: [Microsoft Net](https://support.microsoft.com/en-us/help/556003)


[^20]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^21]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^22]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^23]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^24]: [Technet Net Use](https://technet.microsoft.com/bb490717.aspx)


[^25]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^26]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^27]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^28]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^29]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^30]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^31]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^32]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^33]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^34]: [Microsoft Net Utility](https://msdn.microsoft.com/en-us/library/aa939914)


[^35]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^36]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^37]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^38]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^39]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^40]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^41]: [Microsoft Net Localgroup](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc725622(v=ws.11))


[^42]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^43]: [FireEye APT40 March 2019](https://www.fireeye.com/blog/threat-research/2019/03/apt40-examining-a-china-nexus-espionage-actor.html)


[^44]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^45]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^46]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^47]: [Huntress INC Ransomware May 2024](https://www.huntress.com/blog/lolbin-to-inc-ransomware)


[^48]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^49]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^50]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^51]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)


[^52]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


[^53]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


[^54]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


