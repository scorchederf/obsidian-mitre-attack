---
aliases: 
    - S1058
    
mitre-attack: https://attack.mitre.org/software/S1058
---

## S1058

[Prestige](https://attack.mitre.org/software/S1058) ransomware has been used by [Sandworm Team](https://attack.mitre.org/groups/G0034) since at least March 2022, including against transportation and related logistics industries in Ukraine and Poland in October 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Prestige](https://attack.mitre.org/software/S1058) has been deployed using the Default Domain Group Policy Object from an Active Directory Domain Controller.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Prestige](https://attack.mitre.org/software/S1058) has attempted to stop the MSSQL Windows service to ensure successful encryption using `C:\Windows\System32\net.exe stop MSSQLSERVER`.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Prestige](https://attack.mitre.org/software/S1058) has leveraged the CryptoPP C++ library to encrypt files on target systems using AES and appended filenames with `.enc`.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Prestige](https://attack.mitre.org/software/S1058) has been executed on a target system through a scheduled task created by [Sandworm Team](https://attack.mitre.org/groups/G0034) using [Impacket](https://attack.mitre.org/software/S0357).[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Prestige](https://attack.mitre.org/software/S1058) can delete the backup catalog from the target system using: `c:\Windows\System32\wbadmin.exe delete catalog -quiet` and can also delete volume shadow copies using: `\Windows\System32\vssadmin.exe delete shadows /all /quiet`.[^1] <br> |
| [[Modify Registry\|T1112]] | Modify Registry | [Prestige](https://attack.mitre.org/software/S1058) has the ability to register new registry keys for a new extension handler via `HKCR\.enc` and `HKCR\enc\shell\open\command`.[^1]  |
| [[Native API\|T1106]] | Native API | [Prestige](https://attack.mitre.org/software/S1058) has used the `Wow64DisableWow64FsRedirection()` and `Wow64RevertWow64FsRedirection()` functions to disable and restore file system redirection.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Prestige](https://attack.mitre.org/software/S1058) can use PowerShell for payload execution on targeted systems.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Prestige](https://attack.mitre.org/software/S1058) can traverse the file system to discover files to encrypt by identifying specific extensions defined in a hardcoded list.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^2]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


