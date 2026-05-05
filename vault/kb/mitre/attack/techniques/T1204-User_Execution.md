---
aliases: 
    - T1204
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1204-User_Execution
tactic: 
     - Execution
platforms:
     - Linux - Windows - macOS - IaaS - Containers
permissions required:
     - none
---

## Description

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]].<br><br>While [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[kb/mitre/attack/techniques/T1534-Internal_Spearphishing\|Internal Spearphishing]].<br><br>Adversaries may also deceive users into performing actions such as:<br><br>* Enabling [[kb/mitre/attack/techniques/T1219-Remote_Access_Tools\|Remote Access Tools]], allowing direct control of the system to the adversary<br>* Running malicious JavaScript in their browser, allowing adversaries to [[kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie\|Steal Web Session Cookie]]s[^6] [^1] <br>* Downloading and executing malware for [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]]<br>* Coerceing users to copy, paste, and execute malicious code manually[^2] [^5] <br><br>For example, tech support scams can be facilitated through [[kb/mitre/attack/techniques/T1566-Phishing\|Phishing]], vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [[kb/mitre/attack/techniques/T1219-Remote_Access_Tools\|Remote Access Tools]].[^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity. |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Application control may be able to prevent the running of executables masquerading as other files. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent executable files from running unless they meet a prevalence, age, or trusted list criteria and to prevent Office applications from creating potentially malicious executable content by blocking malicious code from being written to disk. Note: cloud-delivered protection must be enabled to use certain rules. [^4]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1204.001-Malicious_Link\|T1204.001]] | Malicious Link |
| [[kb/mitre/attack/techniques/T1204.002-Malicious_File\|T1204.002]] | Malicious File |
| [[kb/mitre/attack/techniques/T1204.003-Malicious_Image\|T1204.003]] | Malicious Image |
| [[kb/mitre/attack/techniques/T1204.004-Malicious_Copy_and_Paste\|T1204.004]] | Malicious Copy and Paste |
| [[kb/mitre/attack/techniques/T1204.005-Malicious_Library\|T1204.005]] | Malicious Library |




> [!info]- References
> [^1]: [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)

> [^2]: [Reliaquest-execution](https://www.reliaquest.com/blog/new-execution-technique-in-clearfake-campaign/)

> [^3]: [Telephone Attack Delivery](https://www.proofpoint.com/us/blog/threat-insight/caught-beneath-landline-411-telephone-oriented-attack-delivery)

> [^4]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^5]: [proofpoint-selfpwn](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn)

> [^6]: [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)


