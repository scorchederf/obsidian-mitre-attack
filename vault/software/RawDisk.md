---
aliases: 
    - S0364
    
mitre-attack: https://attack.mitre.org/software/S0364
---

## S0364

[RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.[^3] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to help overwrite components of disk structure like the MBR and disk partitions.[^1] [^5]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [RawDisk](https://attack.mitre.org/software/S0364) has been used to directly access the hard disk to help overwrite arbitrarily sized portions of disk content.[^4]  |
| [[Data Destruction\|T1485]] | Data Destruction | [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.[^1] [^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^2]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^3]: [EldoS RawDisk ITpro](https://www.itprotoday.com/windows-78/eldos-provides-raw-disk-access-vista-and-xp)


[^4]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^5]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)


