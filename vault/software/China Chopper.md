---
aliases: 
    - S0020
    
mitre-attack: https://attack.mitre.org/software/S0020
---

## S0020

[China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.[^13]  It has been used by several threat groups.[^1] [^2] [^14] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Password Guessing\|T1110.001]] | Password Guessing | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can perform brute force password guessing against authentication portals.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can upload local files.[^2] [^13] [^9] [^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | [China Chopper](https://attack.mitre.org/software/S0020)'s client component is packed with UPX.[^13]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [China Chopper](https://attack.mitre.org/software/S0020)'s server component is capable of opening a command terminal.[^21] [^13] [^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [China Chopper](https://attack.mitre.org/software/S0020)'s server component executes code sent via HTTP POST commands.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can download remote files.[^2] [^13] [^9] [^6] [^11]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can spider authentication portals.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can change the timestamp of files.[^2] [^13] [^9]  |
| [[Web Shell\|T1505.003]] | Web Shell | [China Chopper](https://attack.mitre.org/software/S0020)'s server component is a Web Shell payload.[^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can list directory contents.[^2] [^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy |
| [[Fox Kitten\|G0117]] | Fox Kitten |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[APT41\|G0096]] | APT41 |
| [[ToddyCat\|G1022]] | ToddyCat |
| [[HAFNIUM\|G0125]] | HAFNIUM |
| [[Leviathan\|G0065]] | Leviathan |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^2]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^3]: [apt41_dcsocytec_dec2022](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)


[^4]: China Chopper


[^5]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^6]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^7]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^8]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^9]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^10]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^11]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^12]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^13]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)


[^14]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^15]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^16]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^17]: [FireEye Exchange Zero Days March 2021](https://www.fireeye.com/blog/threat-research/2021/03/detection-response-to-exploitation-of-microsoft-exchange-zero-day-vulnerabilities.html)


[^18]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^19]: [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)


[^20]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^21]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


