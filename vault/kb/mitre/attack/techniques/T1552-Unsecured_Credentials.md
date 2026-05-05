---
aliases: 
    - T1552
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1552-Unsecured_Credentials
tactic: 
     - Credential Access
platforms:
     - Windows - SaaS - IaaS - Linux - macOS - Containers - Network Devices - Office Suite - Identity Provider
permissions required:
     - none
---

## Description

Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [[kb/mitre/attack/techniques/T1552.003-Shell_History\|Shell History]]), operating system or application-specific repositories (e.g. [[kb/mitre/attack/techniques/T1552.002-Credentials_in_Registry\|Credentials in Registry]]),  or other specialized files/artifacts (e.g. [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|Private Keys]]).[^3] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.[^7]  |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] captures credentials by recording them through an alternative network listener registered to the `mpnotify.exe` process, allowing for cleartext recording of logon information.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-Active_Directory_Configuration\|M1015]] | Active Directory Configuration | Remove vulnerable Group Policy Preferences.[^2]  |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint systems or servers. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Restrict file shares to specific directories with access only to necessary users. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | If it is necessary that software must store credentials in the Registry, then ensure the associated accounts have limited permissions so they cannot be abused if obtained by an adversary. |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Use strong passphrases for private keys to make cracking difficult. Do not store credentials within the Registry. Establish an organizational policy that prohibits password storage in files. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | There are multiple methods of preventing a user's command history from being flushed to their .bash_history file, including use of the following commands:<br>`set +o history` and `set -o history` to start logging again;<br>`unset HISTFILE` being added to a user's .bash_rc file; and<br>`ln -s /dev/null ~/.bash_history` to write commands to `/dev/null`instead. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit network access to sensitive services, such as the Instance Metadata API. |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Limit access to the Instance Metadata API. A properly configured Web Application Firewall (WAF) may help prevent external adversaries from exploiting Server-side Request Forgery (SSRF) attacks that allow access to the Cloud Instance Metadata API.[^5]  |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | When possible, store keys on separate cryptographic hardware instead of on the local system.  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Preemptively search for files containing passwords or other credentials and take actions to reduce the exposure risk when found. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Apply patch KB2962486 which prevents credentials from being stored in GPPs.[^6] [^1]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files |
| [[kb/mitre/attack/techniques/T1552.002-Credentials_in_Registry\|T1552.002]] | Credentials in Registry |
| [[kb/mitre/attack/techniques/T1552.003-Shell_History\|T1552.003]] | Shell History |
| [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|T1552.004]] | Private Keys |
| [[kb/mitre/attack/techniques/T1552.005-Cloud_Instance_Metadata_API\|T1552.005]] | Cloud Instance Metadata API |
| [[kb/mitre/attack/techniques/T1552.006-Group_Policy_Preferences\|T1552.006]] | Group Policy Preferences |
| [[kb/mitre/attack/techniques/T1552.007-Container_API\|T1552.007]] | Container API |
| [[kb/mitre/attack/techniques/T1552.008-Chat_Messages\|T1552.008]] | Chat Messages |




> [!info]- References
> [^1]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)

> [^2]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)

> [^3]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)

> [^4]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)

> [^5]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)

> [^6]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)

> [^7]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)


