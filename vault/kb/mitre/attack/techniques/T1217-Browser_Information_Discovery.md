---
aliases: 
    - T1217
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1217-Browser_Information_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.[^3] <br><br>Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|Credentials In Files]] associated with logins cached by a browser.<br><br>Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).[^2] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to gather browser data such as bookmarks and visited sites.[^1]  |








> [!info]- References
> [^1]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^2]: [Chrome Roaming Profiles](https://support.google.com/chrome/a/answer/7349337)

> [^3]: [Kaspersky Autofill](https://www.kaspersky.com/blog/browser-data-theft/27871/)


