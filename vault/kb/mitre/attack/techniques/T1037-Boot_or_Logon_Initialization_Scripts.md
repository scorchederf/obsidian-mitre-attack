---
aliases: 
    - T1037
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1037-Boot_or_Logon_Initialization_Scripts
tactic: 
     - Persistence - Privilege Escalation
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.[^2] [^1]  Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  <br><br>Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. <br><br>An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Restrict write access to logon scripts to specific administrators. |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1037.001-Logon_Script_Windows\|T1037.001]] | Logon Script (Windows) |
| [[kb/mitre/attack/techniques/T1037.002-Login_Hook\|T1037.002]] | Login Hook |
| [[kb/mitre/attack/techniques/T1037.003-Network_Logon_Script\|T1037.003]] | Network Logon Script |
| [[kb/mitre/attack/techniques/T1037.004-RC_Scripts\|T1037.004]] | RC Scripts |
| [[kb/mitre/attack/techniques/T1037.005-Startup_Items\|T1037.005]] | Startup Items |




> [!info]- References
> [^1]: [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)

> [^2]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


