---
aliases: 
    - T1495
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1495-Firmware_Corruption
tactic: 
     - Impact
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system.[^1]  Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.<br><br>In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable.[^4] [^2]  Depending on the device, this attack may also result in [[kb/mitre/attack/techniques/T1485-Data_Destruction\|Data Destruction]]. 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Prevent adversary access to privileged accounts or access necessary to replace system firmware. |
| [[kb/mitre/attack/mitigations/M1046-Boot_Integrity\|M1046]] | Boot Integrity | Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Patch the BIOS and other firmware as necessary to prevent successful use of known vulnerabilities. |






> [!info]- References
> [^1]: [Symantec Chernobyl W95.CIH](https://web.archive.org/web/20190508170055/https://www.symantec.com/security-center/writeup/2000-122010-2655-99)

> [^2]: [cisa_malware_orgs_ukraine](https://www.cisa.gov/uscert/ncas/alerts/aa22-057a)

> [^3]: [MITRE Trustworthy Firmware Measurement](http://www.mitre.org/publications/project-stories/going-deep-into-the-bios-with-mitre-firmware-security-research)

> [^4]: [dhs_threat_to_net_devices](https://cyber.dhs.gov/assets/report/ar-16-20173.pdf)


