---
aliases: 
    - T1010
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1010-Application_Window_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.[^1]  For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|Security Software Discovery]]) to evade.[^5] <br><br>Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]] commands and [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] functions.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | APT-C-36 used a customized version of [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] to monitor browser windows for strings relating to specific Colombian financial institutions.[^2] <br> |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can list all windows on victim systems.[^3]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.[^4]  |








> [!info]- References
> [^1]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)

> [^2]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)

> [^3]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^4]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^5]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


