---
aliases: 
    - S0057
    
mitre-attack: https://attack.mitre.org/software/S0057
---

## S0057

The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover processes running on a system.[^6]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover services running on a system.[^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Tasklist](https://attack.mitre.org/software/S0057) can be used to enumerate security software currently running on a system by process name of known products.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[APT5\|G1023]] | APT5 |
| [[APT29\|G0016]] | APT29 |
| [[MirrorFace\|G1054]] | MirrorFace |
| [[OilRig\|G0049]] | OilRig |
| [[Ke3chang\|G0004]] | Ke3chang |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[APT1\|G0006]] | APT1 |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Deep Panda\|G0009]] | Deep Panda |
| [[Turla\|G0010]] | Turla |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^2]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^3]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^4]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^5]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^6]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)


[^7]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^8]: [Alperovitch 2014](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)


[^9]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^10]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^11]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^12]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^13]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^14]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^15]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^16]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^17]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


