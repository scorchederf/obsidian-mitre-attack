---
aliases: 
    - T1069
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1069-Permission_Groups_Discovery
tactic: 
     - Discovery
platforms:
     - Containers - IaaS - Identity Provider - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.<br><br>Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.[^3] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the local privileges for the infected host.[^1]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1069.001-Local_Groups\|T1069.001]] | Local Groups |
| [[kb/mitre/attack/techniques/T1069.002-Domain_Groups\|T1069.002]] | Domain Groups |
| [[kb/mitre/attack/techniques/T1069.003-Cloud_Groups\|T1069.003]] | Cloud Groups |




> [!info]- References
> [^1]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^2]: [K8s Authorization Overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)

> [^3]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)


