---
aliases: 
    - T1098
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
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
mitre-attack: kb/mitre/attack/techniques/T1098-Account_Manipulation
tactic: 
     - Persistence - Privilege Escalation
platforms:
     - Containers - ESXi - IaaS - Identity Provider - Linux - macOS - Network Devices - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.[^5]  These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. <br><br>In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]].


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-Mimikatz\|S0002]] | Mimikatz | The [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The `LSADUMP::ChangeNTLM` and `LSADUMP::SetNTLM` modules can also manipulate the password hash of an account without knowing the clear text value.[^7] [^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Ensure that low-privileged user accounts do not have permissions to modify accounts or account-related policies. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Restrict access to potentially sensitive files that deal with authentication and/or authorization. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Protect domain controllers by ensuring proper security configuration for critical servers to limit access by potentially unnecessary protocols and services, such as SMB file sharing. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Remove unnecessary and potentially abusable authentication and authorization mechanisms where possible. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1098.001-Additional_Cloud_Credentials\|T1098.001]] | Additional Cloud Credentials |
| [[kb/mitre/attack/techniques/T1098.002-Additional_Email_Delegate_Permissions\|T1098.002]] | Additional Email Delegate Permissions |
| [[kb/mitre/attack/techniques/T1098.003-Additional_Cloud_Roles\|T1098.003]] | Additional Cloud Roles |
| [[kb/mitre/attack/techniques/T1098.004-SSH_Authorized_Keys\|T1098.004]] | SSH Authorized Keys |
| [[kb/mitre/attack/techniques/T1098.005-Device_Registration\|T1098.005]] | Device Registration |
| [[kb/mitre/attack/techniques/T1098.006-Additional_Container_Cluster_Roles\|T1098.006]] | Additional Container Cluster Roles |
| [[kb/mitre/attack/techniques/T1098.007-Additional_Local_or_Domain_Groups\|T1098.007]] | Additional Local or Domain Groups |




> [!info]- References
> [^1]: [Microsoft User Modified Event](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738)

> [^2]: [Microsoft Security Event 4670](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4670)

> [^3]: [Metcalf 2015](http://adsecurity.org/?p=1275)

> [^4]: [GitHub Mimikatz Issue 92 June 2017](https://github.com/gentilkiwi/mimikatz/issues/92)

> [^5]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)

> [^6]: [InsiderThreat ChangeNTLM July 2017](https://blog.stealthbits.com/manipulating-user-passwords-with-mimikatz-SetNTLM-ChangeNTLM)

> [^7]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)


