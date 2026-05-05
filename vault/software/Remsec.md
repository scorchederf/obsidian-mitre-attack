---
aliases: 
    - S0125
    
mitre-attack: https://attack.mitre.org/software/S0125
---

## S0125

[Remsec](https://attack.mitre.org/software/S0125) is a modular backdoor that has been used by [Strider](https://attack.mitre.org/groups/G0041) and appears to have been designed primarily for espionage purposes. Many of its modules are written in Lua. [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Remsec](https://attack.mitre.org/software/S0125) can perform DLL injection.[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Remsec](https://attack.mitre.org/software/S0125) has a plugin to drop and execute vulnerable Outpost Sandbox or avast! Virtualization drivers in order to gain kernel mode privileges.[^2]  |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [Remsec](https://attack.mitre.org/software/S0125) contains a module to move data from airgapped networks to Internet-connected systems by using a removable USB device.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Remsec](https://attack.mitre.org/software/S0125) is capable of listing contents of folders on the victim. [Remsec](https://attack.mitre.org/software/S0125) also searches for custom network encryption software on victims.[^1] [^3] [^2]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [Remsec](https://attack.mitre.org/software/S0125) can add or remove applications or ports on the Windows firewall or disable it entirely.[^2]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Remsec](https://attack.mitre.org/software/S0125) can exfiltrate data via a DNS tunnel or email, separately from its C2 channel.[^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Remsec](https://attack.mitre.org/software/S0125) can obtain a list of active connections and open ports.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Remsec](https://attack.mitre.org/software/S0125) is capable of deleting files on the victim. It also securely removes itself after collecting and exfiltrating data.[^1] [^3] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Remsec](https://attack.mitre.org/software/S0125) contains a keylogger component.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Remsec](https://attack.mitre.org/software/S0125) can obtain a process list from the victim.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Some data in [Remsec](https://attack.mitre.org/software/S0125) is encrypted using RC5 in CBC mode, AES-CBC with a hardcoded key, RC4, or Salsa20. Some data is also base64-encoded.[^1] [^2]  |
| [[Password Filter DLL\|T1556.002]] | Password Filter DLL | [Remsec](https://attack.mitre.org/software/S0125) harvests plain-text credentials as a password filter registered on domain controllers.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | The [Remsec](https://attack.mitre.org/software/S0125) loader implements itself with the name Security Support Provider, a legitimate Windows function. Various [Remsec](https://attack.mitre.org/software/S0125) .exe files mimic legitimate file names used by Microsoft, Symantec, Kaspersky, Hewlett-Packard, and VMWare. [Remsec](https://attack.mitre.org/software/S0125) also disguised malicious modules using similar filenames as custom network encryption software on victims.[^8] [^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Remsec](https://attack.mitre.org/software/S0125) is capable of using ICMP, TCP, and UDP for C2.[^1] [^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Remsec](https://attack.mitre.org/software/S0125) can ping or traceroute a remote host.[^2]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Remsec](https://attack.mitre.org/software/S0125) is capable of using SMTP for C2.[^1] [^3] [^2] [^4]  |
| [[Lua\|T1059.011]] | Lua | [Remsec](https://attack.mitre.org/software/S0125) can use modules written in Lua for execution.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Remsec](https://attack.mitre.org/software/S0125) contains a network loader to receive executable modules from remote attackers and run them on the local victim. It can also upload and download files over HTTP and HTTPS.[^1] [^2]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Remsec](https://attack.mitre.org/software/S0125) can dump the SAM database.[^2]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Remsec](https://attack.mitre.org/software/S0125) has a package that collects documents from any inserted USB sticks.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Remsec](https://attack.mitre.org/software/S0125) schedules the execution one of its modules by creating a new scheduler task.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Remsec](https://attack.mitre.org/software/S0125) can obtain the OS version information, computer name, processor architecture, machine role, and OS edition.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [Remsec](https://attack.mitre.org/software/S0125) can obtain a list of users.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Remsec](https://attack.mitre.org/software/S0125) can obtain information about network configuration, including the routing table, ARP cache, and DNS cache.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Remsec](https://attack.mitre.org/software/S0125) can obtain information about the current user.[^2]  |
| [[Device Driver Discovery\|T1652]] | Device Driver Discovery | [Remsec](https://attack.mitre.org/software/S0125) has a plugin to detect active drivers of some security products.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Remsec](https://attack.mitre.org/software/S0125) is capable of using HTTP and HTTPS for C2.[^1] [^3] [^2]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Remsec](https://attack.mitre.org/software/S0125) has a plugin that can perform ARP scanning as well as port scanning.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Remsec](https://attack.mitre.org/software/S0125) has a plugin detect security products via active drivers.[^2]  |
| [[DNS\|T1071.004]] | DNS | [Remsec](https://attack.mitre.org/software/S0125) is capable of using DNS for C2.[^1] [^3] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Strider\|G0041]] | Strider |



## References

[^1]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)


[^2]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^3]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)


[^4]: [Threatpost Sauron](https://threatpost.com/projectsauron-apt-on-par-with-equation-flame-duqu/119725/)


[^5]: [Kaspersky ProjectSauron Blog](https://securelist.com/faq-the-projectsauron-apt/75533/)


[^6]: ProjectSauron


[^7]: [Symantec Strider Blog](http://www.symantec.com/connect/blogs/strider-cyberespionage-group-turns-eye-sauron-targets)


[^8]: [ComputerWeekly Strider](https://www.computerweekly.com/news/450302128/Strider-cyber-attack-group-deploying-malware-for-espionage)


[^9]: [Kaspersky Lua](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07190154/The-ProjectSauron-APT_research_KL.pdf)


