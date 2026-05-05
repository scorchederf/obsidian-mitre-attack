---
aliases: 
    - S0390
    
mitre-attack: https://attack.mitre.org/software/S0390
---

## S0390

[SQLRat](https://attack.mitre.org/software/S0390) is malware that executes SQL scripts to avoid leaving traditional host artifacts. [FIN7](https://attack.mitre.org/groups/G0046) has been observed using it.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [SQLRat](https://attack.mitre.org/software/S0390) has used been observed deleting scripts once used.[^2] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SQLRat](https://attack.mitre.org/software/S0390) has used SQL to execute JavaScript and VB scripts on the host system.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SQLRat](https://attack.mitre.org/software/S0390) can make a direct SQL connection to a Microsoft database controlled by the attackers, retrieve an item from the bindata table, then write and execute the file on disk.[^2] 	 |
| [[Malicious File\|T1204.002]] | Malicious File | [SQLRat](https://attack.mitre.org/software/S0390) relies on users clicking on an embedded image to execute the scripts.[^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [SQLRat](https://attack.mitre.org/software/S0390) has used a character insertion obfuscation technique, making the script appear to contain Chinese characters.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SQLRat](https://attack.mitre.org/software/S0390) has scripts that are responsible for deobfuscating additional scripts.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SQLRat](https://attack.mitre.org/software/S0390) has created scheduled tasks in `%appdata%\Roaming\Microsoft\Templates\`.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SQLRat](https://attack.mitre.org/software/S0390) has used PowerShell to create a Meterpreter session.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: SQLRat


[^2]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)


