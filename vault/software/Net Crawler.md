---
aliases: 
    - S0056
    
mitre-attack: https://attack.mitre.org/software/S0056
---

## S0056

[Net Crawler](https://attack.mitre.org/software/S0056) is an intranet worm capable of extracting credentials using credential dumpers and spreading to systems on a network over SMB by brute forcing accounts with recovered passwords and using [PsExec](https://attack.mitre.org/software/S0029) to execute a copy of [Net Crawler](https://attack.mitre.org/software/S0056). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Password Cracking\|T1110.002]] | Password Cracking | [Net Crawler](https://attack.mitre.org/software/S0056) uses a list of known credentials gathered through credential dumping to guess passwords to accounts as it spreads throughout a network.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Net Crawler](https://attack.mitre.org/software/S0056) uses [PsExec](https://attack.mitre.org/software/S0029) to perform remote service manipulation to execute a copy of itself as part of lateral movement.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Net Crawler](https://attack.mitre.org/software/S0056) uses credential dumpers such as [Mimikatz](https://attack.mitre.org/software/S0002) and [Windows Credential Editor](https://attack.mitre.org/software/S0005) to extract cached credentials from Windows systems.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Net Crawler](https://attack.mitre.org/software/S0056) uses Windows admin shares to establish authenticated sessions to remote systems over SMB as part of lateral movement.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cleaver\|G0003]] | Cleaver |



## References

[^1]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


