---
aliases: 
    - T1653
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1653-Power_Settings
tactic: 
     - Persistence
platforms:
     - Windows - Linux - macOS - Network Devices
permissions required:
     - none
---

## Description

Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity.[^1] <br><br>Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering a state, such as standby, that can terminate malicious activity.[^4] [^2] <br><br>For example, `powercfg` controls all configurable power system settings on a Windows system and can be abused to prevent an infected host from locking or shutting down.[^5]  Adversaries may also extend system lock screen timeout settings.[^6]  Other relevant settings, such as disk and hibernate timeout, can be similarly abused to keep the infected machine running even if no user is active.[^7] <br><br>Aware that some malware cannot survive system reboots, adversaries may entirely delete files used to invoke system shut down or reboot.[^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Periodically inspect systems for abnormal and unexpected power settings that may indicate malicious activty. |






> [!info]- References
> [^1]: [Sleep, shut down, hibernate](https://www.avg.com/en/signal/should-you-shut-down-sleep-or-hibernate-your-pc-or-mac-laptop)

> [^2]: [systemdsleep Linux](https://man7.org/linux/man-pages/man5/systemd-sleep.conf.5.html)

> [^3]: [Condi-Botnet-binaries](https://www.fortinet.com/blog/threat-research/condi-ddos-botnet-spreads-via-tp-links-cve-2023-1389)

> [^4]: [Microsoft: Powercfg command-line options](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options?adlt=strict)

> [^5]: [Two New Monero Malware Attacks Target Windows and Android Users](https://securityintelligence.com/news/two-new-monero-malware-attacks-target-windows-and-android-users/)

> [^6]: [BATLOADER: The Evasive Downloader Malware](https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html)

> [^7]: [CoinLoader: A Sophisticated Malware Loader Campaign](https://www.avira.com/en/blog/coinloader-a-sophisticated-malware-loader-campaign)


