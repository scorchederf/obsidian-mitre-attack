---
aliases: 
    - T1683
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1683-Generate_Content
tactic: 
     - Resource Development
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support [[kb/mitre/attack/techniques/T1684-Social_Engineering\|Social Engineering]], fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective.[^1] <br><br>Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., [[kb/mitre/attack/techniques/T1682-Query_Public_AI_Services\|Query Public AI Services]]); for obtaining access to AI tools used in content generation, see [[kb/mitre/attack/techniques/T1588.007-Artificial_Intelligence\|Artificial Intelligence]]. <br><br>Content may be leveraged in support of techniques such as [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]], [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]], [[kb/mitre/attack/techniques/T1684-Social_Engineering\|Social Engineering]], [[kb/mitre/attack/techniques/T1657-Financial_Theft\|Financial Theft]], or [[kb/mitre/attack/techniques/T1585-Establish_Accounts\|Establish Accounts]]. Generated or developed content does not include malicious code or scripts (i.e., [[kb/mitre/attack/techniques/T1587-Develop_Capabilities\|Develop Capabilities]] and [[kb/mitre/attack/techniques/T1588.007-Artificial_Intelligence\|Artificial Intelligence]]).




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators.  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1683.001-Written_Content\|T1683.001]] | Written Content |
| [[kb/mitre/attack/techniques/T1683.002-Audio-Visual_Content\|T1683.002]] | Audio-Visual Content |




> [!info]- References
> [^1]: [IBM AI-Generated Content](https://www.ibm.com/think/insights/ai-generated-content)


