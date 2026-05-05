---
aliases: 
    - S1125
    
mitre-attack: https://attack.mitre.org/software/S1125
---

## S1125

[AcidRain](https://attack.mitre.org/software/S1125) is an ELF binary targeting modems and routers using MIPS architecture.[^1]  [AcidRain](https://attack.mitre.org/software/S1125) is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with [Sandworm Team](https://attack.mitre.org/groups/G0034).[^1]  US and European government sources linked [AcidRain](https://attack.mitre.org/software/S1125) to Russian government entities, while Ukrainian government sources linked [AcidRain](https://attack.mitre.org/software/S1125) specifically to [Sandworm Team](https://attack.mitre.org/groups/G0034).[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [AcidRain](https://attack.mitre.org/software/S1125) reboots the target system once the various wiping processes are complete.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [AcidRain](https://attack.mitre.org/software/S1125) performs an in-depth wipe of the target filesystem and various attached storage devices through either a data overwrite or calling various IOCTLS to erase it.[^1]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [AcidRain](https://attack.mitre.org/software/S1125) iterates over device file identifiers on the target, opens the device file, and either overwrites the file or calls various IOCTLS commands to erase it.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AcidRain](https://attack.mitre.org/software/S1125) identifies specific files and directories in the Linux operating system associated with storage devices.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)


[^2]: [AcidRain State Department 2022](https://www.state.gov/attribution-of-russias-malicious-cyber-activity-against-ukraine/)


[^3]: [Vincens AcidPour 2024](https://cyberscoop.com/viasat-malware-wiper-acidrain/)


