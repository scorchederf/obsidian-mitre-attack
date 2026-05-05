---
aliases: 
    - S0552
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0552-AdFind
---

## Description

[[kb/mitre/attack/software/S0552-AdFind\|AdFind]] is a free command-line query tool that can be used for gathering information from Active Directory.[^4] [^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can extract subnet information from Active Directory.[^4] [^1] [^2]  |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] has the ability to query Active Directory for computers.[^4] [^1] [^2] [^3]  |
| [[kb/mitre/attack/techniques/T1069.002-Domain_Groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can enumerate domain groups.[^4] [^1] [^2] [^5]  |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can enumerate domain users.[^4] [^1] [^2] [^3] [^5]  |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can gather information about organizational units (OUs) and domain trusts from Active Directory.[^4] [^1] [^2] [^5]  |





> [!info]- References
> [^1]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)

> [^2]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)

> [^3]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)

> [^4]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)

> [^5]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


