---
aliases: 
    - T1074
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/collection
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1074-Data_Staged
tactic: 
     - Collection
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[kb/mitre/attack/techniques/T1560-Archive_Collected_Data\|Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[kb/mitre/attack/software/S0106-cmd\|cmd]] and bash may be used to copy data into a staging location.[^2] <br><br>In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[kb/mitre/attack/techniques/T1578.002-Create_Cloud_Instance\|Create Cloud Instance]] and stage data in that instance.[^1] <br><br>Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1074.001-Local_Data_Staging\|T1074.001]] | Local Data Staging |
| [[kb/mitre/attack/techniques/T1074.002-Remote_Data_Staging\|T1074.002]] | Remote Data Staging |




> [!info]- References
> [^1]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)

> [^2]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)


