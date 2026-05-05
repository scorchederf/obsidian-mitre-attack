---
aliases: 
    - S0160
    
mitre-attack: https://attack.mitre.org/software/S0160
---

## S0160

[certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [certutil](https://attack.mitre.org/software/S0160) may be used to Base64 encode collected data.[^1] [^17]  |
| [[Install Root Certificate\|T1553.004]] | Install Root Certificate | [certutil](https://attack.mitre.org/software/S0160) can be used to install browser root certificates as a precursor to performing [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) between connections to banking websites. Example command: `certutil -addstore -f -user ROOT ProgramData\cert512121.der`.[^24]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [certutil](https://attack.mitre.org/software/S0160) has been used to decode binaries hidden inside certificate files as Base64 information.[^13]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [certutil](https://attack.mitre.org/software/S0160) can be used to download files from a given URL.[^1] [^17]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |
| [[APT28\|G0007]] | APT28 |
| [[Kimsuky\|G0094]] | Kimsuky |
| [[Turla\|G0010]] | Turla |
| [[OilRig\|G0049]] | OilRig |
| [[Medusa Group\|G1051]] | Medusa Group |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Higaisa\|G0126]] | Higaisa |
| [[FIN13\|G1016]] | FIN13 |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[APT41\|G0096]] | APT41 |
| [[Rancor\|G0075]] | Rancor |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |



## References

[^1]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)


[^2]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^3]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^4]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^5]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^6]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^7]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^8]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^9]: [PTSecurity Higaisa 2020](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)


[^10]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^11]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^12]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^13]: [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)


[^14]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^15]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^16]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^17]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)


[^18]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^19]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


[^20]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^21]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^22]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^23]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^24]: [Palo Alto Retefe](https://researchcenter.paloaltonetworks.com/2015/08/retefe-banking-trojan-targets-sweden-switzerland-and-japan/)


