---
aliases: 
    - S0552
    
mitre-attack: https://attack.mitre.org/software/S0552
---

## S0552

[AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.[^1] [^3] [^12] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [AdFind](https://attack.mitre.org/software/S0552) can gather information about organizational units (OUs) and domain trusts from Active Directory.[^1] [^3] [^12] [^9]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain groups.[^1] [^3] [^12] [^9]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [AdFind](https://attack.mitre.org/software/S0552) can extract subnet information from Active Directory.[^1] [^3] [^12]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [AdFind](https://attack.mitre.org/software/S0552) has the ability to query Active Directory for computers.[^1] [^3] [^12] [^19]  |
| [[Domain Account\|T1087.002]] | Domain Account | [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain users.[^1] [^3] [^12] [^19] [^9]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[FIN7\|G0046]] | FIN7 |
| [[Play\|G1040]] | Play |
| [[BlackByte\|G1043]] | BlackByte |
| [[FIN6\|G0037]] | FIN6 |
| [[Akira\|G1024]] | Akira |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[APT29\|G0016]] | APT29 |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^4]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^5]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^6]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^7]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^8]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^9]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^10]: [ESET T3 Threat Report 2021](https://www.welivesecurity.com/wp-content/uploads/2022/02/eset_threat_report_t32021.pdf)


[^11]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^12]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)


[^13]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^14]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^15]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


[^16]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


[^17]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^18]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^19]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^20]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^21]: [Secureworks GOLD IONIC April 2024](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)


[^22]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


