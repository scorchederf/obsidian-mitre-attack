---
aliases: 
    - T1682
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1682-Query_Public_AI_Services
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]]), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for [[kb/mitre/attack/techniques/T1684-Social_Engineering\|Social Engineering]] approaches, identifying contact information for use in [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]] or [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]], or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion.[^2] [^1] <br><br>Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources (i.e., [[kb/mitre/attack/techniques/T1683-Generate_Content\|Generate Content]] or [[kb/mitre/attack/techniques/T1585-Establish_Accounts\|Establish Accounts]]. For obtaining access to AI tools and services, see [[kb/mitre/attack/techniques/T1588.007-Artificial_Intelligence\|Artificial Intelligence]].




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators. |






> [!info]- References
> [^1]: [GTIG AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)

> [^2]: [MSFT-AI](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)


