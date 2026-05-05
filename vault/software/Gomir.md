---
aliases: 
    - S1198
    
mitre-attack: https://attack.mitre.org/software/S1198
---

## S1198

Gomir is a Linux backdoor variant of the Go-based malware [GoBear](https://attack.mitre.org/software/S1197), uniquely assoicated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Gomir](https://attack.mitre.org/software/S1198) uses a custom encryption algorithm for content sent to command and control infrastructure.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Gomir](https://attack.mitre.org/software/S1198) creates a systemd service named `syslogd` for persistence.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Gomir](https://attack.mitre.org/software/S1198) probes arbitrary network endpoints for TCP connectivity.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Gomir](https://attack.mitre.org/software/S1198) uses Base64-encoded content in HTTP communications to command and control infrastructure.[^1]  |
| [[Cron\|T1053.003]] | Cron | [Gomir](https://attack.mitre.org/software/S1198) will configure a crontab for process execution to start the backdoor on reboot if it is not initially running under group 0 privileges.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Gomir](https://attack.mitre.org/software/S1198) reads command line arguments and parses them for functionality when executed from a Linux shell, and can execute arbitrary strings passed to it as shell commands.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Gomir](https://attack.mitre.org/software/S1198) periodically communicates to its command and control infrastructure through HTTP POST requests.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Gomir](https://attack.mitre.org/software/S1198) can start a reverse proxy to initiate connections to arbitrary endpoints in victim networks.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Gomir](https://attack.mitre.org/software/S1198) collects information about directory and file structures, including total number of subdirectories, total number of files, and total size of files on infected systems.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Gomir](https://attack.mitre.org/software/S1198) collects network information on infected systems such as listing interface names, MAC and IP addresses, and IPv6 addresses.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Gomir](https://attack.mitre.org/software/S1198) collects information on infected systems such as hostname, username, CPU, and RAM information.[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Gomir](https://attack.mitre.org/software/S1198) checks the effective group ID of its process when initially executed to determine if it is in group 0, denoting superuser privileges in Linux environments.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Gomir](https://attack.mitre.org/software/S1198) deletes its original executable and terminates its original process after creating a systemd service.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Gomir](https://attack.mitre.org/software/S1198) uses reverse proxy functionality that employs SSL to encrypt communications.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


