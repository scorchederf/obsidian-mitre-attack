---
aliases: 
    - T1518
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1518-Software_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [[kb/mitre/attack/techniques/T1518-Software_Discovery\|Software Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Such software may be deployed widely across the environment for configuration management or security reasons, such as [[kb/mitre/attack/techniques/T1072-Software_Deployment_Tools\|Software Deployment Tools]], and may allow adversaries broad access to infect devices or move laterally.<br><br>Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|Exploitation for Privilege Escalation]].


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered a list of installed software on the infected host.[^1]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery |
| [[kb/mitre/attack/techniques/T1518.002-Backup_Software_Discovery\|T1518.002]] | Backup Software Discovery |




> [!info]- References
> [^1]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


