---
aliases: 
    - T1614
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1614-System_Location_Discovery
tactic: 
     - Discovery
platforms:
     - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

<br>Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [[kb/mitre/attack/techniques/T1614-System_Location_Discovery\|System Location Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.[^4] [^3] [^6]  Windows API functions such as `GetLocaleInfoW` can also be used to determine the locale of the host.[^4]  In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.[^2] [^1] <br><br>Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.[^8] [^3] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can determine the country a victim host is located in.[^7]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can identify the location of targeted devices.[^5]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1614.001-System_Language_Discovery\|T1614.001]] | System Language Discovery |




> [!info]- References
> [^1]: [Microsoft Azure Instance Metadata 2021](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows)

> [^2]: [AWS Instance Identity Documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)

> [^3]: [Sophos Geolocation 2016](https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/)

> [^4]: [FBI Ragnar Locker 2020](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)

> [^5]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^6]: [Bleepingcomputer RAT malware 2020](https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/)

> [^7]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^8]: [Securelist Trasparent Tribe 2020](https://securelist.com/transparent-tribe-part-1/98127/)


