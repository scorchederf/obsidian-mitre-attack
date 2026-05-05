---
aliases: 
    - S0345
    
mitre-attack: https://attack.mitre.org/software/S0345
---

## S0345

[Seasalt](https://attack.mitre.org/software/S0345) is malware that has been linked to [APT1](https://attack.mitre.org/groups/G0006)'s 2010 operations. It shares some code similarities with [OceanSalt](https://attack.mitre.org/software/S0346).[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Seasalt](https://attack.mitre.org/software/S0345) uses cmd.exe to create a reverse shell on the infected endpoint.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Seasalt](https://attack.mitre.org/software/S0345) has the capability to identify the drive type on a victim.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Seasalt](https://attack.mitre.org/software/S0345) uses HTTP for C2 communications.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Seasalt](https://attack.mitre.org/software/S0345) has a command to perform a process listing.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Seasalt](https://attack.mitre.org/software/S0345) has masqueraded as a service called "SaSaut" with a display name of "System Authorization Service" in an apparent attempt to masquerade as a legitimate service.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Seasalt](https://attack.mitre.org/software/S0345) has a command to download additional files.[^2] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Seasalt](https://attack.mitre.org/software/S0345) obfuscates configuration data.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Seasalt](https://attack.mitre.org/software/S0345) is capable of installing itself as a service.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Seasalt](https://attack.mitre.org/software/S0345) has a command to delete a specified file.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Seasalt](https://attack.mitre.org/software/S0345) creates a Registry entry to ensure infection after reboot under `HKLM\Software\Microsoft\Windows\currentVersion\Run`.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT1\|G0006]] | APT1 |



## References

[^1]: Seasalt


[^2]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^3]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


