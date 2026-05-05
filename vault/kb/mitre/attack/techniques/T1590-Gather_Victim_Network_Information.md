---
aliases: 
    - T1590
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1590-Gather_Victim_Network_Information
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.<br><br>Adversaries may gather this information in various ways, such as direct collection actions via [[kb/mitre/attack/techniques/T1595-Active_Scanning\|Active Scanning]] or [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]]. Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1596-Search_Open_Technical_Databases\|Search Open Technical Databases]]).[^1] [^2] [^3]  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1595-Active_Scanning\|Active Scanning]] or [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1583-Acquire_Infrastructure\|Acquire Infrastructure]] or [[kb/mitre/attack/techniques/T1584-Compromise_Infrastructure\|Compromise Infrastructure]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1199-Trusted_Relationship\|Trusted Relationship]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1590.001-Domain_Properties\|T1590.001]] | Domain Properties |
| [[kb/mitre/attack/techniques/T1590.002-DNS\|T1590.002]] | DNS |
| [[kb/mitre/attack/techniques/T1590.003-Network_Trust_Dependencies\|T1590.003]] | Network Trust Dependencies |
| [[kb/mitre/attack/techniques/T1590.004-Network_Topology\|T1590.004]] | Network Topology |
| [[kb/mitre/attack/techniques/T1590.005-IP_Addresses\|T1590.005]] | IP Addresses |
| [[kb/mitre/attack/techniques/T1590.006-Network_Security_Appliances\|T1590.006]] | Network Security Appliances |




> [!info]- References
> [^1]: [WHOIS](https://who.is/)

> [^2]: [DNS Dumpster](https://dnsdumpster.com/)

> [^3]: [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)


