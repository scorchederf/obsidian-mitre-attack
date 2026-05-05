---
aliases: 
    - T1543
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/containers
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1543-Create_or_Modify_System_Process
tactic: 
     - Persistence - Privilege Escalation
platforms:
     - Containers - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may create or modify system-level processes to repeatedly execute malicious payloads as part of persistence. When operating systems boot up, they can start processes that perform background system functions. On Windows and Linux, these system processes are referred to as services.[^3]  On macOS, launchd processes known as [[kb/mitre/attack/techniques/T1543.004-Launch_Daemon\|Launch Daemon]] and [[kb/mitre/attack/techniques/T1543.001-Launch_Agent\|Launch Agent]] are run to finish system initialization and load user specific parameters.[^5]  <br><br>Adversaries may install new services, daemons, or agents that can be configured to execute at startup or a repeatable interval in order to establish persistence. Similarly, adversaries may modify existing services, daemons, or agents to achieve the same effect.  <br><br>Services, daemons, or agents may be created with administrator privileges but executed under root/SYSTEM privileges. Adversaries may leverage this functionality to create or modify system processes in order to escalate privileges.[^4]   




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with system-level process changes and service configurations. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Restrict read/write access to system-level process files to only select privileged users who have a legitimate need to manage system services. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Ensure that Driver Signature Enforcement is enabled to restrict unsigned drivers from being installed.  |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent an application from writing a signed vulnerable driver to the system.[^2]  On Windows 10 and 11, enable Microsoft Vulnerable Driver Blocklist to assist in hardening against third party-developed drivers.[^1]    |
| [[kb/mitre/attack/mitigations/M1045-Code_Signing\|M1045]] | Code Signing | Enforce registration and execution of only legitimately signed service drivers where possible. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Where possible, consider enforcing the use of container services in rootless mode to limit the possibility of privilege escalation or malicious effects on the host running the container. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1543.001-Launch_Agent\|T1543.001]] | Launch Agent |
| [[kb/mitre/attack/techniques/T1543.002-Systemd_Service\|T1543.002]] | Systemd Service |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service |
| [[kb/mitre/attack/techniques/T1543.004-Launch_Daemon\|T1543.004]] | Launch Daemon |
| [[kb/mitre/attack/techniques/T1543.005-Container_Service\|T1543.005]] | Container Service |




> [!info]- References
> [^1]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)

> [^2]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)

> [^3]: [TechNet Services](https://technet.microsoft.com/en-us/library/cc772408.aspx)

> [^4]: [OSX Malware Detection](https://papers.put.as/papers/macosx/2016/RSA_OSX_Malware.pdf)

> [^5]: [AppleDocs Launch Agent Daemons](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)


