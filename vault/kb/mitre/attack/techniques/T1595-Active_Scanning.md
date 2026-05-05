---
aliases: 
    - T1595
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1595-Active_Scanning
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.<br><br>Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP.[^1] [^2]  Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]] or [[kb/mitre/attack/techniques/T1596-Search_Open_Technical_Databases\|Search Open Technical Databases]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1587-Develop_Capabilities\|Develop Capabilities]] or [[kb/mitre/attack/techniques/T1588-Obtain_Capabilities\|Obtain Capabilities]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]] or [[kb/mitre/attack/techniques/T1190-Exploit_Public-Facing_Application\|Exploit Public-Facing Application]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1595.001-Scanning_IP_Blocks\|T1595.001]] | Scanning IP Blocks |
| [[kb/mitre/attack/techniques/T1595.002-Vulnerability_Scanning\|T1595.002]] | Vulnerability Scanning |
| [[kb/mitre/attack/techniques/T1595.003-Wordlist_Scanning\|T1595.003]] | Wordlist Scanning |




> [!info]- References
> [^1]: [Botnet Scan](https://www.caida.org/publications/papers/2012/analysis_slash_zero/analysis_slash_zero.pdf)

> [^2]: [OWASP Fingerprinting](https://wiki.owasp.org/index.php/OAT-004_Fingerprinting)


