---
aliases: 
    - T1115
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1115-Clipboard_Data
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may collect data stored in the clipboard from users copying information within or between applications. <br><br>For example, on Windows adversaries can access clipboard data by using `clip.exe` or `Get-Clipboard`.[^2] [^8] [^3]  Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [[kb/mitre/attack/techniques/T1565.002-Transmitted_Data_Manipulation\|Transmitted Data Manipulation]]).[^9] <br><br>macOS and Linux also have commands, such as `pbpaste`, to grab clipboard contents.[^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can retrieve the current content of the user clipboard.[^10]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] steals and modifies data from the clipboard.[^5] [^4]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can harvest clipboard data on both Windows and macOS systems.[^7]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.[^6]    |








> [!info]- References
> [^1]: [Operating with EmPyre](https://medium.com/rvrsh3ll/operating-with-empyre-ea764eda3363)

> [^2]: [MSDN Clipboard](https://msdn.microsoft.com/en-us/library/ms649012)

> [^3]: [CISA_AA21_200B](https://www.cisa.gov/uscert/ncas/alerts/aa21-200b)

> [^4]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^5]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^6]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)

> [^7]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^8]: [clip_win_server](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/clip)

> [^9]: [mining_ruby_reversinglabs](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)

> [^10]: [Github Koadic](https://github.com/offsecginger/koadic)


