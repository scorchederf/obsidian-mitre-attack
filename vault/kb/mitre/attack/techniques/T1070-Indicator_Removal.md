---
aliases: 
    - T1070
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1070-Indicator_Removal
tactic: 
     - Stealth
platforms:
     - Containers - ESXi - Linux - macOS - Network Devices - Office Suite - Windows
permissions required:
     - none
---

## Description

Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.<br><br>Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.<br><br>These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can clean saved cookies and logins from the web browser.[^2]  |
| [[kb/mitre/attack/software/S0527-CSPY_Downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-CSPY_Downloader\|CSPY Downloader]] has the ability to remove values it writes to the Registry.[^4]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can remove artifacts from the compromised host, including created Registry keys.[^3]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can erase file references to payloads in-memory after being reflectively loaded and executed.[^1]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[kb/mitre/attack/mitigations/M1029-Remote_Data_Storage\|M1029]] | Remote Data Storage | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.  |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1070.003-Clear_Command_History\|T1070.003]] | Clear Command History |
| [[kb/mitre/attack/techniques/T1070.004-File_Deletion\|T1070.004]] | File Deletion |
| [[kb/mitre/attack/techniques/T1070.005-Network_Share_Connection_Removal\|T1070.005]] | Network Share Connection Removal |
| [[kb/mitre/attack/techniques/T1070.006-Timestomp\|T1070.006]] | Timestomp |
| [[kb/mitre/attack/techniques/T1070.007-Clear_Network_Connection_History_and_Configurations\|T1070.007]] | Clear Network Connection History and Configurations |
| [[kb/mitre/attack/techniques/T1070.008-Clear_Mailbox_Data\|T1070.008]] | Clear Mailbox Data |
| [[kb/mitre/attack/techniques/T1070.009-Clear_Persistence\|T1070.009]] | Clear Persistence |
| [[kb/mitre/attack/techniques/T1070.010-Relocate_Malware\|T1070.010]] | Relocate Malware |




> [!info]- References
> [^1]: [Donut Github](https://github.com/TheWover/donut)

> [^2]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^4]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


