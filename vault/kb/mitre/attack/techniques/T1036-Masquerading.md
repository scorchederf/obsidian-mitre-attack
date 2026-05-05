---
aliases: 
    - T1036
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1036-Masquerading
tactic: 
     - Stealth
platforms:
     - Containers - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.<br><br>Renaming abusable system utilities to evade security monitoring is also a form of [[kb/mitre/attack/techniques/T1036-Masquerading\|Masquerading]].[^1] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train users not to open email attachments or click unknown links (URLs). Such training fosters more secure habits within your organization and will limit many of the risks.   |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Consider defining and enforcing a naming convention for user accounts to more easily spot generic account names that do not fit the typical schema. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Use file system access controls to protect folders such as C:\\Windows\\System32. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | Implement security controls on the endpoint, such as a Host Intrusion Prevention System (HIPS), to identify and prevent execution of potentially malicious files (such as those with mismatching file signatures). |
| [[kb/mitre/attack/mitigations/M1045-Code_Signing\|M1045]] | Code Signing | Require signed binaries. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Audit user accounts to ensure that each one has a defined purpose. |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically quarantine suspicious files. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1036.001-Invalid_Code_Signature\|T1036.001]] | Invalid Code Signature |
| [[kb/mitre/attack/techniques/T1036.002-Right-to-Left_Override\|T1036.002]] | Right-to-Left Override |
| [[kb/mitre/attack/techniques/T1036.003-Rename_Legitimate_Utilities\|T1036.003]] | Rename Legitimate Utilities |
| [[kb/mitre/attack/techniques/T1036.004-Masquerade_Task_or_Service\|T1036.004]] | Masquerade Task or Service |
| [[kb/mitre/attack/techniques/T1036.005-Match_Legitimate_Resource_Name_or_Location\|T1036.005]] | Match Legitimate Resource Name or Location |
| [[kb/mitre/attack/techniques/T1036.006-Space_after_Filename\|T1036.006]] | Space after Filename |
| [[kb/mitre/attack/techniques/T1036.007-Double_File_Extension\|T1036.007]] | Double File Extension |
| [[kb/mitre/attack/techniques/T1036.008-Masquerade_File_Type\|T1036.008]] | Masquerade File Type |
| [[kb/mitre/attack/techniques/T1036.009-Break_Process_Trees\|T1036.009]] | Break Process Trees |
| [[kb/mitre/attack/techniques/T1036.010-Masquerade_Account_Name\|T1036.010]] | Masquerade Account Name |
| [[kb/mitre/attack/techniques/T1036.011-Overwrite_Process_Arguments\|T1036.011]] | Overwrite Process Arguments |
| [[kb/mitre/attack/techniques/T1036.012-Browser_Fingerprint\|T1036.012]] | Browser Fingerprint |




> [!info]- References
> [^1]: [LOLBAS Main Site](https://lolbas-project.github.io/)


