---
aliases: 
    - S0273
    
mitre-attack: https://attack.mitre.org/software/S0273
---

## S0273

[Socksbot](https://attack.mitre.org/software/S0273) is a backdoor that  abuses Socket Secure (SOCKS) proxies. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Socksbot](https://attack.mitre.org/software/S0273) creates a suspended svchost process and injects its DLL into it.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Socksbot](https://attack.mitre.org/software/S0273) can write and execute PowerShell scripts.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Socksbot](https://attack.mitre.org/software/S0273) can start SOCKS proxy threads.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Socksbot](https://attack.mitre.org/software/S0273) can take screenshots.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Socksbot](https://attack.mitre.org/software/S0273) can list all running processes.[^1]  |




## References

[^1]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^2]: Socksbot


