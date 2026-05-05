---
aliases: 
    - S0359
    
mitre-attack: https://attack.mitre.org/software/S0359
---

## S0359

[Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate trusted domains by using commands such as `nltest /domain_trusts`.[^1] [^11]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate remote domain controllers using options such as `/dclist` and `/dsgetdc`.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Play\|G1040]] | Play |
| [[MirrorFace\|G1054]] | MirrorFace |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[FIN8\|G0061]] | FIN8 |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |



## References

[^1]: [Nltest Manual](https://ss64.com/nt/nltest.html)


[^2]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^3]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^4]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^5]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^6]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^7]: [DFIR Ryuk in 5 Hours October 2020](https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/)


[^8]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^9]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^10]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^11]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)


[^12]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^13]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^14]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


[^15]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^16]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^17]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


