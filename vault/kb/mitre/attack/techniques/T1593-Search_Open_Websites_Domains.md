---
aliases: 
    - T1593
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts.[^1] [^2] [^3] <br><br>Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]] or [[kb/mitre/attack/techniques/T1596-Search_Open_Technical_Databases\|Search Open Technical Databases]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1585-Establish_Accounts\|Establish Accounts]] or [[kb/mitre/attack/techniques/T1586-Compromise_Accounts\|Compromise Accounts]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]] or [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Application developers uploading to public code repositories should be careful to avoid publishing sensitive information such as credentials and API keys. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Scan public code repositories for exposed credentials or other sensitive information before making commits. Ensure that any leaked credentials are removed from the commit history, not just the current latest version of the code. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1593.001-Social_Media\|T1593.001]] | Social Media |
| [[kb/mitre/attack/techniques/T1593.002-Search_Engines\|T1593.002]] | Search Engines |
| [[kb/mitre/attack/techniques/T1593.003-Code_Repositories\|T1593.003]] | Code Repositories |




> [!info]- References
> [^1]: [Cyware Social Media](https://cyware.com/news/how-hackers-exploit-social-media-to-break-into-your-company-88e8da8e)

> [^2]: [SecurityTrails Google Hacking](https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks)

> [^3]: [ExploitDB GoogleHacking](https://www.exploit-db.com/google-hacking-database)


