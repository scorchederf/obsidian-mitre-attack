---
aliases: 
    - S0040
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0040-HTRAN
---

## Description

[[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. [^2] [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1014-Rootkit\|T1014]] | Rootkit | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can install a rootkit to hide network connections from the host OS.[^3]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can inject into into running processes.[^3]  |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can proxy TCP socket connections to obfuscate command and control infrastructure.[^2] [^3]  |





> [!info]- References
> [^1]: HUC Packet Transmit Tool

> [^2]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)

> [^3]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


