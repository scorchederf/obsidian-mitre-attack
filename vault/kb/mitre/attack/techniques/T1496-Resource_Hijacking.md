---
aliases: 
    - T1496
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/impact
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1496-Resource_Hijacking
tactic: 
     - Impact
platforms:
     - Windows - IaaS - Linux - macOS - Containers - SaaS
permissions required:
     - none
---

## Description

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. <br><br>Resource hijacking may take a number of different forms. For example, adversaries may:<br><br>* Leverage compute resources in order to mine cryptocurrency<br>* Sell network bandwidth to proxy networks<br>* Generate SMS traffic for profit<br>* Abuse cloud-based messaging services to send large quantities of spam messages<br><br>In some cases, adversaries may leverage multiple types of Resource Hijacking at once.[^1] 






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1496.001-Compute_Hijacking\|T1496.001]] | Compute Hijacking |
| [[kb/mitre/attack/techniques/T1496.002-Bandwidth_Hijacking\|T1496.002]] | Bandwidth Hijacking |
| [[kb/mitre/attack/techniques/T1496.003-SMS_Pumping\|T1496.003]] | SMS Pumping |
| [[kb/mitre/attack/techniques/T1496.004-Cloud_Service_Hijacking\|T1496.004]] | Cloud Service Hijacking |




> [!info]- References
> [^1]: [Sysdig Cryptojacking Proxyjacking 2023](https://sysdig.com/blog/labrat-cryptojacking-proxyjacking-campaign/)


