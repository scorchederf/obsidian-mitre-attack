---
aliases: 
    - S1136
    
mitre-attack: https://attack.mitre.org/software/S1136
---

## S1136

[BFG Agonizer](https://attack.mitre.org/software/S1136) is a wiper related to the open-source project CRYLINE-v.5.0. The malware is associated with wiping operations conducted by the [Agrius](https://attack.mitre.org/groups/G1030) threat actor.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [BFG Agonizer](https://attack.mitre.org/software/S1136) uses elevated privileges to call `NtRaiseHardError` to induce a "blue screen of death" on infected systems, causing a system crash. Once shut down, the system is no longer bootable.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [BFG Agonizer](https://attack.mitre.org/software/S1136) uses DLL unhooking to remove user mode inline hooks that security solutions often implement. [BFG Agonizer](https://attack.mitre.org/software/S1136) also uses IAT unhooking to remove user-mode IAT hooks that security solutions also use.[^1]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [BFG Agonizer](https://attack.mitre.org/software/S1136) retrieves a device handle to `\\\\.\\PhysicalDrive0` to wipe the boot sector of a given disk.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BFG Agonizer](https://attack.mitre.org/software/S1136) wipes the boot sector of infected machines to inhibit system recovery.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Agrius\|G1030]] | Agrius |



## References

[^1]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


