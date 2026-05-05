---
aliases: 
    - S1151
    
mitre-attack: https://attack.mitre.org/software/S1151
---

## S1151

[ZeroCleare](https://attack.mitre.org/software/S1151) is a wiper malware that has been used in conjunction with the [RawDisk](https://attack.mitre.org/software/S0364) driver since at least 2019 by suspected Iran-nexus threat actors including activity targeting the energy and industrial sectors in the Middle East and political targets in Albania.[^2] [^5] [^4] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [ZeroCleare](https://attack.mitre.org/software/S1151) can use the `IOCTL_DISK_GET_DRIVE_GEOMETRY_EX`, `IOCTL_DISK_GET_DRIVE_GEOMETRY`, and `IOCTL_DISK_GET_LENGTH_INFO` system calls to compute disk size.[^4]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [ZeroCleare](https://attack.mitre.org/software/S1151) has used a vulnerable signed VBoxDrv driver to bypass Microsoft Driver Signature Enforcement (DSE) protections and subsequently load the unsigned [RawDisk](https://attack.mitre.org/software/S0364) driver.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [ZeroCleare](https://attack.mitre.org/software/S1151) can deploy a vulnerable, signed driver on a compromised host to bypass operating system safeguards.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [ZeroCleare](https://attack.mitre.org/software/S1151) can receive command line arguments from an operator to corrupt the file system using the [RawDisk](https://attack.mitre.org/software/S0364) driver.[^4]  |
| [[Native API\|T1106]] | Native API | [ZeroCleare](https://attack.mitre.org/software/S1151) can call the `GetSystemDirectoryW` API to locate the system directory.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ZeroCleare](https://attack.mitre.org/software/S1151) has the ability to uninstall the [RawDisk](https://attack.mitre.org/software/S0364) driver and delete the `rwdsk` file on disk.[^4] [^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [ZeroCleare](https://attack.mitre.org/software/S1151) can use a malicious PowerShell script to bypass Windows controls.[^1]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [ZeroCleare](https://attack.mitre.org/software/S1151) can corrupt the file system and wipe the system drive on targeted hosts.[^4] [^5] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [IBM ZeroCleare Wiper December 2019](https://securityintelligence.com/posts/new-destructive-wiper-zerocleare-targets-energy-sector-in-the-middle-east/)


[^2]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)


[^3]: ZEROCLEAR


[^4]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^5]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)


