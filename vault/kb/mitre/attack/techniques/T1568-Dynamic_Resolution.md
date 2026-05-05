---
aliases: 
    - T1568
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1568-Dynamic_Resolution
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.<br><br>Adversaries may use dynamic resolution for the purpose of [[kb/mitre/attack/techniques/T1008-Fallback_Channels\|Fallback Channels]]. When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.[^7] [^2] [^5] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has used dynamic DNS domains in C2 communications.[^8]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can be configured to use dynamic DNS.[^6]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | In some cases a local DNS sinkhole may be used to help prevent behaviors associated with dynamic resolution. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Malware researchers can reverse engineer malware variants that use dynamic resolution and determine future C2 infrastructure that the malware will attempt to contact, but this is a time and resource intensive effort.[^1] [^4]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1568.001-Fast_Flux_DNS\|T1568.001]] | Fast Flux DNS |
| [[kb/mitre/attack/techniques/T1568.002-Domain_Generation_Algorithms\|T1568.002]] | Domain Generation Algorithms |
| [[kb/mitre/attack/techniques/T1568.003-DNS_Calculation\|T1568.003]] | DNS Calculation |




> [!info]- References
> [^1]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)

> [^2]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)

> [^3]: [Data Driven Security DGA](https://datadrivensecurity.info/blog/posts/2014/Oct/dga-part2/)

> [^4]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)

> [^5]: [ESET Sednit 2017 Activity](https://www.welivesecurity.com/2017/12/21/sednit-update-fancy-bear-spent-year/)

> [^6]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)

> [^7]: [Talos CCleanup 2017](http://blog.talosintelligence.com/2017/09/avast-distributes-malware.html)

> [^8]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


