---
aliases: 
    - T1505
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1505-Server_Software_Component
tactic: 
     - Persistence
platforms:
     - Windows - Linux - macOS - Network Devices - ESXi
permissions required:
     - none
---

## Description

Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications.[^4] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Enforce the principle of least privilege by limiting privileges of user accounts so only authorized accounts can modify and/or add server software components.[^5]  |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Consider using Group Policy to configure and block modifications to service and other critical server parameters in the Registry.[^3]  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Do not allow administrator accounts that have permissions to add component software on these services to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Consider disabling software components from servers when possible to prevent abuse by adversaries.[^2]  |
| [[kb/mitre/attack/mitigations/M1045-Code_Signing\|M1045]] | Code Signing | Ensure all application component binaries are signed by the correct application developers. |
| [[kb/mitre/attack/mitigations/M1046-Boot_Integrity\|M1046]] | Boot Integrity | Enabling secure boot allows validation of software and drivers during initial system boot. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1505.001-SQL_Stored_Procedures\|T1505.001]] | SQL Stored Procedures |
| [[kb/mitre/attack/techniques/T1505.002-Transport_Agent\|T1505.002]] | Transport Agent |
| [[kb/mitre/attack/techniques/T1505.003-Web_Shell\|T1505.003]] | Web Shell |
| [[kb/mitre/attack/techniques/T1505.004-IIS_Components\|T1505.004]] | IIS Components |
| [[kb/mitre/attack/techniques/T1505.005-Terminal_Services_DLL\|T1505.005]] | Terminal Services DLL |
| [[kb/mitre/attack/techniques/T1505.006-vSphere_Installation_Bundles\|T1505.006]] | vSphere Installation Bundles |




> [!info]- References
> [^1]: [US-CERT Alert TA15-314A Web Shells](https://www.us-cert.gov/ncas/alerts/TA15-314A)

> [^2]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)

> [^3]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)

> [^4]: [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)

> [^5]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


