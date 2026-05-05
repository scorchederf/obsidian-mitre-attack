---
aliases: 
    - T1596
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1596-Search_Open_Technical_Databases
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.[^4] [^1] [^7] [^3] [^5] [^6] [^2] <br><br>Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]] or [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1583-Acquire_Infrastructure\|Acquire Infrastructure]] or [[kb/mitre/attack/techniques/T1584-Compromise_Infrastructure\|Compromise Infrastructure]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]] or [[kb/mitre/attack/techniques/T1199-Trusted_Relationship\|Trusted Relationship]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1596.001-DNS_Passive_DNS\|T1596.001]] | DNS／Passive DNS |
| [[kb/mitre/attack/techniques/T1596.002-WHOIS\|T1596.002]] | WHOIS |
| [[kb/mitre/attack/techniques/T1596.003-Digital_Certificates\|T1596.003]] | Digital Certificates |
| [[kb/mitre/attack/techniques/T1596.004-CDNs\|T1596.004]] | CDNs |
| [[kb/mitre/attack/techniques/T1596.005-Scan_Databases\|T1596.005]] | Scan Databases |




> [!info]- References
> [^1]: [DNS Dumpster](https://dnsdumpster.com/)

> [^2]: [Shodan](https://shodan.io)

> [^3]: [Medium SSL Cert](https://medium.com/@menakajain/export-download-ssl-certificate-from-server-site-url-bcfc41ea46a2)

> [^4]: [WHOIS](https://who.is/)

> [^5]: [SSLShopper Lookup](https://www.sslshopper.com/ssl-checker.html)

> [^6]: [DigitalShadows CDN](https://www.digitalshadows.com/blog-and-research/content-delivery-networks-cdns-can-leave-you-exposed-how-you-might-be-affected-and-what-you-can-do-about-it/)

> [^7]: [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)


