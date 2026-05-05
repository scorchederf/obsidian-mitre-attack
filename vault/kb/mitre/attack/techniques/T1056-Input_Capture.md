---
aliases: 
    - T1056
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/collection
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1056-Input_Capture
tactic: 
     - Collection - Credential Access
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [[kb/mitre/attack/techniques/T1056.004-Credential_API_Hooking\|Credential API Hooking]]) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [[kb/mitre/attack/techniques/T1056.003-Web_Portal_Capture\|Web Portal Capture]]).


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.[^2]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging |
| [[kb/mitre/attack/techniques/T1056.002-GUI_Input_Capture\|T1056.002]] | GUI Input Capture |
| [[kb/mitre/attack/techniques/T1056.003-Web_Portal_Capture\|T1056.003]] | Web Portal Capture |
| [[kb/mitre/attack/techniques/T1056.004-Credential_API_Hooking\|T1056.004]] | Credential API Hooking |




> [!info]- References
> [^1]: [Adventures of a Keystroke](http://opensecuritytraining.info/Keylogging_files/The%20Adventures%20of%20a%20Keystroke.pdf)

> [^2]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)


