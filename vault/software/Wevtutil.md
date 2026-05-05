---
aliases: 
    - S0645
    
mitre-attack: https://attack.mitre.org/software/S0645
---

## S0645

[Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to disable specific event logs on the system.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to export events from a specific log.[^1] [^5]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to clear system and security event logs from the system.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[Play\|G1040]] | Play |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [Wevtutil Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)


[^2]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^3]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^4]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^5]: [F-Secure Lazarus Cryptocurrency Aug 2020](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)


[^6]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^7]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^8]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^9]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


