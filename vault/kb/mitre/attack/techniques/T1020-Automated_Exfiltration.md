---
aliases: 
    - T1020
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1020-Automated_Exfiltration
tactic: 
     - Exfiltration
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection.[^2]  <br><br>When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|Exfiltration Over C2 Channel]] and [[kb/mitre/attack/techniques/T1048-Exfiltration_Over_Alternative_Protocol\|Exfiltration Over Alternative Protocol]].


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to automatically send collected data back to the threat actors' C2.[^1]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] sent collected system and network information compiled into a report to an adversary-controlled C2.[^3]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1020.001-Traffic_Duplication\|T1020.001]] | Traffic Duplication |




> [!info]- References
> [^1]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^2]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)

> [^3]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


