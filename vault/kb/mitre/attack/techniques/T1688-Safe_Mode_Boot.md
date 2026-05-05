---
aliases: 
    - T1688
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1688-Safe_Mode_Boot
tactic: 
     - Defense Impairment
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating system with a limited set of drivers and services. Third-party security software such as endpoint detection and response (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode with Networking. It is possible to start additional services after a safe mode boot.[^6] [^1] <br><br>Adversaries may abuse safe mode to disable endpoint defenses that may not start with a limited boot. Hosts can be forced into safe mode after the next reboot via modifications to Boot Configuration Data (BCD) stores, which are files that manage boot application settings.[^3] <br><br>Adversaries may also add their malicious applications to the list of minimal services that start in safe mode by modifying relevant Registry values (i.e. [[kb/mitre/attack/techniques/T1112-Modify_Registry\|Modify Registry]]). Malicious [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|Component Object Model]] (COM) objects may also be registered and loaded in safe mode.[^2] [^5] [^4] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles, that may be abused to remotely boot a machine in safe mode.[^2]  |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Ensure that endpoint defenses run in safe mode.[^2]  |






> [!info]- References
> [^1]: [Sophos Safe Mode Boot](https://www.sophos.com/en-us/blog/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection)

> [^2]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)

> [^3]: [Microsoft bcdedit](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit)

> [^4]: [BleepingComputer REvil 2021](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/)

> [^5]: [Cybereason safe mode boot](https://www.cybereason.com/blog/research/medusalocker-ransomware)

> [^6]: [Microsoft Windows Startup Settings](https://support.microsoft.com/en-us/windows/windows-startup-settings-1af6ec8c-4d4a-4b23-adb7-e76eef0b847f)


