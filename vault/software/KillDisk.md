---
aliases: 
    - S0607
    
mitre-attack: https://attack.mitre.org/software/S0607
---

## S0607

[KillDisk](https://attack.mitre.org/software/S0607) is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of [BlackEnergy](https://attack.mitre.org/software/S0089) malware during cyber attacks against Ukraine in 2015. [KillDisk](https://attack.mitre.org/software/S0607) has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some [KillDisk](https://attack.mitre.org/software/S0607) variants.[^5] [^4] [^6] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [KillDisk](https://attack.mitre.org/software/S0607) has used the `FindNextFile` command as part of its file deletion process.[^1]  |
| [[Native API\|T1106]] | Native API | [KillDisk](https://attack.mitre.org/software/S0607) has called the Windows API to retrieve the hard disk handle and shut down the machine.[^6]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [KillDisk](https://attack.mitre.org/software/S0607) retrieves the hard disk name by calling the `CreateFileA to \\.\PHYSICALDRIVE0` API.[^6]  |
| [[Shared Modules\|T1129]] | Shared Modules | [KillDisk](https://attack.mitre.org/software/S0607) loads and executes functions from a DLL.[^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | [KillDisk](https://attack.mitre.org/software/S0607) has called `GetCurrentProcess`.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [KillDisk](https://attack.mitre.org/software/S0607) deletes Application, Security, Setup, and System Windows Event Logs.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [KillDisk](https://attack.mitre.org/software/S0607) uses VMProtect to make reverse engineering the malware more difficult.[^6]  |
| [[Service Stop\|T1489]] | Service Stop | [KillDisk](https://attack.mitre.org/software/S0607) terminates various processes to get the user to reboot the victim machine.[^1]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [KillDisk](https://attack.mitre.org/software/S0607) attempts to reboot the machine by terminating specific processes.[^1]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [KillDisk](https://attack.mitre.org/software/S0607) overwrites the first sector of the Master Boot Record with “0x00”.[^6]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [KillDisk](https://attack.mitre.org/software/S0607) has a ransomware component that encrypts files with an AES key that is also RSA-1028 encrypted.[^5]  |
| [[File Deletion\|T1070.004]] | File Deletion | [KillDisk](https://attack.mitre.org/software/S0607) has the ability to quit and delete itself.[^8]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [KillDisk](https://attack.mitre.org/software/S0607) registers as a service under the Plug-And-Play Support name.[^8]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [KillDisk](https://attack.mitre.org/software/S0607) has attempted to get the access token of a process by calling `OpenProcessToken`. If [KillDisk](https://attack.mitre.org/software/S0607) gets the access token, then it attempt to modify the token privileges with `AdjustTokenPrivileges`.[^1]  |
| [[Data Destruction\|T1485]] | Data Destruction | [KillDisk](https://attack.mitre.org/software/S0607) deletes system files to make the OS unbootable. [KillDisk](https://attack.mitre.org/software/S0607) also targets and deletes files with 35 different file extensions.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT38\|G0082]] | APT38 |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)


[^2]: [ESET Lazarus KillDisk April 2018](https://www.welivesecurity.com/2018/04/03/lazarus-killdisk-central-american-casino/)


[^3]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^4]: [ESEST Black Energy Jan 2016](http://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)


[^5]: [KillDisk Ransomware](https://www.bleepingcomputer.com/news/security/killdisk-disk-wiping-malware-adds-ransomware-component/)


[^6]: [Trend Micro KillDisk 1](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)


[^7]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^8]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


