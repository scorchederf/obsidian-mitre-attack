---
aliases: 
    - T1136
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1136-Create_Account
tactic: 
     - Persistence
platforms:
     - Windows - IaaS - Linux - macOS - Network Devices - Containers - SaaS - Office Suite - Identity Provider - ESXi
permissions required:
     - none
---

## Description

Adversaries may create an account to maintain access to victim systems.[^2]  With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.<br><br>Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Limit the number of accounts with permissions to create other accounts. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Protect domain controllers by ensuring proper security configuration for critical servers. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Configure access controls and firewalls to limit access to domain controllers and systems used to create and manage accounts. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1136.001-Local_Account\|T1136.001]] | Local Account |
| [[kb/mitre/attack/techniques/T1136.002-Domain_Account\|T1136.002]] | Domain Account |
| [[kb/mitre/attack/techniques/T1136.003-Cloud_Account\|T1136.003]] | Cloud Account |




> [!info]- References
> [^1]: [Microsoft User Creation Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)

> [^2]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


