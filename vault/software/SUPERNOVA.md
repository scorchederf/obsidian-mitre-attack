---
aliases: 
    - S0578
    
mitre-attack: https://attack.mitre.org/software/S0578
---

## S0578

[SUPERNOVA](https://attack.mitre.org/software/S0578) is an in-memory web shell written in .NET C#. It was discovered in November 2020 during the investigation of [APT29](https://attack.mitre.org/groups/G0016)'s SolarWinds cyber operation but determined to be unrelated. Subsequent analysis suggests [SUPERNOVA](https://attack.mitre.org/software/S0578) may have been used by the China-based threat group SPIRAL.[^6] [^2] [^1] [^4] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SUPERNOVA](https://attack.mitre.org/software/S0578) had to receive an HTTP GET request containing a specific set of parameters in order to execute.[^6] [^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [SUPERNOVA](https://attack.mitre.org/software/S0578) was installed via exploitation of a SolarWinds Orion API authentication bypass vulnerability (CVE-2020-10148).[^3] [^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SUPERNOVA](https://attack.mitre.org/software/S0578) has masqueraded as a legitimate SolarWinds DLL.[^6] [^2]  |
| [[Web Shell\|T1505.003]] | Web Shell | [SUPERNOVA](https://attack.mitre.org/software/S0578) is a Web shell.[^2] [^6] [^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SUPERNOVA](https://attack.mitre.org/software/S0578) contained Base64-encoded strings.[^4]  |




## References

[^1]: [SolarWinds Advisory Dec 2020](https://www.solarwinds.com/sa-overview/securityadvisory)


[^2]: [Unit42 SUPERNOVA Dec 2020](https://unit42.paloaltonetworks.com/solarstorm-supernova/)


[^3]: [Carnegie Mellon University Supernova Dec 2020](https://www.kb.cert.org/vuls/id/843464)


[^4]: [CISA Supernova Jan 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-027a)


[^5]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^6]: [Guidepoint SUPERNOVA Dec 2020](https://www.guidepointsecurity.com/supernova-solarwinds-net-webshell-analysis/)


[^7]: [Splunk Supernova Jan 2021](https://www.splunk.com/en_us/blog/security/detecting-supernova-malware-solarwinds-continued.html)


