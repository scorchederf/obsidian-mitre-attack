---
aliases: 
    - S0091
    
mitre-attack: https://attack.mitre.org/software/S0091
---

## S0091

[Epic](https://attack.mitre.org/software/S0091) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [Epic](https://attack.mitre.org/software/S0091) uses the `rem reg query` command to obtain values from Registry keys.[^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `tasklist /v` command to obtain a list of processes.[^6] [^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Epic](https://attack.mitre.org/software/S0091) uses HTTP and HTTPS for C2 communications.[^6] [^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Epic](https://attack.mitre.org/software/S0091) collects the user name from the victim’s machine.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `net time` command  to get the system time from the machine and collect the current date and time zone information.[^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Epic](https://attack.mitre.org/software/S0091) recursively searches for all .doc files on the system and collects a directory listing of the Desktop, %TEMP%, and %WINDOWS%\Temp directories.[^6] [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Epic](https://attack.mitre.org/software/S0091) has a command to delete a file from the machine.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Epic](https://attack.mitre.org/software/S0091) collects the OS version, hardware information, computer name, available system memory status, and system and user language settings.[^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `net use`, `net session`, and `netstat` commands to gather information on network connections.[^6] [^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `net view` command on the victim’s machine.[^6]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [Epic](https://attack.mitre.org/software/S0091) compresses the collected data with bzip2 before sending it to the C2 server.[^3]  |
| [[Extra Window Memory Injection\|T1055.011]] | Extra Window Memory Injection | [Epic](https://attack.mitre.org/software/S0091) has overwritten the function pointer in the extra window memory of Explorer's Shell_TrayWnd in order to execute malicious code in the context of the explorer.exe process.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Turla](https://attack.mitre.org/groups/G0010) has used valid digital certificates from Sysprint AG to sign its [Epic](https://attack.mitre.org/software/S0091) dropper.[^6]  |
| [[Local Account\|T1087.001]] | Local Account | [Epic](https://attack.mitre.org/software/S0091) gathers a list of all user accounts, privilege classes, and time of last logon.[^3]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Epic](https://attack.mitre.org/software/S0091) encrypts collected data using a public key framework before sending it over the C2 channel.[^6]  Some variants encrypt the collected data with AES and encode it with base64 before transmitting it to the C2 server.[^3]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Epic](https://attack.mitre.org/software/S0091) gathers information on local group names.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Epic](https://attack.mitre.org/software/S0091) encrypts commands from the C2 server using a hardcoded key.[^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `nbtstat -n` and `nbtstat -s` commands on the victim’s machine.[^6]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Epic](https://attack.mitre.org/software/S0091) uses the `tasklist /svc` command to list the services on the system.[^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Epic](https://attack.mitre.org/software/S0091) searches for anti-malware services running on the victim’s machine and terminates itself if it finds them.[^6]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Epic](https://attack.mitre.org/software/S0091) collects disk space information.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Epic](https://attack.mitre.org/software/S0091) heavily obfuscates its code to make analysis more difficult.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: Epic


[^2]: [ESET Recon Snake Nest](https://recon.cx/2018/brussels/resources/slides/RECON-BRX-2018-Visiting-The-Snake-Nest.pdf)


[^3]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)


[^4]: WorldCupSec


[^5]: TadjMakhal


[^6]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^7]: Tavdig


[^8]: [Secureworks IRON HUNTER Profile](http://www.secureworks.com/research/threat-profiles/iron-hunter)


[^9]: Wipbot


