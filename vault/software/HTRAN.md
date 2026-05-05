---
aliases: 
    - S0040
    
mitre-attack: https://attack.mitre.org/software/S0040
---

## S0040

[HTRAN](https://attack.mitre.org/software/S0040) is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. [^5] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [HTRAN](https://attack.mitre.org/software/S0040) can proxy TCP socket connections to obfuscate command and control infrastructure.[^5] [^2]  |
| [[Rootkit\|T1014]] | Rootkit | [HTRAN](https://attack.mitre.org/software/S0040) can install a rootkit to hide network connections from the host OS.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [HTRAN](https://attack.mitre.org/software/S0040) can inject into into running processes.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[APT12\|G0005]] | APT12 |



## References

[^1]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^2]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^3]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^4]: HUC Packet Transmit Tool


[^5]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)


[^6]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


