---
aliases: 
    - S0002
    
mitre-attack: https://attack.mitre.org/software/S0002
---

## S0002

[Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. [^30]  [^63] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DCSync\|T1003.006]] | DCSync | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DCSync/NetSync.[^30] [^90] [^46] [^52] [^8]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.[^30] [^90] [^46] [^52] [^8] 	 |
| [[Rogue Domain Controller\|T1207]] | Rogue Domain Controller | [Mimikatz](https://attack.mitre.org/software/S0002)’s `LSADUMP::DCShadow` module can be used to make AD updates by temporarily setting a computer to be a DC.[^30] [^63]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Mimikatz](https://attack.mitre.org/software/S0002)'s `CRYPTO::Extract` module can extract keys by interacting with Windows cryptographic application programming interface (API) functions.[^63]  |
| [[SID-History Injection\|T1134.005]] | SID-History Injection | [Mimikatz](https://attack.mitre.org/software/S0002)'s `MISC::AddSid` module can append any SID or user/group account to a user's SID-History. [Mimikatz](https://attack.mitre.org/software/S0002) also utilizes [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) to expand the scope of other components such as generated Kerberos Golden Tickets and DCSync beyond a single domain.[^63] [^61]  |
| [[Security Support Provider\|T1547.005]] | Security Support Provider | The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper contains an implementation of an SSP.[^30]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Mimikatz](https://attack.mitre.org/software/S0002)'s `SEKURLSA::Pth` module can impersonate a user, with only a password hash, to execute arbitrary commands.[^63] [^52] [^8]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The `LSADUMP::ChangeNTLM` and `LSADUMP::SetNTLM` modules can also manipulate the password hash of an account without knowing the clear text value.[^63] [^83]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | [Mimikatz](https://attack.mitre.org/software/S0002)’s `LSADUMP::DCSync` and `KERBEROS::PTT` modules implement the three steps required to extract the krbtgt account hash and create/use Kerberos tickets.[^63] [^61] [^36] [^52]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DPAPI.[^30] [^90] [^46] [^52] 	 |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create golden tickets.[^55] [^8]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the SAM table.[^30] [^90] [^46] [^52]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSASS Memory.[^30] [^90] [^46] [^52]  |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create silver tickets.[^55]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Mimikatz](https://attack.mitre.org/software/S0002) contains functionality to acquire credentials from the Windows Credential Manager.[^47]  |
| [[Steal or Forge Authentication Certificates\|T1649]] | Steal or Forge Authentication Certificates | [Mimikatz](https://attack.mitre.org/software/S0002)'s `CRYPTO` module can create and export various types of authentication certificates.[^63]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSA.[^30] [^90] [^46] [^52]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |
| [[APT29\|G0016]] | APT29 |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[FIN7\|G0046]] | FIN7 |
| [[DarkHydrus\|G0079]] | DarkHydrus |
| [[TA505\|G0092]] | TA505 |
| [[Agrius\|G1030]] | Agrius |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[APT33\|G0064]] | APT33 |
| [[Akira\|G1024]] | Akira |
| [[Tonto Team\|G0131]] | Tonto Team |
| [[APT39\|G0087]] | APT39 |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird |
| [[Cobalt Group\|G0080]] | Cobalt Group |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Ke3chang\|G0004]] | Ke3chang |
| [[menuPass\|G0045]] | menuPass |
| [[APT5\|G1023]] | APT5 |
| [[TEMP.Veles\|G0088]] | TEMP.Veles |
| [[APT28\|G0007]] | APT28 |
| [[APT1\|G0006]] | APT1 |
| [[FIN13\|G1016]] | FIN13 |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[Thrip\|G0076]] | Thrip |
| [[LAPSUS$\|G1004]] | LAPSUS$ |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy |
| [[Indrik Spider\|G0119]] | Indrik Spider |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[Leafminer\|G0077]] | Leafminer |
| [[APT41\|G0096]] | APT41 |
| [[Medusa Group\|G1051]] | Medusa Group |
| [[Cleaver\|G0003]] | Cleaver |
| [[APT38\|G0082]] | APT38 |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[Turla\|G0010]] | Turla |
| [[Chimera\|G0114]] | Chimera |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[Carbanak\|G0008]] | Carbanak |
| [[PittyTiger\|G0011]] | PittyTiger |
| [[HEXANE\|G1001]] | HEXANE |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[OilRig\|G0049]] | OilRig |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[Play\|G1040]] | Play |
| [[FIN6\|G0037]] | FIN6 |
| [[Whitefly\|G0107]] | Whitefly |
| [[BlackByte\|G1043]] | BlackByte |



## References

[^1]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^2]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^3]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^4]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^5]: [Symantec Thrip June 2018](https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets)


[^6]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^7]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^8]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^9]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^10]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


[^11]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^12]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^13]: [PTSecurity Cobalt Dec 2016](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)


[^14]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^15]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^16]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^17]: [Unit 42 MuddyWater Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/)


[^18]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^19]: [Netscout Stolen Pencil Dec 2018](https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/)


[^20]: [BitDefender Chafer May 2020](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)


[^21]: [ESET Turla Mosquito May 2018](https://www.welivesecurity.com/2018/05/22/turla-mosquito-shift-towards-generic-tools/)


[^22]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


[^23]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^24]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^25]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^26]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


[^27]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^28]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)


[^29]: [Symantec Whitefly March 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)


[^30]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)


[^31]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^32]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^33]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^34]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^35]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^36]: [Harmj0y DCSync Sept 2015](http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/)


[^37]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^38]: [Check Point Scattered Spider JUL 2025](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)


[^39]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^40]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


[^41]: [Dark Reading APT39 JAN 2019](https://www.darkreading.com/attacks-breaches/iran-ups-its-traditional-cyber-espionage-tradecraft/d/d-id/1333764)


[^42]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^43]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^44]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^45]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^46]: [Directory Services Internals DPAPI Backup Keys Oct 2015](https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/)


[^47]: [Delpy Mimikatz Crendential Manager](https://github.com/gentilkiwi/mimikatz/wiki/howto-~-credential-manager-saved-credentials)


[^48]: [Microsoft 365 Defender Solorigate](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)


[^49]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^50]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^51]: [FireEye TRITON 2019](https://www.fireeye.com/blog/threat-research/2019/04/triton-actor-ttp-profile-custom-attack-tools-detections.html)


[^52]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^53]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^54]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^55]: [GitHub Mimikatz kerberos Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-kerberos)


[^56]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^57]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^58]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^59]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^60]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^61]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^62]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^63]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)


[^64]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^65]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^66]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^67]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^68]: [MSTIC Octo Tempest Operations October 2023](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)


[^69]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^70]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^71]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^72]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


[^73]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^74]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^75]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^76]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^77]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^78]: [MSTIC DEV-0537 Mar 2022](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)


[^79]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^80]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^81]: [Secureworks IRON LIBERTY July 2019](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector)


[^82]: [Bizeul 2014](https://airbus-cyber-security.com/the-eye-of-the-tiger/)


[^83]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^84]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^85]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^86]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^87]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^88]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^89]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^90]: [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)


[^91]: [Unit42 OilRig Playbook 2023](https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)


[^92]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^93]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


[^94]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


