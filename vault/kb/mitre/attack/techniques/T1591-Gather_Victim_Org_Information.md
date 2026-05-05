---
aliases: 
    - T1591
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1591-Gather_Victim_Org_Information
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.<br><br>Adversaries may gather this information in various ways, such as direct elicitation via [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]]. Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1593.001-Social_Media\|Social Media]] or [[kb/mitre/attack/techniques/T1594-Search_Victim-Owned_Websites\|Search Victim-Owned Websites]]).[^2] [^1]  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]] or [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1585-Establish_Accounts\|Establish Accounts]] or [[kb/mitre/attack/techniques/T1586-Compromise_Accounts\|Compromise Accounts]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]] or [[kb/mitre/attack/techniques/T1199-Trusted_Relationship\|Trusted Relationship]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1591.001-Determine_Physical_Locations\|T1591.001]] | Determine Physical Locations |
| [[kb/mitre/attack/techniques/T1591.002-Business_Relationships\|T1591.002]] | Business Relationships |
| [[kb/mitre/attack/techniques/T1591.003-Identify_Business_Tempo\|T1591.003]] | Identify Business Tempo |
| [[kb/mitre/attack/techniques/T1591.004-Identify_Roles\|T1591.004]] | Identify Roles |




> [!info]- References
> [^1]: [SEC EDGAR Search](https://www.sec.gov/edgar/search/)

> [^2]: [ThreatPost Broadvoice Leak](https://threatpost.com/broadvoice-leaks-350m-records-voicemail-transcripts/160158/)


