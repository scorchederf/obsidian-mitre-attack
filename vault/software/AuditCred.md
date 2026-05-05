---
aliases: 
    - S0347
    
mitre-attack: https://attack.mitre.org/software/S0347
---

## S0347

[AuditCred](https://attack.mitre.org/software/S0347) is a malicious DLL that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032) during their 2018 attacks.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [AuditCred](https://attack.mitre.org/software/S0347) can search through folders and files on the system.[^3]  |
| [[Proxy\|T1090]] | Proxy | [AuditCred](https://attack.mitre.org/software/S0347) can utilize proxy for communications.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [AuditCred](https://attack.mitre.org/software/S0347) can delete files from the system.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [AuditCred](https://attack.mitre.org/software/S0347) can inject code from files to other running processes.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [AuditCred](https://attack.mitre.org/software/S0347) can download files and additional malware.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [AuditCred](https://attack.mitre.org/software/S0347) can open a reverse shell on the system to execute commands.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [AuditCred](https://attack.mitre.org/software/S0347) uses XOR and RC4 to perform decryption on the code functions.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [AuditCred](https://attack.mitre.org/software/S0347) is installed as a new service on the system.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [AuditCred](https://attack.mitre.org/software/S0347) encrypts the configuration.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: Roptimizer


[^2]: AuditCred


[^3]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


