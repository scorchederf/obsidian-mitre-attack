---
aliases: 
    - T1014
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1014-Rootkit
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. [^5]  <br><br>Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [[kb/mitre/attack/techniques/T1542.001-System_Firmware\|System Firmware]]. [^1]  Rootkits have been seen for Windows, Linux, and Mac OS X systems. [^3]  [^4] <br><br>Rootkits that reside or modify boot sectors are known as [[kb/mitre/attack/techniques/T1542.003-Bootkit\|Bootkit]]s and specifically target the boot process of the operating system.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0040-HTRAN\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can install a rootkit to hide network connections from the host OS.[^2]  |








> [!info]- References
> [^1]: [Wikipedia Rootkit](https://en.wikipedia.org/wiki/Rootkit)

> [^2]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)

> [^3]: [CrowdStrike Linux Rootkit](https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/)

> [^4]: [BlackHat Mac OSX Rootkit](http://www.blackhat.com/docs/asia-14/materials/Tsai/WP-Asia-14-Tsai-You-Cant-See-Me-A-Mac-OS-X-Rootkit-Uses-The-Tricks-You-Havent-Known-Yet.pdf)

> [^5]: [Symantec Windows Rootkits](https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf)


