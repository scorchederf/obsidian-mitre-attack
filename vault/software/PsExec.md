---
aliases: 
    - S0029
    
mitre-attack: https://attack.mitre.org/software/S0029
---

## S0029

[PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.[^35] [^52] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [PsExec](https://attack.mitre.org/software/S0029), a tool that has been used by adversaries, writes programs to the `ADMIN$` network share to execute commands on remote systems.[^29]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PsExec](https://attack.mitre.org/software/S0029) can leverage Windows services to escalate privileges from administrator to SYSTEM with the `-s` argument.[^35]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [PsExec](https://attack.mitre.org/software/S0029) can be used to download or upload a file over a network share.[^29]  |
| [[Service Execution\|T1569.002]] | Service Execution | Microsoft Sysinternals [PsExec](https://attack.mitre.org/software/S0029) is a popular administration tool that can be used to execute binaries on remote systems using a temporary Windows service.[^35]  |
| [[Domain Account\|T1136.002]] | Domain Account | [PsExec](https://attack.mitre.org/software/S0029) has the ability to remotely create accounts on target systems.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[Turla\|G0010]] | Turla |
| [[Chimera\|G0114]] | Chimera |
| [[APT1\|G0006]] | APT1 |
| [[Thrip\|G0076]] | Thrip |
| [[Moses Staff\|G1009]] | Moses Staff |
| [[BlackTech\|G0098]] | BlackTech |
| [[Cleaver\|G0003]] | Cleaver |
| [[DarkVishnya\|G0105]] | DarkVishnya |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[Storm-1811\|G1046]] | Storm-1811 |
| [[HAFNIUM\|G0125]] | HAFNIUM |
| [[Akira\|G1024]] | Akira |
| [[APT39\|G0087]] | APT39 |
| [[Play\|G1040]] | Play |
| [[FIN5\|G0053]] | FIN5 |
| [[FIN6\|G0037]] | FIN6 |
| [[Indrik Spider\|G0119]] | Indrik Spider |
| [[TEMP.Veles\|G0088]] | TEMP.Veles |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[APT29\|G0016]] | APT29 |
| [[BlackByte\|G1043]] | BlackByte |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Carbanak\|G0008]] | Carbanak |
| [[Leafminer\|G0077]] | Leafminer |
| [[Medusa Group\|G1051]] | Medusa Group |
| [[FIN8\|G0061]] | FIN8 |
| [[Fox Kitten\|G0117]] | Fox Kitten |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[OilRig\|G0049]] | OilRig |
| [[Cobalt Group\|G0080]] | Cobalt Group |
| [[Naikon\|G0019]] | Naikon |
| [[Threat Group-1314\|G0028]] | Threat Group-1314 |
| [[menuPass\|G0045]] | menuPass |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^4]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^5]: [Securelist DarkVishnya Dec 2018](https://securelist.com/darkvishnya/89169/)


[^6]: [Dell TG-1314](https://web.archive.org/web/20150626073312/http://www.secureworks.com/resources/blog/living-off-the-land/)


[^7]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^8]: [Dragos Xenotime 2018](https://dragos.com/resource/xenotime/)


[^9]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^10]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


[^11]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^12]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^13]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^14]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^15]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)


[^16]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^17]: [Symantec Thrip June 2018](https://www.symantec.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets)


[^18]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^19]: [FireEye TRITON 2019](https://www.fireeye.com/blog/threat-research/2019/04/triton-actor-ttp-profile-custom-attack-tools-detections.html)


[^20]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^21]: [Symantec Palmerworm Sep 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt)


[^22]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


[^23]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^24]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^25]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^26]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^27]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^28]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^29]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)


[^30]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^31]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^32]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^33]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^34]: [Secureworks IRON LIBERTY July 2019](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector)


[^35]: [Russinovich Sysinternals](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)


[^36]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


[^37]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^38]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^39]: [Symantec Dragonfly Sept 2017](https://docs.broadcom.com/doc/dragonfly_threat_against_western_energy_suppliers)


[^40]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^41]: [Netscout Stolen Pencil Dec 2018](https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/)


[^42]: [BitDefender Chafer May 2020](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)


[^43]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


[^44]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^45]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^46]: [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)


[^47]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


[^48]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^49]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^50]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^51]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^52]: [SANS PsExec](https://www.sans.org/blog/protecting-privileged-domain-accounts-psexec-deep-dive/)


[^53]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^54]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^55]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^56]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^57]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^58]: [FireEye FIN6 April 2016](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)


[^59]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


