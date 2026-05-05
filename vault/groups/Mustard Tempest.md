---
aliases: 
    - Mustard Tempest
    - DEV-0206
    - TA569
    - GOLD PRELUDE
    - UNC1543
mitre-attack: https://attack.mitre.org/groups/G1020
---

## G1020

[Mustard Tempest](https://attack.mitre.org/groups/G1020) is an initial access broker that has operated the [SocGholish](https://attack.mitre.org/software/S1124) distribution network since at least 2017. [Mustard Tempest](https://attack.mitre.org/groups/G1020) has partnered with [Indrik Spider](https://attack.mitre.org/groups/G0119) to provide access for the download of additional malware including LockBit, [WastedLocker](https://attack.mitre.org/software/S0612), and remote access tools.[^6] [^7] [^5] [^9] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malvertising\|T1583.008]] | Malvertising | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has posted false advertisements including for software packages and browser updates in order to distribute malware.[^6]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has hosted payloads on acquired second-stage servers for periods of either days, weeks, or months.[^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used the filename `AutoUpdater.js` to mimic legitimate update files and has also used the Cyrillic homoglyph characters С `(0xd0a1)` and а `(0xd0b0)`, to produce the filename `Сhrome.Updаte.zip`.[^3] [^9]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has sent victims emails containing links to compromised websites.[^9]  |
| [[Domains\|T1584.001]] | Domains | [Mustard Tempest](https://attack.mitre.org/groups/G1020) operates a global network of compromised websites that redirect into a traffic distribution system (TDS) to select victims for a fake browser update page.[^5] [^9] [^8] [^3]  |
| [[SEO Poisoning\|T1608.006]] | SEO Poisoning | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has poisoned search engine results to return fake software updates in order to distribute malware.[^6] [^9]  |
| [[Drive-by Target\|T1608.004]] | Drive-by Target | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has injected malicious JavaScript into compromised websites to infect victims via drive-by download.[^9] [^8] [^3] [^5]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used drive-by downloads for initial infection, often using fake browser updates as a lure.[^9] [^8] [^3] [^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has lured users into downloading malware through malicious links in fake advertisements and spearphishing emails.[^6] [^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used implants to perform system reconnaissance on targeted systems.[^6]  |
| [[Server\|T1583.004]] | Server | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has acquired servers to host second-stage payloads that remain active for a period of either days, weeks, or months.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has deployed secondary payloads and third stage implants to compromised hosts.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[SocGholish\|S1124]] | SocGholish | [^6] [^5] [^9]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^6]  |



## References

[^1]: DEV-0206


[^2]: UNC1543


[^3]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^4]: GOLD PRELUDE


[^5]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^6]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^7]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^8]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)


[^9]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^10]: TA569


