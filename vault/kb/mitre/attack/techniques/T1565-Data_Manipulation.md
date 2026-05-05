---
aliases: 
    - T1565
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1565-Data_Manipulation
tactic: 
     - Impact
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, thus threatening the integrity of the data.[^2]  By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.<br><br>The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Ensure least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. |
| [[kb/mitre/attack/mitigations/M1029-Remote_Data_Storage\|M1029]] | Remote Data Storage | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Identify critical business and system processes that may be targeted by adversaries and work to isolate and secure those systems against unauthorized access and tampering. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Consider encrypting important information to reduce an adversary’s ability to perform tailored data modifications. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1565.001-Stored_Data_Manipulation\|T1565.001]] | Stored Data Manipulation |
| [[kb/mitre/attack/techniques/T1565.002-Transmitted_Data_Manipulation\|T1565.002]] | Transmitted Data Manipulation |
| [[kb/mitre/attack/techniques/T1565.003-Runtime_Data_Manipulation\|T1565.003]] | Runtime Data Manipulation |




> [!info]- References
> [^1]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)

> [^2]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


