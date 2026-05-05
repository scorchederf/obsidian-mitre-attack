---
aliases: 
    - S0698
    
mitre-attack: https://attack.mitre.org/software/S0698
---

## S0698

[HermeticWizard](https://attack.mitre.org/software/S0698) is a worm that has been used to spread [HermeticWiper](https://attack.mitre.org/software/S0697) in attacks against organizations in Ukraine since at least 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [HermeticWizard](https://attack.mitre.org/software/S0698) can use a list of hardcoded credentials to to authenticate via NTLMSSP to the SMB shares on remote systems.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HermeticWizard](https://attack.mitre.org/software/S0698) can use `cmd.exe` for execution on compromised hosts.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [HermeticWizard](https://attack.mitre.org/software/S0698) has been signed by valid certificates assigned to Hermetica Digital.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [HermeticWizard](https://attack.mitre.org/software/S0698) can use `OpenRemoteServiceManager` to create a service.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [HermeticWizard](https://attack.mitre.org/software/S0698) has been named `exec_32.dll` to mimic a legitimate MS Outlook .dll.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to use `wevtutil cl system` to clear event logs.[^1]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [HermeticWizard](https://attack.mitre.org/software/S0698) can use a list of hardcoded credentials in attempt to authenticate to SMB shares.[^1]  |
| [[Native API\|T1106]] | Native API | [HermeticWizard](https://attack.mitre.org/software/S0698) can connect to remote shares using `WNetAddConnection2W`.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [HermeticWizard](https://attack.mitre.org/software/S0698) can find machines on the local network by gathering known local IP addresses through `DNSGetCacheDataTable`, `GetIpNetTable`,`WNetOpenEnumW(RESOURCE_GLOBALNET, RESOURCETYPE_ANY)`,`NetServerEnum`,`GetTcpTable`, and `GetAdaptersAddresses.`[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [HermeticWizard](https://attack.mitre.org/software/S0698) can use WMI to create a new process on a remote machine via `C:\windows\system32\cmd.exe /c start C:\windows\system32\\regsvr32.exe /s /iC:\windows\<filename>.dll`.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to scan ports on a compromised network.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [HermeticWizard](https://attack.mitre.org/software/S0698) can copy files to other machines on a compromised network.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [HermeticWizard](https://attack.mitre.org/software/S0698) has used `regsvr32.exe /s /i` to execute malicious payloads.[^1]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [HermeticWizard](https://attack.mitre.org/software/S0698) can execute files on remote machines using DCOM.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to encrypt PE files with a reverse XOR loop.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to create a new process using `rundll32`.[^1]  |




## References

[^1]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


