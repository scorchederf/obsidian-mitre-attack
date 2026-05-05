---
aliases: 
    - S1184
    
mitre-attack: https://attack.mitre.org/software/S1184
---

## S1184

[BOLDMOVE](https://attack.mitre.org/software/S1184) is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. [BOLDMOVE](https://attack.mitre.org/software/S1184) includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. [BOLDMOVE](https://attack.mitre.org/software/S1184) is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs.[^1]  The record for [BOLDMOVE](https://attack.mitre.org/software/S1184) only covers known Linux variants.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [BOLDMOVE](https://attack.mitre.org/software/S1184) is capable of spawning a remote command shell.[^1]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [BOLDMOVE](https://attack.mitre.org/software/S1184) calls the signal function to ignore the signals SIGCHLD, SIGHIP, and SIGPIPE prior to starting primary logic.[^1]  |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | [BOLDMOVE](https://attack.mitre.org/software/S1184) can free all resources and terminate itself on victim machines.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BOLDMOVE](https://attack.mitre.org/software/S1184) can list information of all files in the system recursively from the root directory or from a specified directory.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [BOLDMOVE](https://attack.mitre.org/software/S1184) uses the WolfSSL library to implement SSL encryption for command and control communication.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [BOLDMOVE](https://attack.mitre.org/software/S1184) contains a watchdog-like feature that monitors a particular file for modification. If modification is detected, the legitimate file is backed up and replaced with a trojanized file to allow for persistence through likely system upgrades.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BOLDMOVE](https://attack.mitre.org/software/S1184) enumerates network interfaces on the infected host.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [BOLDMOVE](https://attack.mitre.org/software/S1184) is associated with exploitation of CVE-2022-49475 in FortiOS.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BOLDMOVE](https://attack.mitre.org/software/S1184) can remove files on victim systems.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BOLDMOVE](https://attack.mitre.org/software/S1184) uses web services for command and control communication.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BOLDMOVE](https://attack.mitre.org/software/S1184) performs system survey actions following initial execution.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [BOLDMOVE](https://attack.mitre.org/software/S1184) can disable the Fortinet daemons `moglogd` and `syslogd` to evade detection and logging.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BOLDMOVE](https://attack.mitre.org/software/S1184) verifies it is executing from a specific path during execution.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [BOLDMOVE](https://attack.mitre.org/software/S1184) is capable of relaying traffic from command and control servers to follow-on systems.[^1]  |




## References

[^1]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)


