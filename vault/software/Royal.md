---
aliases: 
    - S1073
    
mitre-attack: https://attack.mitre.org/software/S1073
---

## S1073

[Royal](https://attack.mitre.org/software/S1073) is ransomware that first appeared in early 2022;  a version that also targets ESXi servers was later observed in February 2023. [Royal](https://attack.mitre.org/software/S1073) employs partial encryption and multiple threads to evade detection and speed encryption. [Royal](https://attack.mitre.org/software/S1073) has been used in attacks against multiple industries worldwide--including critical infrastructure. Security researchers have identified similarities in the encryption routines and TTPs used in [Royal](https://attack.mitre.org/software/S1073) and [Conti](https://attack.mitre.org/software/S0575) attacks and noted a possible connection between their operators.[^5] [^2] [^1] [^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Royal](https://attack.mitre.org/software/S1073) uses a multi-threaded encryption process that can partially encrypt targeted files with the OpenSSL library and the AES256 algorithm.[^2] [^1] [^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Royal](https://attack.mitre.org/software/S1073) can use `RmShutDown` to kill  applications and services using the resources that are targeted for encryption.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery |  [Royal](https://attack.mitre.org/software/S1073) can use `GetNativeSystemInfo` to enumerate system processors.[^2] [^4]  |
| [[Hypervisor CLI\|T1059.012]] | Hypervisor CLI | Royal ransomware uses `esxcli` to gather a list of running VMs and terminate them.[^4]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Royal](https://attack.mitre.org/software/S1073) can use SMB to connect to move laterally.[^2]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Royal](https://attack.mitre.org/software/S1073) can scan the network interfaces of targeted systems.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Royal](https://attack.mitre.org/software/S1073) can delete shadow copy backups with vssadmin.exe using the command `delete shadows /all /quiet`.[^2] [^1] [^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Royal](https://attack.mitre.org/software/S1073) can enumerate the shared resources of a given IP addresses using the API call `NetShareEnum`.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Royal](https://attack.mitre.org/software/S1073) can enumerate IP addresses using `GetIpAddrTable`.[^2]  |
| [[Native API\|T1106]] | Native API | [Royal](https://attack.mitre.org/software/S1073) can use multiple APIs for discovery, communication, and execution.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Royal](https://attack.mitre.org/software/S1073) establishes a TCP socket for C2 communication using the API `WSASocketW`.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery |  [Royal](https://attack.mitre.org/software/S1073) can use `GetLogicalDrives` to enumerate logical drives.[^2] [^4]  |
| [[Phishing\|T1566]] | Phishing | [Royal](https://attack.mitre.org/software/S1073) has been spread through the use of phishing campaigns including "call back phishing" where victims are lured into calling a number provided through email.[^2] [^1] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Royal](https://attack.mitre.org/software/S1073) can use `GetCurrentProcess` to enumerate processes.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Royal](https://attack.mitre.org/software/S1073) can identify specific files and directories to exclude from the encryption process.[^2] [^1] [^4]  |




## References

[^1]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)


[^2]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^3]: [CISA Royal AA23-061A March 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)


[^4]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)


[^5]: [Microsoft Royal ransomware November 2022](https://www.microsoft.com/en-us/security/blog/2022/11/17/dev-0569-finds-new-ways-to-deliver-royal-ransomware-various-payloads/)


