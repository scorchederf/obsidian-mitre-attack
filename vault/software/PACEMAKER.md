---
aliases: 
    - S1109
    
mitre-attack: https://attack.mitre.org/software/S1109
---

## S1109

[PACEMAKER](https://attack.mitre.org/software/S1109) is a credential stealer that was used by [APT5](https://attack.mitre.org/groups/G1023) as early as 2020 including activity against US Defense Industrial Base (DIB) companies.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proc Filesystem\|T1003.007]] | Proc Filesystem | [PACEMAKER](https://attack.mitre.org/software/S1109) has the ability to extract credentials from OS memory.[^1]  |
| [[Ptrace System Calls\|T1055.008]] | Ptrace System Calls | [PACEMAKER](https://attack.mitre.org/software/S1109) can use PTRACE to attach to a targeted process to read process memory.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [PACEMAKER](https://attack.mitre.org/software/S1109) can enter a loop to read `/proc/` entries every 2 seconds in order to read a target application's memory.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [PACEMAKER](https://attack.mitre.org/software/S1109) can use a simple bash script for execution.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PACEMAKER](https://attack.mitre.org/software/S1109) can parse `/proc/"process_name"/cmdline` to look for the string `dswsd` within the command line.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PACEMAKER](https://attack.mitre.org/software/S1109) has written extracted data to `tmp/dsserver-check.statementcounters`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


