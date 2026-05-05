---
aliases: 
    - T1124
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1124-System_Time_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or `systemsetup` on macOS.[^12] [^5] [^10]  These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain.[^1] [^3] <br><br>System time information may be gathered in a number of ways, such as with [[kb/mitre/attack/software/S0039-Net\|Net]] on Windows by performing `net time \\hostname` to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using `w32tm /tz`.[^5]  In addition, adversaries can discover device uptime through functions such as `GetTickCount()` to determine how long it has been since the system booted up.[^6] <br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] commands such as `show clock detail` can be used to see the current time configuration.[^15]  On ESXi servers, `esxcli system clock get` can be used for the same purpose.<br><br>In addition, system calls – such as `time()` – have been used to collect the current time on Linux devices.[^7]  On macOS systems, adversaries may use commands such as `systemsetup -gettimezone` or `timeIntervalSinceNow` to gather current time zone information or current date and time.[^2] [^4] <br><br>This information could be useful for performing other techniques, such as executing a file with a [[kb/mitre/attack/techniques/T1053-Scheduled_Task_Job\|Scheduled Task/Job]][^13] , or to discover locality information based on time zone to assist in victim targeting (i.e. [[kb/mitre/attack/techniques/T1614-System_Location_Discovery\|System Location Discovery]]). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time.[^11] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-Net\|S0039]] | Net | The `net time` command can be used in [[kb/mitre/attack/software/S0039-Net\|Net]] to determine the local or remote system time.[^8]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect start time information from a compromised host.[^9]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can check whether the current system hour and day of the week are within operating hours defined it its configuration.[^14]  |








> [!info]- References
> [^1]: [Mac Time Sync](https://www.macinstruct.com/tutorials/synchronize-your-macs-clock-with-a-time-server/)

> [^2]: [System Information Discovery Technique](https://www.picussecurity.com/resource/the-system-information-discovery-technique-explained-mitre-attack-t1082)

> [^3]: [linux system time](https://wiki.archlinux.org/title/System_time)

> [^4]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)

> [^5]: [Technet Windows Time Service](https://technet.microsoft.com/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-time-service-tools-and-settings)

> [^6]: [Virtualization/Sandbox Evasion](https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis)

> [^7]: [MAGNET GOBLIN](https://research.checkpoint.com/2024/magnet-goblin-targets-publicly-facing-servers-using-1-day-vulnerabilities/)

> [^8]: [TechNet Net Time](https://technet.microsoft.com/bb490716.aspx)

> [^9]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^10]: [systemsetup mac time](https://support.apple.com/en-gb/guide/remote-desktop/apd95406b8d/mac)

> [^11]: [AnyRun TimeBomb](https://any.run/cybersecurity-blog/time-bombs-malware-with-delayed-execution/)

> [^12]: [MSDN System Time](https://msdn.microsoft.com/ms724961.aspx)

> [^13]: [RSA EU12 They're Inside](https://www.rsaconference.com/writable/presentations/file_upload/ht-209_rivner_schwartz.pdf)

> [^14]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)

> [^15]: [show_clock_detail_cisco_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s2.html#wp1896741674)


