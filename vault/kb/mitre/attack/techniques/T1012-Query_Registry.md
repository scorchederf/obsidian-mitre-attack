---
aliases: 
    - T1012
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1012-Query_Registry
tactic: 
     - Discovery
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.<br><br>The Registry contains a significant amount of information about the operating system, configuration, software, and security.[^6]  Information can easily be queried using the [[kb/mitre/attack/software/S0075-Reg\|Reg]] utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [[kb/mitre/attack/techniques/T1012-Query_Registry\|Query Registry]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0075-Reg\|S0075]] | Reg | [[kb/mitre/attack/software/S0075-Reg\|Reg]] may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.[^3]  |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.[^7] [^1]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can obtain Registry data from targeted systems.[^2]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.[^4]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can search the registry files of a compromised host.[^5]  |








> [!info]- References
> [^1]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^2]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^3]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)

> [^4]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^5]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^6]: [Wikipedia Windows Registry](https://en.wikipedia.org/wiki/Windows_Registry)

> [^7]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


