---
aliases: 
    - S0106
    
mitre-attack: https://attack.mitre.org/software/S0106
---

## S0106

[cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. [^8] <br><br>Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., `dir` [^1] ), deleting files (e.g., `del` [^9] ), and copying files (e.g., `copy` [^2] ).

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [cmd](https://attack.mitre.org/software/S0106) can be used to find files and directories with native functionality such as `dir` commands.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected external system.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [cmd](https://attack.mitre.org/software/S0106) can be used to find information about the operating system.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [cmd](https://attack.mitre.org/software/S0106) can be used to delete files from the file system.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [cmd](https://attack.mitre.org/software/S0106) is used to execute programs and other actions at the command-line interface.[^8]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected internal system.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER |
| [[APT18\|G0026]] | APT18 |
| [[menuPass\|G0045]] | menuPass |
| [[Orangeworm\|G0071]] | Orangeworm |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |



## References

[^1]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)


[^2]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)


[^3]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^4]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^5]: [Dell Lateral Movement](http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/)


[^6]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^7]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^8]: [TechNet Cmd](https://technet.microsoft.com/en-us/library/bb490880.aspx)


[^9]: [TechNet Del](https://technet.microsoft.com/en-us/library/cc771049.aspx)


[^10]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^11]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


