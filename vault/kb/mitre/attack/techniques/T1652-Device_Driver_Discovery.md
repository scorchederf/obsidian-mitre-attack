---
aliases: 
    - T1652
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1652-Device_Driver_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|Security Software Discovery]]) or other defenses (e.g., [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]]), as well as potential exploitable vulnerabilities (e.g., [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|Exploitation for Privilege Escalation]]).<br><br>Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()` API function on Windows.[^6] [^5]  Information about device drivers (as well as associated services, i.e., [[kb/mitre/attack/techniques/T1007-System_Service_Discovery\|System Service Discovery]]) may also be available in the Registry.[^4] <br><br>On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod` and `modinfo`.[^3] [^2] [^1] 








> [!info]- References
> [^1]: [modinfo man](https://linux.die.net/man/8/modinfo)

> [^2]: [lsmod man](https://man7.org/linux/man-pages/man8/lsmod.8.html)

> [^3]: [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)

> [^4]: [Microsoft Registry Drivers](https://learn.microsoft.com/windows-hardware/drivers/install/overview-of-registry-trees-and-keys)

> [^5]: [Microsoft EnumDeviceDrivers](https://learn.microsoft.com/windows/win32/api/psapi/nf-psapi-enumdevicedrivers)

> [^6]: [Microsoft Driverquery](https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery)


