---
aliases: 
    - T1113
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1113-Screen_Capture
tactic: 
     - Collection
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as `CopyFromScreen`, `xwd`, or `screencapture`.[^16] [^1] <br>


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.[^10]  |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-TimedScreenshot` Exfiltration module can take screenshots at regular intervals.[^13] [^3]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] takes automated screenshots of the infected machine.[^6] [^4]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] is capable of capturing screenshots on Windows and macOS systems.[^9]  |
| [[kb/mitre/attack/software/S0591-ConnectWise\|S0591]] | ConnectWise | [[kb/mitre/attack/software/S0591-ConnectWise\|ConnectWise]] can take screenshots on remote hosts.[^2]  |
| [[kb/mitre/attack/software/S0592-RemoteUtilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-RemoteUtilities\|RemoteUtilities]] can take screenshots on a compromised host.[^15]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can take screenshots of the victim’s active display.[^14]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can take a screenshot of the current desktop.[^7]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can take screen shots of a compromised machine.[^8]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can take screenshots on compromised hosts.[^5]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to view the screen on compromised hosts.[^12]  |
| [[kb/mitre/attack/software/S1209-Quick_Assist\|S1209]] | Quick Assist | [[kb/mitre/attack/software/S1209-Quick_Assist\|Quick Assist]] allows for the remote administrator to take screenshots of the running system.[^11]  |








> [!info]- References
> [^1]: [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)

> [^2]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)

> [^3]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^4]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^5]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^6]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)

> [^7]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^8]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^9]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^10]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^11]: [Microsoft Quick Assist 2024](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)

> [^12]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)

> [^13]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)

> [^14]: [GitHub Sliver Screen](https://github.com/BishopFox/sliver/blob/master/implant/sliver/screen/screenshot_windows.go)

> [^15]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)

> [^16]: [CopyFromScreen .NET](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen?view=netframework-4.8)


