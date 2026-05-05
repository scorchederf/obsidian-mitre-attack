---
aliases: 
    - T1529
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1529-System_Shutdown_Reboot
tactic: 
     - Impact
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] (e.g. `reload`).[^4] [^5]  They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.<br><br>Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.<br><br>Adversaries may also use Windows API functions, such as `InitializeSystemShutdownExW` or `ExitWindowsEx`, to force a system to shut down or reboot.[^3] [^2]  Alternatively, the `NtRaiseHardError`or `ZwRaiseHardError` Windows API functions with the `ResponseOption` parameter set to `OptionShutdownSystem` may deliver a “blue screen of death” (BSOD) to a system.[^7] [^8] [^10]  In order to leverage these API functions, an adversary may need to acquire `SeShutdownPrivilege` (e.g., via [[kb/mitre/attack/techniques/T1134-Access_Token_Manipulation\|Access Token Manipulation]]).[^2] <br> In some cases, the system may not be able to boot again. <br><br>Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [[kb/mitre/attack/techniques/T1561.002-Disk_Structure_Wipe\|Disk Structure Wipe]] or [[kb/mitre/attack/techniques/T1490-Inhibit_System_Recovery\|Inhibit System Recovery]], to hasten the intended effects on system availability.[^9] [^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can shutdown and restart remote devices.[^6]  |








> [!info]- References
> [^1]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)

> [^2]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)

> [^3]: [CrowdStrike Blog](https://www.crowdstrike.com/en-us/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)

> [^4]: [Microsoft Shutdown Oct 2017](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)

> [^5]: [alert_TA18_106A](https://www.cisa.gov/uscert/ncas/alerts/TA18-106A)

> [^6]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^7]: [SonicWall](https://www.sonicwall.com/blog/disarming-darkgate-a-deep-dive-into-thwarting-the-latest-darkgate-variant)

> [^8]: [NtRaiseHardError](https://ntdoc.m417z.com/ntraiseharderror)

> [^9]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)

> [^10]: [NotMe-BSOD](https://github.com/lzcapp/NotMe-BSOD)


