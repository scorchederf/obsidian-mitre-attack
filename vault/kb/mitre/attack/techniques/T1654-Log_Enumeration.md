---
aliases: 
    - T1654
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1654-Log_Enumeration
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records ([[kb/mitre/attack/techniques/T1087-Account_Discovery\|Account Discovery]]), security or vulnerable software ([[kb/mitre/attack/techniques/T1518-Software_Discovery\|Software Discovery]]), or hosts within a compromised network ([[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|Remote System Discovery]]).<br><br>Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] on Windows to access and/or export security event information.[^2] [^5]  In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.[^3] <br><br>Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.<br><br>In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.[^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can collect CloudTrail event histories and CloudWatch logs.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit the ability to access and export sensitive logs to privileged accounts where possible. |






> [!info]- References
> [^1]: [Permiso GUI-Vil 2023](https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/)

> [^2]: [WithSecure Lazarus-NoPineapple Threat Intel Report 2023](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf)

> [^3]: [SIM Swapping and Abuse of the Microsoft Azure Serial Console](https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial)

> [^4]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)

> [^5]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


