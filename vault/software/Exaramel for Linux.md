---
aliases: 
    - S0401
    
mitre-attack: https://attack.mitre.org/software/S0401
---

## S0401

[Exaramel for Linux](https://attack.mitre.org/software/S0401) is a backdoor written in the Go Programming Language and compiled as a 64-bit ELF binary. The Windows version is tracked separately under [Exaramel for Windows](https://attack.mitre.org/software/S0343).[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Exaramel for Linux](https://attack.mitre.org/software/S0401) has a command to download a file from  and to a remote C2 server.[^3] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can run `whoami` to identify the system owner.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Exaramel for Linux](https://attack.mitre.org/software/S0401) uses HTTPS for C2 communications.[^3] [^1]  |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | [Exaramel for Linux](https://attack.mitre.org/software/S0401) has a hardcoded location that it uses to achieve persistence if the startup system is Upstart or System V and it is running as root.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can decrypt its configuration file.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can attempt to find a new C2 server if it receives an error.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Exaramel for Linux](https://attack.mitre.org/software/S0401) has a hardcoded location under systemd that it uses to achieve persistence if it is running as root.[^3] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can uninstall its persistence mechanism and delete its configuration file.[^1]  |
| [[Setuid and Setgid\|T1548.001]] | Setuid and Setgid | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can execute commands with high privileges via a specific binary with setuid functionality.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Exaramel for Linux](https://attack.mitre.org/software/S0401) uses RC4 for encrypting the configuration.[^3] [^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Exaramel for Linux](https://attack.mitre.org/software/S0401) has a command to execute a shell command on the system.[^3] [^1]  |
| [[Cron\|T1053.003]] | Cron | [Exaramel for Linux](https://attack.mitre.org/software/S0401) uses crontab for persistence if it does not have root privileges.[^3] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^2]: Exaramel for Linux


[^3]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


