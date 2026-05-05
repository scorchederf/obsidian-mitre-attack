---
aliases: 
    - S1167
    
mitre-attack: https://attack.mitre.org/software/S1167
---

## S1167

[AcidPour](https://attack.mitre.org/software/S1167) is a variant of [AcidRain](https://attack.mitre.org/software/S1125) designed to impact a wider range of x86 architecture Linux devices. [AcidPour](https://attack.mitre.org/software/S1167) is an x86 ELF binary that expands on the targeted devices and locations in [AcidRain](https://attack.mitre.org/software/S1125) by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, [AcidPour](https://attack.mitre.org/software/S1167) can impact a variety of device types including IoT, networking, and ICS embedded device types.[^1]  [AcidPour](https://attack.mitre.org/software/S1167) is a wiping payload associated with the [Sandworm Team](https://attack.mitre.org/groups/G0034) threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [AcidPour](https://attack.mitre.org/software/S1167) includes functionality to reboot the victim system following wiping actions, similar to [AcidRain](https://attack.mitre.org/software/S1125).[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [AcidPour](https://attack.mitre.org/software/S1167) includes functionality to identify MMC and SD cards connected to the victim device.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [AcidPour](https://attack.mitre.org/software/S1167) can identify various system locations and mapped devices on Linux systems as a precursor to wiping activity.[^1]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [AcidPour](https://attack.mitre.org/software/S1167) includes functionality to overwrite victim devices with the content of a buffer to wipe disk content.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AcidPour](https://attack.mitre.org/software/S1167) can identify specific files and directories within the Linux operating system corresponding with storage devices for follow-on wiping activity, similar to [AcidRain](https://attack.mitre.org/software/S1125).[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [AcidPour](https://attack.mitre.org/software/S1167) includes a self-delete function where the malware deletes itself from disk after execution and program load into memory.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [AcidPour](https://attack.mitre.org/software/S1167) can perform an in-depth wipe of victim filesystems and attached storage devices through either data overwrite or calling various IOCTLS to erase them, similar to [AcidRain](https://attack.mitre.org/software/S1125).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)


[^2]: [CERT-UA TelecomAttack 2023](https://cert.gov.ua/article/6123309)


