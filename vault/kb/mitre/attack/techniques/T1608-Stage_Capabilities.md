---
aliases: 
    - T1608
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1608-Stage_Capabilities
tactic: 
     - Resource Development
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting. To support their operations, an adversary may need to take capabilities they developed ([[kb/mitre/attack/techniques/T1587-Develop_Capabilities\|Develop Capabilities]]) or obtained ([[kb/mitre/attack/techniques/T1588-Obtain_Capabilities\|Obtain Capabilities]]) and stage them on infrastructure under their control. These capabilities may be staged on infrastructure that was previously purchased/rented by the adversary ([[kb/mitre/attack/techniques/T1583-Acquire_Infrastructure\|Acquire Infrastructure]]) or was otherwise compromised by them ([[kb/mitre/attack/techniques/T1584-Compromise_Infrastructure\|Compromise Infrastructure]]). Capabilities may also be staged on web services, such as GitHub or Pastebin, or on Platform-as-a-Service (PaaS) offerings that enable users to easily provision applications.[^3] [^6] [^1] [^11] [^7] <br><br>Staging of capabilities can aid the adversary in a number of initial access and post-compromise behaviors, including (but not limited to):<br><br>* Staging web resources necessary to conduct [[kb/mitre/attack/techniques/T1189-Drive-by_Compromise\|Drive-by Compromise]] when a user browses to a site.[^4] [^2] [^8] <br>* Staging web resources for a link target to be used with spearphishing.[^5] [^10] <br>* Uploading malware or tools to a location accessible to a victim network to enable [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|Ingress Tool Transfer]].[^3] <br>* Installing a previously acquired SSL/TLS certificate to use to encrypt command and control traffic (ex: [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|Asymmetric Cryptography]] with [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|Web Protocols]]).[^9] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1608.001-Upload_Malware\|T1608.001]] | Upload Malware |
| [[kb/mitre/attack/techniques/T1608.002-Upload_Tool\|T1608.002]] | Upload Tool |
| [[kb/mitre/attack/techniques/T1608.003-Install_Digital_Certificate\|T1608.003]] | Install Digital Certificate |
| [[kb/mitre/attack/techniques/T1608.004-Drive-by_Target\|T1608.004]] | Drive-by Target |
| [[kb/mitre/attack/techniques/T1608.005-Link_Target\|T1608.005]] | Link Target |
| [[kb/mitre/attack/techniques/T1608.006-SEO_Poisoning\|T1608.006]] | SEO Poisoning |




> [!info]- References
> [^1]: [Malwarebytes Heroku Skimmers](https://www.malwarebytes.com/blog/news/2019/12/theres-an-app-for-that-web-skimmers-found-on-paas-heroku)

> [^2]: [Gallagher 2015](http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/)

> [^3]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)

> [^4]: [FireEye CFR Watering Hole 2012](https://web.archive.org/web/20201024230407/https://www.fireeye.com/blog/threat-research/2012/12/council-foreign-relations-water-hole-attack-details.html)

> [^5]: [Malwarebytes Silent Librarian October 2020](https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/)

> [^6]: [Dragos Heroku Watering Hole](https://www.dragos.com/blog/industry-news/a-new-water-watering-hole/)

> [^7]: [Netskope Cloud Phishing](https://www.netskope.com/blog/a-big-catch-cloud-phishing-from-google-app-engine-and-azure-app-service)

> [^8]: [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)

> [^9]: [DigiCert Install SSL Cert](https://www.digicert.com/kb/ssl-certificate-installation.htm)

> [^10]: [Proofpoint TA407 September 2019](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian)

> [^11]: [Netskope GCP Redirection](https://www.netskope.com/blog/targeted-attacks-abusing-google-cloud-platform-open-redirection)


