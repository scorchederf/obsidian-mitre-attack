---
aliases: 
    - S0521
    
mitre-attack: https://attack.mitre.org/software/S0521
---

## S0521

[BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.[^3] [^9] [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Groups\|T1069.002]] | Domain Groups | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain groups and members.[^9]  |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to collect local admin information via GPO.[^3]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [BloodHound](https://attack.mitre.org/software/S0521) can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.[^3] [^10]  |
| [[Local Groups\|T1069.001]] | Local Groups | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about local groups and members.[^9]  |
| [[Domain Account\|T1087.002]] | Domain Account | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain users, including identification of domain admin accounts.[^9]  |
| [[Local Account\|T1087.001]] | Local Account | [BloodHound](https://attack.mitre.org/software/S0521) can identify users with local administrator rights.[^9]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BloodHound](https://attack.mitre.org/software/S0521) can collect information on user sessions.[^9]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BloodHound](https://attack.mitre.org/software/S0521) can enumerate and collect the properties of domain computers, including domain controllers.[^9]  |
| [[Native API\|T1106]] | Native API | [BloodHound](https://attack.mitre.org/software/S0521) can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [BloodHound](https://attack.mitre.org/software/S0521) can use PowerShell to pull Active Directory information from the target environment.[^9]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to map domain trusts and identify misconfigurations for potential abuse.[^9]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[APT29\|G0016]] | APT29 |
| [[Chimera\|G0114]] | Chimera |
| [[TA505\|G0092]] | TA505 |
| [[Play\|G1040]] | Play |
| [[Ember Bear\|G1003]] | Ember Bear |



## References

[^1]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^5]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^6]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^7]: [ESET T3 Threat Report 2021](https://www.welivesecurity.com/wp-content/uploads/2022/02/eset_threat_report_t32021.pdf)


[^8]: [FoxIT Wocao December 2019](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)


[^9]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)


[^10]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^11]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^12]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^13]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


