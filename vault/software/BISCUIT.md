---
aliases: 
    - S0017
    
mitre-attack: https://attack.mitre.org/software/S0017
---

## S0017

[BISCUIT](https://attack.mitre.org/software/S0017) is a backdoor that has been used by [APT1](https://attack.mitre.org/groups/G0006) since as early as 2007. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to periodically take screenshots of the system.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [BISCUIT](https://attack.mitre.org/software/S0017) malware contains a secondary fallback command and control server that is contacted after the primary command and control server.[^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to collect the processor type, operation system, computer name, and whether the system is a laptop or PC.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to collect the system `UPTIME`.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to enumerate running processes and identify their owners.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to download a file from the C2 server.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [BISCUIT](https://attack.mitre.org/software/S0017) can capture keystrokes.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [BISCUIT](https://attack.mitre.org/software/S0017) uses SSL for encrypting C2 communications.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to gather the username from the system.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to launch a command shell on the system.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT1\|G0006]] | APT1 |



## References

[^1]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^2]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^3]: BISCUIT


